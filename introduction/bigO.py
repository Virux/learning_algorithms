# a notation that tells how fast or slow algorithms are
# helps in determining how fast or slow other people's algos are before we use
# knowing how long an algo run is not enough because it can lead to wrong assumptions
# one has to know how long the run time increases with an increase of the list size
# this is where big O notation comes in handy
# big O lets us compare the number of operations btn algo letting us determine how
# fast they grow

# WORSE-CASE RUN TIME
# big O notation uses worse-case runtime
# if gives you an assurance that a linear runtime can not be faster that 0(n)



# COMMON BIG O RUNTIMES
'''
    1: 0(log n) - logarithm time - binary searching
    2: 0(n) - linear time - simple searching
    3: 0(n * log n) - fast sorting algo - quicksort
    4: 0(n!) - very slow algo - the travelling salesman
    5: 0(n2) - a slow sorting algo - selection sort

'''

# binary search is faster than simpple search
# binary search gets faster than simple search as the number of items in the list increases
# algorithm speed is not measured in seconds
# algorithm speed is measured by the growth of operations of the algo
# algo speed in written in big O 