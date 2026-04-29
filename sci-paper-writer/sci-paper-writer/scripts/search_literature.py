#!/usr/bin/env python3
"""
Literature search script for SCI Paper Writer skill.
Searches CrossRef, Semantic Scholar, and PubMed for real academic papers.

Usage:
    python3 search_literature.py "query" [--limit N] [--source crossref|semantic|pubmed]
    python3 search_literature.py "machine learning in healthcare" --limit 10 --source crossref

Dependencies: requests (standard in most Python environments)
"""

import argparse
import json
import sys
import urllib.request
import urllib.parse
import urllib.error
import xml.etree.ElementTree as ET


def search_crossref(query: str, limit: int = 10) -> list:
    """Search CrossRef for academic papers."""
    params = urllib.parse.urlencode({
        "query": query,
        "rows": limit,
        "sort": "relevance",
        "select": "DOI,title,author,published-print,container-title,type,is-referenced-by-count"
    })
    url = f"https://api.crossref.org/works?{params}"

    req = urllib.request.Request(url, headers={
        "User-Agent": "SCI-Paper-Writer/1.0 (mailto:research@example.com)"
    })

    try:
        with urllib.request.urlopen(req, timeout=15) as resp:
            data = json.loads(resp.read().decode())
    except urllib.error.URLError as e:
        print(f"[CrossRef Error] {e}", file=sys.stderr)
        return []

    results = []
    for item in data.get("message", {}).get("items", []):
        title_list = item.get("title", [])
        title = title_list[0] if title_list else "No title"

        authors = []
        for a in item.get("author", [])[:5]:
            name = f"{a.get('given', '')} {a.get('family', '')}".strip()
            if name:
                authors.append(name)
        if len(item.get("author", [])) > 5:
            authors.append("et al.")

        year = ""
        pub_date = item.get("published-print", {}).get("date-parts", [[]])
        if pub_date and pub_date[0]:
            year = str(pub_date[0][0])

        journal_list = item.get("container-title", [])
        journal = journal_list[0] if journal_list else ""

        doi = item.get("DOI", "")
        citations = item.get("is-referenced-by-count", 0)

        results.append({
            "title": title,
            "authors": authors,
            "year": year,
            "journal": journal,
            "doi": doi,
            "citations": citations,
            "source": "CrossRef"
        })

    return results


def search_semantic_scholar(query: str, limit: int = 10) -> list:
    """Search Semantic Scholar for academic papers."""
    params = urllib.parse.urlencode({
        "query": query,
        "limit": limit,
        "fields": "title,authors,year,venue,citationCount,url,externalIds"
    })
    url = f"https://api.semanticscholar.org/graph/v1/paper/search?{params}"

    try:
        with urllib.request.urlopen(url, timeout=15) as resp:
            data = json.loads(resp.read().decode())
    except urllib.error.URLError as e:
        print(f"[Semantic Scholar Error] {e}", file=sys.stderr)
        return []

    results = []
    for item in data.get("data", []):
        authors = [a.get("name", "") for a in item.get("authors", [])[:5]]
        if len(item.get("authors", [])) > 5:
            authors.append("et al.")

        ext_ids = item.get("externalIds", {}) or {}
        doi = ext_ids.get("DOI", "")

        results.append({
            "title": item.get("title", "No title"),
            "authors": authors,
            "year": str(item.get("year", "")),
            "journal": item.get("venue", ""),
            "doi": doi,
            "citations": item.get("citationCount", 0),
            "source": "Semantic Scholar"
        })

    return results


