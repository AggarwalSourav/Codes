def count(number):
    binary=bin(number)
    bit_count=binary.count('1')
    print(bit_count)
user=int(input())
result=count(user)
