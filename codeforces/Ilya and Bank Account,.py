# https://codeforces.com/contest/313/problem/A
account = int(input())
    
if account >= 0:
    print(account)
elif account < 0:
    if int(str(account)[:-1]) > int(str(account)[:-2] + str(account)[-1]):
        print(int(str(account)[:-1]))
    else:
        print(int(str(account)[:-2] + str(account)[-1]))