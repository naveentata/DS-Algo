print("Print all subsequences whoes sum is k")
def fun(idx, sumi, temp_arr,  k, arr, n):
    if idx == n:
        if sumi == k:
            print(temp_arr)
        return
    # Take idx
    temp_arr.append(arr[idx])
    sumi+=arr[idx]
    fun(idx+1, sumi, temp_arr, k, arr, n)
    # Not take idx
    temp_arr.pop()
    sumi-=arr[idx]
    fun(idx+1, sumi, temp_arr, k, arr, n)
    

a = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

fun(0, 0, [], 10, a, len(a))

# Print all subsequences whoes sum is k
# [1, 2, 3, 4]
# [1, 2, 7]
# [1, 3, 6]
# [1, 4, 5]
# [1, 9]
# [2, 3, 5]
# [2, 8]
# [3, 7]
# [4, 6]
# [10]
