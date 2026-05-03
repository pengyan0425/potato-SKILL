# English Academic Rewrite Strategy

Apply these rules to AI-generated English academic text to lower AI-detection probability while **preserving grammatical correctness and scholarly tone**. The goal is to eliminate AI mechanical patterns (perfect parallelism, buzzword clustering, rigid template structures) without flattening the text into casual or colloquial English.

---

## Rule 1: Vary Sentence Openings and Structure

AI English heavily repeats formulaic openers. Break the pattern:

- Avoid starting multiple consecutive sentences with "In this paper/study/chapter, we...", "Furthermore", "Moreover", "Additionally".
- Vary subject types: use real nouns (the model, the dataset, prior work), gerunds (Training the network...), and occasional adverbial openers (Under these conditions...) instead of always using "we" or "this study".
- Alternate sentence length: place a 10-word short sentence after a 35-word complex one.
- Use occasional questions or rhetorical transitions: "What explains this gap?" or "The reason is straightforward."

**Example:**
- AI原文: In this study, we propose a novel framework for object detection. Furthermore, we evaluate the model on multiple benchmarks. Additionally, we compare our results with state-of-the-art methods.
- 改写后: We propose a framework that simplifies the anchor-design stage in object detection. The model was evaluated on COCO and Pascal VOC; across both datasets, it matched or outperformed existing state-of-the-art methods, though training took slightly longer.

---

## Rule 2: Replace AI-Buzzwords with Natural Academic Alternatives

Certain words are disproportionately flagged by AI detectors. Substitute them:

| AI-heavy term | Natural academic alternative |
|---|---|
| delve into | examine, look at, explore, analyze |
| underscore | highlight, emphasize, point out |
| crucial | important, critical, key |
| tapestry | (remove; use pattern, structure, or omit) |
| landscape | field, area, space |
| navigate | address, handle, manage, work through |
| realm | area, domain, field |
| multifaceted | complex, having several aspects |
| pivotal | key, central, decisive |
| inherent | built-in, natural, unavoidable |
| robust | strong, stable, reliable (use selectively) |
| novel | new (most of the time; reserve "novel" for truly unprecedented) |
| harness | use, apply, take advantage of |
| facilitate | help, enable, allow |
| shed light on | clarify, explain, reveal |

Never cluster two or more of these replacements in a single sentence.

---

## Rule 3: Diversify Connectives and Logical Transitions

AI text overuses formal additive connectives. Vary them:

- Replace every "Furthermore/Moreover/In addition/Additionally" with: "Also", "At the same time", "This is not the only issue", "The same logic applies to...", or drop the connective and use a semicolon.
- Replace every "However/Nevertheless" with: "Yet", "That said", "The opposite is true for...", "In practice, though".
- Replace "Therefore/Thus/Consequently" with: "So", "This means", "As a result", "What follows is".
- Avoid triple-connective sequences (e.g., "Moreover... Furthermore... Additionally...").

**However**, note that standard academic connectives are perfectly acceptable in formal sections (abstract, introduction, literature review) when used naturally rather than mechanically.

---

## Rule 4: Use Passive Voice Appropriately (Do Not Eliminate)

AI text often overuses passive voice, but **natural academic English in hydrology, meteorology, and Earth sciences relies heavily on passive and impersonal constructions**. Do not blanket-convert passives to actives.

- Keep passive voice when: (a) the agent is unknown or irrelevant, (b) object-focus is rhetorically needed, (c) disciplinary convention demands it, or (d) describing standardized methods.
- Examples of natural academic passives from the literature:
  - "The propagation characteristics... vary significantly depending on geographical location, climatic conditions, land cover, and geological factors."
  - "Drought propagation can be affected by local factors such as water, energy, topography, watershed discharge, and storage state."
  - "GRACE-derived groundwater drought indices have been widely used in..."
  - "It has been summarized that drought propagation has common features of pooling, attenuation, lag, lengthening, and reduction of area."
- Convert to active ONLY when the actor (usually "we") adds clarity or emphasis: "We trained the model on ImageNet" is better than "The model was trained on ImageNet" only when the training procedure itself is the focus.
- Reduce -tion / -ment / -ness nouns where they create unnecessary abstraction: "The establishment of the framework" -> "Once the framework was in place".

