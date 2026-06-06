# 贡献指南

首先，感谢你对这个项目的关注！我们很欢迎社区的贡献。

## 📋 贡献方式

我们接受以下形式的贡献：

- 🐛 **报告 Bug** - 帮助我们找到和修复问题
- ✨ **添加新特性** - 实现新的推荐算法或改进
- 📚 **补充论文** - 添加新的推荐系统相关论文
- 📝 **改进文档** - 完善 README、注释和说明
- 🎓 **读书笔记** - 分享你的学习笔记和总结
- 💻 **改进代码** - 优化现有实现，提升代码质量
- 🌍 **翻译** - 将文档翻译成其他语言

## 🚀 开发流程

### 1. Fork 本仓库

访问 [https://github.com/singmiya/recsys](https://github.com/singmiya/recsys)，点击右上角的 **Fork** 按钮。

### 2. 克隆你的 Fork

```bash
git clone https://github.com/YOUR_USERNAME/recsys.git
cd recsys
git remote add upstream https://github.com/singmiya/recsys.git
```

### 3. 创建特性分支

```bash
git checkout -b feature/your-feature-name
```

分支命名规范：
- `feature/` - 新功能
- `fix/` - Bug 修复
- `docs/` - 文档更新
- `refactor/` - 代码重构
- `test/` - 测试相关

### 4. 进行修改

确保你的代码符合以下规范：

#### Python 代码规范
- 遵循 [PEP 8](https://www.python.org/dev/peps/pep-0008/) 风格指南
- 使用有意义的变量名和函数名
- 为复杂逻辑添加注释
- 每个函数添加 docstring

#### 示例

```python
def collaborative_filtering(user_item_matrix, num_neighbors=10):
    """
    实现基于用户的协同过滤推荐算法
    
    Args:
        user_item_matrix (np.ndarray): 用户-物品评分矩阵
        num_neighbors (int): 近邻数量，默认为 10
        
    Returns:
        np.ndarray: 推荐评分矩阵
        
    Example:
        >>> matrix = np.random.rand(100, 50)
        >>> predictions = collaborative_filtering(matrix)
    """
    pass
```

### 5. 提交更改

```bash
git add .
git commit -m "type: description"
```

提交信息规范（遵循 Conventional Commits）：

```
feat: 添加新的推荐算法
fix: 修复矩阵分解中的 bug
docs: 更新 README 文档
refactor: 重构协同过滤模块
test: 添加单元测试
chore: 更新依赖版本
```

### 6. 推送到你的 Fork

```bash
git push origin feature/your-feature-name
```

### 7. 创建 Pull Request

1. 在 GitHub 上访问你的 Fork
2. 点击 **Compare & pull request**
3. 添加清晰的标题和描述
4. 点击 **Create Pull Request**

## 📝 Pull Request 检查清单

提交 PR 前，请确保：

- [ ] 代码遵循 PEP 8 风格指南
- [ ] 添加了必要的注释和文档
- [ ] 包含了测试用例（如适用）
- [ ] 更新了 README 或相关文档
- [ ] 提交信息清晰明确
- [ ] 没有合并冲突

## 📚 添加论文

如果要添加新论文：

1. 将论文放在 `papers/` 文件夹中
2. 在论文名称前添加分类标签：
   - `[CF]` - 协同过滤
   - `[CB]` - 基于内容
   - `[DL]` - 深度学习
   - `[CTR]` - CTR 预测
   - `[RNN]` - 序列推荐

3. 在 README 中添加论文链接和简要说明

示例：
```markdown
- [CF] Collaborative Filtering Recommendation Algorithm - 2020
```

## 💡 最佳实践

### 代码质量
- 保持代码简洁易读
- 避免重复代码，使用函数或类抽象
- 使用有意义的名称
- 添加类型提示

### 文档
- 为公共函数���加 docstring
- 在复杂算法前添加说明
- 提供使用示例

### 测试
- 为新功能编写测试
- 确保测试通过
- 提高代码覆盖率

## 🤔 常见问题

**Q: 我可以修改其他用户的代码吗？**
A: 可以，但请在 commit message 中清楚说明原因，并给予原作者信用。

**Q: 如何处理合并冲突？**
A: 
```bash
git fetch upstream
git rebase upstream/master
# 解决冲突
git rebase --continue
git push -f origin feature/your-feature-name
```

**Q: PR 需要多长时间才能被合并？**
A: 通常 1-7 天，我们会尽快审查。

## 📞 获取帮助

- 创建 Issue 讨论想法
- 在 Discussion 中提问
- 查看现有 Issues 了解常见问题

## 🎉 致谢

感谢所有贡献者的支持和帮助！

---

**规则很简单：遵守 [行为准则](CODE_OF_CONDUCT.md)，我们会以最大的热情欢迎你的贡献！** 🚀
