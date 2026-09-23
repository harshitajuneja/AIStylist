from .database import supabase
from .rules import UNDERTONE_RULES


def match_accessories(
    product,
    request
):

    result = (
        supabase
        .table("accessories")
        .select("*")
        .execute()
    )

    accessories = result.data or []

    matches = []

    for accessory in accessories:

        score = 0
        reasons = []

        # Undertone

        if request.undertone:

            if request.undertone.lower() in [
                x.lower()
                for x in (
                    accessory.get(
                        "undertones"
                    ) or []
                )
            ]:

                score += 20

                reasons.append(
                    "complements your undertone"
                )

        # Occasion

        if request.occasion:

            if request.occasion.lower() in [
                x.lower()
                for x in (
                    accessory.get(
                        "occasion"
                    ) or []
                )
            ]:

                score += 20

        # Style

        product_styles = (
            product.get("style") or []
        )

        accessory_styles = (
            accessory.get("style") or []
        )

        if set(
            x.lower()
            for x in product_styles
        ) & set(
            x.lower()
            for x in accessory_styles
        ):

            score += 20

            reasons.append(
                "matches the dress aesthetic"
            )

        # Neckline

        compatible_necklines = (
            accessory.get(
                "compatible_necklines"
            ) or []
        )

        if product.get("neckline") in (
            compatible_necklines
        ):

            score += 20

            reasons.append(
                "works with the neckline"
            )

        matches.append({

            "accessory": accessory,

            "score": score,

            "reasons": reasons

        })

    matches.sort(
        key=lambda x: x["score"],
        reverse=True
    )

    return matches[:3]