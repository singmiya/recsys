# 推荐系统年度核心论文清单 (2009 - 2026) 📚

> **导读说明**：本目录完整收录了推荐系统领域 2009 - 2026 年的重要论文 PDF，共计 **33 篇唯一论文**（另有 2 份配套 PPT、1 份 arXiv 重复版本）。
> 全文按技术演进划分为 **七个时代**，从经典协同过滤与矩阵分解奠基，一路纵览至大模型与智能体推荐的最前沿脉络。
> 标注 👑 的论文为该时代最具影响力的必读经典。

---

## 📊 目录结构与论文统计

```
papers/recsys/
├── 2009/  # 2 篇 — 协同过滤早期反思
├── 2010/  # 3 篇 — 信任传播与社交推荐
├── 2011/  # 2 篇 — 序数回归与购后推荐
├── 2012/  # 3 篇 — ALS 排序与图分割近邻
├── 2013/  # 1 篇 + 1 PPT — 并行 SGD 加速
├── 2014/  # 1 篇 — 停留时间信号
├── 2015/  # 1 篇 — 上下文感知事件推荐
├── 2016/  # 2 篇 + 1 PPT — 多样性与局部模型
├── 2017/  # 3 篇 — DeepFM 与特征交叉
├── 2018/  # 1 篇 — SASRec 序列推荐
├── 2019/  # 3 篇 — BERT4Rec / NGCF / 知识图谱
├── 2020/  # ⚠️ 空（待补充）
├── 2021/  # ⚠️ 空（待补充）
├── 2022/  # 2 篇 — 自监督学习综述与端侧推荐
├── 2023/  # 5 篇 + 1 重复 — 扩散/生成/因果/多模态
├── 2024/  # 5 篇 + 1 重复 — LLM 推荐 & 对比学习 GNN
├── 2025/  # 3 篇 — 扩散综述 & Agentic Rec
└── 2026/  # 1 篇 — 生成式推荐全景综述
```

---

## 🚀 2025 - 2026 年最新前沿：大模型与智能体推荐 (LLM & Agent-Rec)

推荐系统全面告别传统的"特征交叉/漏斗排序"，转向以大语言模型为底座的"语义对齐、多轮交互、端到端生成及智能体决策"时代。

### 1. "A Survey on Generative Recommendation: Data, Model, and Tasks" (2026)
* **关键词**: Generative Rec, Tokenization, End-to-End, 生成式推荐全景
* **难度评级**: ⭐⭐⭐⭐⭐
* **核心价值**: 2026 年最新的生成式推荐全景综述。从数据、模型、任务三个维度系统梳理了生成式推荐领域的完整技术栈，涵盖 ID Tokenization、语义编码、端到端生成范式的最新进展。
* **文件**: `2026/2026_Generative_Recommendation_Survey_arXiv2510.27157.pdf`

### 2. "Towards Agentic Recommender Systems in the Era of Multimodal Large Language Models" (2025)
* **关键词**: AI Agents, Personalized Action, Agentic Rec, 多模态大模型
* **难度评级**: ⭐⭐⭐⭐⭐
* **核心价值**: 2025 年最前沿的智能体推荐论文。详细阐述了推荐系统如何从"被动填充信息流"演进为具有自主规划、工具调用与多模态理解能力的个性化 AI Agent，标志着推荐范式从排序到行动的根本性转变。
* **文件**: `2025/2025_Towards_Agentic_Recommender_Systems_arXiv2503.16734.pdf`

### 3. "Diffusion Models in Recommendation Systems: A Survey" (2025)
* **关键词**: Diffusion Model, 生成模型, 去噪扩散, 兴趣轨迹
* **难度评级**: ⭐⭐⭐⭐
* **核心价值**: 对扩散模型在推荐系统中的应用做了全面综述，覆盖用户兴趣建模、数据增强、反事实推理等场景，是理解 Diffusion × RecSys 交叉领域的最佳入门文献。
* **文件**: `2025/2025_Diffusion_Models_in_Recommendation_Systems_Survey_arXiv2501.10548.pdf`

