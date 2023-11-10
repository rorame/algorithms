n, k = map(int, input().split())
# n! / (k! * (n - k)!)

def fac(x):
    if x <= 1:
        return 1
    return x * fac(x-1)

res = fac(n) / (fac(k) * fac(n - k))
print(int(res))

# RE in last task