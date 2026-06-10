from typing import TypedDict


class ShoppingState(TypedDict):

    product_url: str

    product_data: dict

    reviews: list

    review_summary: str

    aspect: str

    aspect_summary: str

    verdict: str