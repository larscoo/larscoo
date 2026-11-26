"""
Generates all profile graphics (light + dark) into assets/.
Edit the CONTENT section, then run:  python tools/build.py
"""
from pathlib import Path
from html import escape

ROOT = Path(__file__).resolve().parent.parent
OUT = ROOT / "assets"

# ───────────────────────── CONTENT ─────────────────────────
NAME = "Lars"
NICK = "larscoo"
ROLE = "ICT System Administrator"
STUDY = "BSc Data & Computational Science @ FH Graubünden"
PLACE = "Switzerland, GL"

ABOUT = [
    ("01", "System administrator", "Keeping infrastructure dependable and turning repetitive work into clear, maintainable automation."),
    ("02", "Data scientist in training", "Studying Data & Computational Science at FH Graubünden and learning through practical projects."),
    ("03", "Practical builder", "Combining operations, software and data to create tools that solve real-world problems."),
]

PROJECTS = [
    ("DevOps", "ShelfOps", "Library application with Flask, PostgreSQL, Docker, CI/CD, Kubernetes and observability."),
    ("Automation", "Strava to Notion", "Syncs bike and running activities to Notion and sends monthly summaries to Discord."),
    ("Deep learning", "DL Swisstopo", "Toolkit for labelling map tiles and training models to detect Swiss pedestrian crossings."),
]

STACK = {
    "Development": [("Python", "Py", "#3776AB"), ("Flask", "Fl", "#3F3F46"),
                    ("REST APIs", "{}", "#0E7490"), ("HTML", "<>", "#E34F26"),
                    ("CSS", "#", "#1572B6"), ("SQL", "Sq", "#64748B")],
    "Data & ML": [("Pandas", "Pd", "#6B46C1"), ("NumPy", "Np", "#4DABCF"),
                  ("PyTorch", "Pt", "#EE4C2C"), ("Jupyter", "Jp", "#F37626"),
                  ("Matplotlib", "Mp", "#11557C"), ("scikit-learn", "Sk", "#F7931E")],
    "Infrastructure": [("Linux", "Lx", "#3F3F46"), ("Bash", "Sh", "#4EAA25"),
                       ("Docker", "Dk", "#2496ED"), ("Kubernetes", "K8", "#326CE5"),
                       ("Terraform", "Tf", "#7B42BC"), ("GitHub Actions", "GA", "#2088FF")],
    "Databases": [("PostgreSQL", "Pg", "#336791"), ("MySQL", "My", "#00758F"),
                  ("SQLite", "Sl", "#0F80CC"), ("Notion", "N", "#52525B")],
    "Observability": [("Prometheus", "Pr", "#E6522C"), ("Grafana", "Gf", "#F46800"),
                      ("Health checks", "+", "#22C55E"), ("Trivy", "Tr", "#1904DA")],
    "Tools": [("Git", "Gt", "#F05032"), ("GitHub", "Gh", "#3F3F46"),
              ("VS Code", "VS", "#007ACC"), ("PyCharm", "PC", "#21D789"),
              ("IntelliJ IDEA", "IJ", "#FE315D")],
}

LINKS = ["LinkedIn", "GitHub", "YouTube", "Instagram"]

