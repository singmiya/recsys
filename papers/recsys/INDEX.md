# RecSys 论文库索引 (2018-2026)

## 📚 概述

本目录收录了推荐系统领域的重要论文，主要来自以下会议和期刊：

- **RecSys** - ACM Recommenders Systems (推荐系统顶级会议)
- **SIGIR** - Information Retrieval (信息检索)
- **KDD** - Knowledge Discovery and Data Mining (数据挖掘)
- **IJCAI/AAAI** - 人工智能顶级会议
- **WWW** - 万维网会议
- **CIKM** - 信息与知识管理
- **ICDM** - 数据挖掘
- **NeurIPS** - 神经信息处理系统

> **导读说明**：本仓库已在前半部分系统收录了 2009 - 2017 年的奠基性经典（涵盖传统协同过滤、矩阵分解 SVD 变体、Factorization Machines 交互以及深度学习开山之作 Wide & Deep、NCF 等）。本索引紧密承接 2017 年后的技术演进，纵览从 Transformer 序列建模、图神经网络（GNN）、对比学习，到大模型（LLM）与生成式智能体推荐的完整前沿脉络。

---

## 🗂️ 论文分类结构

```
papers/recsys/
├── 2009-2017/  # 奠基性经典（协同过滤、SVD、FM、Wide&Deep、NCF）
├── 2018/       # SASRec (自注意力序列推荐)
├── 2019/       # BERT4Rec, NGCF, Unifying KG
├── 2020/       # 待收录
├── 2021/       # 待收录
├── 2022/       # SSL Survey, On-Device Session-Based
├── 2023/       # Causal Inf, Multimodal Survey, DiffRec, GeneRec, TIGER, SSL Survey
├── 2024/       # Collaborative LLM, Generative Rec, LLM Survey, Spatio-Temporal CL
├── 2025/       # Diffusion Survey, Intent-Aware Diffusion, Agentic RecSys
└── 2026/       # Generative Recommendation Survey
```

---

## 📖 推荐论文清单

### 🎯 核心推荐算法

#### 协同过滤 (Collaborative Filtering)

1. **"Neural Graph Collaborative Filtering"** (SIGIR 2019) 👑 顶级必读
   - 关键词：NGCF, 图卷积网络 (GCN), 协同过滤
   - 难度：⭐⭐⭐⭐
   - 核心价值：开创了图神经网络推荐的黄金时代。该模型摒弃了传统方法只在最后做向量点积的局限，直接将用户-物品的显式二部图高阶拓扑结构融入到 Embedding 的信息传递（Message Passing）中。

2. **"Large Language Models for Collaborative Filtering: Reframing Continuous Semantics"** (2025)
   - 关键词：LLM-Rec, Collaborative Embedding, Semantic Alignment
   - 难度：⭐⭐⭐⭐
   - 核心价值：攻克了大模型难以有效融合离散用户行为数据的痛点，通过连续向量对齐技术，让大语言模型能够完美理解和处理传统的协同过滤（CF）信号。

#### 矩阵分解 (Matrix Factorization)

1. **"DeepFM: A Factorization-Machine based Neural Network for CTR Prediction"** (IJCAI 2018) 👑 工业常青树
   - 关键词：DeepFM, CTR 预测, 因子分解机, 特征高阶交叉
   - 难度：⭐⭐⭐
   - 核心价值：将线性 FM 模块与深层 DNN 模块并联共享输入，同时兼顾了低阶显式特征交叉与高阶隐式非线性交互，至今仍是工业界 CTR 预估的主流基准之一。

### 🧠 深度学习推荐

#### Transformer / Attention 机制

1. **"Self-Attentive Sequential Recommendation"** (ICDM 2018) 👑 序列推荐奠基
   - 关键词：SASRec, 自注意力机制, 序列建模
   - 难度：⭐⭐⭐
   - 核心价值：经典的单向 Transformer 序列推荐模型。用实验和严格的数学推导证明了 Self-Attention 在捕捉用户长短期动态兴趣上演化效果完爆传统的 GRU 和 LSTM 模型。

2. **"BERT4Rec: Sequential Recommendation with Bidirectional Encoder Representations from Transformers"** (CIKM 2019) 👑 必读
   - 关键词：BERT, 双向 Transformer, Cloze Task
   - 难度：⭐⭐⭐⭐
   - 核心价值：成功将 NLP 中的双向 Transformer 引入序列推荐，打破了过去传统 RNN 只能单向（从左到右）建模的限制。引入完形填空（Cloze Task）任务，大幅提升了点击序列下一跳预测的准确率。

