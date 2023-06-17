import re

# string = input('Enter a string : ')
string = 'he was at patil farmhouse'

# ----------------------------------------------------- findall() -----------------------------------------------------
# '\d+' return the list of numbers in the string
# Example : My roll number is 21
# Output : ['21']
find = re.findall('\d+', string)
print(find, '\n')

# ----------------------------------------------------- search() -----------------------------------------------------
search = re.search('at', string)
print("Start and end of the searched strigng : ", search.start(), search.end())
print("Searched string : ", search.group(0), '\n')

# ----------------------------------------------------- split() -----------------------------------------------------
splits = re.split('at', string)
print('Split string is : ', splits, '\n')

# ----------------------------------------------------- sub() -----------------------------------------------------
sub = re.sub('at', '5757', string)
print('Replaced string using pattern is : ', sub, '\n')

# ----------------------------------------------------- Validating phone number -----------------------------------------------------
pattern = re.compile(r'^\d{4}-\d{6}$')
# 4 - operator code
# 6 - subscriber code
phone_number = '9172-263791'
if pattern.match(phone_number):
    print("Valid phone number")
else:
    print("Not a valid phone number")

# ----------------------------------------------------- Validating email -----------------------------------------------------
pattern = re.compile(r'^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$')
email = 'prathampatil@gmail.com'
if pattern.match(email):
    print("Valid email address")
else:
    print("Not a valid email address")

# ----------------------------------------------------- Validating social security number -----------------------------------------------------
pattern = re.compile(r'^\d{3}-\d{2}-\d{4}$')
ssn = '123-24-2564'
if pattern.match(ssn):
    print("Valid ssn")
else:
    print("Not a valid ssn")