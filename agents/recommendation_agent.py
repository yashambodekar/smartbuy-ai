import json
import re

from utils.llm import llm


def recommendation_agent(state):

    product_data = state.get(
        "product_data",
        {}
    )

    category = state.get(
        "category",
        "Unknown"
    )

    pros = state.get(
        "pros",
        []
    )

    cons = state.get(
        "cons",
        []
    )

    review_score = state.get(
        "review_score",
        0
    )

    prompt = f"""
    You are an expert shopping advisor.

    Current Product:
    {product_data.get('title')}

    Category:
    {category}

    Pros:
    {pros}

    Cons:
    {cons}

    Review Score:
    {review_score}/10

    Suggest 3 alternative products.

    For each product provide:

    - name
    - reason

    Return ONLY valid JSON.

    Example:

    {{
      "recommendations": [
        {{
          "name": "Product Name",
          "reason": "Better battery life"
        }}
      ]
    }}
    """

    response = llm.invoke(prompt)

    raw = response.content.strip()

    try:

        raw = re.sub(
            r"```json|```",
            "",
            raw
        ).strip()

        data = json.loads(raw)

        recommendations = data.get(
            "recommendations",
            []
        )

    except Exception as e:

        print(
            "Recommendation Parse Error:",
            e
        )

        recommendations = []

    return {
        **state,
        "recommendations":
        recommendations
    }