from utils.llm import llm


def aspect_agent(state):

    reviews = state.get(
        "reviews",
        []
    )

    aspect = state.get(
        "aspect",
        "general"
    )

    if not reviews:

        return {
            **state,
            "aspect_summary":
            "No reviews found."
        }

    combined_reviews = "\n".join(
        reviews[:10]
    )

    prompt = f"""
    You are an expert e-commerce review analyst.

    Analyze ONLY information related to:

    {aspect}

    Ignore unrelated review content.

    Return:

    1. Aspect Score (/10)
    2. Positive Points
    3. Negative Points
    4. Customer Consensus
    5. Final Verdict on this aspect

    Reviews:

    {combined_reviews}
    """

    response = llm.invoke(
        prompt
    )

    return {
        **state,
        "aspect_summary":
        response.content
    }