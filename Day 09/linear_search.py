def linear_search(arr,target):
    for i in range(0,len(arr)):
        if arr[i]==target:
            return i
    return -1
print(linear_search([1,2,3,4,5,6,7],6))



