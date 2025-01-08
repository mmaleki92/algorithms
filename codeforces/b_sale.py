# https://codeforces.com/contest/34/problem/B

tv_amount, bob_capacity = list(map(int, input().split()))
prices = list(map(int, input().split()))
    
prices.sort()
earn = []
for i in range(1, bob_capacity + 1):
    earn.append(sum(prices[:i]) * -1)
    
earn.sort(reverse=True)
if earn[0] >= 0: 
    print(earn[0])
else:
    print(0)