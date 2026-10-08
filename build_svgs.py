"""Gera os SVGs do perfil do GitHub (tema claro e escuro) a partir de um só desenho.

Direção de arte: "sala de controle" — superfície lisa, números pesados, rótulos
em monoespaçada como painel de status, fios finos, ícones de traço desenhados à
mão, UM acento. Sem degradê, sem brilho, sem emoji, sem pílula.
"""
from pathlib import Path

OUT = Path(__file__).parent / "assets"
OUT.mkdir(exist_ok=True)

THEMES = {
    "dark": dict(bg="#0F1115", panel="#161920", line="#262A33", ink="#EEECE7", sub="#A9AEB8",
                 mute="#6E7480", accent="#3FB8A4"),
    "light": dict(bg="#F5F3EF", panel="#FFFFFF", line="#E1DDD5", ink="#15171C", sub="#454A54",
                  mute="#7A7F89", accent="#0E7A6B"),
}

SANS = "'Segoe UI', 'Helvetica Neue', Helvetica, Arial, sans-serif"
MONO = "'Cascadia Mono', 'SFMono-Regular', Consolas, 'Liberation Mono', monospace"

# Ícones de traço, desenhados numa grade 48x48 (stroke = currentColor do grupo).
ICONS = {
    # headset
    "teamspeak": "M10 28v-4a14 14 0 0 1 28 0v4 M10 28h6v10h-6z M32 28h6v10h-6z M38 38c0 4-4 6-10 6h-3",
    # mira
    "hunteds": "M24 8v8 M24 32v8 M8 24h8 M32 24h8 M24 14a10 10 0 1 1 0 20a10 10 0 1 1 0-20 M24 22v4 M22 24h4",
    # grade de blocos + tecla
    "mythor": "M8 10h14v12H8z M26 10h14v12H26z M8 26h14v12H8z M26 30h14v8H26z M30 34h6",
    # espada
    "deletebra": "M34 8l6 0 0 6-18 18-6-6z M16 26l6 6 M12 30l6 6 M10 38l-3 3 M14 34l-6 6",
    # esfera com estrelas
    "otdbo": "M24 8a16 16 0 1 1 0 32a16 16 0 1 1 0-32 M24 18l1.6 3.4 3.7.5-2.7 2.6.7 3.7-3.3-1.8-3.3 1.8.7-3.7-2.7-2.6 3.7-.5z",
    # volante
    "midnight": "M24 8a16 16 0 1 1 0 32a16 16 0 1 1 0-32 M24 20a4 4 0 1 1 0 8a4 4 0 1 1 0-8 M10 22h10 M28 22h10 M24 28v12",
    # coroa (lampião / servidor moderno)
    "lampiao": "M10 34l4-18 8 9 2-11 2 11 8-9 4 18z M10 38h28",
    # janelas empilhadas
    "wapplink": "M8 12h24v18H8z M16 20h24v18H16z M20 24h2 M24 24h2",
}


def esc(text: str) -> str:
    return text.replace("&", "&amp;").replace("<", "&lt;").replace(">", "&gt;")


def svg(width: int, height: int, body: str, t: dict, label: str) -> str:
    return (
        f'<svg xmlns="http://www.w3.org/2000/svg" width="{width}" height="{height}" '
        f'viewBox="0 0 {width} {height}" role="img" aria-label="{esc(label)}">\n'
        f'<rect width="{width}" height="{height}" fill="{t["bg"]}"/>\n{body}</svg>\n'
    )


def icon(name: str, x: int, y: int, color: str, scale: float = 1.0) -> str:
    return (
        f'<g transform="translate({x} {y}) scale({scale})" fill="none" stroke="{color}" '
        f'stroke-width="2.2" stroke-linecap="round" stroke-linejoin="round">'
        f'<path d="{ICONS[name]}"/></g>\n'
    )