#### Graph Neural Networks (图神经网络)

1. **"Neural Graph Collaborative Filtering"** (SIGIR 2019) 👑 顶级必读
   - 关键词：NGCF, 图卷积网络 (GCN), 协同过滤
   - 难度：⭐⭐⭐⭐
   - 核心价值：开创了图神经网络推荐的黄金时代。将用户-物品的显式二部图高阶拓扑结构融入到 Embedding 的信息传递中。

#### 对比学习 (Contrastive Learning)

1. **"Contrastive Learning for Recommender Systems"** (KDD 2022)
   - 关键词：Contrastive Learning, Self-Supervised, Data Sparsity
   - 难度：⭐⭐⭐
   - 核心价值：奠定了自监督对比学习在推荐领域的统治地位。通过对用户行为序列进行 Mask（掩码）或 Drop（丢弃）构建辅助任务，极大缓解了数据稀疏带来的过拟合。

2. **"Spatio-Temporal Contrastive Learning for Session-Based Recommendation"** (2024)
   - 关键词：时空对比学习, 会话推荐
   - 难度：⭐⭐⭐
   - 核心价值：将时空信息融入对比学习框架，提升会话推荐的序列建模能力。

#### 扩散模型 (Diffusion Models)

1. **"Diffusion Models for Recommendation Systems"** (RecSys 2023)
   - 关键词：扩散模型 (Diffusion), 生成模型, 兴趣轨迹
   - 难度：⭐⭐⭐⭐
   - 核心价值：标志着去噪扩散模型正式跨界进入推荐领域，用于拟合和生成高维稀疏的用户长周期动态兴趣轨迹。

2. **"Intent-aware Diffusion with Contrastive Learning for Recommendation"** (2025)
   - 关键词：意图感知, 扩散模型, 对比学习
   - 难度：⭐⭐⭐⭐
   - 核心价值：在扩散推荐框架中引入用户意图感知与对比学习联合优化，进一步提升兴趣建模精度。

### 🎯 CTR 预测

1. **"DeepFM: A Factorization-Machine based Neural Network for CTR Prediction"** (IJCAI 2018) 👑 工业常青树
   - 关键词：DeepFM, CTR 预测, 因子分解机, 特征高阶交叉
   - 难度：⭐⭐⭐
   - 核心价值：FM 线性模块与深层 DNN 模块并联共享输入，兼顾低阶显式特征交叉与高阶隐式非线性交互，至今仍是工业界 CTR 预估主流基准。

### 📊 知识图谱推荐

1. **"Unifying Knowledge Graph Learning and Recommendation: Towards a Better Understanding of User Preferences"** (WWW 2019)
   - 关键词：知识图谱 + 推荐融合, 语义推荐
   - 难度：⭐⭐⭐
   - 核心价值：将知识图谱学习与推荐系统统一建模，通过知识图谱增强用户偏好理解的语义深度，提升推荐可解释性。

### 🎬 多模态推荐

1. **"Multimodal Recommendation Systems: Beyond Text and Images"** (RecSys 2024)
   - 关键词：多模态推荐, 视频表征, 跨模态对齐
   - 难度：⭐⭐⭐
   - 核心价值：针对短视频、电商直播等复杂多模态场景，利用 Transformer 架构提取音视频、图像与文本的交织特征，大幅提升长尾物品推荐精度。

### 🎯 序列推荐

1. **"Self-Attentive Sequential Recommendation"** (ICDM 2018) 👑 序列推荐奠基
   - 关键词：SASRec, 自注意力机制, 序列建模
   - 难度：⭐⭐⭐
   - 核心价值：经典的单向 Transformer 序列推荐模型。Self-Attention 在捕捉用户长短期动态兴趣上效果完爆传统 GRU 和 LSTM。

2. **"BERT4Rec: Sequential Recommendation with Bidirectional Encoder Representations from Transformers"** (CIKM 2019) 👑 必读
   - 关键词：BERT, 双向 Transformer, Cloze Task
   - 难度：⭐⭐⭐⭐
   - 核心价值：双向 Transformer + 完形填空（Cloze Task），打破 RNN 单向限制，大幅提升序列下一跳预测准确率。

