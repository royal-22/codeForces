def perfectMatrix():
    for i in range(1, 6):
            nums = [int(x) for x in input().split()]
            if 1 in nums:
                return i, nums.index(1) + 1
ind = perfectMatrix()
print(abs(ind[0]-3) + abs(ind[1]-3))
