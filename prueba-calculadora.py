#*********************************************
# Creacion de nuevo repositorio en GitHub
# Creacion de nuevo proyecto calculadora basica
# creacion  de menu de opciones
# permitir al usuario que intruduzca 2 numeros para realizar la operacion matematica.
# Mostrar resultado en pantalla
# Release : 10/11/2022
# Developer : Natalia Rincon
#************************************************

#Creamos menu para que el usuario elija la operacion que desea realizar

print("Seleccione la operacion que desea realizar: ")
print("1- sumar")
print("2- restar")
print("3- multiplicar")
print("4- dividir")

#crea la variable con input para que guarde la operacion que el usuario seleccione.
#verifica que sea un de las opciones validas.
#si la opcion es valida pide al usuario que ingrese dos numeros para realizar la operacion
#crea la logica de la calculadora
#arroja resultado en pantalla

while True:
        selecciona = input("ingresa el numero de la operacion que deseas realizar ( 1suma| 2resta| 3multiplica| 4divide| ): ")
        if selecciona in ('1' , '2' , '3' , '4'):
              num1 = int(input("ingresa tu primer numero: "))
              num2 = int(input("ingresa tu segundo numero: "))
              if selecciona == '1':
                     res1 = int(num1) + int(num2)
                     print("La suma es:" , res1)
                     
              if selecciona == '2' :
               res1 = int(num1) - int(num2)
               print("la resta es: " , res1)

        if selecciona == '3' :
               res1 = int(num1) * int(num2)
               print("la multiplicacion es: " , res1)
        if selecciona == '4' :      
               res1 = int(num1) / int(num2)
               print("la division es: " , res1)              
            
                     

