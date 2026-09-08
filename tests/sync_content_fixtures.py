import importlib.util
import os

HERE = os.path.dirname(os.path.abspath(__file__))
SCRIPT = os.path.join(HERE, os.pardir, "scripts", "sync-content.py")


def load_module():
    spec = importlib.util.spec_from_file_location("sync_content", SCRIPT)
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    return module


SOURCE_FILES = {
    "_config.yml": (
        "title: DefiPrime.com\n"
        "collections_dir: collections\n"
        "collections:\n"
        "  lending:\n"
        "    output: true\n"
        "    permalink: /product/:name\n"
        "  perps:\n"
        "    output: true\n"
        "    permalink: /product/:name\n"
        "  events:\n"
        "  alternatives:\n"
        "    output: true\n"
        "    permalink: /product/:name\n"
        "defaults:\n"
        "  - values:\n"
        '      layout: "product"\n'
    ),
    "collections/_posts/2020-01-01-hello.md": (
        "---\r\n"
        "git-date: 2020-01-01T00:00:00-08:00\r\n"
        "layout: [blog]\r\n"
        'title: "Hello"\r\n'
        "permalink: hello\r\n"
        "tags: ['Interview']\r\n"
        "redirect_from:\r\n"
        "  - old-hello\r\n"
        "---\r\n"
        "Watch this.\r\n"
        "\r\n"
        '{% youtube "https://www.youtube.com/watch?v=qQQkn361niI" %}\r\n'
    ),
    "collections/_posts/2019-04-01-lending.md": (
        "---\n"
        "layout: page\n"
        'title: "Lending"\n'
        "permalink: decentralized-lending\n"
        "category: products\n"
        "filter-by: ecosystem, platform, type, filter\n"
        "redirect_from:\n"
        "  - decentralized_lending\n"
        "cards: lending\n"
        "---\n"
        "Lending copy.\n"
    ),
    "collections/_lending/APY.Vision.md": (
        "---\nproduct-title: APY.Vision\ntype: non-custodial\n---\n"
    ),
    "collections/_lending/Aevo.md": (
        "---\nproduct-title: Aevo\ncoltitle: \"Lending\"\n---\nlending copy\n"
    ),
    "collections/_perps/Aevo.md": (
        "---\nproduct-title: Aevo\ncoltitle: \"Perps\"\n---\nperps copy\n"
    ),
    "collections/_alternatives/1inch.md": (
        "---\n"
        "layout: alternatives\n"
        'title: "1inch Alternatives"\n'
        "permalink: 1inch-alternatives\n"
        "---\n"
        "Alternatives copy.\n"
    ),
    "collections/_events/2025-01-01-devcon.md": (
        '---\r\nproduct-title: "Devcon"\r\ndate: 2026-05-05\r\n---\r\n'
    ),
    "index.md": (
        "---\n"
        "layout: default\n"
        "pagetitle: DeFi\n"
        "featured-image: /images/og.png\n"
        "redirect_from:\n"
        "  - product\n"
        "---\n"
        "\n"
        "{% assign posts = site.categories.blog %}\n"
    ),
    "blog.md": (
        "---\n"
        "layout: blog-list\n"
        "title: DeFi Blog\n"
        "permalink: /blog/\n"
        "pagination:\n"
        "  enabled: true\n"
        "  category: blog\n"
        "---\n"
        "{% for post in paginator.posts %}{% endfor %}\n"
    ),
    "alternatives.md": (
        "---\n"
        "layout: alternatives\n"
        "title: DeFi Alternatives\n"
        "h1title: DeFi Alternatives\n"
        "permalink: /alternatives/\n"
        "---\n"
        "\n"
        "Filter by category and explore the ecosystem.\n"
    ),
    "about.md": (
        "---\n"
        "layout: static\n"
        "title: About\n"
        "permalink: about\n"
        "---\n"
        "\n"
        "Plain prose, no template tags.\n"
    ),
    "ethereum.md": (
        "---\n"
        "layout: ecosystem\n"
        "title: Ethereum DeFi Ecosystem\n"
        "permalink: ethereum\n"
        "---\n"
        "\n"
        "{% assign all_projects = site.lending %}\n"
        "We have {{ counter }} projects.\n"
    ),
    "404.md": (
        "---\n"
        "layout: default\n"
        "title: Not Found\n"
        "permalink: 404.html\n"
        "---\n"
        "{% for post in site.posts %}{% endfor %}\n"
    ),
    "README.md": "---\ntitle: readme\n---\nignore me\n",
    "CLAUDE.md": "# Project Instructions\n",
    "robots.txt": "User-agent: *\nAllow: /\n",
    "llms.txt": (
        "---\nlayout: null\npermalink: /llms.txt\n---\n{% for post in site.posts %}{% endfor %}\n"
    ),
    "_data/authors.yml": ("Defiprime:\r\n  name: Sergej\r\n  slug: sawinyh\r\n"
                          "sawinyh:\r\n  name: Sergej\r\n"),
    "images/og.png": "PNGDATA",
    "images/blog/new.png": "NEWPNG",
    "defiprime.tokenlist.json": '{"name": "defiprime"}\n',
    "favicon.ico": "ICO",
    "favicon.png": "PNG",
    "ogp-template.png": "OGP",
}

