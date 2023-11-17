import random
import matplotlib.pyplot as plt


def multiplicative_weights_algorithm(weights, action, outcome, learning_rate):
    # Update weights based on the outcome of the action
    for i in range(len(weights)):
        if i == action:
            weights[i] *= (
                (1 + learning_rate) if outcome == "win" else (1 - learning_rate)
            )
        else:
            weights[i] *= (
                (1 - learning_rate) if outcome == "win" else (1 + learning_rate)
            )

    # Normalize weights to sum to 1
    total_weight = sum(weights)
    weights = [w / total_weight for w in weights]

    return weights


def play_round(player_action, computer_action):
    if player_action == computer_action:
        return "draw"
    elif (
        (player_action == "rock" and computer_action == "scissors")
        or (player_action == "paper" and computer_action == "rock")
        or (player_action == "scissors" and computer_action == "paper")
    ):
        return "win"
    else:
        return "lose"


def plot_bar_chart(weights):
    actions = ["Rock", "Paper", "Scissors"]
    plt.bar(actions, weights, color=["red", "green", "blue"])
    plt.title("Multiplicative Weights Algorithm - Bar Chart")
    plt.xlabel("Actions")
    plt.ylabel("Weights")
    plt.show()


def plot_line_chart(weights_history):
    plt.plot(weights_history)
    plt.title("Multiplicative Weights Algorithm - Line Chart")
    plt.xlabel("Iterations")
    plt.ylabel("Weights")
    plt.legend(["Rock", "Paper", "Scissors"])
    plt.show()


def main():
    num_iterations = 75
    learning_rate = 0.1
    weights = [1 / 3, 1 / 3, 1 / 3]
    actions = ["rock", "paper", "scissors"]
    weights_history = [weights.copy()]

    for i in range(num_iterations):
        computer_action = "paper" if i % 3 < 2 else "scissors"
        player_action = random.choices(["rock", "paper", "scissors"], weights)[0]
        outcome = play_round(player_action, computer_action)
        weights = multiplicative_weights_algorithm(
            weights, actions.index(player_action), outcome, learning_rate
        )

        # Plot bar chart every iteration
        # plot_bar_chart(weights)

        # Record weights for line chart
        weights_history.append(weights.copy())

    # Plot line chart after all iterations
    plot_line_chart(weights_history)


if __name__ == "__main__":
    main()