3. **"Efficient On-Device Session-Based Recommendation"** (2022)
   - 关键词：端侧推理, 会话推荐, 轻量化
   - 难度：⭐⭐⭐
   - 核心价值：面向移动设备的轻量级会话推荐方案，兼顾推理效率与推荐精度。

### 🤖 大模型推荐 (LLM-Rec)

1. **"Exploring the Frontiers of Recommendation Systems: Large Language Models as Recommender Systems"** (RecSys 2024)
   - 关键词：LLM, Zero-Shot, In-Context Learning
   - 难度：⭐⭐⭐
   - 核心价值：深入评估了大模型在推荐召回与重排阶段的真实工业表现，给出了 Prompt 工程在实际推荐场景下的优势、局限性与算力瓶颈分析。

2. **"Enhancing ID-based Recommendation with Large Language Models"** (TOIS 2024)
   - 关键词：LLM 增强, ID 推荐, 混合架构
   - 难度：⭐⭐⭐
   - 核心价值：探索如何用大语言模型增强传统 ID-based 推荐系统，实现语义信号与协同信号的有效融合。

### 🎨 生成式推荐 (Generative Rec)

1. **"Generative Recommendation: Towards Next-Generation Recommender Systems"** (2025)
   - 关键词：Generative Rec, Tokenization, End-to-End
   - 难度：⭐⭐⭐⭐
   - 核心价值：奠定了生成式推荐的理论框架。探讨了如何打破传统的"检索-粗排-精排"漏斗，将整个系统重构成直接端到端生成物品 ID 或文本的全新生成流。

2. **"Recommender Systems with Generative Retrieval (TIGER)"** (NeurIPS 2023)
   - 关键词：生成式检索, Semantic ID, 候选召回
   - 难度：⭐⭐⭐⭐
   - 核心价值：提出基于 Semantic ID 的生成式检索框架，用生成模型替代传统双塔召回，开启新一代召回范式。

### 🎨 去偏推荐

1. **"Causal Inference in Recommender Systems: A Survey and Future Directions"** (KDD 2021)
   - 关键词：因果推断, 选择偏差, 反事实推断
   - 难度：⭐⭐⭐⭐
   - 核心价值：系统性地引入因果推断（Causal Inference）方法，用于消除推荐系统中根深蒂固的流行度偏差和位置曝光偏差，实现真正捕捉用户兴趣的无偏推荐。

### 🤖 AI Agent 推荐

1. **"Recommender AI Agents: A Survey on Agentic Personalization"** (2026)
   - 关键词：AI Agents, Personalized Action, Long-term Memory
   - 难度：⭐⭐⭐⭐⭐
   - 核心价值：2026 年最前沿的主动推荐综述。详细阐述了推荐系统如何从"被动填充信息流"演进为具有长期记忆、能自发进行规划决策并调用工具的个性化 AI Agent。

### 📱 移动端推荐

1. **"Efficient On-Device Session-Based Recommendation"** (2022)
   - 关键词：端侧推理, 会话推荐, 轻量化模型
   - 难度：⭐⭐⭐
   - 核心价值：面向移动设备的轻量级会话推荐方案，解决端侧算力受限场景下的实时推荐问题。

---

## 🏆 顶级论文推荐阅读顺序

### 第一阶段（基础概念，1-2 周）
1. **DeepFM** (2018) — 理解 FM 线性交叉 + DNN 非线性交叉的经典范式
2. **SASRec** (2018) — 掌握自注意力机制在序列建模中的应用
3. **Unifying Knowledge Graph Learning and Recommendation** (2019) — 知识图谱增强推荐

### 第二阶段（深度学习推荐，2-3 周）
1. **BERT4Rec** (2019) — Transformer 双向序列推荐
2. **Neural Graph Collaborative Filtering** (2019) — GNN 图协同过滤
3. **Contrastive Learning for Recommender Systems** (2022) — 自监督对比学习范式

### 第三阶段（前沿探索，3-4 周）
1. **Causal Inference in Recommender Systems** (2021) — 因果推断与去偏
2. **Diffusion Models for Recommendation Systems** (2023) — 扩散模型推荐
3. **Large Language Models as Recommender Systems** (2024) — 大模型工业落地

### 第四阶段（最新前沿，2-3 周）
1. **Generative Recommendation** (2025) — 生成式推荐框架
2. **Recommender AI Agents** (2026) — 智能体主动推荐

---

## 🔗 论文获取方式

### 学术资源
- **arXiv**: https://arxiv.org/
- **Google Scholar**: https://scholar.google.com/
- **ACM Digital Library**: https://dl.acm.org/
- **IEEE Xplore**: https://ieeexplore.ieee.org/

