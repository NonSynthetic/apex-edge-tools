# apex-edge — x402 machine-payable utility edge

Pay-per-call utility API for agents. Prices in USDC on Base and Solana via
[x402](https://x402.org); unpaid calls return HTTP 402 payment descriptors.

- **MCP endpoint (Streamable HTTP):** `https://api.nonsynthetic.net/mcp`
- **REST:** `https://api.nonsynthetic.net/api/v1/*` (`openapi.json`, `llms.txt`)
- **Registry:** `net.nonsynthetic/apex-edge` (official MCP Registry)
- **Well-known:** `nonsynthetic.net/.well-known/agent-card.json` · `/.well-known/x402`

No auth, no signup — connect an MCP client or `curl -X POST` a tool call and
handle the 402 challenge.

Contents: `client.py` (x402-aware client example), `action.yml` (agent action
descriptor), `server.json` (MCP registry manifest), `index.html` (landing).
