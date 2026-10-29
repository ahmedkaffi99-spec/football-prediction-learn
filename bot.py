import math


def poisson_probability(goals_expected, goals):
    return (
        math.exp(-goals_expected)
        * goals_expected ** goals
        / math.factorial(goals)
    )


def predict_match(home_xg, away_xg):
    results = []

    for home_goals in range(8):
        for away_goals in range(8):
            probability = (
                poisson_probability(home_xg, home_goals)
                * poisson_probability(away_xg, away_goals)
            )

            results.append(
                (home_goals, away_goals, probability)
            )

    home_win = sum(
        p for h, a, p in results if h > a
    )
    draw = sum(
        p for h, a, p in results if h == a
    )
    away_win = sum(
        p for h, a, p in results if h < a
    )

    top_scores = sorted(
        results, key=lambda item: item[2], reverse=True
    )[:5]

    print("\n=== POISSON MATCH PREDICTION ===")
    print(f"Home xG: {home_xg}")
    print(f"Away xG: {away_xg}")

    print("\n1X2 Probabilities:")
    print(f"Home Win: {home_win * 100:.2f}%")
    print(f"Draw:     {draw * 100:.2f}%")
    print(f"Away Win: {away_win * 100:.2f}%")

    print("\nTop 5 Exact Scores:")
    for home, away, prob in top_scores:
        print(f"{home}-{away}: {prob * 100:.2f}%")


if __name__ == "__main__":
    predict_match(1.6, 1.1)
