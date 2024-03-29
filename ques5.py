# Consider a list (list = []). You can perform the following commands:
# insert i e: Insert integer e at position i 
# print: Print the list
# remove e: Delete the first occurrence of integer e
# append e: Insert integer e at the end of the list
# sort: Sort the list
# pop: Pop the last element from the list
# reverse: Reverse the list.
# Initialize your list and read in the value of n followed by n lines of commands 
# where each command will be of the 7 types listed above.

# Iterate through each command in order and perform the corresponding operation on your list.

n = int(input())
l = []
for i in range(n):
    cmd = input().split()
    if cmd[0] == 'insert' :
        l.insert(int(cmd[1]),int(cmd[2]))
    elif cmd[0] == 'print' :
        print(l)
    elif cmd[0] == 'remove' :
        l.remove(int(cmd[1]))
    elif cmd[0] == 'append' :
        l.append(int(cmd[1]))
    elif cmd[0] == 'sort' :
        l.sort()
    elif cmd[0] == 'pop' :
        l.pop()
    elif cmd[0] == 'reverse' :
        l.reverse()