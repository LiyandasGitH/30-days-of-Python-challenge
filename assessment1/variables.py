# Variables in Python 


first_name = 'Liyanda'
last_name = 'Tonisi'
country = 'South Africa'
city = 'Cape Town'
age = 22 
is_married = False
skills = ['HTML', 'CSS', 'Python']
personal_info = {
    'firstname': 'Liyanda',
    'lastname': 'Tonisi',
    'country': 'South Africa',
    'city': 'Cape Town'
}

# Printing values stored in the variables 


print('First name:', first_name)
print('First name length:', len(first_name))
print('Last name:', last_name)
print('Last name length:', len(last_name))
print('Country:', country)
print('City:', city)
print('Age:', age)
print('Married:', is_married)
print('Skills:', skills)
print('Person information:', personal_info)


# Declaring multiple variables in one line

first_name, last_name, country, age, is_married = 'Liyanda', 'Tonisi', 'South Africa', 22, False

print(first_name, last_name, country, age, is_married)
print('First name:', first_name)
print('Last name:', last_name)
print('Country:', country)
print('Age:', age)
print('Married', is_married)