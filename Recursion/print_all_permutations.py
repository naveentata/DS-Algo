def fun(arr, ds, map):
    if len(ds) == len(arr):
        print(ds)
        return
    for i in range(len(arr)):
        if not map[i]:
            map[i] = True
            ds.append(arr[i])
            fun(arr, ds, map)
            ds.pop()
            map[i] = False

a = ['a','b','c']
map =[ False for i in range(len(a))]
fun(a, [], map)


# ['a', 'b', 'c']
# ['a', 'c', 'b']
# ['b', 'a', 'c']
# ['b', 'c', 'a']
# ['c', 'a', 'b']
# ['c', 'b', 'a']


# Second approach without extra space of map. Using swap method

def fun(idx, arr):
    if idx == len(arr):
        print(arr)
        return
    for i in range(idx,len(arr)):
        arr[i], arr[idx] = arr[idx], arr[i]
        fun(idx+1, arr)
        arr[i], arr[idx] = arr[idx], arr[i]

a = ['a','b','c']
# map =[ False for i in range(len(a))]
fun(0, a)


