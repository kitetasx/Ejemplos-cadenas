#String
#Para concatenar o combinar dos cadenas se utiliza el operador +
text1 = "fundamentos con"
text2 = "Python"
result = text1 + text2
print(result)
name = "kite"
lastName = "Hurtado"
fullName = name + "" + lastName
print(fullName)

#Format String
#Mostrar el precio de un producto con dos decimales
price = 97
text3 = f"The price is {price: .2f} dollars"
print(text3)



#Math operation
text4 = f"La multiplicacion es {20 * 59} "
print(text4)

#String capitalize()
text5 = "python es un lenguaje de alto nivel de programacion"
result1 = text5.capitalize()
print(result1)

#String casefold()
title = "Cien Años de Soledad"
titleConvert = title.casefold()
print(titleConvert)

#String Center
fruit = "banana"
textCenter = fruit.center(20, "-")
print(textCenter)

#String count
#longitud de la cadena
title1 = "I love apples, apple are my favorite fruit"
result2 = title1.count("apple")
print(result2)

#String endswith
text6 = "Curso, fundamentos con Python."
result3 = text6.endswith(".")
print(result3)

#String expandtabs
letter = "F\tu\tP"
letterSpaces = letter.expandtabs(2)
print(letterSpaces)

#String  find
text7 = "Hola, bienvenidos a Colombia."
result4 = text7.find("bienvenidos")
print(result4)

#Funcion tile
text8 = "welcome to my world"
result5 = text8.title()
print(result5)

#Funcion isalnum
alphanumeric = "python312"
result6 = alphanumeric.isalnum()
print(result6)

#Funcion isalpha

letters = "Space X"
result7 = letters.isalpha()
print(result7)
