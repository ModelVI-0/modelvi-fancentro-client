# modelvi-fancentro-client — schedule posts to Fancentro via the ModelVI API

A minimal **example integration** (Python) that schedules posts to **Fancentro** through the [ModelVI](https://modelvi.com/sign-up?utm_source=github&utm_medium=owned-track&utm_campaign=modelvi-fancentro-client) partner API — one of the 14 creator platforms ModelVI posts to (code `FNC`).

**[▶ Get your API key →](https://modelvi.com/sign-up?utm_source=github&utm_medium=owned-track&utm_campaign=modelvi-fancentro-client)** · [API docs](https://modelvi.com/agent-api) · [Pricing](https://modelvi.com/pricing)

![example](https://img.shields.io/badge/example-MIT-blue) ![python](https://img.shields.io/badge/python-3.9+-green)

---

> **Honest scope:** ModelVI is an independent posting/automation tool. **Fancentro is a third-party platform ModelVI posts _to_** — this is **not** an official Fancentro API and isn't affiliated with Fancentro. It's a small client that uses ModelVI's partner API to schedule content on a creator's connected Fancentro account (platform code `FNC`).

## What this is

An MIT-licensed example that authenticates with a ModelVI partner key (`mvk_<keyId>_<secret>`) and schedules a post to Fancentro via `POST /schedule` with `platforms: ["FNC"]`. It talks only to the public ModelVI partner API.

## Quickstart

```bash
pip install requests
export MODELVI_API_KEY="mvk_<keyId>_<secret>"
python example.py
```

`example.py` reads a model id from `GET /model_list`, then sends `POST /schedule` with the caption (`title`), `platforms: ["FNC"]`, `scheduledAt` (ISO-8601 UTC), and `type` (`1`=FREE · `2`=FANS · `3`=PAID). Responses are `{ "success": true, "payload": … }`.

## Use cases / keywords

**fancentro posting bot** · postbot fancentro · fancentro automation · fancentro scheduler · schedule fancentro posts · post to Fancentro via API · creator posting automation.

## Honest note

Minimal example — no retries/pagination/media upload. Authoritative reference: **[modelvi.com/agent-api](https://modelvi.com/agent-api)** · **[modelvi.com/partner-api-docs](https://modelvi.com/partner-api-docs)**. Public ModelVI partner API only; no proprietary logic here.

**[▶ Get your API key →](https://modelvi.com/sign-up?utm_source=github&utm_medium=owned-track&utm_campaign=modelvi-fancentro-client)** — see [pricing](https://modelvi.com/pricing). MIT licensed.