### 推荐系统相关网站
- **RecSys 官网**: https://recsys.acm.org/
- **SIGIR 官网**: https://sigir.org/
- **KDD 官网**: https://www.kdd.org/

### 预印本和开源资源
- **arXiv**: 自由获取预印本
- **GitHub**: 许多论文包含代码实现
- **Papers with Code**: https://paperswithcode.com/

---

## 📝 论文阅读笔记模板

```markdown
# 论文标题

## 基本信息
- **作者**:
- **发表年份**:
- **会议/期刊**:
- **论文链接**:

## 核心贡献
1.
2.
3.

## 关键技术
-
-

## 实验结果
- 数据集:
- 指标改进:

## 个人总结
- 优点:
- 缺点:
- 应用场景:

## 相关论文
-
-
```

---

## 🎯 按主题分类

### 协同过滤相关
- 矩阵分解 (DeepFM)
- 图方法 (NGCF)
- LLM 增强协同过滤

### 深度学习相关
- Transformer / Attention (SASRec, BERT4Rec)
- GNN 推荐 (NGCF)
- 对比学习 (CL4Rec, Spatio-Temporal CL)
- 扩散模型 (DiffRec, Intent-Aware Diffusion)

### 序列推荐相关
- 自注意力序列建模 (SASRec)
- 双向 Transformer 序列 (BERT4Rec)
- 端侧会话推荐 (On-Device)

### 大模型 & 生成式推荐
- LLM 工业落地 (LLMs for Recommendation, Enhancing ID-based)
- 生成式检索 (TIGER)
- 生成式推荐范式 (Generative Rec)
- AI Agent 推荐

### 多模态 & 知识增强
- 知识图谱推荐 (Unifying KG)
- 多模态推荐 (Multimodal RecSys)

### 系统问题相关
- 去偏学习 (Causal Inference)
- 端侧推理 (On-Device Session-Based)

---

## 📊 论文统计

| 类别 | 数量 | 难度区间 |
|------|------|----------|
| 协同过滤 / GNN | 3 | ⭐⭐⭐ - ⭐⭐⭐⭐ |
| Transformer / 序列推荐 | 4 | ⭐⭐⭐ - ⭐⭐⭐⭐ |
| 对比学习 | 2 | ⭐⭐⭐ |
| 扩散模型 | 2 | ⭐⭐⭐⭐ |
| 大模型推荐 (LLM) | 2 | ⭐⭐⭐ - ⭐⭐⭐⭐ |
| 生成式推荐 | 2 | ⭐⭐⭐⭐ |
| 多模态 / 知识图谱 | 2 | ⭐⭐⭐ |
| 因果推断 / 去偏 | 1 | ⭐⭐⭐⭐ |
| AI Agent | 1 | ⭐⭐⭐⭐⭐ |
| 移动端推荐 | 1 | ⭐⭐⭐ |

---

## 🎓 学习路线图

```
基础阶段
   ↓
协同过滤 → 矩阵分解 (DeepFM)
   ↓
进阶阶段
   ↓
自注意力序列 (SASRec) → 双向 Transformer (BERT4Rec)
   ↓
高级阶段
   ↓
GNN 推荐 (NGCF) → 对比学习 → 因果推断
   ↓
前沿阶段
   ↓
扩散模型 → 大模型推荐 (LLM) → 生成式推荐 → AI Agent
```

---

## 💬 常见问题

**Q: 应该从哪篇论文开始读？**
A: 建议从 DeepFM (2018) 和 SASRec (2018) 开始，前者覆盖经典特征交叉，后者是序列推荐的 Transformer 入门。

**Q: 需要读所有论文吗？**
A: 不必。选择与你研究方向相关的论文深入学习。👑 标注的为必读经典。

**Q: 如何理解复杂的论文？**
A:
1. 先读摘要和结论
2. 看图表理解核心思想
3. 重点阅读方法部分
4. 查阅引用的基础论文

**Q: 论文找不到怎么办？**
A: 可以尝试在以下位置查找：
- arXiv preprint
- 作者个人主页
- GitHub repositories
- Papers with Code

---

## 🔄 持续更新

本索引会定期更新最新的 RecSys 和相关会议论文。

**最后更新**: 2026年6月6日
**维护者**: singmiya

---

**开始你的推荐系统论文阅读之旅吧！** 📚✨
