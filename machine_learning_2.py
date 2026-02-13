"""
BINARY CLASSIFICATION (NO TRAINING)

Goal:
Classify whether a student prefers group work (1)
or prefers solo work (0).

This version does NOT learn.
Weights are chosen manually.
"""


# ------------------------------------------------------------
# 1) ACTIVATION FUNCTION (Step Function)
# ------------------------------------------------------------
def step_activation(z):
    if z >= 0:
        return 1
    else:
        return 0


# ------------------------------------------------------------
# 2) COMPUTE RAW SCORE (z = w·x + b)
# ------------------------------------------------------------
def weighted_sum(features, weights, bias):
    total = 0.0
    for i in range(len(weights)):
        total += features[i] * weights[i]
    total += bias
    return total


# ------------------------------------------------------------
# 3) PREDICT CATEGORY
# ------------------------------------------------------------
def predict(features, weights, bias):
    z = weighted_sum(features, weights, bias)
    return step_activation(z)


# ------------------------------------------------------------
# 4) MAIN PROGRAM
# ------------------------------------------------------------
def main():

    # Features:
    # [group_success_rate, solo_success_rate,
    #  speaks_in_groups_rate, chooses_group_when_free]

    student = [0.80, 0.60, 0.70, 1]

    # MANUALLY CHOSEN WEIGHTS
    # We are encoding our assumptions:
    # - Group success matters a lot (positive)
    # - Solo success pushes toward solo preference (negative)
    # - Speaking in groups matters
    # - Choosing group when free matters a lot

    weights = [2.0, -1.5, 1.2, 2.5]

    # Bias shifts baseline tendency
    bias = -1.0

    prediction = predict(student, weights, bias)

    print("Weights:", weights)
    print("Bias:", bias)
    print("Prediction (1=group, 0=solo):", prediction)


if __name__ == "__main__":
    main()
