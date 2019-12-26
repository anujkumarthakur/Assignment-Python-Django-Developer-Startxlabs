'''2.       Write a function that satisfies the following rules:
            Return true if the string in the first element of the list contains all of the letters of the 
            string in the second element of the list.
    examples
            ["hello", "Hello"]
            should return true because all of the letters in the second string are present in the first, ignoring case.
            ["hello", "hey"]
            should return false because the string "hello" does not contain a "y".
            ["Alien", "line"]
            should return true because all of the letters in "line" are present in "Alien".
'''

def stringComapre(str1, str2):
    for i in range(0, len(str2)):
        if(str1.index(str2[i]) < 0):
            return false
    return True
if __name__ == "__main__":
    str1 = str(input("Enter first string : "))
    str2 = str(input("Enter second string : "))
    x = stringComapre(str1.lower(), str2.lower())
    print(x)



















