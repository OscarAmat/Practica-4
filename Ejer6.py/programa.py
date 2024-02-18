def main():
    ingrese_fraccion= str(input('Ingrese una fracción: '))
    x,y=ingrese_fraccion.split('/')
    while x<=y :
        try:
            x=int(x)
            y=int(y)
            a=x/y
        except ValueError:
            print("Error dado que solo se permiten números enteros")
            return main()
        break
    while x>y:
        try:
            x=int(x)
            y=int(y)
            a=x/y
            return main()
        except ValueError:
            print("Error dado que solo se permiten números enteros")
            return main()
        except ZeroDivisionError:
            print("Ingresar una fraccion")
            return main() 
        break    
    a=x/y
    porcentaje=a*100
    porcentaje=int(porcentaje)
    if 1>=a<0.01:
       print('E')
    elif 1>=a>0.99:
       print('F')
    else:
        print(f'{porcentaje}%')    
    
main()