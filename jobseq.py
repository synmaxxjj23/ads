def job_sequencing():
    n = int(input("Enter the number of jobs: "))
    d = [0] * (n + 1)
    profits = [0] * (n + 1)

    for i in range(n):
        profit, deadline = map(int, input(f"Enter the profits and deadlines of Job {i + 1}: ").split())
        profits[i + 1] = profit
        d[i + 1] = deadline

    # Sorting jobs based on profits in descending order
    for i in range(1, n):
        for j in range(1, n - i + 1):
            if profits[j] < profits[j + 1]:
                # Swap profits
                profits[j], profits[j + 1] = profits[j + 1], profits[j]
                # Swap deadlines accordingly
                d[j], d[j + 1] = d[j + 1], d[j]

    j = [0] * (n + 1)
    j[0] = 0
    d[0] = 0
    j[1] = 1
    k = 1

    for i in range(2, n + 1):
        r = k
        while (d[j[r]] > d[i]) and (d[j[r]] != r):
            r -= 1
        if (d[j[r]] <= d[i]) and (d[i] > r):
            for x in range(k, r, -1):
                j[x + 1] = j[x]
            j[r + 1] = i
            k += 1

    profit = 0
    print("Final Job Sequence:")
    for i in range(1, n + 1):
        print(j[i], end=" ")
        profit += profits[j[i]]
    print("\nTotal Profit:", profit)

# Call the job_sequencing function to execute the code
job_sequencing()