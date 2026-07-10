import unittest
import os
from src.engine import RecommenderEngine

class TestRecommenderEngine(unittest.TestCase):
    def setUp(self):
        # We assume data is in a 'data' folder relative to the project root
        self.engine = RecommenderEngine('data/movies.csv', 'data/ratings.csv')

    def test_engine_initialization(self):
        # This checks if the files were actually loaded
        self.assertIsNotNone(self.engine.movies)
        self.assertIsNotNone(self.engine.ratings)

if __name__ == '__main__':
    unittest.main()