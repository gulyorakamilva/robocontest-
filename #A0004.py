# list
# nums = [1, 2, 3, 4, 5, 5, 4, 3, 2]
# # set - {1, 2, 3, 4, 5}
# print(set(nums))

N = int(input())
nums = list(map(int, input().split()))
no_duplicate_nums = set(nums)
no_duplicate_nums = sum(no_duplicate_nums) * 2 - sum(nums)
print(no_duplicate_nums)