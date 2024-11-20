def knapsack():
    n = int(input("Enter the number of Objects: "))
    m = int(input("Enter the total weight of Knapsack: "))

    profits = []
    weights = []
    fracs = [0] * n

    for i in range(n):
        profit, weight = map(float, input(f"Enter the profit and weight of object {i + 1}: ").split())
        profits.append(profit)
        weights.append(weight)

    # Sorting based on profit-to-weight ratio
    ratio = sorted(range(n), key=lambda i: profits[i] / weights[i], reverse=True)

    rem = m
    for i in ratio:
        if weights[i] <= rem:
            rem -= weights[i]
            fracs[i] = 1
        else:
            fracs[i] = rem / weights[i]
            break

    total_profit = sum(fracs[i] * profits[i] for i in range(n))

    print("Fractions of each object taken:", fracs)
    print("Total profit is:", total_profit)

# Call the knapsack function to execute the code
knapsack()