def search_pubmed(query: str, limit: int = 10) -> list:
    """Search PubMed for biomedical papers."""
    # Step 1: Search for IDs
    search_params = urllib.parse.urlencode({
        "db": "pubmed",
        "term": query,
        "retmax": limit,
        "retmode": "json",
        "sort": "relevance"
    })
    search_url = f"https://eutils.ncbi.nlm.nih.gov/entrez/eutils/esearch.fcgi?{search_params}"

    try:
        with urllib.request.urlopen(search_url, timeout=15) as resp:
            search_data = json.loads(resp.read().decode())
    except urllib.error.URLError as e:
        print(f"[PubMed Search Error] {e}", file=sys.stderr)
        return []

    ids = search_data.get("esearchresult", {}).get("idlist", [])
    if not ids:
        return []

    # Step 2: Fetch details
    fetch_params = urllib.parse.urlencode({
        "db": "pubmed",
        "id": ",".join(ids),
        "retmode": "xml"
    })
    fetch_url = f"https://eutils.ncbi.nlm.nih.gov/entrez/eutils/efetch.fcgi?{fetch_params}"

    try:
        with urllib.request.urlopen(fetch_url, timeout=15) as resp:
            xml_data = resp.read().decode()
    except urllib.error.URLError as e:
        print(f"[PubMed Fetch Error] {e}", file=sys.stderr)
        return []

    results = []
    try:
        root = ET.fromstring(xml_data)
        for article in root.findall(".//PubmedArticle"):
            medline = article.find("MedlineCitation")
            art = medline.find("Article") if medline is not None else None
            if art is None:
                continue

            title_el = art.find("ArticleTitle")
            title = title_el.text if title_el is not None and title_el.text else "No title"

            authors = []
            author_list = art.find("AuthorList")
            if author_list is not None:
                for author in author_list.findall("Author")[:5]:
                    last = author.find("LastName")
                    first = author.find("ForeName")
                    name = ""
                    if last is not None and last.text:
                        name = last.text
                    if first is not None and first.text:
                        name = f"{first.text} {name}"
                    if name:
                        authors.append(name)
                if len(author_list.findall("Author")) > 5:
                    authors.append("et al.")

            journal_el = art.find("Journal/Title")
            journal = journal_el.text if journal_el is not None and journal_el.text else ""

            year_el = art.find("Journal/JournalIssue/PubDate/Year")
            year = year_el.text if year_el is not None and year_el.text else ""

            doi_el = article.find(".//ELocationID[@EIdType='doi']")
            doi = doi_el.text if doi_el is not None and doi_el.text else ""

            pmid_el = medline.find("PMID")
            pmid = pmid_el.text if pmid_el is not None and pmid_el.text else ""

            results.append({
                "title": title,
                "authors": authors,
                "year": year,
                "journal": journal,
                "doi": doi,
                "pmid": pmid,
                "citations": None,
                "source": "PubMed"
            })
    except ET.ParseError as e:
        print(f"[PubMed XML Parse Error] {e}", file=sys.stderr)

    return results


def format_results(results: list) -> str:
    """Format results for display."""
    if not results:
        return "No results found."

    lines = []
    for i, r in enumerate(results, 1):
        authors_str = ", ".join(r["authors"]) if r["authors"] else "Unknown"
        year_str = f"({r['year']})" if r["year"] else "(n.d.)"
        journal_str = f"*{r['journal']}*" if r["journal"] else ""
        doi_str = f"DOI: {r['doi']}" if r["doi"] else ""
        pmid_str = f"PMID: {r['pmid']}" if r.get("pmid") else ""
        cite_str = f"Citations: {r['citations']}" if r.get("citations") else ""

        line = f"{i}. {r['title']}"
        line += f"\n   {authors_str} {year_str}"
        if journal_str:
            line += f" — {journal_str}"
        extras = " | ".join(filter(None, [doi_str, pmid_str, cite_str]))
        if extras:
            line += f"\n   [{extras}]"
        line += f"\n   (Source: {r['source']})"
        lines.append(line)

    return "\n\n".join(lines)


def main():
    parser = argparse.ArgumentParser(description="Search academic literature databases.")
    parser.add_argument("query", help="Search query")
    parser.add_argument("--limit", type=int, default=10, help="Max results (default: 10)")
    parser.add_argument("--source", choices=["crossref", "semantic", "pubmed"],
                        default="crossref", help="Database to search (default: crossref)")
    parser.add_argument("--json", action="store_true", help="Output as JSON")

    args = parser.parse_args()

    search_fn = {
        "crossref": search_crossref,
        "semantic": search_semantic_scholar,
        "pubmed": search_pubmed,
    }[args.source]

    print(f"Searching {args.source} for: \"{args.query}\"...", file=sys.stderr)
    results = search_fn(args.query, args.limit)

    if args.json:
        print(json.dumps(results, indent=2, ensure_ascii=False))
    else:
        print(format_results(results))
        print(f"\n--- {len(results)} results from {args.source} ---", file=sys.stderr)


if __name__ == "__main__":
    main()
