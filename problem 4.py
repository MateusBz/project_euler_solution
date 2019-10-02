if __name__ == '__main__':

    for i in range(100, 1000):
        for y in range(100, 1000):
            result = i * y
            if str(result) == str(result)[::-1]:
                print(result)