### 4. "Intent-aware Diffusion with Contrastive Learning for Sequential Recommendation" (2025)
* **关键词**: Diffusion, Contrastive Learning, Sequential Rec, 意图感知
* **难度评级**: ⭐⭐⭐⭐
* **核心价值**: 将扩散模型与对比学习有机结合，引入意图感知机制捕捉用户多粒度行为意图，在序列推荐任务中取得了显著提升，代表了扩散推荐从理论走向精细化的最新方向。
* **文件**: `2025/2025_Intent_aware_Diffusion_with_Contrastive_Learning_arXiv2504.16077.pdf`

---

## 📅 2023 - 2024 年论文：LLM 工业落地、扩散模型与多模态生成

### 1. "Collaborative Large Language Model for Recommender Systems" (2024)
* **关键词**: LLM-Rec, Collaborative Embedding, 语义对齐
* **难度评级**: ⭐⭐⭐⭐
* **核心价值**: 攻克了大模型难以有效融合离散用户行为数据的痛点，通过协同嵌入对齐技术让 LLM 完美理解传统 CF 信号，是 LLM + RecSys 工业落地的关键突破。
* **文件**: `2024/2024_Collaborative_Large_Language_Model_for_Recommender_Systems.pdf`

### 2. "Enhancing ID-based Recommendation with Large Language Models (LLM4IDRec)" (2024)
* **关键词**: LLM, ID-based Rec, 语义增强, 冷启动
* **难度评级**: ⭐⭐⭐⭐
* **核心价值**: 针对工业界大量 ID-based 特征与大模型语义空间不对齐的困境，提出将 LLM 语义知识注入 ID 嵌入的方案，在不破坏现有召回/排序架构的前提下实现性能飞跃。
* **文件**: `2024/2024_Enhancing_ID_based_Recommendation_with_LLM_TOIS.pdf`

### 3. "A Review of Modern Recommender Systems Using Generative Models (Gen-RecSys)" (KDD 2024)
* **关键词**: 生成式推荐综述, Diffusion, LLM, GAN
* **难度评级**: ⭐⭐⭐⭐
* **核心价值**: KDD 2024 的生成式推荐综述，系统回顾了基于 GAN、VAE、Diffusion 和 LLM 的生成式推荐方法，为研究者提供了从传统判别式到生成式范式的完整过渡指南。
* **文件**: `2024/2024_GenRecSys_KDD24_Review.pdf`

### 4. "Exploring the Impact of Large Language Models on Recommender Systems: An Extensive Review" (2024)
* **关键词**: LLM, Zero-Shot, In-Context Learning, Prompt 工程
* **难度评级**: ⭐⭐⭐
* **核心价值**: 深入评估了大模型在推荐召回与重排阶段的真实表现，给出了 Prompt 工程在实际推荐场景下的优势、局限性与算力瓶颈分析，是理解 LLM 推荐落地的必读参考。
* **文件**: `2024/2024_LLMs_for_Recommendation_Survey_arXiv2402.18590.pdf`

### 5. "Spatio-Temporal Contrastive Learning Enhanced GNNs for Session-based Recommendation" (2024)
* **关键词**: 对比学习, 时空建模, 会话推荐, GNN
* **难度评级**: ⭐⭐⭐⭐
* **核心价值**: 将时空信息与对比学习同时引入 GNN 会话推荐框架，捕捉用户在空间和时间维度上的动态偏好迁移，显著提升了短会话场景下的推荐精度。
* **文件**: `2024/2024_Spatio_Temporal_Contrastive_Learning_Session_Recommendation.pdf`

### 6. "Recommender Systems with Generative Retrieval (TIGER)" (NeurIPS 2023)
* **关键词**: Generative Retrieval, Semantic ID, Tokenization
* **难度评级**: ⭐⭐⭐⭐⭐
* **核心价值**: NeurIPS 2023 里程碑论文。提出用语义 Token（Semantic ID）替代传统物品 ID，将推荐问题重构为序列到序列的生成式检索任务，开辟了 Generative Retrieval 全新赛道。
* **文件**: `2023/2023_Recommender_Systems_with_Generative_Retrieval_TIGER_NeurIPS.pdf`

