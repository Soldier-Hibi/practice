a = input().lower()
result = ""
for i in range(len(a)):
    if i % 2 == 0:
        result += a[i].upper()
    else:
        result += a[i].lower()
print(result)