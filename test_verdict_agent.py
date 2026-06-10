from scraper.amazon_scraper import scrape_product
from utils.sample_loader import load_sample

from agents.review_agent import review_agent
from agents.aspect_agent import aspect_agent
from agents.verdict_agent import verdict_agent


url = input("Amazon URL: ")
aspect = input("Aspect: ")

product = scrape_product(url)

if len(product["reviews"]) == 0:
    product = load_sample()

state = {
    "product_data": {
        "title": product["title"],
        "price": product["price"],
        "rating": product["rating"],
        "review_count": product["review_count"]
    },
    "reviews": product["reviews"],
    "aspect": aspect
}

state = review_agent(state)

state = aspect_agent(state)

state = verdict_agent(state)

print("\n")
print("=" * 60)
print("FINAL VERDICT")
print("=" * 60)

print(state["verdict"])