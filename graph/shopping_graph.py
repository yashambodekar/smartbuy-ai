from langgraph.graph import StateGraph
from models.state import ShoppingState

from agents.product_agent import product_agent
from agents.review_agent import review_agent
from agents.verdict_agent import verdict_agent


def build_graph():

    graph = StateGraph(ShoppingState)

    graph.add_node(
        "product_agent",
        product_agent
    )

    graph.add_node(
        "review_agent",
        review_agent
    )

    graph.add_node(
        "verdict_agent",
        verdict_agent
    )

    graph.add_edge(
        "product_agent",
        "review_agent"
    )

    graph.add_edge(
        "review_agent",
        "verdict_agent"
    )

    graph.set_entry_point(
        "product_agent"
    )

    graph.set_finish_point(
        "verdict_agent"
    )

    return graph.compile()