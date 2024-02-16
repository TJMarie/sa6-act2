numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9]
# Combine filter and map in a single expression
result = list(map(lambda x: x ** 2, filter(lambda x: x if x % 3 == 0 else None, numbers)))
print(result)
