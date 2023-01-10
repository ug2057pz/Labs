'''Part 3: camelCase

Write a program that turns a sentence into camel case. The first word is lowercase, the rest of the words have their initial letter capitalized, and all of the words are joined together. For example, with the input "fOnt proCESSOR and ParsER", your program will output "fontProcessorAndParser". 

Optional extra question: print a warning message if the input will not produce a valid variable name. You don't need to be exhaustive in checking, but test for a few common issues, such as starting with a number, or containing invalid characters such as # or + or ".  Or, would it be easier to check that the name only contains valid characters?

Test your program with different example inputs, and comment your code'''

C = input("Enter a sentence : ") # ask user to input sentence
str_arr = C.split() # split the input sentence into words

result = "" # initialize result as empty string

result += str_arr[0].lower() # Converting first word ( word at index 0 ) of the input sentence into its lowercase
for i in str_arr[1:]: # Now, we'll start iterating from index 1 and onwards
    result += (i.capitalize()) # Capitalizing rest of the words

print("Output : " , result) # printing the required resultant string