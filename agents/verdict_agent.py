from utils.llm import llm


def verdict_agent(state):

    product_data = state.get(
        "product_data",
        {}
    )

    review_summary = state.get(
        "review_summary",
        ""
    )

    aspect = state.get(
        "aspect",
        "general"
    )

    aspect_summary = state.get(
        "aspect_summary",
        ""
    )

    prompt = f"""
    You are an expert shopping advisor.

    Product Details:
    {product_data}

    Overall Review Analysis:
    {review_summary}

    Aspect Analyzed:
    {aspect}

    Aspect Analysis:
    {aspect_summary}

    Based on all the above information provide:

    1. Overall Product Score (0-100)
    2. BUY / CONSIDER / AVOID
    3. Top Reasons to Buy
    4. Potential Concerns
    5. Final Recommendation (2-3 lines)

    Keep the answer structured and concise.
    """

    response = llm.invoke(
        prompt
    )

    return {
        **state,
        "verdict": response.content
    }