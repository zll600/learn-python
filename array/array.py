def array_test():
    arr = [3, 2, 4, 5]

    arr.pop()

    arr.append(6)

    print(arr)
    print("Index of 4: ", arr.index(4))

    arr.remove(4)
    print("Removed 4: ", arr)

    arr.reverse()
    print("reversed: ", arr)
    print("sorted return: ", sorted(arr))

    arr.sort()
    print("sorted in place: ", arr)

def main():
    array_test()

if __name__ == '__main__':
    main()
