from scraper.amazon_scraper import scrape_product
from utils.sample_loader import load_sample

from agents.aspect_discovery_agent import (
    aspect_discovery_agent
)

url = input(
    "Amazon URL: "
)

product = scrape_product(
    url
)

if len(product["reviews"]) == 0:
    product = load_sample()

state = {
    "reviews": product["reviews"]
}

result = aspect_discovery_agent(
    state
)

print("\nDetected Aspects:\n")

for aspect in result[
    "detected_aspects"
]:
    print("-", aspect)