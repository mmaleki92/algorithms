# https://codeforces.com/contest/460/problem/A

socks_num, m = list(map(int, input().split()))
days_count = 0
    
while True:   
    
    days_count += 1
    socks_num -= 1
    
    if days_count % m == 0 and days_count != 0:
        socks_num += 1
    if socks_num == 0:
        break
    
print(days_count)