ICONS = {
    "LinkedIn": ("#0A66C2", "M20.447 20.452h-3.554v-5.569c0-1.328-.027-3.037-1.852-3.037-1.853 0-2.136 1.445-2.136 2.939v5.667H9.351V9h3.414v1.561h.046c.477-.9 1.637-1.85 3.37-1.85 3.601 0 4.267 2.37 4.267 5.455v6.286zM5.337 7.433c-1.144 0-2.063-.926-2.063-2.065 0-1.138.92-2.063 2.063-2.063 1.14 0 2.064.925 2.064 2.063 0 1.139-.925 2.065-2.064 2.065zm1.782 13.019H3.555V9h3.564v11.452zM22.225 0H1.771C.792 0 0 .774 0 1.729v20.542C0 23.227.792 24 1.771 24h20.451C23.2 24 24 23.227 24 22.271V1.729C24 .774 23.2 0 22.222 0h.003z"),
    "GitHub": (None, "M12 .297c-6.63 0-12 5.373-12 12 0 5.303 3.438 9.8 8.205 11.385.6.113.82-.258.82-.577 0-.285-.01-1.04-.015-2.04-3.338.724-4.042-1.61-4.042-1.61C4.422 18.07 3.633 17.7 3.633 17.7c-1.087-.744.084-.729.084-.729 1.205.084 1.838 1.236 1.838 1.236 1.07 1.835 2.809 1.305 3.495.998.108-.776.417-1.305.76-1.605-2.665-.3-5.466-1.332-5.466-5.93 0-1.31.465-2.38 1.235-3.22-.135-.303-.54-1.523.105-3.176 0 0 1.005-.322 3.3 1.23.96-.267 1.98-.399 3-.405 1.02.006 2.04.138 3 .405 2.28-1.552 3.285-1.23 3.285-1.23.645 1.653.24 2.873.12 3.176.765.84 1.23 1.91 1.23 3.22 0 4.61-2.805 5.625-5.475 5.92.42.36.81 1.096.81 2.22 0 1.606-.015 2.896-.015 3.286 0 .315.21.69.825.57C20.565 22.092 24 17.592 24 12.297c0-6.627-5.373-12-12-12"),
    "YouTube": ("#FF0000", "M23.498 6.186a3.016 3.016 0 0 0-2.122-2.136C19.505 3.545 12 3.545 12 3.545s-7.505 0-9.377.505A3.017 3.017 0 0 0 .502 6.186C0 8.07 0 12 0 12s0 3.93.502 5.814a3.016 3.016 0 0 0 2.122 2.136c1.871.505 9.376.505 9.376.505s7.505 0 9.377-.505a3.015 3.015 0 0 0 2.122-2.136C24 15.93 24 12 24 12s0-3.93-.502-5.814zM9.545 15.568V8.432L15.818 12l-6.273 3.568z"),
    "Instagram": ("#E4405F", "M7.0301.084c-1.2768.0602-2.1487.264-2.911.5634-.7888.3075-1.4575.72-2.1228 1.3877-.6652.6677-1.075 1.3368-1.3802 2.127-.2954.7638-.4956 1.6365-.552 2.914-.0564 1.2775-.0689 1.6882-.0626 4.947.0062 3.2586.0206 3.6671.0825 4.9473.061 1.2765.264 2.1482.5635 2.9107.308.7889.72 1.4573 1.388 2.1228.6679.6655 1.3365 1.0743 2.1285 1.38.7632.295 1.6361.4961 2.9134.552 1.2773.056 1.6884.069 4.9462.0627 3.2578-.0062 3.668-.0207 4.9478-.0814 1.28-.0607 2.147-.2652 2.9098-.5633.7889-.3086 1.4578-.72 2.1228-1.3881.665-.6682 1.0745-1.3378 1.3795-2.1284.2957-.7632.4966-1.636.552-2.9124.056-1.2809.0692-1.6898.063-4.948-.0063-3.2583-.021-3.6668-.0817-4.9465-.0607-1.2797-.264-2.1487-.5633-2.9117-.3084-.7889-.72-1.4568-1.3876-2.1228C21.2982 1.33 20.628.9208 19.8378.6165 19.074.321 18.2017.1197 16.9244.0645 15.6471.0093 15.236-.005 11.977.0014 8.718.0076 8.31.0215 7.0301.0839m.1402 21.6932c-1.17-.0509-1.8053-.2453-2.2287-.408-.5606-.216-.96-.4771-1.3819-.895-.422-.4178-.6811-.8186-.9-1.378-.1644-.4234-.3624-1.058-.4171-2.228-.0595-1.2645-.072-1.6442-.079-4.848-.007-3.2037.0053-3.583.0607-4.848.05-1.169.2456-1.805.408-2.2282.216-.5613.4762-.96.895-1.3816.4188-.4217.8184-.6814 1.3783-.9003.423-.1651 1.0575-.3614 2.227-.4171 1.2655-.06 1.6447-.072 4.848-.079 3.2033-.007 3.5835.005 4.8495.0608 1.169.0508 1.8053.2445 2.228.408.5608.216.96.4754 1.3816.895.4217.4194.6816.8176.9005 1.3787.1653.4217.3617 1.056.4169 2.2263.0602 1.2655.0739 1.645.0796 4.848.0058 3.203-.0055 3.5834-.061 4.848-.051 1.17-.245 1.8055-.408 2.2294-.216.5604-.4763.96-.8954 1.3814-.419.4215-.8181.6811-1.3783.9-.4224.1649-1.0577.3617-2.2262.4174-1.2656.0595-1.6448.072-4.8493.079-3.2045.007-3.5825-.006-4.848-.0608M16.953 5.5864A1.44 1.44 0 1 0 18.39 4.144a1.44 1.44 0 0 0-1.437 1.4424M5.8385 12.012c.0067 3.4032 2.7706 6.1557 6.173 6.1493 3.4026-.0065 6.157-2.7701 6.1506-6.1733-.0065-3.4032-2.771-6.1565-6.174-6.1498-3.403.0067-6.156 2.771-6.1496 6.1738M8 12.0077a4 4 0 1 1 4.008 3.9921A3.9996 3.9996 0 0 1 8 12.0077"),
}

