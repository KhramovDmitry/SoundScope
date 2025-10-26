n = int(input())
nums = set()

for _ in range(n):
    num = input()
    for i in num:
        nums.add(i)

print(len(nums))