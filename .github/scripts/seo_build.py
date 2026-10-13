#!/usr/bin/env python3
"""Apply consistent on-page SEO metadata and JSON-LD to the static ToolNest build."""
from pathlib import Path
from html import unescape
import json, re, sys, xml.etree.ElementTree as ET

ROOT = Path(sys.argv[1] if len(sys.argv) > 1 else "site")
BASE = "https://shepherd2761.github.io/Shepherd82/"
SITE_NAME = "ToolNest"

def clean_html(value):
    value = re.sub(r"<[^>]+>", " ", value or "")
    return re.sub(r"\s+", " ", unescape(value)).strip()

def absolute_url(rel):
    rel = rel.replace("\\", "/")
    if rel == "index.html":
        return BASE
    if rel.endswith("/index.html"):
        return BASE + rel[:-len("index.html")]
    return BASE + rel

def get_title(html):
    m = re.search(r"<title\b[^>]*>(.*?)</title\s*>", html, re.I | re.S)
    if m:
        return clean_html(m.group(1))
    m = re.search(r"<h1\b[^>]*>(.*?)</h1\s*>", html, re.I | re.S)
    name = clean_html(m.group(1)) if m else "Free Online Tool"
    return f"{name} | {SITE_NAME}"

def get_h1(html, title):
    m = re.search(r"<h1\b[^>]*>(.*?)</h1\s*>", html, re.I | re.S)
    if m:
        return clean_html(m.group(1))
    if title:
        return re.sub(r"\s*[|—-]\s*(ToolNest.*|ToolNest Blog)$", "", title, flags=re.I).strip()
    return "ToolNest"

def get_description(html, h1, path):
    m = re.search(r'<meta\b[^>]*name=["\']description["\'][^>]*content=["\']([^"\']*)["\'][^>]*>', html, re.I)
    if not m:
        m = re.search(r'<meta\b[^>]*content=["\']([^"\']*)["\'][^>]*name=["\']description["\'][^>]*>', html, re.I)
    desc = clean_html(m.group(1)) if m else ""
    boilerplate = ("this page is designed for one specific task", "this page is designed to be", "use this free browser-based tool", "simple information about how this site")
    if desc and len(desc) >= 70 and not any(x in desc.lower() for x in boilerplate):
        return desc[:157].rsplit(" ", 1)[0] if len(desc) > 160 else desc
    if path == "index.html":
        return "Use free online calculators, converters, text utilities, image tools and QR code generators. Fast, mobile-friendly and no signup required."
    if path.startswith("blog/") and path != "blog/index.html":
        m = re.search(r"<h1\b[^>]*>.*?</h1\s*>((?:(?!<h[1-6]\b).){0,1800})", html, re.I | re.S)
        p = re.search(r"<p\b[^>]*>(.*?)</p\s*>", m.group(1), re.I | re.S) if m else None
        body = clean_html(p.group(1)) if p else ""
        if body and len(body) >= 55:
            return (body[:157].rsplit(" ", 1)[0] if len(body) > 160 else body)
        return f"Learn {h1.lower()} with clear examples, practical steps and useful free tools from ToolNest."
    if path in ("about.html", "contact.html", "privacy.html"):
        return {
            "about.html": "Learn about ToolNest, a collection of free, browser-based calculators, converters and everyday online utilities.",
            "contact.html": "Find how to contact ToolNest with feedback, questions, corrections or suggestions for new free online tools.",
            "privacy.html": "Read the ToolNest privacy policy to understand how browser-based tools, advertising and site data are handled."
        }[path]
    if path == "tools/index.html":
        return "Browse free online calculators, unit converters, text tools, business calculators and other browser-based utilities on ToolNest."
    if path == "blog/index.html":
        return "Read practical guides, formulas and examples for calculators, conversions, text tools and everyday online tasks."
    m = re.search(r"<h1\b[^>]*>.*?</h1\s*>((?:(?!<h[1-6]\b).){0,1400})", html, re.I | re.S)
    p = re.search(r"<p\b[^>]*>(.*?)</p\s*>", m.group(1), re.I | re.S) if m else None
    body = clean_html(p.group(1)) if p else ""
    if body and 55 <= len(body) <= 160 and not any(x in body.lower() for x in boilerplate):
        return body
    return f"Use the free {h1.lower()} online to get a quick result in your browser. Simple, mobile-friendly and no signup required."

