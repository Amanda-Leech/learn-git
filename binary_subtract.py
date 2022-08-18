def binary_subtract(num1, num2):
    max_length = max(len(num1), len(num2))
    greater = num1 if num1 > num2 else num2
    smaller = num1 if num1 < num2 else num2
    greater, smaller = [
        list(greater.zfill(max_length))[::-1],
        list(smaller.zfill(max_length))[::-1],
    ]
    result = []

    for i in range(len(smaller)):
        result.append(int(greater[i])-int(smaller[i]))
    for i, num in enumerate(result):
        if num < 0:
            result[i] += 2
            result[i+1] -= 1
        result[i] = str(result[i])

    return" ".join(result[::-1])

print(binary_subtract("11110", "1010"))