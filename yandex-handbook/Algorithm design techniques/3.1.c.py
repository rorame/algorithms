# (n + k - 1)! / (k! * (n - 1)!)
def fac(x):
    if x <= 1:
        return 1
    return x * fac(x - 1)

n, k = map(int, input().split())
res = fac(n + k - 1) / (fac(k) * (fac(n - 1)))
print(int(res))