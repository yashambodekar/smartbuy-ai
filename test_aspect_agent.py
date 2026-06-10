from scraper.amazon_scraper import scrape_product
from utils.sample_loader import load_sample
from agents.aspect_agent import aspect_agent

url = input("Amazon URL: ")
aspect = input("Aspect: ")

product = scrape_product(url)

if len(product["reviews"]) == 0:
    product = load_sample()

state = {
    "reviews": product["reviews"],
    "aspect": aspect
}

result = aspect_agent(
    state
)

print("\n")
print(result["aspect_summary"])