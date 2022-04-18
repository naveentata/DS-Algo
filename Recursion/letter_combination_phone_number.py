print("Letter Combinations of a Phone Number")
# https://leetcode.com/problems/letter-combinations-of-a-phone-number/
map = {
            '2' : ['a','b','c'],
            '3' : ['d','e','f'],
            '4' : ['g','h','i'],
            '5' : ['j','k','l'],
            '6' : ['m','n','o'],
            '7' : ['p','q','r','s'],
            '8' : ['t','u','v'],
            '9' : ['w','x','y','z']
            
        }
# print(map)


def fun(idx, string, map, temp_arr):
    if idx == len(string):
        print(temp_arr)
        return
    # print(idx, string, temp_arr)

    for j in range(len(map[string[idx]])):
        temp_arr.append(map[string[idx]][j])
        fun(idx+1,string, map, temp_arr )
        temp_arr.pop()
fun(0,['2','7'], map, [])

# ['a', 'p']
# ['a', 'q']
# ['a', 'r']
# ['a', 's']
# ['b', 'p']
# ['b', 'q']
# ['b', 'r']
# ['b', 's']
# ['c', 'p']
# ['c', 'q']
# ['c', 'r']
# ['c', 's']
