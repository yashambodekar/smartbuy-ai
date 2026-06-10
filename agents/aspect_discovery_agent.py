from utils.llm import llm
import ast
import json


def aspect_discovery_agent(state):

    reviews = state.get(
        "reviews",
        []
    )

    if not reviews:

        return {
            **state,
            "detected_aspects": []
        }

    combined_reviews = "\n".join(
        reviews[:10]
    )

    prompt = f"""
    You are an expert e-commerce review analyst.

    Analyze the reviews and identify the
    most discussed product aspects from the reviews.

    Examples:

    Phone:
    ["battery","camera","display"]

    Face Wash:
    ["acne control","oil control","fragrance"]

    Shoes:
    ["comfort","durability","grip"]

    Return ONLY a valid Python list.

    Reviews:

    {combined_reviews}
    """

    response = llm.invoke(prompt)

    try:

        aspects = ast.literal_eval(
          response.content.strip()
       )

    except:

        aspects = []

    return {
        **state,
        "detected_aspects": aspects
    }