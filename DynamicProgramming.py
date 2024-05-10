def climbStairs(n):
    if n == 1:
        return 1

    one, two = 1, 1
    for i in range(n - 1):
        result = one + two
        one, two = two, result

    return result


def fibonacci(n, memo={}):
    if n in memo:
        return memo[n]
    if n <= 2:
        return 1

    memo[n] = fibonacci(n - 1, memo) + fibonacci(n - 2, memo)
    return memo[n]






def fibonacci(n, memo={}):
    if n in memo:
        return memo[n]
    if n <= 2:
        return 1
    memo[n] = fibonacci(n - 1) + fibonacci(n - 2)
    return memo[n]


def gridTraveller(m, n, memo={}):
    key = m, n
    if key in memo:
        return memo[(m, n)]
    if n == 0 or m == 0:
        return 0
    if m == 1 and n == 1:
        return 1
    memo[key] = gridTraveller(m - 1, n) + gridTraveller(m, n - 1)
    return memo[key]


def targetSum(n, target, memo={}):
    if target in memo:
        return memo[target]
    if target == 0:
        return True
    if target < 0:
        return False
    for i in n:
        remaider = target - i
        if targetSum(n, remaider):
            memo[target] = True
            return True

    memo[target] = False
    return False



def ClimbingStairsOwn(n):
    if n == 1:
        return 1
    if n < 1:
        return 0







def howSum(n, target, memo={}):
    if target in memo:
        return memo[target]
    if target == 0:
        return []
    if target < 0:
        return None
    for i in n:
        remainder = target - i
        remainderResult = howSum(n, remainder)

        if remainderResult is not None:
            memo[target] = remainderResult + [i]
            return memo[target]

    return None




#
# def bestSum(n, target, memo={}):



print(climbStairs(5))
# print(fibonacci(5))
#
# print(fibonacci(60))

# print(gridTraveller(10, 10))
#
# print(targetSum([2, 3, 4, 5, 5, 6, 7, 8], 10))
# print(targetSum([2, 3, 4, 5, 5, 6, 7, 8], 300))


# print(howSum([2, 3, 4, 5, 5, 6, 7, 8, 10], 300))
# print(howSum([2, 3, 4, 5, 5, 6, 7, 8], 10))

