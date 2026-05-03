# Chinese Academic Rewrite Strategy

Apply these rules to AI-generated Chinese academic text to lower AI-detection probability while **preserving scholarly register**. The goal is to eliminate AI mechanical patterns (uniform sentence length, rigid parallelism, excessive enumeration, buzzword clustering) without vernacularizing the text into colloquial Chinese.

---

## Rule 1: Maintain Scholarly Register While Varying Rhythm

AI Chinese academic text tends toward mechanically uniform sentence structure. Break this pattern **within** the academic register:

- Alternate sentence length: place concise sentences (8-15 characters) amid complex ones, but keep all diction formal.
- Vary syntactic openings; do not begin every sentence with "本文/本研究/该方法".
- Avoid rigid four-character parallel structures (排比). Merge or stagger parallel clauses into flowing prose.
- Use judiciously varied transitions that remain academic: "换言之", "基于此", "有鉴于此", "从另一个维度看".
- Do NOT use modal particles: 呢, 啊, 吧, 哦, 嘛, 呗.

**Example:**
- AI原文: "本文旨在探讨深度学习技术在医疗影像诊断中的应用。首先，分析现有方法的局限性；其次，提出改进模型；最后，通过实验验证有效性。"
- 改写后: "本文围绕深度学习在医疗影像诊断中的应用展开讨论。现有方法在处理小样本数据时存在明显局限，针对这一问题，我们重新设计了网络结构，并在多个公开数据集上开展测试。实验结果表明，新模型在准确率上具有明显提升。"

---

## Rule 2: Use Objective Voice and Formal Subjects

AI text often oscillates awkwardly between passive impersonality and forced active voice. Follow Chinese academic conventions:

- Use objective, impersonal expressions: "采用...方法", "基于...数据", "通过...分析", "利用...技术".
- Vary the subject across sentences; do not default to "本文/本研究" every time.
- Acceptable alternatives: "研究结果表明", "上述方法", "分析结果显示", "进一步分析发现", "对比可知".
- Avoid sentence subjects like "这一发现" or "上述现象" when a concrete noun works better: "实验结果" instead of "上述结果", "对比分析" instead of "这一比较".
- Keep "本文/本研究/笔者" usage natural to the genre: use "本文" for the paper itself, "本研究" for the broader project, "笔者" sparingly.

**Example:**
- AI原文: "本研究提出了一个模型。该模型效果很好。本文发现这个模型很稳定。"
- 改写后: "本文提出一种新的评估模型。验证结果显示，该模型不仅具有较好的识别精度，且在多源数据输入条件下表现出良好的稳定性。"

---

## Rule 3: Use Formal Connectives Naturally (Do Not Ban Them)

Academic Chinese relies on standard connectives. The problem is **mechanical overuse**, not the words themselves.

- Acceptable and common in scholarly writing: 首先/其次/此外/然而/因此/值得注意的是/综上所述.
- Avoid robotic enumeration: "第一...第二...第三..." across every paragraph. Use them where logical ordering genuinely aids comprehension, but prefer causal or contrastive flow elsewhere.
- Replace mechanical repetition with varied transitions: "在此基础上", "相比之下", "这意味着", "与此同时", "从另一角度看", "有鉴于此", "进一步地".

**Example:**
- AI原文: "首先，数据预处理是整个流程的基础。其次，模型训练需要大量计算资源。最后，评估指标决定了结果的可信度。"
- 改写后: "数据预处理为后续流程奠定基础。模型训练阶段消耗的计算资源较大，而评估指标的选择则会直接影响结果的可信度。"

---

## Rule 4: Eliminate Unnecessary Quotation Marks

Use quotation marks ("" or '') ONLY in these cases:
- Direct quotation from another work.
- First introduction of a technical term that may confuse readers; after first use, drop the quotes.
- Specific nomenclature requiring distinction (e.g., coined concepts).

Remove quotes around: common academic terms, self-evident concepts, every instance of "本研究", "本文", "上述方法".

**Example:**
- AI原文: 本研究提出了一种"多尺度特征融合网络"，该"网络"在"图像分类"任务中表现优异。
- 改写后: 本研究提出一种多尺度特征融合网络，该网络在图像分类任务中表现较好。

---

## Rule 5: Normalize Parenthetical Results

Never frame results with parentheses like "结果显示（准确率提升了5%）". Instead, state directly: "准确率提升了5%" or "实验表明准确率提升了5个百分点".

