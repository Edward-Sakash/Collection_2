# Exercise 2 (Collections - Swap)
"""def swap(lst, i, j):
    lst[i], lst[j] = lst[j], lst[i]
    return lst"""

def swap(lst, i, j):
    temp = lst[i]
    lst[i] = lst[j]
    lst[j] = temp
    return lst


swap_list = [23, 65, 19, 90]
print(">swap(swap_list, 1, 3)")
print(swap(swap_list, 1, 3))  # Output: [23, 90, 19, 65]

print("-------------------------------------------")

# Exercise 3 (Collections - Digit Filter)
# Solution 1: Using a list comprehansion
def digit_filter(lst):
    return [s for s in lst if not any(c.isdigit() for c in s)]

l33t = ['Digital Car33r Institute', 'DCI', 'Digital', 'Career', 'Inst1tut3']
print("> digit_filter(l33t)")
print(digit_filter(l33t))  # Output: ['DCI', 'Digital', 'Career']

print("-------------------------------------------")

# Solution 2: Using a For Loop
def digit_filter(lst):
    result = []
    for s in lst:
        if not any(c.isdigit() for c in s):
            result.append(s)
    return result

l33t = ['Digital Car33r Institute', 'DCI', 'Digital', 'Career', 'Inst1tut3']
print("> digit_filter(l33t)")
print(digit_filter(l33t))  # Output: ['DCI', 'Digital', 'Career']

print("-------------------------------------------")

# Exercise 4( Collections- even numbers):
# Method 1: Using a List Comprehension
def filter_even_numbers(numbers):
    return [n for n in numbers if n % 2 == 0]

numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
print("numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]  ---->",filter_even_numbers(numbers))  # Output: [2, 4, 6, 8, 10]

print("-------------------------------------------")

# Method 2: Using the filter() Function with a Lambda Function
def filter_even_numbers(numbers):
    return list(filter(lambda n: n % 2 == 0, numbers))

numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
print("numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]  ---->",filter_even_numbers(numbers))  # Output: [2, 4, 6, 8, 10]

print("-------------------------------------------")

# Method 3: Using a List Comprehension with the filter() Function
def filter_even_numbers(numbers):
    return [n for n in filter(lambda n: n % 2 == 0, numbers)]

numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
print("numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]  ---->",filter_even_numbers(numbers))  # Output: [2, 4, 6, 8, 10]

print("-------------------------------------------")

# Method 4: Using a List Comprehension with the modulo operator and a ternary operator
def filter_even_numbers(numbers):
    return [n for n in numbers if n % 2 == 0]

numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
print("numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]  ---->",filter_even_numbers(numbers))  # Output: [2, 4, 6, 8, 10]

print("-------------------------------------------")

