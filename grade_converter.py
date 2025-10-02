# FILE NAME - grade_converter.py

# NAME: Dennis Ruggio
# DATE: 10/2/25
# BRIEF DESCRIPTION: grade_converter.py lab



# 1. Make sure you fill out the comments above
# 2. Write your code in the proper spot
# 3. Be sure to answer the Reflection Questions and Attestation below
# 4. The Sample Output has been included in this code for your convenience



########## ENTER YER CODE BELOW THIS LINE ##########

print('===== Grade Converter =====')

percent = int(input('Enter a numerical grade (1-100): '))

if percent > 100:
    print('A+')
elif percent >= 90:
    print('A')
elif percent >= 80:
    print('B')
elif percent >= 70:
    print('C')
elif percent >= 65:
    print('D')
else:
    print('F')

########### END YER CODE ABOVE THIS LINE ###########

    



########################################
#          SAMPLE OUTPUT
########################################

'''
===== Grade Converter =====
Enter a numerical grade (1-100): 101
A+
'''


'''
===== Grade Converter =====
Enter a numerical grade (1-100): -78
F
'''


'''
===== Grade Converter =====
Enter a numerical grade (1-100): 64
F
'''


'''
===== Grade Converter =====
Enter a numerical grade (1-100): 65
D
'''


'''
===== Grade Converter =====
Enter a numerical grade (1-100): 66
D
'''

########################################
#          REFLECTION QUESTIONS
########################################

'''

1. What is something you would tell a future student to be careful about when
   doing this lab?

This lab already had the code in place but it actually leads to my struggle before I opened this:
I ended up making it way more complicated than it needed to be using elif to generate grade based on the user input number versus the grade ranges for the actual grade.
My more complicated code for reference:

#
print('===== Grade Converter =====')
grade = int(input('Enter a numerical grade (1-100): '))
   
   
if grade < 65:
   print('F')
elif 65 <= grade < 70:
   print('D')
elif 70 <= grade < 80:
   print('C')
elif 80 <= grade < 90:
   print('B')
elif 90 <= grade < 100:
   print('A')
else:
   print('A+')
#





'''
