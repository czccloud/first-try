def is_perfect_number(n):
   
    if n <= 1:
        return False
    divisor_sum = 0
    for i in range(1, n):
        if n % i == 0:
            divisor_sum += i
    return divisor_sum == n

perfect_numbers = [num for num in range(1, 1001) if is_perfect_number(num)]
print("1000以内的完数有：", perfect_numbers)