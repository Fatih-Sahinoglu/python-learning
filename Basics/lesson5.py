text="it's a lesson about strings methods."

print(text.capitalize()) #Capitalize the first letter of the string
print(text.title())      #Capitalize the first letter of each word in the string
# if there is word like f7f7 it will F7F7 

print(text.casefold())   #Convert the string to lowercase for caseless matching but its slower than lower()

print(text.swapcase())   #Swap the case of each character in the string

print(text.isupper())    #Check if all characters in the string are uppercase (TRUE)
print(text.islower())    #Check if all characters in the string are lowercase (TRUE)

print(text.center(40,"*"))  #Center the string within a specified width (40) and fill with "*"

print(text.count("s"))  #Count how many times "s" appears in the string

print(text.find("lesson"))  #Find the index of first "lesson" in the string (7)
#If not found, returns -1

print(text.isalnum())  #Check if all characters in the string are alphanumeric (FALSE, because of spaces and punctuation)
print(text.isalpha())  #Check if all characters in the string are alphabetic (FALSE, because of spaces and punctuation)
print(text.isdigit())  #Check if all characters in the string are digits (FALSE)    

print(text.strip())  #Remove space at first and last
