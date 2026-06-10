# scraper/amazon_scraper.py

import requests
from bs4 import BeautifulSoup
import re

from utils.cache import (
    save_cache,
    load_cache
)

def clean_review(review_text):

    review_text = re.sub(
        r"Verified Purchase",
        "",
        review_text
    )

    review_text = re.sub(
        r"Read more.*",
        "",
        review_text
    )

    review_text = re.sub(
        r"Helpful.*",
        "",
        review_text
    )

    review_text = re.sub(
        r"\s+",
        " ",
        review_text
    )

    return review_text.strip()


def scrape_product(url):

    headers = {
        "User-Agent": (
            "Mozilla/5.0 (Windows NT 10.0; Win64; x64) "
            "AppleWebKit/537.36 (KHTML, like Gecko) "
            "Chrome/137.0.0.0 Safari/537.36"
        ),
        "Accept-Language": "en-US,en;q=0.9"
    }

    

    try:
       
       if not url.startswith(("http://", "https://")):
           url = "https://" + url

       response = requests.get(
        url,
        headers=headers,
        timeout=20
    )
    except Exception as e:

        print(
        "Request Failed:",
        e
        )

        cached = load_cache()

        if cached:
             cached["source"] = "cache"
             return cached

        return {
        "title": "N/A",
        "price": "N/A",
        "rating": "N/A",
        "review_count": "N/A",
        "reviews": []
        }

    print("Status:", response.status_code)
    print("Final URL:", response.url)

    # print("\nTITLE FOUND:")
    # print(title)

    print("\nPAGE LENGTH:")
    print(len(response.text))

    with open("amazon_debug.html", "w", encoding="utf-8") as f:
      f.write(response.text)

    soup = BeautifulSoup(
        response.text,
        "html.parser"
    )

    # -----------------------
    # Product Details
    # -----------------------

    title = soup.find(id="productTitle")
    title = title.get_text(strip=True) if title else "N/A"

    price = soup.find(class_="a-price-whole")
    price = price.get_text(strip=True) if price else "N/A"

    rating = soup.find(
        "span",
        class_="a-icon-alt"
    )
    rating = rating.get_text(strip=True) if rating else "N/A"

    review_count = soup.find(
        id="acrCustomerReviewText"
    )
    review_count = (
        review_count.get_text(strip=True)
        if review_count
        else "N/A"
    )

    # -----------------------
    # Reviews
    # -----------------------

    review_tags = soup.select(
        '[data-hook="review"]'
    )

    print("\nReview Tags Found:", len(review_tags))

    reviews = []

    for review in review_tags:

        review_text = review.get_text(
            separator=" ",
            strip=True
        )

        review_text = clean_review(review_text)

        if len(review_text) > 50:
            reviews.append(review_text)

    print("Reviews Extracted:", len(reviews))

    # Debug
    for i, review in enumerate(reviews[:3]):

        print(f"\nReview {i+1}")

        print(review[:300])

        print("=" * 50)

    product_data = {
      "title": title,
      "price": price,
      "rating": rating,
      "review_count": review_count,
      "reviews": reviews,
      "source": "live"
   }

    if title != "N/A":

       save_cache(
        product_data
       )

       print(
        "Cache Updated"
       )

       return product_data
    
    print(
    "Scraping failed. Loading cache..."
    )

    cached = load_cache()

    if cached:
       cached["source"] = "cache"
       return cached
    
    return product_data