SECTIONS = {"s01": "About me", "s02": "Featured projects", "s03": "Tools I work with"}

# ───────────────────────── THEMES ─────────────────────────
THEMES = {
    "light": dict(bg="#FBFAF8", card="#FFFFFF", ink="#16161D", muted="#6B6B78",
                  line="#E7E5EE", chip="#F2F0F8", a1="#6A11CB", a2="#2575FC",
                  k="#A626A4", s="#2E8B57", t="#C2410C"),
    "dark": dict(bg="#0D1117", card="#161B22", ink="#E6EDF3", muted="#8B949E",
                 line="#30363D", chip="#1F2630", a1="#A78BFA", a2="#60A5FA",
                 k="#F472B6", s="#86EFAC", t="#FDBA74"),
}
SANS = "'Segoe UI', -apple-system, BlinkMacSystemFont, 'Helvetica Neue', Arial, sans-serif"
MONO = "'SF Mono', 'Cascadia Code', Consolas, 'Liberation Mono', monospace"

def e(s):
    return escape(s, quote=True)

def wrap(text, n):
    lines, cur = [], ""
    for w in text.split():
        if len(cur) + len(w) + 1 > n and cur:
            lines.append(cur); cur = w
        else:
            cur = f"{cur} {w}".strip()
    return lines + ([cur] if cur else [])

def svg(w, h, body, c):
    return (f'<svg xmlns="http://www.w3.org/2000/svg" width="{w}" height="{h}" viewBox="0 0 {w} {h}">'
            f'<defs><linearGradient id="g" x1="0" y1="0" x2="1" y2="1">'
            f'<stop offset="0" stop-color="{c["a1"]}"/><stop offset="1" stop-color="{c["a2"]}"/></linearGradient>'
            f'<style>.sans{{font-family:{SANS}}}.mono{{font-family:{MONO}}}</style></defs>{body}</svg>')

