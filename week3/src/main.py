# main.py
from src.engine import RecommenderEngine

def main():
    # Initialize your engine
    engine = RecommenderEngine('data/movies.csv', 'data/ratings.csv')
    
    try:
        user_id = int(input("Enter User ID: "))
        recs = engine.get_recommendations(user_id)
        
        print(f"\nTop Recommendations for User {user_id}:")
        for i, row in recs.iterrows():
            print(f"{i+1}. {row['title']} (Similarity Score: {row['score']:.2f})")
            
    except Exception as e:
        print(f"Error: Could not generate recommendations. {e}")

if __name__ == "__main__":
    main()