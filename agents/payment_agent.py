def payment_agent(state):

    product_data = state.get(
        "product_data",
        {}
    )

    offers = state.get(
        "payment_offers",
        []
    )

    price_text = product_data.get(
        "price",
        "0"
    )

    try:

        product_price = float(
            price_text.replace(",", "")
        )

    except:

        product_price = 0

    if not offers:

        return {
            **state,
            "best_payment_option": None,
            "best_price": product_price,
            "total_savings": 0
        }

    best_offer = None
    best_price = product_price

    for offer in offers:

        discounted_price = (
            product_price
            - offer["discount"]
        )

        if discounted_price < best_price:

            best_price = discounted_price

            best_offer = offer

    return {
        **state,

        "best_payment_option":
        best_offer,

        "best_price":
        best_price,

        "total_savings":
        product_price - best_price
    }