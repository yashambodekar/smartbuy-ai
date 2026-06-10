from typing import TypedDict


class ShoppingState(TypedDict):

    # Input
    product_url: str

    # Product Information
    product_data: dict

    # Raw Reviews
    reviews: list

    # Review Intelligence Agent Output
    category: str

    detected_aspects: list

    pros: list

    cons: list

    sentiment: str

    review_score: float

    review_summary: str

    # Aspect Analysis Agent Input
    aspect: str

    # Aspect Analysis Agent Output
    aspect_score: float

    aspect_pros: list

    aspect_cons: list

    aspect_summary: str

    # Verdict Generator Output
    final_score: float

    recommendation: str

    verdict: str