# ───────────────────────── GRAPHICS ─────────────────────────
def hero(c):
    W, H = 1280, 440
    code = [
        [("class ", c["k"]), (NICK, c["ink"]), (":", c["muted"])],
        [("  role  ", c["ink"]), ("= ", c["muted"]), ('"System Admin"', c["s"])],
        [("  study ", c["ink"]), ("= ", c["muted"]), ('"Data Science"', c["s"])],
        [("  base  ", c["ink"]), ("= ", c["muted"]), ('"Switzerland, Glarus"', c["s"])],
        [("  focus ", c["ink"]), ("= ", c["muted"]), ("[", c["muted"]), ('"Automation"', c["s"]), (",", c["muted"])],
        [("           ", c["muted"]), ('"Docker/Kubernetes"', c["s"]), (",", c["muted"])],
        [("           ", c["muted"]), ('"Machine Learning"', c["s"]), ("]", c["muted"])],
    ]
    code_svg = ""
    for i, line in enumerate(code):
        spans = "".join(f'<tspan fill="{col}">{e(t)}</tspan>' for t, col in line)
        code_svg += f'<text x="790" y="{180 + i*30}" class="mono" font-size="17" xml:space="preserve">{spans}</text>'
    body = f'''
<style>
@keyframes f1{{0%,100%{{transform:translate(0,0)}}50%{{transform:translate(40px,25px)}}}}
@keyframes f2{{0%,100%{{transform:translate(0,0)}}50%{{transform:translate(-35px,-20px)}}}}
@keyframes blink{{0%,49%{{opacity:1}}50%,100%{{opacity:0}}}}
@keyframes up{{from{{opacity:0;transform:translateY(12px)}}to{{opacity:1;transform:none}}}}
.o1{{animation:f1 9s ease-in-out infinite}}.o2{{animation:f2 11s ease-in-out infinite}}
.cur{{animation:blink 1.1s step-end infinite}}
.u1{{animation:up .8s ease-out both}}.u2{{animation:up .8s .15s ease-out both}}.u3{{animation:up .8s .3s ease-out both}}
</style>
<clipPath id="clip"><rect width="{W}" height="{H}" rx="28"/></clipPath>
<g clip-path="url(#clip)">
  <rect width="{W}" height="{H}" fill="{c["bg"]}"/>
  <circle class="o1" cx="1120" cy="60" r="220" fill="{c["a2"]}" opacity=".16"/>
  <circle class="o2" cx="640" cy="440" r="200" fill="{c["a1"]}" opacity=".13"/>
  <g opacity=".5" stroke="{c["line"]}">{"".join(f'<line x1="{x}" y1="0" x2="{x}" y2="{H}"/>' for x in range(0, W, 64))}</g>
</g>
<rect x=".5" y=".5" width="{W-1}" height="{H-1}" rx="28" fill="none" stroke="{c["line"]}"/>
<g class="u1"><text x="72" y="112" class="mono" font-size="18" fill="{c["a2"]}">// hello, world</text></g>
<g class="u2"><text x="68" y="190" class="sans" font-size="60" font-weight="700" fill="{c["ink"]}">Hi, I'm <tspan fill="url(#g)">{e(NAME)}</tspan></text></g>
<g class="u3">
  <text x="72" y="252" class="sans" font-size="23" fill="{c["ink"]}">{e(ROLE)}</text>
  <text x="72" y="288" class="sans" font-size="21" fill="{c["muted"]}">{e(STUDY)}</text>
  <rect x="72" y="326" width="{len(PLACE)*10 + 56}" height="40" rx="20" fill="{c["chip"]}" stroke="{c["line"]}"/>
  <circle cx="96" cy="346" r="6" fill="url(#g)"/>
  <text x="112" y="352" class="sans" font-size="16" fill="{c["ink"]}">{e(PLACE)}</text>
</g>
<rect x="760" y="96" width="452" height="290" rx="18" fill="{c["card"]}" stroke="{c["line"]}"/>
<circle cx="788" cy="124" r="6" fill="#FF5F57"/><circle cx="808" cy="124" r="6" fill="#FEBC2E"/><circle cx="828" cy="124" r="6" fill="#28C840"/>
<text x="1184" y="129" text-anchor="end" class="mono" font-size="13" fill="{c["muted"]}">{e(NICK.lower())}.py</text>
<line x1="760" y1="146" x2="1212" y2="146" stroke="{c["line"]}"/>
{code_svg}
<rect class="cur" x="806" y="362" width="10" height="20" fill="{c["a2"]}"/>
'''
    return svg(W, H, body, c)

def section(title, num, c):
    W, H = 1280, 96
    body = f'''<text x="4" y="62" class="mono" font-size="18" fill="{c["a2"]}">{num}</text>
<text x="52" y="64" class="sans" font-size="34" font-weight="700" fill="{c["ink"]}">{e(title)}</text>
<rect x="4" y="84" width="1272" height="1" fill="{c["line"]}"/><rect x="4" y="83" width="120" height="3" rx="1.5" fill="url(#g)"/>'''
    return svg(W, H, body, c)

