# write a function to create and print a list where values are square of numbers between 1 and n(both included) in python
def print_square(n):
    squares_list = [i**2 for i in range(1, n+1)]
    print(squares_list)
n = 5
print_square(n)
