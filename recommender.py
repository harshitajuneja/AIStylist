from .database import supabase
from .rules import BODY_RULES, UNDERTONE_RULES


def contains_value(field, value):

    if not field or not value:
        return False

    return value.lower() in [
        str(x).lower()
        for x in field
    ]


def score_product(product, request):

    score = 0
    reasons = []

    body_type = request.body_type
    undertone = request.undertone

    # -----------------------------
    # Body type
    # -----------------------------

    if body_type:

        if contains_value(
            product.get("body_types"),
            body_type
        ):
            score += 30
            reasons.append(
                "selected for your body proportions"
            )

        body_rules = BODY_RULES.get(
            body_type,
            {}
        )

        if product.get("silhouette") in body_rules.get(
            "silhouettes",
            []
        ):
            score += 15

        if product.get("neckline") in body_rules.get(
            "necklines",
            []
        ):
            score += 10

    # -----------------------------
    # Undertone
    # -----------------------------

    if undertone:

        if contains_value(
            product.get("undertones"),
            undertone
        ):
            score += 20
            reasons.append(
                "complements your undertone"
            )

        colors = UNDERTONE_RULES.get(
            undertone,
            {}
        ).get("colors", [])

        product_colors = product.get(
            "color",
            []
        )

        if any(
            c.lower() in colors
            for c in product_colors
        ):
            score += 10

    # -----------------------------
    # Occasion
    # -----------------------------

    if request.occasion:

        if contains_value(
            product.get("occasion"),
            request.occasion
        ):
            score += 20
            reasons.append(
                "suited to your occasion"
            )

    # -----------------------------
    # Destination
    # -----------------------------

    if request.destination:

        if contains_value(
            product.get("destination"),
            request.destination
        ):
            score += 10
            reasons.append(
                "well suited to your destination"
            )

    # -----------------------------
    # Style
    # -----------------------------

    if request.style:

        if contains_value(
            product.get("style"),
            request.style
        ):
            score += 20
            reasons.append(
                "matches your preferred aesthetic"
            )

    # -----------------------------
    # Budget
    # -----------------------------

    if request.budget_max:

        if product.get("price") is not None:

            if product["price"] <= request.budget_max:
                score += 10

    return score, reasons


def recommend_dresses(request):

    result = (
        supabase
        .table("products")
        .select("*")
        .execute()
    )

    products = result.data or []

    recommendations = []

    for product in products:

        score, reasons = score_product(
            product,
            request
        )

        if score > 0:

            recommendations.append({
                "product": product,
                "score": score,
                "reasons": reasons
            })

    recommendations.sort(
        key=lambda x: x["score"],
        reverse=True
    )

    return recommendations[:3]