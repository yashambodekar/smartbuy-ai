import json

from utils.llm import llm


def review_agent(state):

    reviews = state.get(
        "reviews",
        []
    )

    if not reviews:

        return {
            **state,
            "category": "unknown",
            "detected_aspects": [],
            "pros": [],
            "cons": [],
            "sentiment": "unknown",
            "review_score": 0.0,
            "review_summary": "No reviews found."
        }

    product_title = state.get(
        "product_data",
        {}
    ).get(
        "title",
        ""
    )

    combined_reviews = "\n".join(
        reviews[:10]
    )

    prompt = f"""
    Product:

    {product_title}

    Reviews:

    {combined_reviews}

    Analyze these reviews.

    Return ONLY valid JSON.

    Format:

    {{
        "category": "",
        "detected_aspects": [],
        "pros": [],
        "cons": [],
        "sentiment": "",
        "review_score": 0,
        "review_summary": ""
    }}

    Rules:

    - review_score between 0 and 10
    - detected_aspects between 3 and 7
    - sentiment should be positive, neutral or negative
    - output only JSON
    """

    response = llm.invoke(
        prompt
    )

    print("\nRAW REVIEW RESPONSE:\n")
    print(response.content)

    try:

        analysis = json.loads(
            response.content.strip()
        )

        return {
            **state,

            "category":
            analysis.get(
                "category",
                "unknown"
            ),

            "detected_aspects":
            analysis.get(
                "detected_aspects",
                []
            ),

            "pros":
            analysis.get(
                "pros",
                []
            ),

            "cons":
            analysis.get(
                "cons",
                []
            ),

            "sentiment":
            analysis.get(
                "sentiment",
                "unknown"
            ),

            "review_score":
            float(
                analysis.get(
                    "review_score",
                    0
                )
            ),

            "review_summary":
            analysis.get(
                "review_summary",
                ""
            )
        }

    except Exception as e:

        print(
            "JSON Parse Error:",
            e
        )

        return {
            **state,
            "category": "unknown",
            "detected_aspects": [],
            "pros": [],
            "cons": [],
            "sentiment": "unknown",
            "review_score": 0.0,
            "review_summary": response.content
        }