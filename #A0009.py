N,K = map(float, input().split())
print(float(K % N))

#M106B
a = int(input())
b = int(input())

if a > b:
    print(">")
elif a < b:
    print("<")
else:
    print("=")