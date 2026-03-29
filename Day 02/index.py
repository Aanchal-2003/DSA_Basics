# Fibonnic -> 0, 1, 1, 2, 3, 5, 8.....

def print_fib(n, a = 0, b = 1):
    if n == 0:
        return
    print(a)
    print_fib(n-1, b, a+b)

print_fib(7, 0, 1)



# subsets
def subsets(nums):
    result = []

    def backtrack(index, current):
        if index == len(nums):
            result.append(current[:])
            return
        
        #include the number
        current.append(nums[index])
        backtrack(index+1, current)

        #exclude the number
        current.pop()
        backtrack(index+1, current)

    backtrack(0, [])
    return result

print(subsets([1, 2]))



#step wise backtracking
# def backtrack(0, []):
#     include 1 
#     backtrack(1, [1])
#         include 2
#         backtrack(2, [1, 2])
#             include 3
#             backtrack(3, [1, 2, 3])
#             exclude 3
#             backtrack(3, [1, 2])
#         exclude 2
#         backtrack(2, [1])
#             include 3
#             backtrack(3, [1, 3])
#             exclude 3
#             backtrack(3, [1])
#     exclude 1
#     backtrack(1, [])
#         include 2
#         backtrack(2, [2])
#             include 3
#             backtrack(3, [2, 3])
#             exclude 3
#             backtrack(3, [2])
#         exclude 2
#         backtrack(2, [])
#             include 3
#             backtrack(3, [3])
    

        