from scraper.amazon_scraper import scrape_product


def product_agent(state):

    product = scrape_product(
        state["product_url"]
    )

    if product.get("source") == "cache":
       print("\nWARNING: Using Cached Product Data\n")

    return {
    **state,
    "product_data": {
        "title": product["title"],
        "price": product["price"],
        "rating": product["rating"],
        "review_count": product["review_count"],
        "source": product.get("source", "unknown")
    },
    "data_source": product.get("source", "unknown"),
    "reviews": product["reviews"]
}