---
name: humanize-text-v2
description: Humanize AI-generated academic text to evade AI detection while retaining scholarly rigor and formal register. Use when the user asks to lower AI rate, reduce AI detection score, humanize text, de-AI content, rewrite AI-sounding draft, make academic writing sound more natural or human-like, avoid AI detector flags, or polish AI-generated chapters/sections for Chinese or English academic papers. This version preserves academic tone rather than vernacularizing into colloquial language.
---

This skill is designed to humanize AI-generated academic text (Chinese or English), reducing AI-detection likelihood while preserving scholarly tone and formal register. It triggers when the user requests to: lower AI rate, reduce AI detection, humanize text, de-AI content, rewrite to avoid AI detection, make text more human-like, or polish AI-generated drafts to sound natural.

## Core Workflow

1. Determine language of input text (Chinese, English, or mixed).
2. Load the corresponding rewrite strategy reference file:
   - **Chinese**: Read `references/chinese-rewrite.md`
   - **English**: Read `references/english-rewrite.md`
3. Rewrite the text following the loaded strategy. Do NOT explain changes inline; output only the rewritten text.
4. Preserve all academic terminology, data, citations, and core arguments. Only modify expression style.

## Key Principles

- **Preserve scholarly register**: The goal is to break AI mechanical patterns (uniform sentence length, rigid parallelism, excessive enumeration, buzzword clustering) without flattening the text into colloquial or casual language. Academic writing has legitimate conventions; do not destroy them in the name of "humanization".
- **Keep formal connectives**: Words like "furthermore", "moreover", "however", "therefore" are standard in academic prose. Vary them to avoid robotic repetition, but do not ban them or replace them with overly casual alternatives.
- **Respect disciplinary voice**: Hydrology, meteorology, and Earth-science papers legitimately use passive voice, impersonal constructions, and precise technical phrasing. Do not force these into active, conversational syntax.
- **Maintain objective voice**: Use "本文/本研究" (Chinese) or "this study/our analysis" (English) naturally; vary with "the results show", "analysis reveals", "comparison indicates".
- **Match disciplinary register**: AI text often imports words from adjacent disciplines (e.g., "占据份额" from economics into hydrology, "支撑" from engineering into geography). Use verbs and collocations natural to the target discipline. Let the field's own phrasing conventions guide word choice.: AI text habitually overstates novelty and significance ("首次", "前所未有", "尚属空白", "重大进展", "for the first time", "unprecedented", "groundbreaking"). **Tone down all self-promotion.** Let methods and results speak for themselves. Use hedging language ("一定程度上", "可能", "有待", "suggests", "indicates", "may") rather than absolute claims.

## Cross-Language Principles

- Keep the original meaning intact; never alter facts, data, or conclusions.
- Maintain an academic register: avoid slang, emojis, or overly casual language.
- Do not add content that was not present in the original; focus on stylistic transformation.
- If the input contains LaTeX, citations, or technical notation, preserve them exactly.

## Output Format

Return the rewritten text directly. If the user provided specific sections (e.g., "rewrite Chapter 3"), maintain the same section boundaries. Do NOT output a summary of changes unless explicitly requested.
