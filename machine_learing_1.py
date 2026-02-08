# -----------------------------
# PREDICTION MODEL (REGRESSION)
# -----------------------------

def predict_absences(features, weights, bias):
    """
    features: list of numbers (x1, x2, x3)
    weights:  list of numbers (w1, w2, w3)
    bias:     single number (b)
    """
    total = 0
    for i in range(len(features)):
        total += features[i] * weights[i]
    total += bias
    return total

# FEATURES
student = [7.5, 2, 8]  # sleep, sports, last month absences

# WEIGHTS (chosen by us, not learned yet)
weights = [-0.4, -0.2, 0.8]
bias = 1.0

prediction = predict_absences(student, weights, bias)
print("Predicted absences next month:", prediction)

# == end part 1 == 


def calculate_error(actual, predicted):
    return actual - predicted

def update_weights(features, weights, bias, error, learning_rate):
    """
    Adjusts the model's weights and bias based on how wrong the prediction was.

    features:       the input values for ONE training example
                    (e.g. [sleep_hours, sports_hours, previous_absences])

    weights:        how important each feature currently is
                    (one weight per feature)

    bias:           the model's baseline prediction before features are considered

    error:          actual_output - predicted_output
                    positive error → prediction was too low
                    negative error → prediction was too high

    learning_rate:  how big a step the model is allowed to take when updating itself
                    (small = cautious learning, large = aggressive learning)
    """

    # Loop through each feature/weight pair
    for i in range(len(weights)):

        # If a feature value is large, it influenced the prediction more,
        # so its weight should change more.
        #
        # If a feature value is zero, it contributed nothing,
        # so its weight will not change at all.
        #
        # learning_rate controls how fast learning happens
        # error tells us which direction to change
        weights[i] += learning_rate * error * features[i]

    # Update the bias separately.
    # This shifts the entire prediction up or down for all future examples.
    bias += learning_rate * error

    # Return the updated model parameters
    return weights, bias


training_data = [
    ([8, 4, 0], 0),  # slept 8h, sports 4h, 0 absences → actually 0 absences next month
    ([6, 1, 3], 4),  # slept 6h, sports 1h, 3 absences → actually 4 absences
    ([7, 3, 1], 1),  # slept 7h, sports 3h, 1 absence → actually 1 absence
    ([5, 0, 4], 6)   # slept 5h, sports 0h, 4 absences → actually 6 absences
]

# The model currently believes nothing matters.
weights = [0.0, 0.0, 0.0]
bias = 0.0

# Learning_rate is how cautious the model is when changing its beliefs.
# Too large → chaos
# Too small → very slow learning
learning_rate = 0.01


# The model learns by changing its weights in the direction that reduces future error.

# We train for multiple passes over the data.
# Each full pass is called an "epoch".
for epoch in range(10):

    print(f"\n--- Epoch {epoch + 1} ---")

    # We show the model each training example one at a time
    for features, actual in training_data:

        # STEP 1: Model makes a prediction
        predicted = predict_absences(features, weights, bias)

        # STEP 2: Measure how wrong the prediction was
        error = calculate_error(actual, predicted)

        # STEP 3: Show students what's happening
        print("Features:", features)
        print("Actual absences:", actual)
        print("Predicted absences:", round(predicted, 2))
        print("Error:", round(error, 2))
        print("Weights before:", [round(w, 3) for w in weights])
        print("Bias before:", round(bias, 3))

        # STEP 4: Adjust weights and bias to reduce error
        weights, bias = update_weights(
            features,
            weights,
            bias,
            error,
            learning_rate
        )

        # STEP 5: Show updated model
        print("Weights after:", [round(w, 3) for w in weights])
        print("Bias after:", round(bias, 3))
        print("-" * 40)
