# Write a function that given an array of N positive integers it will print k largest elements from the array. The output function should print elements in descending order with a comma to seperate them if there is more than one.
# The number of elements in the array will always be larger than or equal to k.

# Example:
# output(1, [5, 8, 9, 12]) should print: 12
# output(3, [12, 54, 3, 4, 6, 7]) should print: 54, 12, 7
#

def output(k, N):
    N.sort(reverse=True)
    lst = map(lambda x : str(x), N[:k])
    return ', '.join(lst)

if __name__ == "__main__":
    print(output(1, [5, 8, 9, 12]))
    print(output(3, [12, 54, 3, 4, 6, 7]))
