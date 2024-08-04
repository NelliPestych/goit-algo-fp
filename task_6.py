items = {
    "pizza": {"cost": 50, "calories": 300},
    "hamburger": {"cost": 40, "calories": 250},
    "hot-dog": {"cost": 30, "calories": 200},
    "pepsi": {"cost": 10, "calories": 100},
    "cola": {"cost": 15, "calories": 220},
    "potato": {"cost": 25, "calories": 350}
}

def greedy_algorithm(items, budget):
    sorted_items = sorted(items.items(), key=lambda x: x[1]['calories'] / x[1]['cost'], reverse=True)
    total_calories = 0
    selected_items = []
    for item, info in sorted_items:
        if info['cost'] <= budget:
            budget -= info['cost']
            total_calories += info['calories']
            selected_items.append(item)
    return selected_items, total_calories

def dynamic_programming(items, budget):
    n = len(items)
    dp = [[0 for _ in range(budget + 1)] for _ in range(n + 1)]
    item_names = list(items.keys())
    for i in range(1, n + 1):
        for w in range(1, budget + 1):
            if items[item_names[i - 1]]['cost'] <= w:
                dp[i][w] = max(dp[i - 1][w],
                               dp[i - 1][w - items[item_names[i - 1]]['cost']] + items[item_names[i - 1]]['calories'])
            else:
                dp[i][w] = dp[i - 1][w]

    total_calories = dp[n][budget]
    selected_items = []
    w = budget
    for i in range(n, 0, -1):
        if dp[i][w] != dp[i - 1][w]:
            selected_items.append(item_names[i - 1])
            w -= items[item_names[i - 1]]['cost']
    selected_items.reverse()
    return selected_items, total_calories

budget = 100

# Використання жадібного алгоритму
selected_items_greedy, total_calories_greedy = greedy_algorithm(items, budget)
print("Жадібний алгоритм вибрав:", selected_items_greedy, "загальна калорійність:", total_calories_greedy)

# Використання динамічного програмування
selected_items_dp, total_calories_dp = dynamic_programming(items, budget)
print("Динамічне програмування вибрало:", selected_items_dp, "загальна калорійність:", total_calories_dp)
