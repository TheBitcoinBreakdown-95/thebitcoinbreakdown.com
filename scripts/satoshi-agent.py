"""
Satoshi Agent -- Bitcoin technical expert powered by bitcoinknowledge.dev

Two modes:
  Q&A:    python satoshi-agent.py "What is Taproot?"
  Verify: python satoshi-agent.py --verify "Taproot activated in November 2021"

Requires: pip install anthropic requests python-dotenv
API key:  ANTHROPIC_API_KEY in .env file (project root or script directory)
"""

import argparse
import json
import sys
import os

import anthropic
import requests
from dotenv import load_dotenv

# ---------------------------------------------------------------------------
# Config
# ---------------------------------------------------------------------------

BKB_BASE = "https://bitcoinknowledge.dev"
MODEL = "claude-opus-4-6"
MAX_TOKENS = 4096
MAX_TOOL_ROUNDS = 10  # safety cap on agentic loop iterations

# ---------------------------------------------------------------------------
# System prompts
# ---------------------------------------------------------------------------

SYSTEM_QA = """\
You are Satoshi, a Bitcoin technical expert who speaks from the primary technical record.

Your knowledge comes from the Bitcoin Knowledge Base tools -- BIPs, BOLTs, bLIPs, \
mailing list archives, Delving Bitcoin forum, GitHub issues/PRs/commits, IRC logs, \
and Optech newsletters.

Rules:
- ALWAYS search the knowledge base before answering. Never answer from memory alone.
- Cite sources precisely: BIP/BOLT numbers, author names, dates, mailing list threads.
- If the KB has no record on a topic, say so plainly. Do not fabricate sources.
- Stay in scope: protocol design, implementation, developer discourse. \
No price talk, investment advice, altcoins, or economic philosophy.
- Be direct and precise. Explain technical concepts clearly but do not simplify \
to the point of inaccuracy."""

SYSTEM_VERIFY = """\
You are Satoshi, a Bitcoin technical verification agent.

Your job: determine whether a claim about Bitcoin's technical record is \
SUPPORTED, UNSUPPORTED, or has NO RECORD in the knowledge base.

Rules:
- Search the knowledge base thoroughly. Use multiple tools if needed.
- Respond with exactly one verdict: SUPPORTED, UNSUPPORTED, or NO RECORD.
- After the verdict, provide the primary source evidence (BIP/BOLT number, \
author, date, quote) that supports your determination.
- If the claim is partially correct, say UNSUPPORTED and explain what is wrong.
- Stay in scope: protocol, implementation, developer discourse only."""

# ---------------------------------------------------------------------------
# Tool definitions (Claude API tool_use format)
# ---------------------------------------------------------------------------

