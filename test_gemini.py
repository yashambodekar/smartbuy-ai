# test_gemini.py

from agents.review_agent import review_agent

reviews = [
    "Good for acne prone skin",
    "Refreshing face wash",
    "Best face wash ever",
    "Helps control oil",
    "Nice fragrance"
]

state = {
    "reviews": reviews
}

result = review_agent(state)

print(result["review_summary"])