Remove parentheses around:
- Numerical outcomes (改用逗号或直接陈述).
- Supplementary clauses that can stand as full sentences.

Keep parentheses ONLY for:
- Citations (e.g., Smith et al., 2020).
- Formulaic or strictly conventional mathematical notation.

**Example:**
- AI原文: 实验结果表明（见表3），新方法的F1分数（0.87）明显高于基线模型（0.79）。
- 改写后: 从表3可以看出，新方法的F1分数达到0.87，明显高于基线模型的0.79。

---

## Rule 6: Reduce Excessive "的" Chains

AI text piles up 的. Break 的-heavy modifiers into clauses:

- "基于注意力机制的深度学习模型" -> "深度学习模型引入了注意力机制".
- "具有较高精度的预测结果" -> "预测结果精度较高".
- "对不同气候区地下水干旱传播特征的影响" -> "影响不同气候区地下水干旱的传播特征".

---

## Rule 7: Soften Absolutes Without Losing Precision

Replace AI absolutes with measured academic qualifiers, but keep precision where data demands it:

- 必然 -> 大概率 / 通常
- 显然 -> 不难看出 / 可以认为
- 毫无疑问 -> 这在一定程度上说明 / 现有证据支持
- 完全/绝对 -> 较为 / 总体上

**Exception**: When presenting definitive statistical results or mathematically proven facts, keep absolute phrasing.

---

## Rule 8: Maintain Academic Modesty --- CRITICAL

AI-generated academic text habitually overstates novelty, significance, and contribution. This is the most common "AI smell" in Chinese academic writing. **Tone down all self-promotion.**

### 8.1 Avoid Absolute Innovation Claims
Never use "首次" / "前所未有" / "尚属空白" / "开创性" / "里程碑" unless you have ironclad evidence that no prior work exists anywhere. Instead:

| AI夸大表述 | 谦逊替代 |
|---|---|
| 首次在全球尺度... | 在全球尺度开展... / 尝试从全球视角... |
| 前所未有的技术手段 | 新的技术手段 / 卫星观测手段 |
| 革命性手段 | 有效手段 / 重要手段 / 可行的技术手段 |
| 尚属空白 | 相对较少 / 尚不多见 / 有待深入 |
| 填补空白 | 丰富现有认识 / 补充相关研究 |
| 开创性地提出 | 提出... / 尝试建立... |

### 8.2 Downgrade Intensifiers
Replace hyperbolic degree adverbs with measured ones:

| 过度拔高 | 谦逊替代 |
|---|---|
| 重大科学进展 | 科学进展 / 一定进展 |
| 深远威胁 | 潜在威胁 / 不容忽视的威胁 |
| 突破性发现 | 新的发现 / 分析结果 |
| 极具重要价值 | 具有参考价值 / 有一定指导意义 |
| 深刻地揭示了 | 揭示了... / 反映出... |
| 为...提供新的视角 | 为...提供参考 / 丰富...认知 |
| 本质上 | 在一定程度上 / 实质上 |

### 8.3 Eliminate Grand-Narrative Section Framing
Do NOT use section labels like "认知创新层面" / "理论突破层面" / "范式转换" / "颠覆性贡献". Simply describe what the study does.

- AI原文: "（1）认知创新层面：首次在全球尺度识别...，揭示...非对称驱动规律。"
- 改写后: "（1）在全球尺度识别...，分析...驱动规律。"

### 8.4 Use Hedging and Qualification
Academic claims should be tentative and open to revision:

- "证明了..." -> "结果表明..." / "分析显示..." / "在一定程度上说明..."
- "明确了..." -> "识别出..." / "厘清了..."
- "彻底地解决了..." -> "有助于缓解..." / "为...提供可能途径"
- "必然导致..." -> "可能引发..." / "在...条件下或将..."

### 8.5 State Value Objectively
When describing significance, let the method or result speak for itself. Do not force superlatives.

- AI原文: "该研究不仅具有重要的科学意义，也可为全球...提供理论支撑。"
- 改写后: "研究结果可为全球...提供参考，对...具有一定指导意义。"

---

## Rule 9: Preferred Academic Sentence Templates

Based on patterns observed in high-quality Chinese hydrology/meteorology journals (e.g., 水资源保护, 地理科学进展, 水科学进展), use these natural academic formulae:

### Introduction / Background
- "干旱是影响范围最广的自然灾害之一，在气候变暖背景下，其发生频率和强度呈显著上升趋势。"
- "与气象干旱、农业干旱和水文干旱相比，地下水干旱具有更深的隐蔽性、更长的持续时间及更缓慢的恢复周期。"
- "然而，现有研究多聚焦于局地或流域尺度，对全球范围内...的整体规律认识不足，尤其缺乏对...的系统刻画。"
- "有鉴于此，本文旨在构建...研究框架，系统揭示...时空规律，为...提供科学依据。"

### Methods
- "为了揭示...特征，采用...方法，基于...数据，分析了..."
- "利用...指数分别对...进行了定量表征，通过...识别干旱事件，并采用...确定..."
- "在此基础上，引入...模型，建立...归因框架，以解析..."

### Results
- "结果表明，...呈显著下降趋势，下降速率约为..."
- "从空间分布上看，...呈现明显的区域差异，高值区主要集中于..."
- "值得注意的是，...不仅...，而且..."
- "对比分析发现，...与...存在显著的非同步响应特征"

### Discussion
- "上述结果表明...这一发现与...的研究结论基本一致。"
- "造成这种差异的原因可能在于..."
- "该结果在一定程度上印证了...的论点。"
- "然而，由于...的限制，...尚未得到充分量化，有待后续研究补充。"

### Conclusion
- "综上所述，本文主要结论如下："
- "研究成果可为...提供科学依据，对...具有重要参考价值。"

---

## Rule 10: Match Disciplinary Register

AI text often imports words from adjacent disciplines, creating subtle semantic dissonance. A term that is standard in economics or engineering can sound odd in geography, hydrology, or ecology. Select verbs and collocations that match the natural usage of the target discipline.

### 10.1 Geography / Hydrology / Earth Sciences Conventions

| Cross-disciplinary intruder | Natural alternative in geo/hydro context |
|---|---|
| 占据最大份额 | 储量最为丰富 / 占比最高 / 构成主要的淡水储备 |
| 份额 / 比重（用于资源） | 比例 / 占比 / 组成 / 储量 |
| 支撑（经济/社会义过强） | 维系 / 保障 / 维持 / 为...提供水源 |
| 深远威胁 | 长期威胁 / 潜在威胁 / 不可忽视的风险 |
| 提供理论支撑 | 提供理论依据 / 提供理论参考 |
| 提供决策支撑 | 提供决策参考 / 为决策提供依据 |
| 关系着...安全 | 关乎...安全 / 直接影响... |
| 引领...发展 | 推动... / 促进... / 为...提供方向 |
| 核心驱动力 | 主导因子 / 主要驱动因素 |
| 赋能... | 有助于... / 为...提供支撑 |

### 10.2 Prefer Natural Collocations Over General Verbs

| Awkward general verb | Disciplinary collocation |
|---|---|
| 进行刻画 | 开展...分析 / 刻画...特征 |
| 做出刻画 | 予以定量刻画 |
| 产生干旱 | 形成干旱 / 引发干旱 |
| 产出数据 | 获取数据 / 生成数据集 |
| 投入应用 | 得到应用 / 用于... |
| 产生差异 | 表现出差异 / 呈现分异 |

### 10.3 Use Earth-Science Register for Physical Processes

When describing physical systems, prefer geoscience phrasing over social-science phrasing:

- AI原文: "地下水在全球淡水储备中占据最大份额。"
- 改写后: "地下水是地球上储量最为丰富的淡水资源。" / "在全球淡水资源中，地下水储量占比最高。"

- AI原文: "并支撑着全球40%以上的灌溉农业。"
- 改写后: "维系着全球40%以上灌溉农业的用水需求。" / "为全球40%以上的灌溉农业提供水源保障。"

- AI原文: "对...构成深远威胁。"
- 改写后: "对...构成长期威胁。" / "给...带来潜在风险。"

- AI原文: "为...提供理论支撑。"
- 改写后: "为...提供理论依据。" / "可为...提供理论参考。"

---

## Rule 11: Preserve Technical Terminology Conventions

- First appearance of a translated term: provide Chinese term followed by English abbreviation in parentheses, e.g., "标准化降水指数（Standardized Precipitation Index, SPI）". After first use, use Chinese abbreviation or full Chinese term.
- Do not translate established English acronyms into awkward Chinese equivalents. Use the internationally accepted form: GRACE, GLDAS, SHAP, RF-SHAP, TWSA.
- Use precise hydrology/meteorology terminology: "传播时间" rather than "响应时间" when the literature standard is "传播"; "游程理论" for run theory; "含水层" for aquifer; "包气带" for vadose zone.
