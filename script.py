def get_amount(arr, amount):
    # Initialize dictionary with value amount + 1
    solves = {}
    for i in range(amount + 1):
        if i == 0:
            solves[i] = 0
            continue
        solves[i] = amount + 1

    # Go through all solves
    for i in range(1, len(solves)):
        # Try all denominations
        for denomination in arr:            
            if denomination <= i:
                next_subproblem = i - denomination

                # If the solve of the next subproblem + 1 is less than the current solve, set the current solve to that number
                if solves[next_subproblem] + 1 < solves[i]:
                    solves[i] = solves[next_subproblem] + 1
    
    return solves[amount]


if __name__ == "__main__":
    arr = list(map(int, input('coin denominations\n').rsplit()))
    amount = int(input('amount\n'))

    print('minimum amount of coins', str(get_amount(arr, amount)))
    