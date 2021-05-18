# Return the number of times a given character occurs in the given string

if __name__ == "__main__":
    string_data = input("Enter a string: ")
    search_string = input("Enter the search string: ")
    print(list(string_data).count(search_string))
