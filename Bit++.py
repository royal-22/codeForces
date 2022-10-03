time = int(input())
res = 0
while time > 0: 
    operation = input()
    if "++" in operation: #operation == "++X" or operation == "X++"
        res += 1
    else:
        res -= 1
    time -= 1
print(res)
