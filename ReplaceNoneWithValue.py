def replaceNoneWithPreviousValues(n, arr):
    numberOfNone = arr.count(None)

    if numberOfNone == 0:
        return arr
    elif numberOfNone == n:
        return arr
    else:
        for i in range(n):
            if arr[i] is None and i != 0:
                arr[i] = arr[i - 1]

        return arr


if __name__ == "__main__":
    n = input("How many numbers do you want to enter: ")
    print("Type the numbers:")

    arr = []
    for _ in range(int(n)):
        strdata = input("Enter  a number: ")
        if strdata == 'None':
            arr.append(None)
        else:
            arr.append(int(strdata))

    print("You have entered {}".format(arr))

    print (" After removing  None with previous value: {}".format(replaceNoneWithPreviousValues(int(n),arr)))
