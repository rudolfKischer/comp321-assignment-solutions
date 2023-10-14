def get_input():
    n = input()
    items = [int(i) for i in input().split()]
    return items

def get_max_discount(items):
    items.sort()
    items.reverse()
    discount_length = 3
    items = items[:(len(items) - (len(items) % discount_length))]
    items_grouped = [items[i:i+discount_length] for i in range(0, len(items), discount_length)]
    discount = sum([group[-1] for group in items_grouped])
    return discount

print(get_max_discount(get_input()))
    
    
