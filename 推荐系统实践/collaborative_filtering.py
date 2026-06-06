"""
协同过滤推荐算法示例

基于用户相似度的推荐算法演示
"""

import numpy as np
from sklearn.metrics.pairwise import cosine_similarity
from typing import Tuple, List


class UserBasedCollaborativeFiltering:
    """基于用户的协同过滤推荐算法"""
    
    def __init__(self, user_item_matrix: np.ndarray, n_neighbors: int = 10):
        """
        初始化协同过滤模型
        
        Args:
            user_item_matrix: 用户-物品评分矩阵 (n_users, n_items)
            n_neighbors: 近邻用户数量
        """
        self.user_item_matrix = user_item_matrix
        self.n_neighbors = n_neighbors
        self.user_similarity = None
        self._compute_similarity()
    
    def _compute_similarity(self):
        """计算用户相似度矩阵"""
        # 使用余弦相似度
        self.user_similarity = cosine_similarity(self.user_item_matrix)
        # 将对角线设为0（用户与自己的相似度）
        np.fill_diagonal(self.user_similarity, 0)
    
    def recommend(self, user_id: int, n_recommendations: int = 5) -> List[int]:
        """
        为指定用户推荐物品
        
        Args:
            user_id: 用户ID
            n_recommendations: 推荐物品数量
            
        Returns:
            推荐物品的索引列表
        """
        # 获取最相似的n个用户
        similar_users = np.argsort(self.user_similarity[user_id])[-self.n_neighbors:]
        
        # 获取相似用户评过分的物品
        user_ratings = self.user_item_matrix[user_id]
        
        # 计算推荐分数
        recommendations = np.zeros(self.user_item_matrix.shape[1])
        
        for similar_user in similar_users:
            similarity = self.user_similarity[user_id, similar_user]
            # 只考虑用户未评过分的物品
            unrated_items = user_ratings == 0
            recommendations[unrated_items] += (
                similarity * self.user_item_matrix[similar_user, unrated_items]
            )
        
        # 返回评分最高的物品
        recommended_items = np.argsort(recommendations)[-n_recommendations:]
        return recommended_items[::-1].tolist()
    
    def evaluate(self, test_matrix: np.ndarray) -> Tuple[float, float]:
        """
        评估模型性能
        
        Args:
            test_matrix: 测试集用户-物品矩阵
            
        Returns:
            (precision, recall)
        """
        precision_list = []
        recall_list = []
        
        for user_id in range(test_matrix.shape[0]):
            # 获取用户实际评过分的物品
            actual_items = set(np.where(test_matrix[user_id] > 0)[0])
            
            if len(actual_items) == 0:
                continue
            
            # 获取推荐物品
            recommended_items = set(self.recommend(user_id, n_recommendations=5))
            
            # 计算precision和recall
            if len(recommended_items) > 0:
                precision = len(actual_items & recommended_items) / len(recommended_items)
                recall = len(actual_items & recommended_items) / len(actual_items)
                
                precision_list.append(precision)
                recall_list.append(recall)
        
        avg_precision = np.mean(precision_list) if precision_list else 0
        avg_recall = np.mean(recall_list) if recall_list else 0
        
        return avg_precision, avg_recall


def main():
    """主程序：演示协同过滤推荐"""
    
    # 创建示例数据：5个用户，10个物品
    # 0表示未评分，1-5表示评分
    user_item_matrix = np.array([
        [5, 4, 0, 0, 1, 0, 3, 0, 0, 0],
        [4, 5, 3, 0, 0, 2, 0, 0, 0, 0],
        [0, 3, 5, 4, 0, 0, 2, 0, 0, 0],
        [0, 0, 4, 5, 0, 0, 0, 3, 0, 0],
        [1, 0, 0, 0, 5, 4, 0, 0, 3, 0],
    ], dtype=float)
    
    # 创建模型
    cf_model = UserBasedCollaborativeFiltering(user_item_matrix, n_neighbors=3)
    
    # 为用户0推荐5个物品
    print("用户 0 的推荐物品:")
    recommendations = cf_model.recommend(user_id=0, n_recommendations=5)
    print(f"推荐物品索引: {recommendations}")
    
    # 为用户1推荐物品
    print("\n用户 1 的推荐物品:")
    recommendations = cf_model.recommend(user_id=1, n_recommendations=5)
    print(f"推荐物品索引: {recommendations}")
    
    print("\n用户相似度矩阵:")
    print(cf_model.user_similarity)


if __name__ == "__main__":
    main()
