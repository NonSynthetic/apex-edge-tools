# apex-edge-tools

Client + CI action for **[apex-edge](https://apex-edge-coral.vercel.app)** — an x402 machine-payable API edge (Base + Solana USDC) with free discovery surfaces and a paid MCP tool surface.

## Paid services

| Offer | Price | Rail |
|---|---|---|
| **Code audit** — audit report, manual delivery ≤24h | **$5** | PayPal checkout (link in storefront PAID card) |
| Corpus search (`/api/v1/search?q=`) — 387-doc research index | $0.01/call | x402 |
| Audit checklist (`/api/v1/audit/checklist`) — 34-item static checklist | $0.05/call | x402 |
| Audit verdict (`/api/v1/audit/verdict`) — LLM security verdict on pasted code | $0.05/call | x402 |
| Pro chat (`/api/v1/chat/pro`) — routed LLM completion | $0.002/call | x402 |
| MCP `tools/call` — hash · uuid · base64 · time · price · corpus_search · checklist | $0.001/call | x402 |
| **Deep audit** — escrowed tier, 72h manual dispute window | **$25** | PayPal (storefront) |
| Tip jar | $1+ | PayPal (storefront) |

**Direct crypto (receive-only):** Base USDC `0xe70F099F0e139f8A2D8ac6E48f7457d99738B968` · Solana USDC `2o3uMNi5FviB3CZpLcFafpbQcmg48jdt8rb7TYePjTuo` · TRX · BTC/Lightning — payTo addresses are also in every 402 challenge envelope.

## Live surfaces
| | |
|---|---|
| Storefront | https://apex-edge-coral.vercel.app |
| MCP endpoint | `POST /mcp` — `tools/list` free, `tools/call` per-tool x402 price ($0.001–$0.25) |
| A2A adapter | `POST /a2a` — `message/send` → price quote + x402 pay route (quote-only, no task execution) |
| Paid catalog | `/.well-known/x402`, `/openapi.json`, `/llms.txt`, `/ai.txt` |
| Agent card | a2aregistry.org (live), registry.modelcontextprotocol.io (indexing) |
| Game | [SWARM ANCHOR](https://nonsynthetic.pages.dev/games/anchor/) |

## Use
```bash
python client.py            # tools/list — free
python client.py hash '{"input":"hello"}'   # returns x402 402 challenge
python client.py corpus_search '{"q":"monetization"}'
```

## In CI
```yaml
- uses: NonSynthetic/apex-edge-tools@v1
  with:
    tool: hash   # optional; probes the paid endpoint's 402 challenge
```

Payment: x402 v2 — Base mainnet USDC (CDP facilitator) or Solana USDC-SPL. Pay-to addresses are in the 402 challenge envelope. No signup, no API keys — pay-per-call.