DEST_FILES = {
    "hugo.toml": 'baseURL = "https://defiprime.com"\n',
    "content/_index.md": "---\npagetitle: DeFi\nfeatured-image: /images/og.png\n---\n",
    "content/blog/_index.md": (
        "---\nlayout: blog-list\ntitle: DeFi Blog\nurl: /blog/\n---\n"
    ),
    "content/ethereum.md": (
        "---\n"
        "layout: ecosystem\n"
        "title: Ethereum DeFi Ecosystem\n"
        "url: ethereum\n"
        "stats_ecosystems:\n"
        '  - label: "Ethereum"\n'
        '    filter: "ethereum"\n'
        "---\n"
    ),
    "content/404.md": '---\nlayout: "404"\ntitle: Not Found\nurl: 404.html\n---\n',
    "content/about.md": "---\nlayout: static\ntitle: About\nurl: about\n---\n\nOld prose.\n",
    "content/stale-page.md": "---\ntitle: stale\n---\n",
    "content/product/_index.md": '---\ntitle: "Products"\ncascade:\n  type: "product"\n---\n',
    "content/product/lending/_index.md": '---\ntitle: "lending"\n---\n',
    "content/product/perps/_index.md": '---\ntitle: "perps"\n---\n',
    "content/product/lending/stale.md": "---\nurl: /product/stale.html\n---\n",
    "content/alternatives/_index.md": '---\ntitle: "Alternatives"\n---\n',
    "content/events/_index.md": '---\ntitle: "Events"\n---\n',
    "content/events/2025-01-01-gone.md": "---\nproduct-title: Gone\n---\n",
    "content/airdrop/_index.md": '---\ntitle: "Airdrops"\n---\n',
    "content/airdrop/some-airdrop.md": "---\ntitle: drop\n---\n",
    "content/crypto-airdrops.md": "---\ntitle: airdrops\n---\n",
    "content/solana-airdrops.md": "---\ntitle: airdrops\n---\n",
    "content/blog/2020-01-01-hello.md": "---\nlayout: blog\nurl: /hello.html\n---\nstale\n",
    "content/blog/2018-01-01-removed.md": "---\nlayout: blog\nurl: /removed.html\n---\n",
    "images/og.png": "LEGACY",
    "static/images/og.png": "OLDPNG",
    "static/images/gone.png": "GONE",
    "static/robots.txt": "old robots\n",
    "data/authors.yaml": "old\n",
    "content/authors/stale/_index.md": "---\nlayout: author_page\n---\n",
    "scripts/migrate-content.sh": "#!/usr/bin/env bash\n",
    "layouts/shortcodes/figure.html": "<figure></figure>\n",
}


def build_tree(root, files):
    for rel, content in files.items():
        path = os.path.join(root, rel)
        os.makedirs(os.path.dirname(path), exist_ok=True)
        with open(path, "w", encoding="utf-8") as handle:
            handle.write(content)


def snapshot(root):
    out = {}
    for dirpath, dirnames, filenames in os.walk(root):
        dirnames[:] = sorted(dirnames)
        for name in sorted(filenames):
            path = os.path.join(dirpath, name)
            with open(path, "r", encoding="utf-8") as handle:
                out[os.path.relpath(path, root)] = handle.read()
    return out
