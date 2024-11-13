# def dog_years(human_years):
    
# #     """
# #     Create a program that counts a dog's age in dog's years. The program should only calculate dog years until 20 human years.
# #     Note: For the first two years, a dog year is equal to 10.5 human years. After that, each dog year equals 4 human years.
# #     2 dog years = 21 human years
# #     1 dog year (for the first 2 years) = 10.5 human years, after that 1 dog year = 4 human years
# #     after 
# #     Expected Output:
# #     ```
# #     Input a dog's age in human years: 15
# #     The dog's age in dog's years is 73
# #     ```
# #     """
    
#     human_years = int(0)
#     if human_years == 1:
#         dogs_age = 10.5
#     elif human_years == 2:
#         dogs_age = 21
#     elif human_years > 2:
#         dogs_age =(human_years - 2) + (human_years * 4)
#         return dogs_age
    
# dog_years(15)
        



def fizzbuzz(num):
#     """
#     Create a program that returns the numbers as a string from 1 to num. 
#     But for multiples of three print “Fizz” instead of the number, 
#     and for multiples of five print “Buzz”. For numbers which are 
#     multiples of both three and five, print “FizzBuzz”.

#     Expected Output:
#     fizzbuzz(15) => "1 2 Fizz 4 Buzz Fizz 7 8 Fizz Buzz 11 Fizz 13 14 FizzBuzz"
#     """

#     #enter your code here

        
        string = ['']
    for i in range (1, num):
        if i % 5 == 0 and i % 3 == 0:
            print('FizzBuzz')
        elif i % 3 == 0:
            print('Fizz')
        elif i % 5 == 0:
            print('Buzz')
        else:
            print(i)
        
fizzbuzz(12)
            
#         # if num % 3 == 0:
#         #     print('Fizz')
#         # elif num % 5 == 0:
#         #     print('Buzz')
#         # elif num % 3 == 0 and num % 5 == 0:
#         #     print('FizzBuzz')
#         # else:
#         #     print(num)

    

# def word_lengths(sentence):
# # #     """
# # #     Create a program that takes a sentence and returns a dictionary with each unique word
# # #     as the key and the length of the word as the value.

# # #     Expected Output:
# # #     ```
# # #     Input a sentence: "Aunty Yankho is amazing"
# # #     Output: {'Aunty': 5, 'Yankho': 6, 'is': 2, 'amazing': 7}
# # #     ```
# # #     """
    
#      sentence = input('')
     
#      special_dictionary = {
#          word : word_length
#      }
     
#      word = sentence.split('')
#      word_length = word.len()
#      for word in sentence:
#          special_dictionary[0].append(word)
    
    

# def cube_sum(number):
# #     """
# #     Create a program that calculates the sum of the cubes of each digit in a number.
    
# #     Expected Output:
# #     ```
# #     cube_sum(123) => 1^3 + 2^3 + 3^3 = 1 + 8 + 27 = 36
# #     ```
# #     """
    
#     for i in number:
#             each_digit = number.split(0)
            
# cube_sum()