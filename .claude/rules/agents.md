# Subagent Usage

- Use subagents to isolate research, exploration, and parallel searches from the main context
- One task per subagent -- do not overload a single agent with multiple unrelated goals
- Provide clear, complete prompts -- the subagent has no prior context
- Do not duplicate work between the main thread and a subagent
- Use `/clear` or context breaks between unrelated tasks to prevent context pollution
- For simple, directed searches (specific file/class/function), use Glob or Grep directly -- subagents are for broader exploration
