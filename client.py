#!/usr/bin/env python3
"""apex-edge MCP client — calls the free tools/list and paid tools/call.

tools/list is free. tools/call returns an HTTP 402 challenge (x402 v2);
complete payment on Base or Solana USDC to the payTo in the challenge.
"""
import json, sys, urllib.request

BASE = "https://api.nonsynthetic.net/mcp"

def rpc(method, params=None):
    body = {"jsonrpc": "2.0", "id": 1, "method": method}
    if params: body["params"] = params
    req = urllib.request.Request(BASE, data=json.dumps(body).encode(),
        headers={"content-type": "application/json"})
    try:
        return json.loads(urllib.request.urlopen(req, timeout=20).read())
    except urllib.error.HTTPError as e:
        if e.code == 402:
            print("PAYMENT REQUIRED (x402):", file=sys.stderr)
            print(json.dumps(json.loads(e.read()), indent=2), file=sys.stderr)
            sys.exit(3)
        raise

if __name__ == "__main__":
    if len(sys.argv) < 2 or sys.argv[1] == "list":
        print(json.dumps(rpc("tools/list"), indent=2))
    else:
        name, args = sys.argv[1], (json.loads(sys.argv[2]) if len(sys.argv) > 2 else {})
        print(json.dumps(rpc("tools/call", {"name": name, "arguments": args}), indent=2))