def meta_tag(name, content):
    return f'<meta name="{name}" content="{content}">'

def prop_tag(prop, content):
    return f'<meta property="{prop}" content="{content}">'

def upsert_meta(head, name, content):
    tag = meta_tag(name, content.replace('"', "&quot;"))
    pattern = re.compile(r'<meta\b(?=[^>]*\bname=["\']' + re.escape(name) + r'["\'])[^>]*>', re.I)
    if pattern.search(head):
        return pattern.sub(tag, head, count=1)
    return head.replace("</head>", tag + "</head>")

def upsert_prop(head, prop, content):
    tag = prop_tag(prop, content.replace('"', "&quot;"))
    pattern = re.compile(r'<meta\b(?=[^>]*\bproperty=["\']' + re.escape(prop) + r'["\'])[^>]*>', re.I)
    if pattern.search(head):
        return pattern.sub(tag, head, count=1)
    return head.replace("</head>", tag + "</head>")

def upsert_link(head, rel, href):
    tag = f'<link rel="{rel}" href="{href}">'
    pattern = re.compile(r'<link\b(?=[^>]*\brel=["\']' + re.escape(rel) + r'["\'])[^>]*>', re.I)
    if pattern.search(head):
        return pattern.sub(tag, head, count=1)
    return head.replace("</head>", tag + "</head>")

def make_schema(path, url, title, description, h1, html):
    items = []
    is_article = path.startswith("blog/") and path != "blog/index.html"
    is_home = path == "index.html"
    is_tools_index = path == "tools/index.html"
    crumbs = [{"@type":"ListItem","position":1,"name":"Home","item":BASE}]
    if path.startswith("blog/"):
        crumbs.append({"@type":"ListItem","position":2,"name":"Blog","item":BASE+"blog/"})
        if is_article:
            crumbs.append({"@type":"ListItem","position":3,"name":h1,"item":url})
    elif path not in ("index.html",):
        crumbs.append({"@type":"ListItem","position":2,"name":h1,"item":url})
    if not is_home:
        items.append({"@context":"https://schema.org","@type":"BreadcrumbList","itemListElement":crumbs})
    if is_home:
        items.append({"@context":"https://schema.org","@type":"WebSite","name":SITE_NAME,"url":BASE,"description":description,"inLanguage":"en"})
        items.append({"@context":"https://schema.org","@type":"Organization","name":SITE_NAME,"url":BASE})
        items.append({"@context":"https://schema.org","@type":"WebPage","name":title,"url":url,"description":description,"isPartOf":{"@type":"WebSite","name":SITE_NAME,"url":BASE}})
    elif is_article:
        article = {"@context":"https://schema.org","@type":"Article","headline":h1[:110],"description":description,"url":url,"mainEntityOfPage":{"@type":"WebPage","@id":url},"author":{"@type":"Organization","name":SITE_NAME},"publisher":{"@type":"Organization","name":SITE_NAME},"inLanguage":"en"}
        items.append(article)
    elif path not in ("404.html",) and not path.startswith("google"):
        page_type = "CollectionPage" if is_tools_index or path == "blog/index.html" else "WebPage"
        items.append({"@context":"https://schema.org","@type":page_type,"name":title,"url":url,"description":description,"isPartOf":{"@type":"WebSite","name":SITE_NAME,"url":BASE},"inLanguage":"en"})
        if path not in ("about.html","contact.html","privacy.html","tools/index.html","blog/index.html") and not path.startswith("blog/"):
            items.append({"@context":"https://schema.org","@type":"WebApplication","name":h1,"url":url,"description":description,"applicationCategory":"UtilitiesApplication","operatingSystem":"Any","offers":{"@type":"Offer","price":"0","priceCurrency":"USD"}})
    return items

