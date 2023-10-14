"""
Farmer Jon has recently bought n tree seedlings that he wants to plant 
in his yard. It takes 1 day for Jon to plant a seedling1, and for each 
tree Jon knows exactly in how many days after planting it grows to full 
maturity. Jon would also like to throw a party for his farmer friends, 
but in order to impress them he would like to organize the party only 
after all the trees have grown. More precisely, the party can be organized
 at earliest on the next day after the last tree has grown up.

Help Jon to find out when is the earliest day when the party can take place. 
Jon can choose the order of planting the trees as he likes, so he wants to 
plant the trees in such a way that the party will be as soon as possible.

Input:
The input consists of two lines. The first line contains a single integer N
 (1 <= N <= 100,000) denoting the number of seedlings. Then a line with N
 integers t_i follows (1 <= t_i <= 1000000), where t_i
 denotes the number of days it takes for the ith tree to grow.

Output:
Your program should output exactly one line containing one integer, denoting
the earliest day when the party can be organized. The days are numbered 1,2,3,...
beginning from the current moment.
"""
def main():
    n_seedlings = int(input())
    growth_times = sorted(list(map(int,input().split())),reverse=True)
    result = []
    for i in range(n_seedlings):
        result.append(growth_times[i]+i+1)

    print(max(result)+1)

main()

