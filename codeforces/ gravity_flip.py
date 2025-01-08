# https://codeforces.com/problemset/problem/405/A
    
col_num = int(input())
s = list(map(int, input().split()))
    
rows = []
max_rows = max(s)
for i in range(max_rows):
    row = []
    for n, j in enumerate(s):
        if j >= max_rows - i:
            row.append(1)
        else:
            row.append(0)
    
    rows.append(row)
# print(rows)
def fun(row):
    row_size = len(row)
    boxes = row.count(1)
    empty = row_size - boxes
    result = [0] * empty + [1] * boxes
    return result
    
gravity_rows = []
for row in rows:
    gravity_rows.append(fun(row))
    
# print(gravity_rows)
    
for i in range(col_num):
    n = 0
    for g_row in gravity_rows:
        n += g_row[i]
    print(n, end=" ")