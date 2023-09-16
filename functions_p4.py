# Write a Python function called max_num()to find the maximum of three numbers.

def max_num(a, b, c):
    return max(a, b, c)

# Write a Python function called mult_list() to multiply all the numbers in a list.

def mult_list(lst):
    result = 1
    for num in lst:
        result *= num
    return result

# Write a Python function called rev_string() to reverse a string.

def rev_string(s):
    return s[::-1]

# Write a Python function called num_within() to check whether a number falls in a given range.
# The function accepts the number, beginning of range, and end of range (inclusive) as arguments.
# Examples: num_within(3,2,4) returns True, num_within(3,1,3) returns True, num_within(10,2,5) returns False.

def num_within(num, start, end):
    return start <= num <= end

# Write a Python function called pascal() that prints out the first n rows of Pascal's triangle.
# The function accepts the number n, the number of rows to print
# Note : Pascal's triangle is an arithmetic and geometric figure first imagined by Blaise Pascal. Each number is the two numbers above it added together.

def pascal(n):
    result = []  # List to store the rows of Pascal's triangle
    for i in range(n):
        if i == 0:
            result.append([1])
        else:
            prev_row = result[-1]
            new_row = [1]
            for j in range(len(prev_row) - 1):
                new_row.append(prev_row[j] + prev_row[j + 1])
            new_row.append(1)
            result.append(new_row)

    # Print the triangle
    for row in result:
        print(' '.join(map(str, row)).center(n*2))

print(max_num(1, 5, 3))  # Output: 5
print(mult_list([1, 2, 3, 4]))  # Output: 24
print(rev_string("hello"))  # Output: "olleh"
print(num_within(3, 2, 4))  # Output: True
print(num_within(10, 2, 5))  # Output: False
pascal(5)
