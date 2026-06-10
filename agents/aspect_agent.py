import json

from utils.llm import llm


def aspect_agent(state):

    reviews = state.get(
        "reviews",
        []
    )

    aspect = state.get(
        "aspect",
        ""
    )

    if not reviews:

        return {
            **state,
            "aspect_score": 0.0,
            "aspect_pros": [],
            "aspect_cons": [],
            "aspect_summary":
            "No reviews found."
        }

    combined_reviews = "\n".join(
        reviews[:10]
    )

    prompt = f"""
    Analyze ONLY information related to:

    {aspect}

    Ignore unrelated information.

    Return ONLY valid JSON.

    Format:

    {{
        "aspect_score": 0,
        "aspect_pros": [],
        "aspect_cons": [],
        "aspect_summary": ""
    }}

    Rules:

    - aspect_score between 0 and 10
    - output only JSON

    Reviews:

    {combined_reviews}
    """

    response = llm.invoke(
        prompt
    )

    print("\nRAW ASPECT RESPONSE:\n")
    print(response.content)

    try:

        analysis = json.loads(
            response.content.strip()
        )

        return {
            **state,

            "aspect_score":
            float(
                analysis.get(
                    "aspect_score",
                    0
                )
            ),

            "aspect_pros":
            analysis.get(
                "aspect_pros",
                []
            ),

            "aspect_cons":
            analysis.get(
                "aspect_cons",
                []
            ),

            "aspect_summary":
            analysis.get(
                "aspect_summary",
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
            "aspect_score": 0.0,
            "aspect_pros": [],
            "aspect_cons": [],
            "aspect_summary":
            response.content
        }