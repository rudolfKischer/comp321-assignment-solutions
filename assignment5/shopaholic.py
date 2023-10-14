
def main():
    n_items = int(input())
    items = sorted(list(map(int,input().split())),reverse=True)
    #print(f"Sorted items: {items}")
    discount = 0
    for i in range(0,n_items-1,3):
        print(items[i])
        if i+2 >= n_items:
            break
        discount+=items[i+2]
    print(discount)

main()