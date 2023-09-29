def get_max_profit(breaks):
    max_profit = current_max = breaks[0]
    for i in range(1, len(breaks)):
        current_max = max(breaks[i], breaks[i] + current_max)
        max_profit = max(max_profit, current_max)

    return max_profit

def main():
    n_breaks, price = map(int, input().split())
    breaks = [int(b) - price for b in input().split()]
    print(get_max_profit(breaks))

main()