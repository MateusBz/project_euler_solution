if __name__ == '__main__':
    new_list = [i for i in range(1, 1000)]
    my_list = [x for x in new_list if x % 5 == 0 or x % 3 == 0]
    print(sum(my_list))