m = list(map(int, input().split()))
m.sort()

# Minimum sum of 4 numbers: drop largest
min_sum = sum(m[:4])
# Maximum sum of 4 numbers: drop smallest
max_sum = sum(m[1:])

print(min_sum, max_sum)