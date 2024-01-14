# n =int(input())
n = 7
# li = [int(x) for x in input().split()]
li = [2, 4, 7, 9, 10, 13]
key = int(input())

isFound = False
for i in range(len(li)):
    if li[i] == key:
        isFound = True
        print(i)
        break
if isFound is False:
    print(-1)