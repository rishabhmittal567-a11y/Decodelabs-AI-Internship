import pandas as pd
from sklearn.metrics.pairwise import cosine_similarity

class RecommenderEngine:
    def __init__(self, movies_path: str, ratings_path: str):
        self.movies = pd.read_csv(movies_path)
        self.ratings = pd.read_csv(ratings_path)
        
        # 1. Create a matrix where rows are movies and columns are binary genre flags
        genre_matrix = self.movies['genres'].str.get_dummies(sep='|')
        self.movie_features = pd.concat([self.movies[['movieId', 'title']], genre_matrix], axis=1)

    def get_recommendations(self, user_id: int, top_n: int = 5):
        # 2. Identify movies the user has rated highly (4.0+)
        liked_movies = self.ratings[(self.ratings['userId'] == user_id) & 
                                    (self.ratings['rating'] >= 4.0)]['movieId']
        
        # 3. Create a 'User Profile' vector by averaging the genre vectors of liked movies
        user_vector = self.movie_features[self.movie_features['movieId'].isin(liked_movies)]
        user_profile = user_vector.drop(['movieId', 'title'], axis=1).mean().values.reshape(1, -1)
        
        # 4. Calculate Cosine Similarity between user profile and all movies
        all_movie_genres = self.movie_features.drop(['movieId', 'title'], axis=1)
        scores = cosine_similarity(user_profile, all_movie_genres).flatten()
        
        # 5. Return titles with the highest scores
        self.movie_features['score'] = scores
        recommendations = self.movie_features.sort_values(by='score', ascending=False)
        return recommendations[['title', 'score']].head(top_n)