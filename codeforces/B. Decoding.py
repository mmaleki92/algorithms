# https://codeforces.com/contest/746/my

# # encoding
# def median_word(s):
#     s_size = len(s)
#     even = s_size % 2 == 0
    
#     if even:
#         return int(len(s) / 2) - 1
#     else:
#         return int(len(s) / 2)
    
# def remove_word(s, i):
#     return s[:i] + s[i + 1:]
    
# s = "logva"
# result = ""
# for i in s:
#     i = median_word(s)
#     result += s[i]
#     s = remove_word(s, i)
#     print(i)
# print(result)
    
n = int(input())
result = input()
s1 = ""
s2 = ""
n = 0
for c in result[::-1]:
    if n % 2 == 0:
        s2 += c
    else:
        s1 += c
    n += 1
print(s1 + s2[::-1])