TOOLS = [
    {
        "name": "bkb_search",
        "description": "Full-text search across the Bitcoin knowledge base. Searches BIPs, BOLTs, mailing lists, GitHub, Delving Bitcoin, IRC, Optech. Use filters to narrow results.",
        "input_schema": {
            "type": "object",
            "properties": {
                "query": {"type": "string", "description": "Search query"},
                "source_type": {"type": "string", "description": "Filter by source type (e.g. 'bip', 'bolt', 'mailing_list', 'github_issue', 'github_pr', 'delving_bitcoin', 'irc', 'optech')"},
                "author": {"type": "string", "description": "Filter by author name"},
                "after": {"type": "string", "description": "Filter results after this date (YYYY-MM-DD)"},
                "before": {"type": "string", "description": "Filter results before this date (YYYY-MM-DD)"},
                "limit": {"type": "integer", "description": "Max results to return (default 10)"},
            },
            "required": ["query"],
        },
    },
    {
        "name": "bkb_get_bip",
        "description": "Get a specific Bitcoin Improvement Proposal by number. Returns full text, cross-references, and concept tags.",
        "input_schema": {
            "type": "object",
            "properties": {
                "number": {"type": "integer", "description": "BIP number (e.g. 341 for Taproot)"},
            },
            "required": ["number"],
        },
    },
    {
        "name": "bkb_get_bolt",
        "description": "Get a specific BOLT (Basis of Lightning Technology) specification by number.",
        "input_schema": {
            "type": "object",
            "properties": {
                "number": {"type": "integer", "description": "BOLT number"},
            },
            "required": ["number"],
        },
    },
    {
        "name": "bkb_get_blip",
        "description": "Get a specific bLIP (Bitcoin Lightning Improvement Proposal) by number.",
        "input_schema": {
            "type": "object",
            "properties": {
                "number": {"type": "integer", "description": "bLIP number"},
            },
            "required": ["number"],
        },
    },
    {
        "name": "bkb_get_lud",
        "description": "Get a specific LNURL document (LUD) by number.",
        "input_schema": {
            "type": "object",
            "properties": {
                "number": {"type": "integer", "description": "LUD number"},
            },
            "required": ["number"],
        },
    },
    {
        "name": "bkb_get_nut",
        "description": "Get a specific Cashu NUT (Notation, Usage, and Terminology) document by number.",
        "input_schema": {
            "type": "object",
            "properties": {
                "number": {"type": "integer", "description": "NUT number"},
            },
            "required": ["number"],
        },
    },
    {
        "name": "bkb_timeline",
        "description": "Get the chronological development history of a Bitcoin concept. Shows how an idea evolved through mailing lists, BIPs, implementations, and activation.",
        "input_schema": {
            "type": "object",
            "properties": {
                "concept": {"type": "string", "description": "Concept name (e.g. 'taproot', 'segwit', 'lightning')"},
            },
            "required": ["concept"],
        },
    },
    {
        "name": "bkb_references",
        "description": "Find all documents that reference a given entity (BIP, BOLT, GitHub item, etc). Useful for tracing how a spec influenced later work.",
        "input_schema": {
            "type": "object",
            "properties": {
                "entity": {"type": "string", "description": "Entity identifier (e.g. 'bip:341', 'bolt:11', 'github:bitcoin/bitcoin#12345')"},
            },
            "required": ["entity"],
        },
    },
    {
        "name": "bkb_find_commit",
        "description": "Search for Git commits by description. Optionally filter by repository.",
        "input_schema": {
            "type": "object",
            "properties": {
                "query": {"type": "string", "description": "Commit description to search for"},
                "repo": {"type": "string", "description": "Repository filter (e.g. 'bitcoin/bitcoin')"},
            },
            "required": ["query"],
        },
    },
    {
        "name": "bkb_get_document",
        "description": "Retrieve a specific document by its full ID. Use when you have a document reference from another tool's output.",
        "input_schema": {
            "type": "object",
            "properties": {
                "document_id": {"type": "string", "description": "Document ID in format 'source_type:source_id'"},
            },
            "required": ["document_id"],
        },
    },
]

# ---------------------------------------------------------------------------
# Tool handlers -- each calls bitcoinknowledge.dev and returns the response
# ---------------------------------------------------------------------------

def call_bkb(endpoint, params=None):
    """Make a GET request to the BKB API. Returns JSON string for Claude."""
    url = f"{BKB_BASE}{endpoint}"
    try:
        resp = requests.get(url, params=params, timeout=30)
        resp.raise_for_status()
        data = resp.json()
        # Truncate very large responses to stay within context limits
        text = json.dumps(data, indent=2)
        if len(text) > 15000:
            text = text[:15000] + "\n... [truncated -- use more specific queries to narrow results]"
        return text
    except requests.exceptions.HTTPError as e:
        if resp.status_code == 404:
            return json.dumps({"error": "not_found", "message": f"No record found at {endpoint}"})
        return json.dumps({"error": "http_error", "status": resp.status_code, "message": str(e)})
    except requests.exceptions.RequestException as e:
        return json.dumps({"error": "connection_error", "message": str(e)})


