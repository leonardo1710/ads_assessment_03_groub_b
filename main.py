def calculate_score(x: int, y: int, z: int):
    sum = x + y + z
    list = [x, y, z]
    if sum <= 21:
        return sum
    elif 11 in list:
        sum -= 10
        if sum > 21:
            return "BUST"
        else:
            return sum
    elif sum - 10 < 21:
        return "BUST"



# Provide your solution here

"""
Even Numbers

"""


def even_positive_numbers(even_list: [int]):
    new_list = []
    for i in even_list:
        if i > 0 and i % 2 == 0:
            new_list.append(i)
    return new_list

# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    print("Test your functions by calling them here. Use different parameter values to test them with different scenarios.")

    result = calculate_score(9,9,9)
    print(result)

    result = calculate_score(2,8,11)
    print(result)

    result = calculate_score(3,8,11)
    print(result)

    result = calculate_score(11,11,11)
    print(result)

    mylist_a = even_positive_numbers([1,2,3])
    print(mylist_a)

    mylist_b = even_positive_numbers([10, 22, 31, 24, 35, 36])
    print(mylist_b)

    mylist_c = even_positive_numbers([-10, -22, 31, 24, 35, 36])
    print(mylist_c)


"""
Even Numbers

Write a function even_positive_numbers that accepts a list as input parameter (method arguments) and returns a new list containing only the even positive (>= 0) numbers from the given list.
Inside "__main__" block below, call your function at least 3 times with different input parameters. Save the returned lists in variables and print them to the console.

Hint: Lists can be passed to function the same way we did with primitive types (see examples below).

Following examples show the return values (not print!) of the function with different lists as input:

    even_numbers([1, 2, 3]) -> [2]
    even_numbers([10, 22, 31, 24, 35, 36]) -> [10, 22, 24, 36]
    even_numbers([-10, -22, 31, 24, 35, 36]) -> [24, 36]
"""

def even_numbers(list: list) -> list:
    evens = []
    for i in list:
        if i%2 == 0 and i >= 0:
            evens.append(i)
    return evens


"""
Blackjack 

Write a function calculate_score that accepts three integers between 1 and 11 (you can assume that only valid integers are passed to it).
The function returns a value based on the following rules:
    - if their sum is less than or equal to 21, return their sum. 
    - if their sum exceeds 21 and there's an eleven, reduce the total sum by 10. 
        - finally, if the sum (even after adjustment) exceeds 21, return 'BUST'
        - else return their sum (after adjustment)

Following examples show the return values (not print!) of the function with different integers as input:

    blackjack(9, 9, 9) → BUST
    blackjack(2, 8, 11) → 21
    blackjack(3, 8, 11) → 12
    blackjack(11, 11, 11) -> BUST
"""

def blackjack(a, b, c):
    sum = a + b + c
    # if sum <= 21:
    #     return sum
    # if a == 11 or b == 11 or c == 11:
    #     sum = sum - 10
    #     if sum <= 21:
    #         return sum
    # return "BUST"

    if sum <= 21:
        return sum
    elif sum <= 31 and 11 in (a, b, c):
        return sum - 10
    else:
        return "BUST"

if __name__ == '__main__':
    # Call your functions here
    print(even_numbers([1, 2, 3, 4, 5, 6]))
    print(even_numbers([10, 22, 31, 24, 35, 36]))
    print(even_numbers([-10, -22, 31, 24, 35, 36]))

    print(blackjack(9, 9, 9))
    print(blackjack(2, 8, 11))
    print(blackjack(11, 11, 11))