### 7. "Generative Recommendation: Towards Next-generation Recommender Paradigm (GeneRec)" (2023)
* **关键词**: Generative Rec, Tokenization, End-to-End, 生成式推荐
* **难度评级**: ⭐⭐⭐⭐⭐
* **核心价值**: 奠定了生成式推荐的理论框架。探讨了如何打破传统的"检索-粗排-精排"漏斗，将整个系统重构成直接端到端生成物品 ID 或文本的全新生成流。
* **文件**: `2023/2023_Generative_Recommendation_GeneRec_arXiv2304.03516.pdf`
* **备注**: 2024 年目录中存有同名文件 `2024_Generative_Recommendation_Towards_Next-generation_Recommender_Paradigm.pdf`，为同一论文的不同版本

### 8. "Diffusion Recommender Model (DiffRec)" (2023)
* **关键词**: 扩散模型 (Diffusion), 去噪生成, 协同过滤
* **难度评级**: ⭐⭐⭐⭐
* **核心价值**: 标志着去噪扩散模型正式跨界进入推荐领域。将用户交互向量视为"噪声图像"，通过反向去噪过程重建用户完整偏好，为高维稀疏数据提供了全新建模视角。
* **文件**: `2023/2023_Diffusion_Recommender_Model_DiffRec.pdf`（正式版）、`2023/2023_Diffusion_Recommender_Model_DiffRec_arXiv2304.04971.pdf`（arXiv 预印本）

### 9. "Causal Inference in Recommender Systems: A Survey and Future Directions" (2023)
* **关键词**: 因果推断, 选择偏差, 反事实推断, 去偏
* **难度评级**: ⭐⭐⭐⭐
* **核心价值**: 系统性地引入因果推断方法，用于消除推荐系统中根深蒂固的流行度偏差和位置曝光偏差，实现真正捕捉用户兴趣的无偏推荐，是该领域最全面的因果综述。
* **文件**: `2023/2023_Causal_Inference_in_Recommender_Systems_Survey.pdf`

### 10. "A Comprehensive Survey on Multimodal Recommender Systems" (2023)
* **关键词**: 多模态推荐, 视频表征, 跨模态对齐, 分类体系
* **难度评级**: ⭐⭐⭐⭐
* **核心价值**: 针对短视频、电商直播等复杂多模态场景，建立了完整的多模态推荐分类体系，涵盖特征提取、模态融合与跨模态对齐的代表性方法，是该方向最权威的综述文献。
* **文件**: `2023/2023_Comprehensive_Survey_on_Multimodal_Recommender_Systems.pdf`

---

## 📅 2022 年论文：自监督对比学习与端侧推荐

### 1. "Self-Supervised Learning for Recommender Systems: A Survey" (2022, IEEE TKDE)
* **关键词**: Contrastive Learning, Self-Supervised, Data Sparsity, 对比学习综述
* **难度评级**: ⭐⭐⭐⭐
* **核心价值**: 奠定了自监督对比学习在推荐领域的统治地位。全面梳理了数据增强、对比目标设计、多任务学习等关键组件，极大缓解了数据稀疏带来的过拟合问题。2023 年目录中存有同论文的副本。
* **文件**: `2022/2022_SSL_for_Recommender_Systems_Survey_arXiv2203.15876.pdf`

### 2. "Efficient On-Device Session-Based Recommendation" (2022)
* **关键词**: On-Device, 端侧推理, 会话推荐, 模型压缩
* **难度评级**: ⭐⭐⭐
* **核心价值**: 面向移动端资源受限场景，探索了如何在设备端高效执行会话推荐，涵盖模型轻量化、推理加速等工程实践，是将学术模型推向真实产品环境的重要参考。
* **文件**: `2022/2022_Efficient_On_Device_Session_Based_Recommendation_arXiv2209.13422.pdf`

---

## 📅 2018 - 2019 年论文：Transformer 序列推荐与图神经网络革命

