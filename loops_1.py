def sum_between(start: int, end: int) -> int:
    """
    Return sum of integers between start and end (both included).
    """
    sum = 0
    while start <= end:
        sum += start
        start += 1
    return sum

def sum_of_multiples(n: int, end: int) -> int:
    """
    Return sum of numbers which are multiples of n between
    0 and end (included).
    """
    num = n
    sum = 0
    while num <= end:
        sum += num
        num += n
    return sum

def cross_sum(numbers: str):
    sum = 0
    for _,char in enumerate(numbers):
        sum += int(char)
    return sum