def hero(t: dict) -> str:
    stats = [
        ("10,000+", "TEAMSPEAK USERS"),
        ("300+", "HOSTING CLIENTS"),
        ("1,000+", "ONLINE · DELETEBRA"),
        ("500+", "ONLINE · OTDBO"),
    ]
    b = []
    b.append(f'<text x="72" y="86" font-family="{MONO}" font-size="15" fill="{t["accent"]}">● SYSTEMS NOMINAL</text>')
    b.append(f'<text x="1208" y="86" font-family="{MONO}" font-size="15" fill="{t["mute"]}" text-anchor="end">since 2016</text>')
    b.append(f'<text x="66" y="196" font-family="{SANS}" font-size="104" font-weight="800" letter-spacing="-3" fill="{t["ink"]}">Lucas A.</text>')
    b.append(f'<text x="72" y="246" font-family="{SANS}" font-size="24" font-weight="600" fill="{t["ink"]}">Founder of TSxHost. Creator of Deletebra and OTDBO.</text>')
    b.append(f'<text x="72" y="280" font-family="{SANS}" font-size="19" fill="{t["sub"]}">I build the tools Tibia guilds run on — and the game servers thousands of players call home.</text>')
    b.append(f'<line x1="72" y1="326" x2="1208" y2="326" stroke="{t["line"]}" stroke-width="1"/>')
    col = (1208 - 72) / 4
    for i, (num, lab) in enumerate(stats):
        x = 72 + i * col
        if i:
            b.append(f'<line x1="{x - 24:.0f}" y1="352" x2="{x - 24:.0f}" y2="430" stroke="{t["line"]}" stroke-width="1"/>')
        b.append(f'<text x="{x:.0f}" y="398" font-family="{SANS}" font-size="52" font-weight="800" letter-spacing="-1.5" fill="{t["ink"]}">{esc(num)}</text>')
        b.append(f'<rect x="{x:.0f}" y="410" width="28" height="3" fill="{t["accent"]}"/>')
        b.append(f'<text x="{x:.0f}" y="436" font-family="{MONO}" font-size="13" letter-spacing="1.4" fill="{t["mute"]}">{esc(lab)}</text>')
    return svg(1280, 480, "\n".join(b) + "\n", t, "Lucas A. — Founder of TSxHost, creator of Deletebra and OTDBO. 10,000+ TeamSpeak users, 300+ clients, 1,000+ players online on Deletebra, 500+ on OTDBO.")


CARDS = [
    ("teamspeak", "TSxHost", "TeamSpeak hosting & guild automation",
     ["Multi-tenant bot for Tibia guilds: live lists,", "respawn queue, monthly schedules, death alerts,",
      "guild bank and a full web control panel."],
     "10,000+ users · 300+ clients", "Laravel · ReactPHP · Node · Redis"),
    ("hunteds", "Hunteds", "Real-time guild-war intelligence",
     ["Who is online, who died, who killed —", "streamed live to every member's browser",
      "the moment it happens."],
     "Live, second by second", "TypeScript · Socket.IO · React"),
    ("mythor", "Mythor", "Shared-account command center",
     ["Multi-guild panel for team-owned characters,", "plus a desktop companion that types",
      "credentials and 2FA on a global hotkey."],
     "Multi-guild · desktop app", "Laravel · Vue · .NET"),
    ("deletebra", "Deletebra", "Tibia 8.60, rebuilt from the binary up",
     ["Reverse-engineered the original client to add", "a Store, Market and Hunt Analyser — and doubled",
      "rendering performance: 425 → 1,000 FPS."],
     "1,000+ online · since 2016", "C++ · x86 RE · Direct3D · Lua"),
    ("otdbo", "OTDBO", "Dragon Ball, as an Open Tibia world",
     ["A full custom universe: transformations,", "item tiers, offline player shops and its own",
      "client experience."],
     "500+ online · since 2021", "C++ · Lua · OTClient"),
    ("midnight", "Midnight Los Santos", "Roleplay server on MTA:SA",
     ["Phone with chat and voice calls, street races,", "car audio from any link, real car models",
      "and a full admin panel — all custom-built."],
     "Built from scratch", "Lua · MTA:SA · Node"),
]


