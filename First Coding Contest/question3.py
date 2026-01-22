amount = int(input())
a = list(map(int, input().split()))

minimum = min(a, key=lambda x:(abs(x), -x))
print(abs(minimum))