processed = 0
urls = []
for file in sorted(ROOT.rglob("*.html")):
    rel = file.relative_to(ROOT).as_posix()
    if rel.startswith(".") or rel.startswith("_") or rel.startswith("google"):
        continue
    if rel == "404.html":
        html = file.read_text(encoding="utf-8")
        if "</head>" in html.lower():
            html = re.sub(r'<meta\b(?=[^>]*\bname=["\']robots["\'])[^>]*>', '', html, flags=re.I)
            html = re.sub(r"</head\s*>", '<meta name="robots" content="noindex,follow"></head>', html, count=1, flags=re.I)
            file.write_text(html, encoding="utf-8")
        continue
    html = file.read_text(encoding="utf-8")
    if not re.search(r"</head\s*>", html, re.I):
        continue
    title = get_title(html)
    h1 = get_h1(html, title)
    desc = get_description(html, h1, rel)
    url = absolute_url(rel)
    if rel == "index.html":
        title = "Free Online Calculators, Converters & Tools | ToolNest"
    elif rel == "tools/index.html":
        title = "Free Online Tools Directory: Calculators & Converters | ToolNest"
    elif rel == "blog/index.html":
        title = "ToolNest Blog: Calculator Guides, Formulas & How-Tos"
    # Remove duplicate/old metadata and schema before rebuilding a clean head.
    head_match = re.search(r"<head\b[^>]*>.*?</head\s*>", html, re.I | re.S)
    if not head_match:
        continue
    head = head_match.group(0)
    head = re.sub(r'<script\b(?=[^>]*type=["\']application/ld\+json["\'])[^>]*>.*?</script\s*>', '', head, flags=re.I | re.S)
    # Existing title is replaced to ensure our chosen title is authoritative.
    title_tag = f"<title>{title}</title>"
    if re.search(r"<title\b[^>]*>.*?</title\s*>", head, re.I | re.S):
        head = re.sub(r"<title\b[^>]*>.*?</title\s*>", title_tag, head, count=1, flags=re.I | re.S)
    else:
        head = head.replace("</head>", title_tag + "</head>")
    head = upsert_meta(head, "description", desc)
    head = upsert_meta(head, "robots", "index,follow,max-image-preview:large,max-snippet:-1,max-video-preview:-1")
    slug_terms = re.sub(r"[-_/]+", " ", rel.replace("/index.html","").replace(".html",""))
    keywords = ", ".join(dict.fromkeys([h1.lower(), slug_terms.lower(), "free online tool", "online calculator" if "calculator" in (h1+rel).lower() else "online converter" if "converter" in (h1+rel).lower() else "browser-based utility"]))
    head = upsert_meta(head, "keywords", keywords[:240])
    head = upsert_link(head, "canonical", url)
    head = upsert_prop(head, "og:title", title)
    head = upsert_prop(head, "og:description", desc)
    head = upsert_prop(head, "og:url", url)
    head = upsert_prop(head, "og:type", "article" if rel.startswith("blog/") and rel != "blog/index.html" else "website")
    head = upsert_prop(head, "og:site_name", SITE_NAME)
    head = upsert_meta(head, "twitter:card", "summary")
    head = upsert_meta(head, "twitter:title", title)
    head = upsert_meta(head, "twitter:description", desc)
    schemas = make_schema(rel, url, title, desc, h1, html)
    schema_script = '<script type="application/ld+json">' + json.dumps(schemas, ensure_ascii=False, separators=(",",":")).replace("</", "<\\/") + '</script>'
    head = head.replace("</head>", schema_script + "</head>")
    html = html[:head_match.start()] + head + html[head_match.end():]
    file.write_text(html, encoding="utf-8")
    processed += 1
    urls.append(url)

# Rebuild sitemap from the actual HTML pages, not a stale hand-maintained subset.
sitemap_urls = sorted(set(urls))
urlset = ET.Element("urlset", {"xmlns":"http://www.sitemaps.org/schemas/sitemap/0.9"})
for url in sitemap_urls:
    entry = ET.SubElement(urlset, "url")
    ET.SubElement(entry, "loc").text = url
ET.indent(urlset, space="  ")
(ROOT / "sitemap.xml").write_bytes(ET.tostring(urlset, encoding="utf-8", xml_declaration=True))
robots = ROOT / "robots.txt"
robots.write_text("User-agent: *\nAllow: /\nDisallow: /404.html\n\nSitemap: " + BASE + "sitemap.xml\n", encoding="utf-8")
print(f"SEO build complete: optimized {processed} HTML pages; sitemap contains {len(sitemap_urls)} canonical URLs.")
