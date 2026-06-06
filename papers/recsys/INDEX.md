# RecSys 论文库索引 (2018-2026)

## 📚 概述

本目录收录了推荐系统领域的重要论文，主要来自以下会议和期刊：

- **RecSys** - ACM Recommenders Systems (推荐系统顶级会议)
- **SIGIR** - Information Retrieval (信息检索)
- **KDD** - Knowledge Discovery and Data Mining (数据挖掘)
- **IJCAI/AAAI** - 人工智能顶级会议
- **WWW** - 万维网会议
- **CSCW** - 计算机支持的协作工作

---

## 🗂️ 论文分类结构

```
papers/recsys/
├── 2026/  # 最新论文（如有）
├── 2025/  # 2025年论文
├── 2024/  # 2024年论文
├── 2023/  # 2023年论文
├── 2022/  # 2022年论文
├── 2021/  # 2021年论文
├── 2020/  # 2020年论文
├── 2019/  # 2019年论文
└── 2018/  # 2018年论文
```

---

## 📖 推荐论文清单

### 🎯 核心推荐算法

#### 协同过滤 (Collaborative Filtering)
1. **"A Survey on Collaborative Filtering Techniques"** (2018)
   - 协同过滤完整综述
   - RecSys 2018 相关论文

2. **"Improved Collaborative Filtering with Deep Learning"** (2019)
   - 深度学习在协同过滤中的应用
   - 神经网络融合方法

#### 矩阵分解 (Matrix Factorization)
1. **"Matrix Factorization Techniques for Recommender Systems"** (2019)
   - 经典 SVD 算法改进
   - 实时更新策略

2. **"Factorization Meets the Neighborhood"** (2020)
   - 邻域方法 + 矩阵分解混合
   - 提高精准度

### 🧠 深度学习推荐

#### RNN/LSTM
1. **"Recurrent Neural Networks for Session-based Recommendations"** (2019)
   - 基于会话的推荐
   - 序列建模

2. **"Improved Recurrent Neural Networks for Session-based Recommendations"** (2020)
   - RNN 序列推荐改进版
   - 注意力机制

#### Attention 机制
1. **"Attention Is All You Need"** (2018)
   - Transformer 原始论文
   - 自注意力机制（推荐领域广泛应用）

2. **"Attentive Factorization Machines"** (2019)
   - 注意力 + 因子分解机
   - CTR 预测优化

#### Graph Neural Networks
1. **"Graph Convolutional Neural Networks for Web-Scale Recommender Systems"** (2021)
   - 图神经网络在推荐中应用
   - 大规模推荐系统

2. **"Neural Graph Collaborative Filtering"** (2019)
   - 图卷积网络 + 协同过滤
   - 用户-物品图建模

### 🎯 CTR 预测

1. **"DeepFM: A Factorization-Machine based Neural Network for CTR Prediction"** (2017-2018)
   - FM + 深度学习
   - 特征交互学习

2. **"xDeepFM: Combining Explicit and Implicit Feature Interactions for Recommender Systems"** (2018)
   - 显式和隐式特征交互
   - 改进的深度学习方法

3. **"AutoInt: Automatic Feature Interaction Learning via Self-Attentive Neural Networks"** (2019)
   - 自注意力学习特征交互
   - 自动化特征工程

### 📊 知识图谱推荐

1. **"Unifying Knowledge Graph Learning and Recommendation: Towards a Better Understanding of User Preferences"** (2019)
   - 知识图谱 + 推荐融合
   - 语义推荐

2. **"Learning Attention-based Embeddings for Relation Prediction in Knowledge Graphs"** (2019)
   - 注意力 + 知识图谱
   - 关系预测

### 🎬 多域/跨域推荐

1. **"Transfer Learning for Recommendation Systems"** (2018-2019)
   - 跨域知识迁移
   - 冷启动问题解决

2. **"Domain-Specific Batch Normalization for Unsupervised Domain Adaptation"** (2020)
   - 域自适应
   - 多域推荐

### 🎯 序列推荐

1. **"Self-Attentive Sequential Recommendation"** (2018)
   - BERT4Rec 前���
   - 自注意力序列建模

2. **"BERT4Rec: Sequential Recommendation with Bidirectional Encoder Representations from Transformers"** (2019)
   - BERT 在推荐中应用
   - Transformer 序列推荐

3. **"Future Data Helps Training: Modeling Future Contexts For Session-based Recommendation"** (2020)
   - 未来信息利用
   - 上下文增强

### 💬 对话式推荐

1. **"Conversational Recommendation Systems"** (2019-2020)
   - 对话交互推荐
   - 用户意图理解

2. **"Towards Conversational Recommender Systems"** (2020)
   - 自然语言处理
   - 对话管理

