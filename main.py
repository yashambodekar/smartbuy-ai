# main.py

from fastapi import FastAPI
from graph.shopping_graph import build_graph

app = FastAPI()
graph = build_graph()

graph.invoke(
    {
        "product_url": "dummy"
    }
)


@app.get("/")
def home():
    return {
        "message": "SmartBuy AI Running"
    }