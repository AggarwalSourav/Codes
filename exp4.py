'''Write a program to display all keys and values of the dictionary
input:
3
ramu 3
ajay 5
satya 50
output:
ramu ajay Satya
3 5 50
'''
def display(num):
    data = {}
    for i in range(num):
        key, value = input().split()
        data[key] = value
    print(' '.join(data.keys()))
    print(' '.join(data.values()))
n = int(input())
display(n)
