numbers = [1,2,3,4,5,6]
squares = [num * num for num in numbers]
print(numbers)
print(squares)
even_numbers = [num for num in numbers if num % 2 == 0]
print(even_numbers)
