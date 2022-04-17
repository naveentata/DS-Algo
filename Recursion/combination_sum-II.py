# print("combination sumII")
def fun(idx, temp_arr,  k, arr):

    if k == 0:
        print(temp_arr)
        return
    # Take idx
    for i in range(idx, len(arr), 1):
        if arr[i] > k:
            break
        if i > idx and arr[i] == arr[i-1]:
            continue
        
        temp_arr.append(arr[i])
        fun(i+1, temp_arr, k-arr[i], arr)
        temp_arr.pop()

a = [10,1,2,7,6,1,5]
a.sort(reverse=False)
fun(0, [], 8, a)


# [1, 1, 6]
# [1, 2, 5]
# [1, 7]
# [2, 6]
