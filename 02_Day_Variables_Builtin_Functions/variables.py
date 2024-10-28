
# Variables in Python

first_name = 'Kishore'
last_name = 'Mada'
country = 'India'
city = 'Kakinada'
age = 22
is_married = False
skills = ['HTML', 'CSS', 'C', 'ML', 'Python']
person_info = {
    'firstname':'Kishore', 
    'lastname':'Mada', 
    'country':'India',
    'city':'AMP'
    }

# Printing the values stored in the variables

print('First name:', first_name)
print('First name length:', len(first_name))
print('Last name: ', last_name)
print('Last name length: ', len(last_name))
print('Country: ', country)
print('City: ', city)
print('Age: ', age)
print('Married: ', is_married)
print('Skills: ', skills)
print('Person information: ', person_info)

# Declaring multiple variables in one line

first_name, last_name, country, age, is_married = 'Kishore', 'Mada', 'India', 22, False

print(first_name, last_name, country, age, is_married)
print('First name:', first_name)
print('Last name: ', last_name)
print('Country: ', country)
print('Age: ', age)
print('Married: ', is_married)
