print("Print all subsequences whoes sum is k. Digit can be used any number of times")
def fun(idx, temp_arr,  k, arr, n):
    if idx == n :
        if k == 0:
            print(temp_arr)
        return
    # Take idx
    if arr[idx]<=k:
        temp_arr.append(arr[idx])
        fun(idx, temp_arr, k-arr[idx], arr, n)
        # Not take idx
        temp_arr.pop()
    fun(idx+1, temp_arr, k, arr, n)
    

a = [3, 2, 4, 6]

fun(0, [],14, a, len(a))

# Print all subsequences whoes sum is k. Digit can be used any number of times
# [3, 3, 3, 3, 2]
# [3, 3, 2, 2, 2, 2]
# [3, 3, 2, 2, 4]
# [3, 3, 2, 6]
# [3, 3, 4, 4]
# [2, 2, 2, 2, 2, 2, 2]
# [2, 2, 2, 2, 2, 4]
# [2, 2, 2, 2, 6]
# [2, 2, 2, 4, 4]
# [2, 2, 4, 6]
# [2, 4, 4, 4]
# [2, 6, 6]
# [4, 4, 6]
