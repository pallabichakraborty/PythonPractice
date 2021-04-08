/*
n this challenge, the user enters a string and a substring. You have to print the number of times that the substring occurs in the given string. String traversal will take place from left to right, not from right to left.

NOTE: String letters are case-sensitive.

Input Format

The first line of input contains the original string. The next line contains the substring.

Constraints
1<=len(string)<=200

Each character in the string is an ascii character.

Output Format

Output the integer number indicating the total number of occurrences of the substring in the original string.

Sample Input

ABCDCDC
CDC

Sample Output

2

Concept

Some string processing examples, such as these, might be useful.
There are a couple of new concepts:
In Python, the length of a string is found by the function len(s), where  is the string.
To traverse through the length of a string, use a for loop:

*/

def count_substring(string, sub_string):
    stringlength=len(string)
    
    pos=0
    occurences=0
    
    while(pos < stringlength):
        if(string[pos:stringlength].find(sub_string)>=0):
            occurences+=1
            pos+=string[pos:stringlength].find(sub_string)+1
        else:
            pos+=1
    
    return occurences

if __name__ == '__main__':
    string = raw_input().strip()
    sub_string = raw_input().strip()
    
    count = count_substring(string, sub_string)
    print count