### 1. "BERT4Rec: Sequential Recommendation with Bidirectional Encoder Representations from Transformers" (CIKM 2019) 👑 必读
* **关键词**: BERT, 双向 Transformer, Cloze Task, 序列推荐
* **难度评级**: ⭐⭐⭐⭐
* **核心价值**: 成功将 NLP 中的双向 Transformer 引入序列推荐，打破了传统 RNN 只能单向（从左到右）建模的限制。引入完形填空（Cloze Task）任务，大幅提升了点击序列下一跳预测的准确率。
* **文件**: `2019/2019_BERT4Rec_CIKM_arXiv1904.06690.pdf`

### 2. "Neural Graph Collaborative Filtering (NGCF)" (SIGIR 2019) 👑 顶级必读
* **关键词**: NGCF, 图卷积网络 (GCN), 协同过滤, Message Passing
* **难度评级**: ⭐⭐⭐⭐⭐
* **核心价值**: 开创了图神经网络推荐的黄金时代。摒弃了传统方法只在最后做向量点积的局限，直接将用户-物品的显式二部图高阶拓扑结构融入到 Embedding 的信息传递（Message Passing）中。
* **文件**: `2019/2019_NGCF_SIGIR_arXiv1905.08108.pdf`

### 3. "Unifying Knowledge Graph Learning and Recommendation: Towards a Better Understanding of User Preferences" (2019)
* **关键词**: 知识图谱, 语义推荐, 联合学习, 用户偏好
* **难度评级**: ⭐⭐⭐⭐
* **核心价值**: 将知识图谱表示学习与推荐系统统一到同一框架下联合优化，利用实体与关系的语义信息增强用户偏好建模，为后续 KG-enhanced Rec 方向提供了方法论基础。
* **文件**: `2019/2019_Unifying_Knowledge_Graph_Learning_and_Recommendation.pdf`

### 4. "Self-Attentive Sequential Recommendation (SASRec)" (ICDM 2018) 👑 序列推荐奠基
* **关键词**: SASRec, 自注意力机制, 序列建模, Transformer
* **难度评级**: ⭐⭐⭐⭐
* **核心价值**: 经典的单向 Transformer 序列推荐模型。用严格的数学推导和实验证明了 Self-Attention 在捕捉用户长短期动态兴趣上完爆传统的 GRU 和 LSTM 模型，是 BERT4Rec 的重要前作。
* **文件**: `2018/2018_SASRec_ICDM_arXiv1808.09781.pdf`

---

## 📅 2017 年论文：深度学习与特征交叉元年

### 1. "DeepFM: A Factorization-Machine based Neural Network for CTR Prediction" (IJCAI 2017 / arXiv 2017) 👑 工业常青树
* **关键词**: DeepFM, CTR 预测, 因子分解机, 特征高阶交叉
* **难度评级**: ⭐⭐⭐⭐
* **核心价值**: 将线性 FM 模块与深层 DNN 模块并联共享输入，同时兼顾低阶显式特征交叉与高阶隐式非线性交互。至今仍是工业界 CTR 预估的主流基准之一，开启了特征自动交叉的深度学习时代。
* **文件**: `2017/2017_DeepFM_arXiv1703.04247.pdf`

### 2. "Translation-based Recommendation" (2017)
* **关键词**: Translation, 嵌入空间, 平移建模, 用户-物品交互
* **难度评级**: ⭐⭐⭐
* **核心价值**: 将用户-物品交互建模为嵌入空间中的平移操作（user + item ≈ context），为推荐系统提供了一种新颖的几何直觉，启发了后续多项基于度量学习的推荐方法。
* **文件**: `2017/Translation-based Recommendation.pdf`

### 3. "Modeling the Assimilation-Contrast Effects in Online Product Rating Systems: Debiasing and Recommendations" (2017)
* **关键词**: 同化对比效应, 评分偏差, 去偏, 在线评分
* **难度评级**: ⭐⭐⭐
* **核心价值**: 从认知心理学角度建模在线评分中的同化-对比效应（先前评分影响后续评分），并提出去偏方法。为推荐系统中的评分偏差问题提供了行为科学视角的解法。
* **文件**: `2017/Modeling the Assimilation-Contrast Effects in Online Product Rating Systems Debiasing and Recommendations.pdf`

---

