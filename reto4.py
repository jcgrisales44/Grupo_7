tupla = (1 , 2, "hola",3.3, "hello",5,4.3 )
lista_ent = []
lista_float = []
lista_str = []
for x in tupla:
  if type(x) == int:
    lista_ent.append(x)
for j in tupla:    
  if type(j) == float:
      lista_float.append(j)
for o in tupla:
  if type(o) == str:
      lista_str.append(o)


print("Datos de tipo int")  
print(" ")
print(lista_ent)
print("Datos de tipo float") 
print(" ")
print(lista_float)
print("Datos de tipo string") 
print(" ")
print(lista_str)
