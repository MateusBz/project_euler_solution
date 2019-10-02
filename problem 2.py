if __name__ == '__main__':
    fibonacci_numbers = [0, 1]
    for i in range(2, 5000):
        fibonacci_numbers.append(fibonacci_numbers[i - 1] + fibonacci_numbers[i - 2])

    my_list = [x for x in fibonacci_numbers if x % 2 == 0 and x < 4000000]

    print(sum(my_list))