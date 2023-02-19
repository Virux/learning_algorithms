# binary search is an algo used to search through a sorted list of items
# supposed you are given an unsorted list, you would need to sort it before
# binary search runs in log time 0(logn)

def binary_search(list, item):
    low = 0
    high = len(list) - 1

    while low <= high:
        mid = (low + high)          # python does down rouding if mid isn't even
        guess = list[mid]

        if guess == item:
            return mid
        if guess > item:
            high = mid - 1
        else:
            low = mid + 1
    return None

my_list = [1, 3, 5, 7, 9]

print(binary_search(my_list, 3)) # => 1
print(binary_search(my_list, -1)) # => None