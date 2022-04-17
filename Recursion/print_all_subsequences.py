print("Print all subsequences")
def fun(idx, temp_arr, arr, n):
    if idx == n:
        print(temp_arr)
        return
    fun(idx+1, temp_arr, arr, n)
    temp_arr.append(arr[idx])
    fun(idx+1, temp_arr, arr, n)
    temp_arr.pop()
    

a = ['n', 'a', 'v', 'e', 'e', 'n']

fun(0, [], a, len(a))