def handle_tool(name, input_data):
    """Route a tool call to the correct BKB endpoint."""
    if name == "bkb_search":
        params = {"q": input_data["query"]}
        for key in ("source_type", "author", "after", "before", "limit"):
            if key in input_data:
                params[key] = input_data[key]
        return call_bkb("/search", params)

    if name == "bkb_get_bip":
        return call_bkb(f"/bip/{input_data['number']}")

    if name == "bkb_get_bolt":
        return call_bkb(f"/bolt/{input_data['number']}")

    if name == "bkb_get_blip":
        return call_bkb(f"/blip/{input_data['number']}")

    if name == "bkb_get_lud":
        return call_bkb(f"/lud/{input_data['number']}")

    if name == "bkb_get_nut":
        return call_bkb(f"/nut/{input_data['number']}")

    if name == "bkb_timeline":
        return call_bkb(f"/timeline/{input_data['concept']}")

    if name == "bkb_references":
        return call_bkb(f"/references/{input_data['entity']}")

    if name == "bkb_find_commit":
        params = {"q": input_data["query"]}
        if "repo" in input_data:
            params["repo"] = input_data["repo"]
        return call_bkb("/find_commit", params)

    if name == "bkb_get_document":
        return call_bkb(f"/document/{input_data['document_id']}")

    return json.dumps({"error": "unknown_tool", "message": f"No handler for tool: {name}"})

# ---------------------------------------------------------------------------
# Agentic loop
# ---------------------------------------------------------------------------

def run_agent(query, verify=False):
    """Run the Satoshi agent: send query, handle tool calls, return final answer."""
    load_dotenv()
    api_key = os.getenv("ANTHROPIC_API_KEY")
    if not api_key:
        print("Error: ANTHROPIC_API_KEY not found. Add it to a .env file.")
        sys.exit(1)

    client = anthropic.Anthropic(api_key=api_key)
    system = SYSTEM_VERIFY if verify else SYSTEM_QA

    if verify:
        user_message = f"Verify this claim: {query}"
    else:
        user_message = query

    messages = [{"role": "user", "content": user_message}]

    for round_num in range(MAX_TOOL_ROUNDS):
        response = client.messages.create(
            model=MODEL,
            max_tokens=MAX_TOKENS,
            system=system,
            tools=TOOLS,
            messages=messages,
            thinking={"type": "adaptive"},
        )

        # Check if Claude wants to use tools
        if response.stop_reason == "tool_use":
            # Collect all tool results for this turn
            tool_results = []
            for block in response.content:
                if block.type == "tool_use":
                    print(f"  [{block.name}] {json.dumps(block.input)}", file=sys.stderr)
                    result = handle_tool(block.name, block.input)
                    tool_results.append({
                        "type": "tool_result",
                        "tool_use_id": block.id,
                        "content": result,
                    })

            # Feed tool results back
            messages.append({"role": "assistant", "content": response.content})
            messages.append({"role": "user", "content": tool_results})
        else:
            # Final text response -- extract and return
            for block in response.content:
                if hasattr(block, "text"):
                    return block.text
            return "[No text response from model]"

    return "[Max tool rounds reached -- agent stopped]"

# ---------------------------------------------------------------------------
# CLI
# ---------------------------------------------------------------------------

def main():
    parser = argparse.ArgumentParser(
        description="Satoshi Agent -- Bitcoin technical expert powered by bitcoinknowledge.dev",
        epilog="Examples:\n"
               '  python satoshi-agent.py "What is Taproot?"\n'
               '  python satoshi-agent.py --verify "Taproot activated in November 2021"\n',
        formatter_class=argparse.RawDescriptionHelpFormatter,
    )
    parser.add_argument("query", help="Your Bitcoin technical question or claim to verify")
    parser.add_argument("--verify", action="store_true", help="Verification mode: check a claim against the technical record")
    args = parser.parse_args()

    print(f"\n{'[VERIFY MODE]' if args.verify else '[Q&A MODE]'} {args.query}\n", file=sys.stderr)
    answer = run_agent(args.query, verify=args.verify)
    print(answer)


if __name__ == "__main__":
    main()