## 📅 2014 - 2016 年论文：隐式反馈、上下文与多样性

### 1. "Adaptive, Personalized Diversity for Visual Discovery" (2016)
* **关键词**: 多样性, 个性化, 视觉发现, 探索-利用
* **难度评级**: ⭐⭐⭐
* **核心价值**: 针对用户缺乏明确意图的视觉浏览场景，提出自适应个性化多样性策略，在保证相关性的同时根据用户探索倾向动态调节推荐多样性，平衡了精准与新颖。
* **文件**: `2016/Adaptive, Personalized Diversity for Visual Discovery.pdf`

### 2. "Local Item-Item Models for Top-N Recommendation" (2016)
* **关键词**: SLIM, 局部模型, Item-based CF, Top-N 推荐
* **难度评级**: ⭐⭐⭐
* **核心价值**: 扩展了 SLIM（Sparse Linear Method）框架，提出为每个用户学习局部 Item-Item 模型，突破了全局共享相似度矩阵的局限，在 Top-N 推荐任务上取得了显著提升。
* **文件**: `2016/Local Item-Item Models for Top-N Recommendation.pdf`（配套 PPT：`2016/Local Item-Item Models for Top-N Recommendation_ppt.pdf`）

### 3. "Context-Aware Event Recommendation in Event-based Social Networks" (2015)
* **关键词**: 上下文感知, 事件推荐, 社交网络, EBSN
* **难度评级**: ⭐⭐⭐
* **核心价值**: 针对基于事件的社交网络（EBSN）场景，融合时间、地点、社交等多维上下文信号进行事件推荐，是将上下文感知方法应用于推荐系统的典型范例。
* **文件**: `2015/Context-Aware Event Recommendation in Event-based Social Networks.pdf`

### 4. "Beyond Clicks: Dwell Time for Personalization" (2014)
* **关键词**: 停留时间, 隐式反馈, 个性化, 用户参与度
* **难度评级**: ⭐⭐
* **核心价值**: 超越简单的点击信号，引入用户在内容上的停留时间（Dwell Time）作为更精细的隐式反馈指标，为个性化推荐提供了更丰富的用户兴趣信号。
* **文件**: `2014/Beyond Clicks- Dwell Time for Personalization.pdf`

---

## 📅 2009 - 2013 年论文：协同过滤与矩阵分解奠基

### 1. "A Fast Parallel SGD for Matrix Factorization in Shared Memory Systems" (2013)
* **关键词**: 并行 SGD, 矩阵分解, 共享内存, 大规模推荐
* **难度评级**: ⭐⭐⭐
* **核心价值**: 由 Chih-Jen Lin 团队提出的共享内存系统下并行 SGD 矩阵分解算法，通过 Hogwild! 式无锁并行大幅加速了 MF 训练，是将矩阵分解推向工业规模的关键工程贡献。
* **文件**: `2013/A Fast Parallel SGD for Matrix Factorization in Shared Memory Systems.pdf`（配套 PPT：`2013/A Fast Parallel SGD for Matrix Factorization in Shared Memory Systems_ppt.pdf`）

### 2. "Alternating Least Squares for Personalized Ranking" (2012)
* **关键词**: ALS, 个性化排序, 隐式反馈, BPR
* **难度评级**: ⭐⭐⭐
* **核心价值**: 将经典 ALS 矩阵分解从显式评分预测扩展到隐式反馈的个性化排序场景，结合 BPR 优化准则，为无显式评分的推荐场景提供了高效的训练方案。
* **文件**: `2012/Alternating Least Squares for Personalized Ranking.pdf`

### 3. "CLiMF: Learning to Maximize Reciprocal Rank with Collaborative Less-is-More Filtering" (2012)
* **关键词**: CLiMF, Reciprocal Rank, Top-N 推荐, 稀疏数据
* **难度评级**: ⭐⭐⭐
* **核心价值**: 直接优化倒数排名（Reciprocal Rank）而非传统的 MSE 损失，在极稀疏数据下仍能为用户推荐少量高相关物品，是"少而精"推荐理念的代表方法。
* **文件**: `2012/CLiMF- Learning to Maximize Reciprocal Rank with Collaborative Less-is-More Filtering.pdf`

