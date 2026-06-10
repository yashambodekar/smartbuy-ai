from typing import TypedDict


class ShoppingState(TypedDict):

    product_url: str

    product_data: dict

    reviews: list

    category: str

    detected_aspects: list

    pros: list

    cons: list

    sentiment: str

    review_score: float

    review_summary: str

    aspect: str

    aspect_score: float

    aspect_pros: list

    aspect_cons: list

    aspect_summary: str

    final_score: float

    recommendation: str

    verdict: str

    data_source: str

    payment_offers: list

    best_payment_option: dict

    best_price: float

    total_savings: float

    recommendations: list