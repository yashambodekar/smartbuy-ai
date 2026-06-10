from scraper.amazon_scraper import scrape_product
from agents.review_agent import review_agent
from utils.sample_loader import load_sample

url = input("Enter Amazon URL: ")

product = scrape_product(url)

if len(product["reviews"]) == 0:

    print(
        "\nUsing Sample Data..."
    )

    product = load_sample()

print("\nTOTAL REVIEWS EXTRACTED:")
print(len(product["reviews"]))

print("\nFIRST 3 REVIEWS:\n")

for i, review in enumerate(product["reviews"][:3]):
    print(f"Review {i+1}:")
    print(review[:300])
    print("=" * 50)

state = {
    "reviews": product["reviews"]
}

result = review_agent(state)

print("\nAI ANALYSIS:\n")
print(result["review_summary"])