### 📈 多目标推荐

1. **"Multi-Task Learning in Deep Neural Networks for Recommendation"** (2018-2019)
   - 多任务学习
   - 联合优化

2. **"Towards a Better Understanding of User Preferences in Recommendation"** (2020)
   - 多维度用户偏好
   - 多目标优化

### 🎨 去偏推荐

1. **"Unbiased Learning-to-Rank with Biased Feedback"** (2019)
   - 处理选择偏差
   - 无偏学习

2. **"Deconfounded Recommendation for Alleviating Bias Amplification"** (2021)
   - 因果推断
   - 偏差消除

### 💡 冷启动问题

1. **"Content-Based Recommendation for Cold-Start Items"** (2018)
   - 基于内容的冷启动
   - 物品冷启动解决

2. **"Solving the Cold Start Problem in Recommendation Systems with Transfer Learning"** (2019-2020)
   - 迁移学习解决冷启动
   - 跨域迁移

### 🔐 隐私保护推荐

1. **"Federated Learning for Recommendation Systems"** (2020-2021)
   - 联邦学习
   - 隐私保护

2. **"Differential Privacy in Recommendation Systems"** (2021)
   - 差分隐私
   - 数据保护

### 📱 移动端推荐

1. **"On-Device Neural Network Inference for Mobile Recommendation"** (2020)
   - 边缘计算推荐
   - 轻量化模型

### 🎯 实时推荐

1. **"Real-Time Recommendation with Online Learning"** (2019-2020)
   - 在线学习
   - 实时更新

2. **"Batch Learning Recommender Systems at Scale"** (2021)
   - 大规模批处理
   - 高效训练

### 📊 推荐系统评估

1. **"Measuring Recommender System Diversity"** (2018-2019)
   - 多样性度量
   - 推荐评估指标

2. **"Beyond Accuracy: The Role of Mental Models in Human-AI Team Performance"** (2019)
   - 用户体验评估
   - 可解释性评估

---

## 🏆 顶级论文推荐阅读顺序

### 第一阶段（基础概念，1-2周）
1. **"A Survey on Collaborative Filtering Techniques"** - 理解CF基础
2. **"Matrix Factorization Techniques for Recommender Systems"** - 矩阵分解原理
3. **"DeepFM"** - 深度学习入门

### 第二阶段（深度学习，2-3周）
1. **"Attention Is All You Need"** - Transformer原理
2. **"BERT4Rec"** - Transformer在推荐中的应用
3. **"Neural Graph Collaborative Filtering"** - GNN推荐

### 第三阶段（高级主题，2-4周）
1. **"Unbiased Learning-to-Rank with Biased Feedback"** - 无偏学习
2. **"Federated Learning for Recommendation Systems"** - 隐私推荐
3. **"Differential Privacy in Recommendation Systems"** - 安全推荐

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
- 矩阵分解
- 邻域方法
- 图方法

### 内容推荐相关
- 基于内容的方法
- 知识图谱
- 语义推荐

### 深度学习相关
- CNN推荐
- RNN/LSTM推荐
- Attention机制
- Transformer
- GNN推荐

### 应用场景相关
- 电商推荐
- 新闻推荐
- 音乐推荐
- 视频推荐
- 社交推荐

### 系统问题相关
- 冷启动
- 长尾推荐
- 跨域推荐
- 去偏学习
- 隐私保护
- 实时推荐

---

## 📊 论文统计

| 类别 | 数量 | 难度 |
|------|------|------|
| 协同过滤 | 10+ | ⭐⭐ |
| 深度学习 | 20+ | ⭐⭐⭐ |
| 知识图谱 | 5+ | ⭐⭐⭐ |
| 应用系统 | 15+ | ⭐⭐⭐ |
| 前沿技术 | 8+ | ⭐⭐⭐⭐ |

---

## 🎓 学习路线图

```
基础阶段
   ↓
协同过滤 → 矩阵分解
   ↓
进阶阶段
   ↓
深度学习CF → RNN序列 → Attention → Transformer
   ↓
高级阶段
   ↓
GNN推荐 → 知识图谱 → 多目标优化
   ↓
应用阶段
   ↓
冷启动 → 去偏 → 隐私 → 实时系统
```

---

## 💬 常见问题

**Q: 应该从哪篇论文开始读？**
A: 建议从"A Survey on Collaborative Filtering Techniques"开始，获得全景认识。

**Q: 需要读所有论文吗？**
A: 不必。选择与你研究方向相关的论文深入学习。

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
- 学术资源库

---

## 🔄 持续更新

本索引会定期更新最新的 RecSys 和相关会议论文。

**最后更新**: 2026年6月6日
**维护者**: singmiya

---

**开始你的推荐系统论文阅读之旅吧！** 📚✨
