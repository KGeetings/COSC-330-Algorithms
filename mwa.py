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


def plot_bar_chart(weights, iteration, prev_weights):
    actions = ["Rock", "Paper", "Scissors"]

    colors = []
    for current, previous in zip(weights, prev_weights):
        if current > previous:
            colors.append("lightgreen")  # if it goes up
        elif current < previous:
            colors.append("lightcoral")  # if it goes down
        else:
            colors.append("darkgray")  # if it stays the same

    plt.bar(actions, weights, color=colors)
    plt.ylim(0, 1)
    for i, value in enumerate(weights):
        plt.text(i, value + 0.01, f"{value:.2f}", ha="center", va="bottom")
    plt.title("Multiplicative Weights Algorithm - Iteration " + str(iteration))
    plt.xlabel("Actions")
    plt.ylabel("Weights")
    plt.savefig(f"./mwa-bar-charts/bar_chart_{iteration}.png")
    plt.close()


def plot_line_chart(weights_history, num_iterations):
    plt.plot(weights_history)
    plt.title("Multiplicative Weights Algorithm - " + str(num_iterations) + " Iterations")
    plt.xlabel("Iterations")
    plt.ylabel("Weights")
    plt.legend(["Rock", "Paper", "Scissors"])
    plt.savefig("./mwa-line-chart " + str(num_iterations) + " iterations.png")
    plt.show()


def main():
    num_iterations = 100
    learning_rate = 0.1
    weights = [1 / 3, 1 / 3, 1 / 3]
    actions = ["rock", "paper", "scissors"]
    weights_history = [weights.copy()]

    # Record weights for line chart
    prev_weights = weights.copy()
    plot_bar_chart(weights, 0, prev_weights)

    for i in range(num_iterations):
        computer_action = "paper" if i % 3 < 2 else "scissors"
        # Have player choose action based on what is weighted more heavily
        player_action = actions[weights.index(max(weights))]
        # player_action = random.choices(["rock", "paper", "scissors"], weights)[0]
        print(
            f"Iteration {i} - Weights (rock, paper, scissors) = {list(map(lambda x: round(x, 2), weights))}, player = {player_action}, computer = {computer_action}"
        )
        outcome = play_round(player_action, computer_action)
        weights = multiplicative_weights_algorithm(
            weights, actions.index(player_action), outcome, learning_rate
        )

        # Record weights for line chart
        weights_history.append(weights.copy())

        # Plot and save bar chart every iteration
        prev_weights = weights_history[i]
        plot_bar_chart(weights, i + 1, prev_weights)

        if i == num_iterations - 1:
            print(
                f"Iteration {i + 1} - Weights (rock, paper, scissors) = {list(map(lambda x: round(x, 2), weights))}"
            )

    # Plot line chart after all iterations
    plot_line_chart(weights_history, num_iterations)


if __name__ == "__main__":
    main()
