def twoSum(arr, target):
    left= 0
    right = len(arr) - 1
    while left < right:
        current = arr[left] + arr[right]
        if current == target:
            return [left, right]
        elif current < target:
            left+=1
        elif current > target:
            right-=1
        else:
            return "None of Number"

print(twoSum([1, 2, 3, 4, 6], 6))


def reverseArray(arr):
    left = 0
    right = len(arr) - 1
    while left < right:
        arr[left], arr[right] = arr[right], arr[left]
        left+=1
        right-=1
    return arr

result = reverseArray([1, 2, 3, 4, 5])
print(result)

def removeDuplicates(arr):
    slow=0
    for fast in range(1, len(arr)):
        if arr[fast] != arr[slow]:
            slow+=1
            arr[slow] = arr[fast]

    print(arr[:slow+1])

removeDuplicates([1, 1, 2, 3, 3, 4])








    