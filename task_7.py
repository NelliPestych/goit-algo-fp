import random
import matplotlib.pyplot as plt

def roll_dice():
    return random.randint(1, 6)

def monte_carlo_simulation(num_rolls):
    sums = [0] * 13  # від 0 до 12
    for _ in range(num_rolls):
        dice_sum = roll_dice() + roll_dice()
        sums[dice_sum] += 1
    return sums

def calculate_probabilities(sums, num_rolls):
    probabilities = [0] * 13
    for i in range(2, 13):
        probabilities[i] = sums[i] / num_rolls * 100
    return probabilities

def plot_probabilities(probabilities):
    plt.bar(range(2, 13), probabilities[2:13], tick_label=range(2, 13))
    plt.xlabel('Сума')
    plt.ylabel('Імовірність (%)')
    plt.title('Імовірності сум при киданні двох кубиків (Метод Монте-Карло)')
    plt.show()

num_rolls = 100000
sums = monte_carlo_simulation(num_rolls)
probabilities = calculate_probabilities(sums, num_rolls)
plot_probabilities(probabilities)