---

## Rule 5: Keep Terminology Precise but Syntax Flexible

- Do NOT simplify or replace technical terms (e.g., stochastic gradient descent, convolutional layer, heteroscedasticity, terrestrial water storage anomaly). Precision is part of academic identity.
- DO restructure the sentence around the term: change clause order, switch between appositive and relative clauses, or split one complex sentence into two.
- Use "we" or "I" only if the discipline allows; otherwise vary impersonal constructions: "The experiments show...", "A closer look at the data reveals...", "One might argue..."

---

## Rule 6: Add Concrete Anchors

AI text drifts into abstraction. Ground it:

- Reference exact dataset names, sample sizes, or metric values: "F1 improved by 4.2 points" rather than "performance improved significantly".
- Mention specific baselines: "Compared with ResNet-50" instead of "Compared with existing methods".
- Include brief methodological specifics: "using a batch size of 32" rather than "under standard settings".

---

## Rule 7: Maintain Academic Modesty --- CRITICAL

AI-generated academic text habitually overstates novelty, significance, and contribution. This is a primary "AI smell" in English academic writing. **Tone down all self-promotion.**

### 7.1 Avoid Absolute Innovation Claims
Never use "for the first time" / "unprecedented" / "pioneering" / "groundbreaking" / "paradigm shift" unless you have ironclad evidence that no prior work exists anywhere. Instead:

| AI exaggerated claim | Modest alternative |
|---|---|
| for the first time at the global scale | at the global scale / we attempt to... |
| unprecedented technical means | new technical means / satellite-based observation |
| revolutionary approach | effective approach / useful method / practical technique |
| remains a blank / gap | relatively limited / scarce / remains to be explored |
| fills a critical gap | complements existing knowledge / adds to current understanding |
| pioneering contribution | contribution / proposed framework |

### 7.2 Downgrade Intensifiers
Replace hyperbolic degree adverbs with measured ones:

| Overstated | Modest alternative |
|---|---|
| major/significant scientific advance | scientific advance / some progress |
| profound/deep threat | potential concern / notable risk |
| breakthrough discovery | finding / result / outcome |
| of paramount importance | of interest / useful / relevant |
| fundamentally reveals | reveals / indicates / suggests |
| provides a new perspective on | provides insight into / informs / contributes to |
| essentially | to some extent / in effect |

### 7.3 Eliminate Grand-Narrative Framing
Do NOT use section labels like "cognitive innovation" / "theoretical breakthrough" / "paradigm shift" / "disruptive contribution". Simply describe what the study does.

- AI原文: "(1) Cognitive innovation: For the first time at the global scale, we identify... and reveal... asymmetric driving laws."
- 改写后: "(1) We identify... at the global scale and analyze... driving patterns."

### 7.4 Use Hedging and Qualification
Academic claims should be tentative and open to revision:

- "proves that..." -> "suggests that..." / "indicates that..." / "the results show..."
- "clearly demonstrates..." -> "the analysis suggests..." / "the data support..."
- "completely solves..." -> "offers a potential solution to..." / "helps address..."
- "inevitably leads to..." -> "may lead to..." / "could potentially result in..."

### 7.5 State Value Objectively
When describing significance, let the method or result speak for itself. Do not force superlatives.

- AI原文: "This study is of great scientific significance and provides theoretical support for global..."
- 改写后: "The results may inform global... and provide a reference for..."

---

## Rule 8: Preferred Academic Sentence Templates (Hydrology/Meteorology Reference)

Based on patterns observed in high-quality English journals (e.g., Journal of Hydrology, Water Resources Research, Climate Dynamics, Remote Sensing), use these natural academic formulae:

### Introduction / Background
- "As extreme climate events become more common with global warming, groundwater is increasingly vital for combating long-term drought and ensuring socio-economic and ecological stability."
- "The significant increase in the frequency and duration of global droughts has attracted widespread attention in the fields of meteorology, agriculture, and hydrology."
- "Understanding the propagation system and the mechanism of the transition from meteorological drought to hydrological drought is essential for drought warning and forecasting."
- "To improve the precision and reliability of the study, this study combines... to carry out the following work."

