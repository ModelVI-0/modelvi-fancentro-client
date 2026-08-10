"""
Minimal example client for the Fancentro API (via fancentroapi.com).

This is an EXAMPLE integration. It shows the smallest useful pattern for
authenticating with your API key and making a request. The endpoint path
below is a PLACEHOLDER -- replace it with a real endpoint from the docs:

    https://fancentroapi.com/docs

Get your API key at:

    https://fancentroapi.com
"""

import os
import sys

import requests  # pip install requests


class FancentroClient:
    """A tiny, extendable client for the Fancentro API.

    Extend this class with one method per endpoint you need. Keeping the
    HTTP details in one place keeps your integration code readable and
    makes Fancentro automation easier to maintain over time.
    """

    def __init__(self, api_key: str, base_url: str, timeout: int = 30):
        if not api_key:
            raise ValueError(
                "Missing API key. Set API_KEY in your environment. "
                "Get one at https://fancentroapi.com"
            )
        self.base_url = base_url.rstrip("/")
        self.timeout = timeout
        self.session = requests.Session()
        # An Authorization header is a common pattern. Confirm the exact
        # scheme the API expects (Bearer token, custom header, etc.) in the
        # official docs: https://fancentroapi.com/docs
        self.session.headers.update(
            {
                "Authorization": f"Bearer {api_key}",
                "Accept": "application/json",
            }
        )

    def ping(self) -> requests.Response:
        """Call a PLACEHOLDER endpoint to confirm connectivity.

        NOTE: "/v1/ping" is NOT guaranteed to exist. Replace it with a real
        endpoint from https://fancentroapi.com/docs (for example an account
        or status endpoint) before using this for anything real.
        """
        # --- replace with the real endpoint from fancentroapi.com/docs ---
        url = f"{self.base_url}/v1/ping"
        # -----------------------------------------------------------------
        return self.session.get(url, timeout=self.timeout)


def main() -> int:
    # Read config from the environment (see .env.example).
    api_key = os.environ.get("API_KEY", "")
    base_url = os.environ.get("BASE_URL", "https://fancentroapi.com")

    try:
        client = FancentroClient(api_key=api_key, base_url=base_url)
    except ValueError as err:
        print(f"Config error: {err}", file=sys.stderr)
        return 1

    print(f"Calling placeholder endpoint on {base_url} ...")

    try:
        response = client.ping()
    except requests.RequestException as err:
        print(f"Request failed: {err}", file=sys.stderr)
        return 1

    # We deliberately DO NOT assume a response schema here: this is an example,
    # and the real response shape is defined by the API docs, not by us.
    print(f"HTTP status: {response.status_code}")
    print("Raw response body (shape defined by the API -- see the docs):")
    print(response.text)

    return 0


if __name__ == "__main__":
    raise SystemExit(main())
