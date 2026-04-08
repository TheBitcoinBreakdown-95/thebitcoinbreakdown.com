# /import-contacts

File one or more contacts into the JC Bitcoin CRM.

## What this command does

Takes contact information in any format -- natural language, pasted CSV snippet, vCard text, or structured data -- and creates or updates contact files in `JC BTC/CRM/contacts/`.

## How to use it

Paste raw contact data after the command. Examples:

**Natural language:**
```
/import-contacts
Add Sarah Chen, telegram @sarahchen, attended meetup #5
```

**Multiple contacts:**
```
/import-contacts
- John Torres, john@example.com, @jt_btc on X, met at meetup #6
- Maya Patel, maya@example.com, phone +12015550123
```

**Pasted from Luma/Meetup/Eventbrite:**
```
/import-contacts
Name: Alex Rivera
Email: alex@example.com
Event: JC BTC #6
```

**From a phone contact (text/Telegram paste):**
```
/import-contacts
Name: Mike D
Phone: 201-555-0198
Telegram: @miked_btc
Source: personal referral from James
```

## What Claude will do

1. Parse the input -- handle any format, ask for clarification only if genuinely ambiguous
2. Normalize each contact: title-case name, lowercase email, strip @ from handles, E.164 phone format
3. Check `CRM/contacts/` for an existing file matching by email (first), then by normalized name
4. **New contact:** generate the next sequential ID (jcbtc-NNN), create `CRM/contacts/firstname-lastname.md`
5. **Existing contact:** update `last_contact` to today, append event ID to `events_attended` if provided
6. Report what was done: file path, ID assigned, fields set, any fields left blank

## Field reference

| Field | Format | Notes |
|-------|--------|-------|
| id | jcbtc-NNN | Auto-assigned, never edit manually |
| name | "First Last" | Title case |
| email | lowercase | |
| phone | +12015551234 | E.164 format |
| telegram | handle | No leading @ |
| x_handle | handle | No leading @ |
| status | new / active / core / speaker / sponsor / inactive | Default: new |
| source | luma / meetup / eventbrite / telegram / x / referral / manual | |
| privacy | normal / sensitive | Use sensitive for public officials, journalists |
| events_attended | ["jcbtc-005", "jcbtc-006"] | Event IDs |

## Rules

- Never put names or PII in commit messages -- use event-level descriptions only
- Raw CSVs and vCards go in `CRM/sources/` (gitignored) -- never commit them
- If unsure whether a contact already exists, check before creating a duplicate
- Leave fields blank rather than guessing -- blank is better than wrong data
