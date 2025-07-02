#1
space = ' '
thirty = 'Thirty'
day = 'days'
of = 'of'
python = 'python'
text = thirty + space + day + space + of + space + python
print (text)
#2 
coding = 'Coding'
For = 'for'
All = 'all'
text = coding + space + For + space + All
print (text)
#3
company = 'Coding For All'
#4
print (company)
#5
print (len(company))
#6
print (f"ACA ESTOY CAMIANDO LA VARIABLE EMPRESA LAS CONVIERTE EN MAYUSCULAS:{company.upper()} \n")
#7
print (company.lower())
#8
print (company.capitalize())
print (company.title())
print (company.swapcase())
#9
cut = company[company.find(' ') + 1:]
print(cut)
#10
print (company.find('Coding'))
#11
print (company.replace('Coding', 'Python'))
#12
print (company.replace('Python', 'Everyone'))
#13
print (company.split(' '))
#14
companys = "Facebook, Google, Microsoft, Apple, IBM, Oracle, Amazon"
print (companys.split(' '))
#15
print(company[0])          # Caracter en el índice 0: 'C'
#16
print(len(company) - 1)    # Último índice: 13
#17
print(company[10])         # Caracter en el índice 10: '
#18
frase_1 = 'Python For Everyone'
acronimo1 = ''.join([word[0] for word in frase_1.split()])
print(acronimo1)  # acronimo de 'Python For Everyone'
#19
frase_2 = 'Coding For All'
acronimo2 = ''.join([word[0] for word in frase_2.split()])
print(acronimo2)  # acronimo de 'Coding For All'

#20
print(frase_2.index('C'))

#21
print(frase_2.index('F'))

#23
oracion = 'You cannot end a sentence with because because because is a conjunction'
print(oracion.find('because'))

#24
print(oracion.rindex('because'))

#25
primera = oracion.find('because')
ultima = oracion.rindex('because') + len('because')
print (oracion[primera:ultima])

#26
print(frase_2.startswith('Coding'))

#26
print(oracion.find('because'))

#28
print(frase_2.startswith('Coding'))

#29
print(frase_2.endswith('coding'))

#30
empresa_con_espacios = '   Coding For All      '
print(empresa_con_espacios.strip())

#31
print('30DaysOfPython'.isidentifier())  # False
print('thirty_days_of_python'.isidentifier())  # True

#32
librerias = ['Django', 'Flask', 'Bottle', 'Pyramid', 'Falcon']
resultado = ' # '.join(librerias)
print(resultado)

#33
print("I am enjoying this challenge.\nI just wonder what is next.")

#34
print("Name\tAge\tCountry\tCity")
print("Asabeneh\t250\tFinland\tHelsinki")

#35
radio = 10
area = 3.14 * radio ** 2
print("The area of a circle with radius {} is {} meters square.".format(radio, int(area)))

#36
a = 8
b = 6
print("{} + {} = {}".format(a, b, a + b))
print("{} - {} = {}".format(a, b, a - b))
print("{} * {} = {}".format(a, b, a * b))
print("{} / {} = {:.2f}".format(a, b, a / b))
print("{} % {} = {}".format(a, b, a % b))
print("{} // {} = {}".format(a, b, a // b))
print("{} ** {} = {}".format(a, b, a ** b))