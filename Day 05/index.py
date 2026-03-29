def maxSum(arr,k):
    window_sum=sum(arr[:k])
    max_sum=window_sum

    for i in range(k,len(arr)):
        window_sum=window_sum-arr[i-k]+arr[i]
        max_sum=max(max_sum, window_sum)
    return max_sum

result = maxSum([1,5,1,3,2,1],3)
print(result)

def average_Window(arr,k):
    result=[]
    window_Sum=sum(arr[:k])
    result.append(window_Sum/k)

    for i in range(k,len(arr)):
        window_Sum=window_Sum-arr[i-k]+arr[i]
        result.append(window_Sum/k)
    return result

print(average_Window([1,3,2,2,-2,3],4))
