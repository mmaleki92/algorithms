#https://codeforces.com/contest/977/problem/B

n = int(input())
s = input()
    
d = {}
max_value = 0
max_two_gram = None
    
for i in range(n - 1):
    two_gram = s[i: i+2]
    
    if two_gram in d:
        d[two_gram] += 1
    else:
        d[two_gram] = 1
    
    if d[two_gram] > max_value:
        max_value = d[two_gram]
        max_two_gram = two_gram
    
print(max_two_gram)