"""
基于内容的推荐算法示例

根据物品特征相似度进行推荐
"""

import numpy as np
from sklearn.metrics.pairwise import cosine_similarity
from typing import List


class ContentBasedRecommender:
    """基于内容的推荐系统"""
    
    def __init__(self, item_features: np.ndarray):
        """
        初始化基于内容的推荐系统
        
        Args:
            item_features: 物品特征矩阵 (n_items, n_features)
        """
        self.item_features = item_features
        self.item_similarity = None
        self._compute_similarity()
    
    def _compute_similarity(self):
        """计算物品相似度矩阵"""
        self.item_similarity = cosine_similarity(self.item_features)
    
    def recommend(self, liked_items: List[int], n_recommendations: int = 5) -> List[int]:
        """
        基于用户喜欢的物品推荐相似物品
        
        Args:
            liked_items: 用户喜欢的物品索引列表
            n_recommendations: 推荐物品数量
            
        Returns:
            推荐物品的索引列表
        """
        if not liked_items:
            return []
        
        # 计算推荐分数
        n_items = self.item_similarity.shape[0]
        recommendation_scores = np.zeros(n_items)
        
        for liked_item in liked_items:
            recommendation_scores += self.item_similarity[liked_item]
        
        # 排除已喜欢的物品
        for liked_item in liked_items:
            recommendation_scores[liked_item] = -np.inf
        
        # 返回评分最高的物品
        recommended_items = np.argsort(recommendation_scores)[-n_recommendations:]
        return recommended_items[::-1].tolist()
    
    def recommend_with_ratings(self, user_ratings: np.ndarray, 
                               n_recommendations: int = 5) -> List[int]:
        """
        基于用户的评分推荐物品
        
        Args:
            user_ratings: 用户对物品的评分向量 (n_items,)
                         0表示未评分
            n_recommendations: 推荐物品数量
            
        Returns:
            推荐物品的索引列表
        """
        # 计算用户的偏好向量（评过分物品特征的加权平均）
        rated_items = np.where(user_ratings != 0)[0]
        
        if len(rated_items) == 0:
            return []
        
        # 计算用户偏好向量
        weights = user_ratings[rated_items] / np.sum(user_ratings[rated_items])
        user_profile = np.average(self.item_features[rated_items], 
                                 axis=0, weights=weights)
        
        # 计算所有物品与用户偏好的相似度
        item_scores = cosine_similarity([user_profile], self.item_features)[0]
        
        # 排除已评分的物品
        item_scores[rated_items] = -np.inf
        
        # 返回评分最高的物品
        recommended_items = np.argsort(item_scores)[-n_recommendations:]
        return recommended_items[::-1].tolist()


def create_movie_features():
    """创建示例电影特征矩阵
    
    特征：[动作, 爱情, 喜剧, 恐怖, 科幻]
    """
    return np.array([
        [1, 0, 0, 0, 1],  # 电影0: 动作科幻
        [0, 1, 1, 0, 0],  # 电影1: 爱情喜剧
        [1, 0, 1, 0, 0],  # 电影2: 动作喜剧
        [0, 1, 0, 0, 1],  # 电影3: 爱情科幻
        [0, 0, 0, 1, 0],  # 电影4: 恐怖
        [1, 0, 0, 1, 1],  # 电影5: 动作恐怖科幻
        [0, 1, 1, 0, 0],  # 电影6: 爱情喜剧
        [1, 1, 0, 0, 1],  # 电影7: 动作爱情科幻
        [0, 0, 1, 0, 0],  # 电影8: 喜剧
        [0, 0, 0, 1, 1],  # 电影9: 恐怖科幻
    ], dtype=float)


def main():
    """主程序：演示基于内容的推荐"""
    
    # 创建电影特征
    movie_features = create_movie_features()
    print("电影特征矩阵:")
    print("特征顺序: [动作, 爱情, 喜剧, 恐怖, 科幻]\n")
    print(movie_features)
    
    # 创建推荐系统
    recommender = ContentBasedRecommender(movie_features)
    
    # 示例1: 用户喜欢电影0（动作科幻）和电影1（爱情喜剧）
    print("\n\n用户喜欢的电影: 0 (动作科幻), 1 (爱情喜剧)")
    liked_items = [0, 1]
    recommendations = recommender.recommend(liked_items, n_recommendations=3)
    print(f"推荐电影: {recommendations}")
    
    # 示例2: 基于用户评分推荐
    print("\n\n用户评分: ")
    user_ratings = np.array([5, 4, 0, 0, 0, 0, 3, 0, 0, 0])  # 评过电影0、1、6
    print(user_ratings)
    
    recommendations = recommender.recommend_with_ratings(user_ratings, n_recommendations=3)
    print(f"推荐电影: {recommendations}")
    
    # 计算相似度
    print("\n\n电影相似度矩阵 (前5x5):")
    print(recommender.item_similarity[:5, :5])


if __name__ == "__main__":
    main()
