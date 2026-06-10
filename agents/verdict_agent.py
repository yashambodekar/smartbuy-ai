def verdict_agent(state):

    review_score = state.get(
        "review_score",
        0
    )

    aspect_score = state.get(
        "aspect_score",
        0
    )

    final_score = round(
        (
            review_score * 0.7
            +
            aspect_score * 0.3
        ),
        1
    )

    if final_score >= 8:

        recommendation = "BUY"

    elif final_score >= 6:

        recommendation = "CONSIDER"

    else:

        recommendation = "AVOID"

    verdict = f"""
Final Score: {final_score}/10

Recommendation: {recommendation}

Sentiment:
{state.get("sentiment","unknown")}

Review Summary:
{state.get("review_summary","")}

Aspect Summary:
{state.get("aspect_summary","")}
"""

    return {
        **state,
        "final_score": final_score,
        "recommendation": recommendation,
        "verdict": verdict
    }