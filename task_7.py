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

# Аналітичні ймовірності для порівняння
analytical_probabilities = {
    2: 2.78,
    3: 5.56,
    4: 8.33,
    5: 11.11,
    6: 13.89,
    7: 16.67,
    8: 13.89,
    9: 11.11,
    10: 8.33,
    11: 5.56,
    12: 2.78
}

# Висновки
with open("readme.md", "w") as f:
    f.write("# Висновки щодо правильності розрахунків\n\n")
    f.write("Аналітичні ймовірності:\n")
    for sum_val, prob in analytical_probabilities.items():
        f.write(f"Сума {sum_val}: {prob}%\n")

    f.write("\nЙмовірності, отримані за допомогою методу Монте-Карло:\n")
    for i in range(2, 13):
        f.write(f"Сума {i}: {probabilities[i]:.2f}%\n")

    f.write("\nПорівняння:\n")
    for i in range(2, 13):
        f.write(f"Сума {i}: аналітична = {analytical_probabilities[i]}%, Монте-Карло = {probabilities[i]:.2f}%\n")

    f.write("\nВисновки:\n")
    f.write("Результати, отримані за допомогою методу Монте-Карло, добре збігаються з аналітичними результатами. Відхилення знаходяться в межах допустимих похибок, що свідчить про правильність обчислень.")
