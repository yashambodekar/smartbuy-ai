from scraper.amazon_scraper import scrape_product


def product_agent(state):

    product = scrape_product(
        state["product_url"]
    )

    return {
        **state,
        "product_data": {
            "title": product["title"],
            "price": product["price"],
            "rating": product["rating"],
            "review_count": product["review_count"]
        },
        "reviews": product["reviews"]
    }