### 4. "Using Graph Partitioning Techniques for Neighbour Selection in User-Based Collaborative Filtering" (2012)
* **关键词**: 图分割, 谱聚类, 近邻选择, User-based CF
* **难度评级**: ⭐⭐
* **核心价值**: 将谱聚类图分割技术引入 User-based CF 的近邻选择阶段，替代传统的全量相似度计算，在保持推荐质量的同时显著降低了计算复杂度。
* **文件**: `2012/Using Graph Partitioning Techniques for Neighbour Selection in User-Based Collaborative Filtering .pdf`

### 5. "OrdRec: An Ordinal Model for Predicting Personalized Item Rating Distributions" (2011)
* **关键词**: OrdRec, 序数回归, 评分分布, 个性化
* **难度评级**: ⭐⭐⭐
* **核心价值**: 突破传统矩阵分解只预测单一评分值的局限，用序数回归模型预测用户对物品的完整评分分布，为理解用户偏好的不确定性提供了新视角。
* **文件**: `2011/OrdRec- An Ordinal Model for Predicting Personalized Item Rating Distributions.pdf`

### 6. "Utilizing Related Product for Post-Purchase Recommendation in E-commerce" (2011)
* **关键词**: 购后推荐, 电商, 关联商品, 场景化推荐
* **难度评级**: ⭐⭐
* **核心价值**: 专门针对电商购后场景设计推荐策略，利用商品间关联关系为已购用户推荐相关商品，是场景化/阶段化推荐思想在电商领域的早期实践。
* **文件**: `2011/Utilizing Related Product for Post-Purchase Recommendation in E-commerce.pdf`

### 7. "A Matrix Factorization Technique with Trust Propagation for Recommendation in Social Networks" (2010)
* **关键词**: Trust Propagation, 社交推荐, 矩阵分解, 信任链
* **难度评级**: ⭐⭐⭐
* **核心价值**: 将社交网络中的信任传播机制融入矩阵分解框架，利用信任链弥补评分数据的稀疏性，是将社交信号引入推荐系统的经典之作。
* **文件**: `2010/A Matrix Factorization Technique with Trust Propagation for Recommendation in Social Networks.pdf`

### 8. "Merging Multiple Criteria to Identify Suspicious Reviews" (2010)
* **关键词**: 虚假评论, 多准则融合, 评论质量, 异常检测
* **难度评级**: ⭐⭐
* **核心价值**: 从多维度准则融合的角度识别在线平台上的虚假评论，为推荐系统中的评论可信度评估和反作弊提供了方法论基础。
* **文件**: `2010/Merging Multiple Criteria to Identify Suspicious Reviews.pdf`

### 9. "The Network Effects of Recommending Social Connections" (2010)
* **关键词**: 社交连接推荐, 网络效应, 企业社交网络
* **难度评级**: ⭐⭐
* **核心价值**: 研究企业社交网络中好友推荐的网络效应——推荐连接如何改变网络拓扑与用户行为，为社交推荐系统的长期影响评估提供了实证分析。
* **文件**: `2010/The Network Effects of Recommending Social Connections.pdf`

### 10. "Collaborative Prediction and Ranking with Non-Random Missing Data" (2009)
* **关键词**: 非随机缺失 (MNAR), 协同预测, 评分选择偏差
* **难度评级**: ⭐⭐⭐
* **核心价值**: 较早系统性地指出推荐数据中"用户选择评分"的过程本身存在非随机缺失（MNAR）偏差，并提出了联合建模观测过程与评分预测的框架，为后续去偏推荐研究奠定了思想基础。
* **文件**: `2009/ Collaborative Prediction and Ranking with Non-Random Missing Data.pdf`

### 11. "Understanding the Effect of Adaptive Preference Elicitation Methods on User Satisfaction of a Recommender System" (RecSys 2009)
* **关键词**: 偏好获取, 用户满意度, 属性引导, 案例引导
* **难度评级**: ⭐⭐
* **核心价值**: 从用户体验角度比较了属性引导（attribute-based）与案例引导（case-based）两种偏好获取方式对推荐系统满意度的影响，强调了推荐系统中用户交互设计的重要性。
* **文件**: `2009/Understanding the Effect of Adaptive Preference Elicitation Methods on User Satisfaction of a Recommender System.pdf`

