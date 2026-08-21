def filter_above_20(numbers):
    result = []

    for n in numbers:
        if n > 20:
            result.append(n)
    return sorted (result)

nums = [12, 27, 33, 28, 38, 45]

print(filter_above_20(nums))