def card(kicker, title, text, c, big=False):
    W, H = 412, 300
    lines = wrap(text, 38)
    desc = "".join(f'<text x="32" y="{176 + i*28}" class="sans" font-size="18" fill="{c["muted"]}">{e(l)}</text>' for i, l in enumerate(lines))
    body = f'''<rect x=".5" y=".5" width="{W-1}" height="{H-1}" rx="22" fill="{c["card"]}" stroke="{c["line"]}"/>
<rect x="32" y="36" width="{len(kicker)*9 + 28}" height="30" rx="15" fill="{c["chip"]}"/>
<text x="46" y="56" class="mono" font-size="14" fill="{c["a2"]}">{e(kicker)}</text>
<text x="32" y="128" class="sans" font-size="{30 if big else 26}" font-weight="700" fill="{c["ink"]}">{e(title)}</text>
<rect x="32" y="146" width="44" height="3" rx="1.5" fill="url(#g)"/>{desc}'''
    return svg(W, H, body, c)

def stack(c):
    W, gap, cols = 1280, 22, 3
    cw = (W - (cols - 1) * gap) // cols
    groups = list(STACK.items())
    out, y0 = "", 0
    for r in range(0, len(groups), cols):
        row = groups[r:r + cols]
        H = 104 + max(len(t) for _, t in row) * 64 + 24
        for i, (group, tools) in enumerate(row):
            x, n = i * (cw + gap), r + i + 1
            out += (f'<rect x="{x+.5}" y="{y0+.5}" width="{cw-1}" height="{H-1}" rx="22" fill="{c["card"]}" stroke="{c["line"]}"/>'
                    f'<text x="{x+30}" y="{y0+52}" class="mono" font-size="14" fill="{c["a2"]}">{n:02d}</text>'
                    f'<text x="{x+62}" y="{y0+53}" class="sans" font-size="22" font-weight="700" fill="{c["ink"]}">{e(group)}</text>'
                    f'<rect x="{x+30}" y="{y0+70}" width="44" height="3" rx="1.5" fill="url(#g)"/>')
            for j, (name, mono, col) in enumerate(tools):
                y = y0 + 98 + j * 64
                out += (f'<rect x="{x+30}" y="{y}" width="44" height="44" rx="12" fill="{col}"/>'
                        f'<text x="{x+52}" y="{y+28}" text-anchor="middle" class="mono" font-size="16" font-weight="700" fill="#FFFFFF">{e(mono)}</text>'
                        f'<text x="{x+92}" y="{y+29}" class="sans" font-size="19" fill="{c["ink"]}">{e(name)}</text>')
                if j < len(tools) - 1:
                    out += f'<rect x="{x+92}" y="{y+54}" width="{cw-122}" height="1" fill="{c["line"]}"/>'
        y0 += H + gap
    return svg(W, y0 - gap, out, c)

def pill(label, c):
    W, H = len(label) * 10 + 62, 40
    color, path = ICONS[label]
    color = color or c["ink"]
    body = f'''<rect x=".5" y=".5" width="{W-1}" height="{H-1}" rx="20" fill="{c["card"]}" stroke="{c["line"]}"/>
<path d="{path}" transform="translate(10 8)" fill="{color}"/>
<text x="44" y="26" class="sans" font-size="16" font-weight="600" fill="{c["ink"]}">{e(label)}</text>'''
    return svg(W, H, body, c)

# ───────────────────────── BUILD ─────────────────────────
def main():
    for theme, c in THEMES.items():
        d = OUT / theme
        d.mkdir(parents=True, exist_ok=True)
        files = {"hero.svg": hero(c), "stack.svg": stack(c)}
        for i, (k, t) in enumerate(SECTIONS.items(), 1):
            files[f"{k}.svg"] = section(t, f"{i:02d}", c)
        for i, (n, t, x) in enumerate(ABOUT, 1):
            files[f"a{i}.svg"] = card(n, t, x, c)
        for i, (k, t, x) in enumerate(PROJECTS, 1):
            files[f"p{i}.svg"] = card(k, t, x, c, big=True)
        for l in LINKS:
            files[f"l-{l.lower()}.svg"] = pill(l, c)
        for name, content in files.items():
            (d / name).write_text(content, encoding="utf-8")
    print(f"Built graphics into {OUT}")

if __name__ == "__main__":
    main()
