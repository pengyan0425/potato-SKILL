# SCI Paper Writer — Guided Drafting Assistant

An [OpenClaw](https://github.com/openclaw/openclaw) skill that assists researchers in drafting SCI journal papers through **guided questioning**, not auto-generation.

## Features

- **7 Writing Modules** — Abstract, Introduction, Data/Study Design, Methods, Results, Discussion, Conclusion
- **Guided Questioning** — Asks targeted questions to extract your ideas, then helps shape them into polished prose
- **Real Literature Search** — Queries CrossRef, Semantic Scholar, and PubMed APIs for actual published papers
- **Ask → Draft → Review Cycle** — You review every draft before moving on
- **Full Manuscript Polish** — Consistency, flow, format, and figure/table review checklist
- **Bilingual** — Supports English and Chinese drafts

## Installation

### Option 1: Copy to OpenClaw skills directory

```bash
cp -r sci-paper-writer ~/.openclaw/skills/
```

### Option 2: Install via ClawHub (if published)

```bash
clawhub install sci-paper-writer
```

## Usage

Once installed, trigger the skill in any OpenClaw session by asking things like:

```
"Help me write a paper on deep learning for medical imaging"
"I need to draft the Methods section of my paper"
"Find recent literature on CRISPR gene editing"
"Review my manuscript draft"
```

The skill will:

1. **Ask about your research** — topic, target journal, study type, what you have so far
2. **Search literature** — find real references using the built-in search script
3. **Guide each section** — ask 3-5 targeted questions per section, then draft based on your answers
4. **Iterate** — you review and correct, the skill revises

### Literature Search

The search script can also be used standalone:

```bash
# Search CrossRef (broadest, default)
python3 scripts/search_literature.py "machine learning in healthcare" --limit 10

# Search PubMed (biomedical)
python3 scripts/search_literature.py "CRISPR gene editing" --source pubmed --limit 5

# Search Semantic Scholar (CS/AI)
python3 scripts/search_literature.py "transformer attention mechanism" --source semantic

# Output as JSON
python3 scripts/search_literature.py "single cell RNA sequencing" --json
```

### Module Structure

| Module | What It Covers |
|--------|---------------|
| **Abstract** | IMRaD structure, action verbs, word limits |
| **Introduction** | Funnel structure (broad → gap → contribution), transition phrases |
| **Data** | Study design, variables, sample size, ethics |
| **Methods** | Reproducibility, parameters, software versions, validation |
| **Results** | Statistical reporting, figure/table references, null results |
| **Discussion** | Interpretation, comparison with literature, limitations, future work |
| **Conclusion** | One-sentence contribution, significance, forward look |
| **Polish** | Consistency check, flow, format compliance, figure quality |

## Design Philosophy

> **Guide, don't ghostwrite.**

This skill treats you as the author. It asks questions to draw out your knowledge, data, and arguments — then helps you express them in clear, publication-ready academic prose. It will never fabricate data, invent citations, or write claims you haven't supported.

## Dependencies

- Python 3.6+ (standard library only — no pip install required)
- Internet connection (for literature search APIs)

## License

MIT
