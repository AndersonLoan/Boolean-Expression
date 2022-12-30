# By submitting this assignment, I agree to the following:
#   "Aggies do not lie, cheat, or steal, or tolerate those who do."
#   "I have not given or received any unauthorized aid on this assignment."
#
# Name(s):         Saylor Sherrodd
#                   Ricardo Mejia
#                   Anderson Loan
#                   Andrew Spears
#                   Spencer Jones
# Section:         574
# Assignment:   Lab 4-5
# Date:         14 9 2022
#


############ Part A ############  
a = str(input('Enter True or False for a: '))
b = str(input('Enter True or False for b: '))
c = str(input('Enter True or False for c: '))

def boolConverter(f):
    if f == 't' or f == 'true' or f == 'True' or f == 'T':
        return True
    elif f == 'f' or f == 'false' or f == 'False' or f == 'F':
        return False
        
a = boolConverter(a)
b = boolConverter(b)
c = boolConverter(c)

############ Part B ############  
print('a and b and c:',a and b and c)
print('a or b or c:',a or b or c)

############ Part C ############  
print('XOR:', (a or b) and not(a and b))
print('Odd number:',(a and b and c)or(a and not b and not c)or(b and not a and not c) or (c and not a and not b))

############ Part D ############  
print('Complex 1:',(not (a and not b) or (not c and b)) and (not b) or (not a and b and not c) or (a and not b) )
print('Complex 2:',(not ((b or not c) and (not a or not c))) or (not (c or not (b and c))) or (a and not c) and (not a or (a and b and c) or (a and ((b and not c) or (not b)))) )
print('Simple 1:',not(b and c) and not(a and b))
print('Simple 2:',not(not a and not c) and not(not a and b and c))
