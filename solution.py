answer = 0
result = []
for num in range(1000, 10000):
    num = str(num)
    s1 = num[0] + num[1] + num[2]
    s2 = num[0] + num[1] + num[3]
    s3 = num[0] + num[2] + num[3]
    s4 = num[1] + num[2] + num[3]
    if s1 == '100':
        answer += 1
        result.append(num)
    if s2 == '100':
        answer += 1
        result.append(num)

    if s3 == '100':
        answer += 1
        result.append(num)

    if s4 == '100':
        answer += 1
        result.append(num)

result = set(result)
print(len(result))