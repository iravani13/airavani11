import lab4d

str1 = 'Hello World!!'
str2 = 'Seneca College'
num1 = 1500
num2 = 1.50

print(lab4d.first_five(str1))
# Will output 'Hello'
print(lab4d.first_five(str2))
# Will output 'Senec'
print(lab4d.last_seven(str1))
# Will output 'World!!'
print(lab4d.last_seven(str2))
# Will output 'College'
print(lab4d.middle_number(num1))
# Will output '50'
print(lab4d.middle_number(num2))
# Will output '.5'
print(lab4d.first_three_last_three(str1, str2))
# Will output 'Helege'
print(lab4d.first_three_last_three(str2, str1))
# Will output 'Send!!'
