# Task Given an integer, n, and n space-separated integers as input,
#  create a tuple,t , of those integers. 
# Then compute and print the result of hash(t).

n = int(input())
integer_list = map(int, input().split())
my_tuple = tuple(integer_list)
print(hash(my_tuple))