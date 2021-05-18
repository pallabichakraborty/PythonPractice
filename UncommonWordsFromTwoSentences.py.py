def findDifferenceInStrings(str1, str2):
    setStr1 = set(str1.split())
    setStr2 = set(str2.split())

    # diffStr1 = setStr1 - setStr2
    # diffStr2 = setStr2 - setStr1
    # list(diffStr1) + list(diffStr2)

    return list(setStr1.symmetric_difference(setStr2))


if __name__ == "__main__":
    print("This program finds the words which are not common in 2 sentences")
    str1 = input("Input first sentence: ")
    str2 = input("Input second sentence: ")

    print("Uncommon words in the 2 sentences are :{}".format(findDifferenceInStrings(str1, str2)))
