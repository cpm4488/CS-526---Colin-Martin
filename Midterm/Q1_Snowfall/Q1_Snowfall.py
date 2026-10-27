import sys 
#If the sum of 3 consecutive days > 1/2 total, the midpoint will be one of those days.

#binary search for day that crosses halfway point
def halfway_day(A, total, low, high):
    if low == high:
        return low
    mid = (low + high) // 2
    if 2 * A[mid] > total:
        return halfway_day(A, total, low, mid)    
    return halfway_day(A, total, mid + 1, high)

#finds halfway day and checks the surrounding days for where the sum > half     
def three_over_half(A, n):
    #if total days <3, there are no 3 consecutive days
    if n < 3:
        return False
    total = A[n]
    m = halfway_day(A, total, 1, n)
    #searches the days around the midpoint and checks sum against total
    for i in range(max(1,m-2), min(m, n-2) +1):
        if 2 * (A[i + 2] - A[i - 1]) > total:
            return True
    return False 

def solve(source):
    lines = [line.split() for line in source if line.strip()]
    n = int(lines[0][0])
    A = [0] + [int(x) for x in lines[1]]
    answer = "YES" if three_over_half(A, n) else "NO"
    print(" ".join(lines[1])+" solution: "+ answer )
    
if __name__ == "__main__":
    solve(sys.stdin)
 
