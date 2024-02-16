numbers = [1, 2, 3, 4, 5, 6]
# Write a lambda function and use filter
even_numbers = list(filter(lambda x: x if x % 2 == 0 else None, numbers))
print(even_numbers)
