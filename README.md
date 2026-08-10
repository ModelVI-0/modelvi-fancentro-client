# fancentro-api-client-example

A minimal, open-source example client for the **Fancentro API** — a clean, readable starting point for developers building **Fancentro automation** and integrations on top of the [fancentroapi.com](https://fancentroapi.com) API service.

> **This is an EXAMPLE integration.** It demonstrates the client pattern, not a production SDK. For the live endpoints, authentication details, rate limits, and request/response schemas, always refer to the official docs at **[fancentroapi.com/docs](https://fancentroapi.com/docs)**.

## What it does

This repository shows the smallest useful pattern for talking to the Fancentro API from your own code:

- Loads your API key from an environment variable (never hard-coded)
- Configures a base URL so you can point at the right environment
- Wraps requests in a tiny, readable `FancentroClient` class you can extend
- Calls a single **placeholder** endpoint so you can confirm connectivity end-to-end

It is intentionally small. Clone it, read it in five minutes, and build your real integration on top.

## Why — the agency use-case

Creator agencies and management teams increasingly script repetitive back-office work instead of doing it by hand. A programmatic **Fancentro API** client is the foundation for that kind of **Fancentro automation**, for example:

- Syncing account or subscription data into your own CRM or dashboard
- Orchestrating routine publishing and back-office workflows
- Pulling reporting data for finance and analytics
- Wiring notifications into Slack, Discord, or internal tools

This example gives your engineers a vetted starting shape so they are not writing HTTP boilerplate from scratch.

## Requirements

- An API key from **[fancentroapi.com](https://fancentroapi.com)** — required; the example will not run without one
- Python 3.9+
- `pip`

## → Get your API key

You need an API key to make any real calls.

**→ Get your API key at [https://fancentroapi.com](https://fancentroapi.com)**

Sign up, create a key in your dashboard, and drop it into your `.env` (below).

## Install

```bash
git clone https://github.com/<your-org>/fancentro-api-client-example.git
cd fancentro-api-client-example
pip install -r requirements.txt
```

## Configure (`.env`)

Copy the example file and fill in your own values:

```bash
cp .env.example .env
```

`.env`:

```dotenv
# Your API key from https://fancentroapi.com (required)
API_KEY=your_api_key_here

# Base URL for the API service (placeholder — confirm the correct value in the docs)
BASE_URL=https://fancentroapi.com
```

Both values are read at runtime. Never commit your real `.env`.

## Usage

Run the example client:

```bash
python client.py
```

`client.py` (see the file for full comments) does three things:

1. Reads `API_KEY` and `BASE_URL` from the environment.
2. Builds a small `FancentroClient` with an `Authorization` header.
3. Calls one **placeholder** endpoint and prints the raw response so you can confirm your key works.

The endpoint path in the example is a placeholder. Replace it with a real endpoint from **[fancentroapi.com/docs](https://fancentroapi.com/docs)** before using this in anything real.

## This is an example

This is an **EXAMPLE** integration — it demonstrates the client pattern, not a production SDK. The endpoint paths and any response handling are placeholders. For the live endpoints, authentication scheme, rate limits, and request/response schemas, see **[https://fancentroapi.com/docs](https://fancentroapi.com/docs)**.

## Links

- API service & signup: **[https://fancentroapi.com](https://fancentroapi.com)**
- API documentation: **[https://fancentroapi.com/docs](https://fancentroapi.com/docs)**

## Disclaimer

This is an independent, unofficial example client provided for developers. "Fancentro" is a trademark of its respective owner; this project is not affiliated with or endorsed by that owner. Use it in accordance with all applicable terms of service and laws.

## License

MIT
