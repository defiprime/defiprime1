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

Hugo site (Go). Content lives under `content/`:

| Directory | What's in it |
|---|---|
| `content/blog` | Blog posts and research articles |
| `content/product/stablecoins`, `content/product/lending`, `content/product/exchanges`, `content/product/perps`, `content/product/derivatives`, `content/product/payments` | Curated DeFi product listings by category |
| `content/product/prediction_markets`, `content/product/yield-aggregators`, `content/product/staking`, `content/product/dao`, `content/product/insurance` | More product categories |
| `content/product/analytics`, `content/product/infrastructure`, `content/product/assets-tokenization`, `content/product/kyc_identity`, `content/product/marketplaces`, `content/product/alternative-savings`, `content/product/assets-management-tools` | Remaining product sections |
| `content/events` | DeFi events calendar |
| `content/alternatives` | "Alternatives to X" comparison pages |

Templates are in `layouts/`, static assets in `assets/` and `static/`. Chain landing pages (e.g. `ethereum.md`, `solana.md`, `base.md`) live at the root of `content/`.

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
hugo server
```

Serves the site with live reload. Build to `public/` with:

```bash
hugo --minify
```

Netlify handles production deploys (see `netlify.toml`).

### Stylesheet

`assets/scss/` is not wired into the Hugo pipeline: the pages link the checked-in `static/assets/css/main.css`. After editing the SCSS, regenerate it with:

```bash
sass --style=compressed --no-source-map assets/scss/main.scss static/assets/css/main.css
```

The checked-in file came out of Jekyll's libsass, so the first run rewrites it in dart-sass formatting (the same rules, different whitespace and selector order).

### Testing

```bash
bash tests/run-tests.sh
```

Runs the parity gate against the golden Jekyll build. Override the golden build's path with the `JEKYLL_GOLDEN` environment variable.

```bash
cd tests && python3 -m unittest discover -p 'test_*.py'
```

Runs the unit suite.

### Content sync

Until cutover, content is authored in the Jekyll checkout and pulled into this repo:

```bash
python3 scripts/sync-content.py --source ../defiprime
```

### Search index

```bash
python3 scripts/algolia-index.py --dry-run
```

Preview what would be pushed to Algolia. Drop `--dry-run` to push for real; the script reads the admin key from `_algolia_api_key`.

## Contributing

See [CONTRIBUTING.md](CONTRIBUTING.md). For corrections or small edits, a PR against `master` works fine. For listing changes or new posts, use the forms above.