def projects(t: dict) -> str:
    cols, card_w, card_h, gap_x, gap_y, top = 2, 556, 238, 24, 24, 24
    rows = (len(CARDS) + cols - 1) // cols
    height = top + rows * card_h + (rows - 1) * gap_y + 24
    b = []
    for i, (ico, name, tagline, desc, metric, stack) in enumerate(CARDS):
        cx = 72 + (i % cols) * (card_w + gap_x)
        cy = top + (i // cols) * (card_h + gap_y)
        b.append(f'<rect x="{cx}" y="{cy}" width="{card_w}" height="{card_h}" rx="6" fill="{t["panel"]}" stroke="{t["line"]}"/>')
        b.append(icon(ico, cx + 28, cy + 26, t["accent"], 0.92))
        b.append(f'<text x="{cx + 88}" y="{cy + 50}" font-family="{SANS}" font-size="26" font-weight="800" letter-spacing="-0.5" fill="{t["ink"]}">{esc(name)}</text>')
        b.append(f'<text x="{cx + 88}" y="{cy + 74}" font-family="{SANS}" font-size="15" font-weight="600" fill="{t["sub"]}">{esc(tagline)}</text>')
        for j, line in enumerate(desc):
            b.append(f'<text x="{cx + 28}" y="{cy + 112 + j * 23}" font-family="{SANS}" font-size="15.5" fill="{t["sub"]}">{esc(line)}</text>')
        b.append(f'<line x1="{cx + 28}" y1="{cy + 182}" x2="{cx + card_w - 28}" y2="{cy + 182}" stroke="{t["line"]}"/>')
        b.append(f'<text x="{cx + 28}" y="{cy + 212}" font-family="{SANS}" font-size="16" font-weight="700" fill="{t["accent"]}">{esc(metric)}</text>')
        b.append(f'<text x="{cx + card_w - 28}" y="{cy + 212}" font-family="{MONO}" font-size="12.5" fill="{t["mute"]}" text-anchor="end">{esc(stack)}</text>')
    return svg(1280, height, "\n".join(b) + "\n", t, "Projects: " + ", ".join(c[1] for c in CARDS))


TIMELINE = [
    ("2016", "Deletebra", ["Opens its doors and grows", "past 1,000 players online."]),
    ("2021", "OTDBO", ["A Dragon Ball universe on Tibia,", "500+ players online."]),
    ("TODAY", "TSxHost", ["10,000+ TeamSpeak users", "and 300+ hosting clients."]),
    ("TODAY", "Hunteds · Mythor", ["Guild-war tooling trusted", "by top guilds."]),
]


def timeline(t: dict) -> str:
    b = []
    y = 70
    col = (1208 - 72) / len(TIMELINE)
    b.append(f'<line x1="72" y1="{y}" x2="1208" y2="{y}" stroke="{t["line"]}" stroke-width="2"/>')
    for i, (year, name, lines) in enumerate(TIMELINE):
        x = 72 + i * col
        b.append(f'<circle cx="{x + 7:.0f}" cy="{y}" r="7" fill="{t["bg"]}" stroke="{t["accent"]}" stroke-width="2.5"/>')
        b.append(f'<text x="{x:.0f}" y="{y - 24}" font-family="{MONO}" font-size="14" letter-spacing="2" fill="{t["accent"]}">{year}</text>')
        b.append(f'<text x="{x:.0f}" y="{y + 46}" font-family="{SANS}" font-size="22" font-weight="800" fill="{t["ink"]}">{esc(name)}</text>')
        for j, line in enumerate(lines):
            b.append(f'<text x="{x:.0f}" y="{y + 74 + j * 22}" font-family="{SANS}" font-size="15" fill="{t["sub"]}">{esc(line)}</text>')
    return svg(1280, 190, "\n".join(b) + "\n", t, "Timeline: Deletebra 2016, OTDBO 2021, TSxHost, Hunteds and Mythor today.")


STACK = [
    ("BACKEND", ["PHP 8.4 · Laravel 12", "Node.js · TypeScript", "Python · Lua", "C · C++ · C#"]),
    ("REAL-TIME & DATA", ["Redis Streams", "Socket.IO · ReactPHP", "MariaDB · MySQL", "Event-driven bots"]),
    ("FRONTEND", ["Filament · Livewire", "Vue · React · Vite", "Tailwind", "Electron · .NET"]),
    ("GAMES & INFRA", ["x86 reverse engineering", "OTX · Canary · OTClient", "TeamSpeak ServerQuery", "Linux · Nginx · Docker"]),
]


def stack(t: dict) -> str:
    b = []
    col = (1208 - 72) / len(STACK)
    for i, (title, items) in enumerate(STACK):
        x = 72 + i * col
        if i:
            b.append(f'<line x1="{x - 24:.0f}" y1="20" x2="{x - 24:.0f}" y2="176" stroke="{t["line"]}"/>')
        b.append(f'<text x="{x:.0f}" y="36" font-family="{MONO}" font-size="13" letter-spacing="1.8" fill="{t["accent"]}">{esc(title)}</text>')
        for j, item in enumerate(items):
            b.append(f'<text x="{x:.0f}" y="{74 + j * 30}" font-family="{SANS}" font-size="17" font-weight="600" fill="{t["ink"]}">{esc(item)}</text>')
    return svg(1280, 196, "\n".join(b) + "\n", t, "Stack: " + "; ".join(f"{a}: {', '.join(c)}" for a, c in STACK))


def section(t: dict, kicker: str, title: str) -> str:
    b = [
        f'<text x="72" y="40" font-family="{MONO}" font-size="14" letter-spacing="2.4" fill="{t["accent"]}">{esc(kicker)}</text>',
        f'<text x="70" y="88" font-family="{SANS}" font-size="38" font-weight="800" letter-spacing="-1" fill="{t["ink"]}">{esc(title)}</text>',
        f'<line x1="72" y1="112" x2="1208" y2="112" stroke="{t["line"]}"/>',
    ]
    return svg(1280, 124, "\n".join(b) + "\n", t, f"{kicker} — {title}")


SECTIONS = {
    "sec-work": ("01 / WORK", "What I've built"),
    "sec-journey": ("02 / JOURNEY", "A decade of Tibia"),
    "sec-stack": ("03 / STACK", "How it's built"),
}

for theme, t in THEMES.items():
    (OUT / f"hero-{theme}.svg").write_text(hero(t), encoding="utf-8")
    (OUT / f"projects-{theme}.svg").write_text(projects(t), encoding="utf-8")
    (OUT / f"timeline-{theme}.svg").write_text(timeline(t), encoding="utf-8")
    (OUT / f"stack-{theme}.svg").write_text(stack(t), encoding="utf-8")
    for key, (kicker, title) in SECTIONS.items():
        (OUT / f"{key}-{theme}.svg").write_text(section(t, kicker, title), encoding="utf-8")

print("ok:", sorted(p.name for p in OUT.glob("*.svg")))
