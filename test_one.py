from agents.product_agent import product_agent
from agents.review_agent import review_agent
from agents.aspect_agent import aspect_agent
from agents.verdict_agent import verdict_agent
from agents.recommendation_agent import recommendation_agent

state = {
    "product_url": input("URL: "),
    "aspect": "freshness"
}

state = product_agent(state)

state = review_agent(state)

state = aspect_agent(state)

state = verdict_agent(state)

state = recommendation_agent(state)

print(state)