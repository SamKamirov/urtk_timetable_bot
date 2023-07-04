import random as rd

symbols = '1234567890AaBbCcDdEeFfGgHhIiJjKkLlMmNnOoPpQqRrSsTtUuVvWwXxYyZz!@#$%^&*()_-+={[}]|:;'

length = int(input('Введите длинну пароля: '))

password = ''

for i in range(length):
    password += symbols[rd.randint(1,len(symbols))]
print(password)
