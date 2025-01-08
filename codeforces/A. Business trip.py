# https://codeforces.com/contest/149/problem/A
k = int(input())
months = list(map(int, input().split()))
    
if k == 0:
    print(0)  # No growth required, so zero months are needed
else:
    months.sort(reverse=True)
    count = 0
    n = 0
    
    for i in months:
        count += 1
        n += i
    
        if n >= k:
            break
    
    if n < k:
        print(-1)
    else:
        print(count)