---

## 📝 补充说明

### ⚠️ 空目录
- **2020/** 和 **2021/** 目录当前为空，待补充该时期重要论文（如 xDeepFM、DIN/DIEN 序列推荐、多任务学习 MMoE 等）。

### 📋 重复文件
| 文件 | 说明 |
|------|------|
| `2023_Diffusion_Recommender_Model_DiffRec.pdf` vs `2023_Diffusion_Recommender_Model_DiffRec_arXiv2304.04971.pdf` | 同一论文的正式版与 arXiv 预印本 |
| `2022_SSL_for_Recommender_Systems_Survey_arXiv2203.15876.pdf` vs `2023_Self_Supervised_Learning_for_Recommender_Systems_Survey.pdf` | 同一论文存于两个年度目录 |
| `2023_Generative_Recommendation_GeneRec_arXiv2304.03516.pdf` vs `2024_Generative_Recommendation_Towards_Next-generation_Recommender_Paradigm.pdf` | 同一论文存于两个年度目录 |

### 📎 配套 PPT
| 论文 | PPT 文件 |
|------|----------|
| A Fast Parallel SGD for MF (2013) | `2013/A Fast Parallel SGD for Matrix Factorization in Shared Memory Systems_ppt.pdf` |
| Local Item-Item Models for Top-N Rec (2016) | `2016/Local Item-Item Models for Top-N Recommendation_ppt.pdf` |

---

## 🏆 推荐阅读路线

### 第一阶段：奠基（1-2 周）
1. **"Collaborative Prediction and Ranking with Non-Random Missing Data"** (2009) — 理解 CF 本质偏差
2. **"A Matrix Factorization Technique with Trust Propagation"** (2010) — 掌握 MF + 社交信号
3. **"DeepFM"** (2017) — 进入深度学习时代

### 第二阶段：深度学习革命（2-3 周）
1. **"SASRec"** (2018) — Self-Attention 序列推荐
2. **"BERT4Rec"** (2019) — 双向 Transformer 推荐
3. **"NGCF"** (2019) — 图神经网络推荐

### 第三阶段：前沿探索（3-4 周）
1. **"Self-Supervised Learning for RecSys Survey"** (2022) — 对比学习范式
2. **"TIGER"** (2023) — 生成式检索
3. **"Towards Agentic Recommender Systems"** (2025) — 智能体推荐

---

## 📊 论文统计总览

| 时代 | 年份 | 论文数 | 核心关键词 | 平均难度 |
|------|------|--------|-----------|----------|
| CF 与 MF 奠基 | 2009-2013 | 11 | 协同过滤、矩阵分解、社交信任 | ⭐⭐~⭐⭐⭐ |
| 隐式反馈与上下文 | 2014-2016 | 4 | 多样性、上下文感知、隐式信号 | ⭐⭐~⭐⭐⭐ |
| 深度学习与特征交叉 | 2017 | 3 | DeepFM、Translation、去偏 | ⭐⭐⭐~⭐⭐⭐⭐ |
| Transformer 与 GNN | 2018-2019 | 4 | SASRec、BERT4Rec、NGCF、KG | ⭐⭐⭐⭐~⭐⭐⭐⭐⭐ |
| 自监督与端侧 | 2022 | 2 | 对比学习、端侧推理 | ⭐⭐⭐~⭐⭐⭐⭐ |
| LLM 与扩散模型 | 2023-2024 | 10 | Diffusion、LLM、生成式检索 | ⭐⭐⭐⭐~⭐⭐⭐⭐⭐ |
| 大模型与智能体 | 2025-2026 | 4 | Agentic Rec、生成式全景 | ⭐⭐⭐⭐~⭐⭐⭐⭐⭐ |

**总计：33 篇唯一论文 + 2 份 PPT + 1 份 arXiv 重复**

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

## 🔗 论文获取方式

### 学术数据库
- **arXiv**: https://arxiv.org/ — 预印本自由获取
- **Google Scholar**: https://scholar.google.com/ — 全文检索与引用追踪
- **ACM Digital Library**: https://dl.acm.org/ — RecSys / SIGIR / KDD 等会议官方源
- **IEEE Xplore**: https://ieeexplore.ieee.org/ — ICDM / TKDE 等期刊

### 推荐系统社区
- **RecSys 官网**: https://recsys.acm.org/
- **SIGIR 官网**: https://sigir.org/
- **KDD 官网**: https://www.kdd.org/

### 开源与代码复现
- **Papers with Code**: https://paperswithcode.com/ — 论文 + 代码一站式查找
- **GitHub**: 多数顶会论文附带官方实现仓库
- **RecBole**: https://recbole.io/ — 推荐系统统一实验框架，内置 100+ 模型复现

---

## 🎓 学习路线图

```
奠基阶段 (1-2 周)
   │
   ├─ 协同过滤本质偏差 → 2009 MNAR 论文
   ├─ 矩阵分解 + 社交信任 → 2010 Trust Propagation
   └─ 深度学习入门 → 2017 DeepFM
   ↓
序列与图建模阶段 (2-3 周)
   │
   ├─ 自注意力序列推荐 → 2018 SASRec
   ├─ 双向 Transformer → 2019 BERT4Rec
   └─ 图神经网络协同过滤 → 2019 NGCF
   ↓
自监督与生成范式阶段 (2-3 周)
   │
   ├─ 对比学习范式 → 2022 SSL 综述
   ├─ 扩散模型推荐 → 2023 DiffRec
   └─ 生成式检索 → 2023 TIGER
   ↓
大模型与智能体前沿 (3-4 周)
   │
   ├─ LLM × 推荐系统 → 2024 LLM4IDRec / Collaborative LLM
   ├─ 智能体推荐 → 2025 Agentic Rec
   └─ 生成式推荐全景 → 2026 Generative Rec Survey
```

---

## 💬 常见问题

**Q: 应该从哪篇论文开始读？**
A: 建议从 2017 年 DeepFM 入手——它兼具经典 CF 思想与深度学习范式，难度适中且工业价值极高。之后再按学习路线图向前回溯奠基论文、向后追踪前沿工作。

**Q: 需要读所有论文吗？**
A: 不必。标注 👑 的论文为各时代必读经典，建议优先精读；其余论文可按研究方向选择性阅读。

**Q: 2020-2021 年为什么是空的？**
A: 这两个年份目录暂未收录论文，计划后续补充 xDeepFM、DIN/DIEN、MMoE 等该时期重要工作。

**Q: 如何理解复杂的论文？**
A:
1. 先读摘要和结论，把握全局
2. 看图表理解核心思想
3. 重点阅读方法部分
4. 结合 RecBole 等框架跑代码复现
5. 查阅引用的基础论文补充前置知识

**Q: 论文找不到全文怎么办？**
A: 可以尝试以下途径：
- arXiv 预印本（文件名中含 arXiv 编号的均可在 arxiv.org 搜索到）
- 作者个人主页 / Google Scholar
- GitHub 仓库（部分论文附带链接）
- 学术社交网络（ResearchGate 请求全文）

**Q: 目录中有重复文件怎么处理？**
A: 部分论文同时存于两个年份目录（如 SSL 综述在 2022/ 和 2023/ 各有一份，DiffRec 有正式版与 arXiv 版）。建议以正式版或最新版为主阅读，arXiv 版可作为补充参考。

---

## 🔄 持续更新

本索引会定期更新最新的 RecSys 及相关会议论文。

**近期计划补充**：
- [ ] 2020 年：xDeepFM、DIN、DIEN 等特征交叉与序列推荐经典
- [ ] 2021 年：MMoE 多任务学习、LightGCN 轻量图推荐等
- [ ] 2023-2024 年：更多 LLM 推荐实证研究
- [ ] 补充各论文的代码仓库链接

**最后更新**: 2026年6月6日 | **维护者**: singmiya

---

**开始你的推荐系统论文阅读之旅吧！** 📚✨
