def ways(n):
    if n < 0:
        return 0
    if n == 0:
        return 1
    return ways(n - 1) + ways(n - 2) + ways(n - 3)
numa = 3
numb = 5
numc = 10

print("ways(",numa,") = ",ways(numa),sep="")
print("ways(",numb,") = ",ways(numb),sep="")
print("ways(",numc,") = ",ways(numc),sep="")