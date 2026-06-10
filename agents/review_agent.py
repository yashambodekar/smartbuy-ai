# agents/review_agent.py

from utils.llm import llm


def review_agent(state):

    reviews = state.get(
    "reviews",
    []
    )

    if not reviews:
       return {
        **state,
        "review_summary": "No reviews found."
       }
    
    print("Total Reviews:", len(reviews))

    for i, review in enumerate(reviews[:5]):
        print(f"\nReview {i+1}:")
        print(review[:200])

    combined_reviews = "\n".join(
        reviews[:10]
    )

    prompt = f"""
    Analyze these product reviews.

    Give:

    1. Top Pros
    2. Top Cons
    3. Overall Sentiment
    4. Buy Recommendation

    Reviews:

    {combined_reviews}
    """

    response = llm.invoke(prompt)

    return {
        **state,
        "review_summary": response.content
    }