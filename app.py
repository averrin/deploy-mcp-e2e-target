"""Minimal HTTP server used as a deployment target for deploy-mcp e2e tests."""

import http.server
import json


class Handler(http.server.BaseHTTPRequestHandler):
    def do_GET(self):
        body = json.dumps({"status": "ok", "service": "deploy-mcp-e2e-target"})
        self.send_response(200)
        self.send_header("Content-Type", "application/json")
        self.end_headers()
        self.wfile.write(body.encode())

    def log_message(self, format, *args):
        pass  # suppress logs


if __name__ == "__main__":
    server = http.server.HTTPServer(("0.0.0.0", 8000), Handler)
    print("e2e target listening on :8000")
    server.serve_forever()
