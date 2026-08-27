
#reverse string

word="hello harsh"

print(word[::-1])


#reverse string

def reverse(string):
    reversed_string = ""

    for char in string:
        reversed_string=char+reversed_string

    return reversed_string
print(reverse("my name is lakhan"))

#Palindrome
def palindrome(string):
    rev_text=""

    for char in string:
        rev_text=char+rev_text
    print(rev_text)

    if rev_text == string:
        print("Palindrome")
    else:
        print("Not Palindrome")
palindrome("olo")

##Palindrome using 2 pointers
def palindrome_pointer(string):
    left=0
    right=len(string)-1

    while left<right:
        if string[left]!=string[right]:
            return False

        left+=1
        right-=1
    return True
print(palindrome_pointer("level"))

##Count vowels / digit / spaces etc...

def count_characters(string):
    vowels=0
    consonants=0
    digits=0
    spaces=0

    for char in string:
        if char.lower() in "aeiou":
            vowels+=1
        elif char.isdigit():
            digits+=1
        elif char.isalpha():
            consonants+=1
        elif char.isspace():
            spaces+=1

    return vowels,consonants,digits,spaces
print(count_characters("Hello my name is 1762hhdwjnk"))


##Remmove spaces

def remove_spaces(string):
    return string.replace(" ","")
print(remove_spaces("Hello my name is 1762hhdwjnk"))