---
git-date: 2019-04-13T21:06:27-07:00
---
<a href="https://defiprime.com"><img src="https://defiprime.com/images/og.png" /></a>
<div align="center">
    <p align="center">
        <a href="#reposize">
            <img src="https://img.shields.io/github/repo-size/sneg55/defiprime.svg" /></a>
        <a href="https://twitter.com/intent/follow?screen_name=defiprime" alt="Follow us on twitter">
            <img src="https://img.shields.io/twitter/follow/defiprime.svg?label=Follow&style=social&logo=twitter" alt="Follow us on twitter"></a>
</div>

**Site:** <https://defiprime.com>
**X / Twitter:** <https://twitter.com/defiprime>
**Newsletter:** <https://defiprime.substack.com/>
**Telegram:** <https://t.me/defiprime>

## What is DeFiprime

DeFiprime is a media outlet covering decentralized finance since 2019. We publish practitioner research and curate a list of DeFi products worth paying attention to. We write for people who build, allocate capital, or regulate in this space.

### What we publish

- **Practitioner research** — risk premiums, yield decomposition, protocol mechanics. If the APY doesn't justify the downside, we show the arithmetic.
- **Regulatory reporting** — SEC releases, MiCA, enforcement actions, read against the primary source rather than a press release.
- **Infrastructure deep-dives** — stablecoin issuers, perps venues, prediction markets, credit markets, settlement layers.
- **Incident coverage** — exploits, governance blow-ups, peg events. What actually happened, and who bore the loss.

Full editorial positioning is on the [about page](https://defiprime.com/about).

## How the repo is organized

Jekyll site (Ruby). Content lives under `collections/`:

| Collection | What's in it |
|---|---|
| `_posts` | Blog posts and research articles |
| `_stablecoins`, `_lending`, `_exchanges`, `_perps`, `_derivatives`, `_payments` | Curated DeFi product listings by category |
| `_prediction-markets`, `_yield-aggregators`, `_staking`, `_dao`, `_insurance` | More product categories |
| `_analytics`, `_infrastructure`, `_assets-tokenization`, `_kyc-identity`, `_marketplaces`, `_alternative-savings`, `_assets-management-tools` | Remaining product sections |
| `_events` | DeFi events calendar |
| `_alternatives` | "Alternatives to X" comparison pages |

Page layouts, includes, and assets are in the standard Jekyll locations (`_layouts/`, `_includes/`, `assets/`, `images/`). Chain landing pages (e.g. `ethereum.md`, `solana.md`, `base.md`) live at the repo root.

## Product listing

We run a curated list. We aren't trying to catalogue every project — we surface the ones worth paying attention to. Criteria we actually apply:

- Live on mainnet with real usage. Not a testnet, not a pitch deck.
- Open to users regardless of jurisdiction, or at minimum honest about its geofencing. "Region is not supported" is not a feature.
- Chain-agnostic. We don't play tribal.
- No pay-to-list. This has always been the rule.

Submit a project via the [listing form](https://forms.fillout.com/t/by3Zq83Wnuus).

## Submitting events

Hosting a DeFi conference, research event, or hackathon? Use the [event listing form](https://forms.fillout.com/t/vGb7Tj5Q65us) and we'll add it to the [events calendar](https://defiprime.com/events).

## Advertising

The only ad format we run is native articles — interviews, use cases, technical explainers. No display ads, no sponsored listings. Listing a project and advertising are separate processes, and listings are free. Use the [advertising form](https://forms.fillout.com/t/ehASQ5qMzxus).

## Local development

```bash
bundle install
bundle exec jekyll serve
```

Site builds to `_site/` and serves on <http://127.0.0.1:4000>. Netlify handles production deploys (see `netlify.toml`).

## Contributing

See [CONTRIBUTING.md](CONTRIBUTING.md). For corrections or small edits, a PR against `master` works fine. For listing changes or new posts, use the forms above.