### Literature Review
- "Liu et al. employed... to study...; Afshar et al. utilized... to investigate..."
- "The above studies show that... is a factor that cannot be ignored, but research on... remains limited."
- "Consequently, there is a pressing need for a more thorough exploration of..."

### Methods
- "The drought response time was determined based on... which was used to identify, pool and exclude the drought events combined with the run theory."
- "For each pixel, multiple meteorological droughts and groundwater drought events may occur, so the two types of drought events need to be matched first."

### Results
- "The results indicate that... is 2-7 months and the sensitivity distribution of... is consistent with..."
- "It should be emphasized that... is considerably more pronounced than..."
- "This could be attributed to the inertial response of... to..., which becomes more apparent over longer temporal scales."

### Discussion
- "The process of drought propagation is complicated, and the spatial distribution of drought propagation characteristics is caused by multiple factors such as..."
- "Compared with..., ... has less precipitation and lower temperatures, and the irrigated agriculture depends more on groundwater."
- "A limitation of our study is that... We look forward to quantifying... in our future studies."

---

## Rule 9: Match Disciplinary Register

AI text often imports words from adjacent disciplines, creating subtle semantic dissonance. A term standard in economics or engineering can sound odd in geography, hydrology, or ecology. Select verbs and collocations that match the natural usage of the target discipline.

### 9.1 Earth Sciences / Hydrology Conventions

| Cross-disciplinary intruder | Natural alternative in geo/hydro context |
|---|---|
| occupies the largest share | represents the largest freshwater reserve / accounts for the greatest proportion of freshwater |
| share / proportion (of a resource, when it sounds economic) | fraction / component / storage |
| supports (economics/society overtones) | sustains / underpins water supply for / provides water for |
| profound threat | long-term threat / potential risk / non-negligible risk |
| provides theoretical support | provides a theoretical basis / offers theoretical insight |
| drives development | promotes / facilitates / advances |
| core driving force | dominant factor / primary driver |
| empowers... | contributes to... / aids... |

### 9.2 Prefer Natural Collocations Over General Verbs

| Awkward general verb | Disciplinary collocation |
|---|---|
| conduct characterization | characterize / quantify / map |
| produce data | obtain data / generate a dataset |
| put into application | has been applied to / is used for |
| generate differences | exhibit variation / show spatial differentiation |

### 9.3 Use Earth-Science Register for Physical Processes

When describing physical systems, prefer geoscience phrasing over social-science phrasing:

- AI原文: "Groundwater occupies the largest share of global freshwater reserves."
- 改写后: "Groundwater constitutes the largest freshwater reserve on Earth." / "Among global freshwater resources, groundwater accounts for the greatest proportion."

- AI原文: "...and supports more than 40% of global irrigated agriculture."
- 改写后: "...and sustains water supply for more than 40% of global irrigated agriculture."

- AI原文: "...poses a profound threat to..."
- 改写后: "...poses a long-term threat to..." / "...carries potential risks for..."

- AI原文: "...provides theoretical support for..."
- 改写后: "...provides a theoretical basis for..." / "...offers theoretical insight into..."

---

## Rule 10: Preserve Technical Terminology Conventions

- First appearance of a term: provide full name followed by abbreviation in parentheses, e.g., "Standardized Precipitation Index (SPI)", "Gravity Recovery and Climate Experiment (GRACE)", "terrestrial water storage anomaly (TWSA)". After first use, use abbreviation.
- Keep internationally accepted acronyms untranslated: GRACE, GLDAS, SHAP, RF, XGBoost, SPEI, SGI, GGDI.
- Use precise disciplinary terminology: "propagation time" rather than "response time" when the literature standard is "propagation"; "run theory" for run-length based drought identification; "attenuation" and "prolonged effects" for drought feature transformations.

---

## Additional Anti-AI Patterns for English

- **Avoid perfect parallelism**: If AI produced three bullet-like sentences starting with "We first... We then... We finally...", collapse or vary them.
- **Use contractions sparingly**: A rare "don't" or "it's" in informal sections (e.g., discussion) can humanize tone, but avoid in formal abstracts or methods.
- **Interject brief evaluation**: AI rarely evaluates. Add a short clause like "which seems counter-intuitive" or "a surprising outcome given prior work".
- **Break template structures**: AI loves "The rest of this paper is organized as follows." If needed, vary: "The sections below walk through each stage in turn."
