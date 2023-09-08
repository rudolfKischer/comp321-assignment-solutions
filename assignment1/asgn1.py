#!/usr/bin/env python3

def q1():
    print("Hello World!")

def q2():
    line = input()
    a, b = line.split()
    a = int(a)
    b = int(b)

    if a < b:
        print(f'{a} {b}')
    else:
        print(f'{b} {a}')
    
    
    


def main():
    q2()

if __name__ == '__main__':
    main()
    

