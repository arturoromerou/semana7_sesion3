from conn import Conexion
import os
import sys

############## CONEXION Y CIERRE CON BD ##############
def main():
    conexion_pg = Conexion(
        direccion_servidor='127.0.0.1',
        usuario='postgres',
        contrasena='Ar2098urd',
        base_datos='retoclase'
    )
    #conexion_pg.crear_tabla()
    menu_comprador(conexion_pg)
    menu_administrador(conexion_pg)
    menu_productos(conexion_pg)

###################### AGREGAR PRODUCTOS ADMINISTRADOR #######################
def insertar_verduras(conexion_pg):
    continuar = True
    while continuar:
        os.system("clear")
        print("*****Almacen******\n")

        nombre_articulo = input("Que articulo es?: ")
        precio = float(input("cuanto cuesta?: "))
        cantidad = int(input("cuantos son?: "))

        conexion_pg.insertar_verduras(nombre_articulo, cantidad, precio)
        
        print("ARTICULO AGREGADO!!!\n")
        print("\n********************************")       
        print('\n[a] Para agregar al mas articulos')
        print('[m] Para regresar al menu principal')
        print('[s] Para salir')
        opcion = input("\nElija una opcion: ")

        if opcion == "s":
            sys.exit()
        elif opcion == "a":
            continuar = True
        elif opcion == "m":
            continuar = False
            os.system("clear")

def insertar_carnes(conexion_pg):
    continuar = True
    while continuar:
        os.system("clear")
        print("*****Almacen******\n")

        nombre_articulo = input("Que articulo es?: ")
        precio = float(input("cuanto cuesta?: "))
        cantidad = int(input("cuantos son?: "))

        conexion_pg.insertar_carnes(nombre_articulo, cantidad, precio)
        
        print("ARTICULO AGREGADO!!!\n")
        print("\n********************************")       
        print('\n[a] Para agregar al mas articulos')
        print('[m] Para regresar al menu principal')
        print('[s] Para salir')
        opcion = input("\nElija una opcion: ")

        if opcion == "s":
            sys.exit()
        elif opcion == "a":
            continuar = True
        elif opcion == "m":
            continuar = False
            os.system("clear")

def insertar_congelados(conexion_pg):
    continuar = True
    while continuar:
        os.system("clear")
        print("*****Almacen******\n")

        nombre_articulo = input("Que articulo es?: ")
        precio = float(input("cuanto cuesta?: "))
        cantidad = int(input("cuantos son?: "))

        conexion_pg.insertar_congelados(nombre_articulo, cantidad, precio)
        
        print("ARTICULO AGREGADO!!!\n")
        print("\n********************************")       
        print('\n[a] Para agregar al mas articulos')
        print('[m] Para regresar al menu principal')
        print('[s] Para salir')
        opcion = input("\nElija una opcion: ")

        if opcion == "s":
            sys.exit()
        elif opcion == "a":
            continuar = True
        elif opcion == "m":
            continuar = False
            os.system("clear")

def insertar_lacteos(conexion_pg):
    continuar = True
    while continuar:
        os.system("clear")
        print("*****Almacen******\n")

        nombre_articulo = input("Que articulo es?: ")
        precio = float(input("cuanto cuesta?: "))
        cantidad = int(input("cuantos son?: "))

        conexion_pg.insertar_lacteos(nombre_articulo, cantidad, precio)
        
        print("ARTICULO AGREGADO!!!\n")
        print("\n********************************")       
        print('\n[a] Para agregar al mas articulos')
        print('[m] Para regresar al menu principal')
        print('[s] Para salir')
        opcion = input("\nElija una opcion: ")

        if opcion == "s":
            sys.exit()
        elif opcion == "a":
            continuar = True
        elif opcion == "m":
            continuar = False
            os.system("clear")

def insertar_quesos(conexion_pg):
    continuar = True
    while continuar:
        os.system("clear")
        print("*****Almacen******\n")

        nombre_articulo = input("Que articulo es?: ")
        precio = float(input("cuanto cuesta?: "))
        cantidad = int(input("cuantos son?: "))

        conexion_pg.insertar_quesos(nombre_articulo, cantidad, precio)
        
        print("ARTICULO AGREGADO!!!\n")
        print("\n********************************")       
        print('\n[a] Para agregar al mas articulos')
        print('[m] Para regresar al menu principal')
        print('[s] Para salir')
        opcion = input("\nElija una opcion: ")

        if opcion == "s":
            sys.exit()
        elif opcion == "a":
            continuar = True
        elif opcion == "m":
            continuar = False
            os.system("clear")

def insertar_abarrotes(conexion_pg):
    continuar = True
    while continuar:
        os.system("clear")
        print("*****Almacen******\n")

        nombre_articulo = input("Que articulo es?: ")
        precio = float(input("cuanto cuesta?: "))
        cantidad = int(input("cuantos son?: "))

        conexion_pg.insertar_abarrotes(nombre_articulo, cantidad, precio)
        
        print("ARTICULO AGREGADO!!!\n")
        print("\n********************************")       
        print('\n[a] Para agregar al mas articulos')
        print('[m] Para regresar al menu principal')
        print('[s] Para salir')
        opcion = input("\nElija una opcion: ")

        if opcion == "s":
            sys.exit()
        elif opcion == "a":
            continuar = True
        elif opcion == "m":
            continuar = False
            os.system("clear")

def insertar_bebidas(conexion_pg):
    continuar = True
    while continuar:
        os.system("clear")
        print("*****Almacen******\n")

        nombre_articulo = input("Que articulo es?: ")
        precio = float(input("cuanto cuesta?: "))
        cantidad = int(input("cuantos son?: "))

        conexion_pg.insertar_bebidas(nombre_articulo, cantidad, precio)
        
        print("ARTICULO AGREGADO!!!\n")
        print("\n********************************")       
        print('\n[a] Para agregar al mas articulos')
        print('[m] Para regresar al menu principal')
        print('[s] Para salir')
        opcion = input("\nElija una opcion: ")

        if opcion == "s":
            sys.exit()
        elif opcion == "a":
            continuar = True
        elif opcion == "m":
            continuar = False
            os.system("clear")

def insertar_panaderia(conexion_pg):
    continuar = True
    while continuar:
        os.system("clear")
        print("*****Almacen******\n")

        nombre_articulo = input("Que articulo es?: ")
        precio = float(input("cuanto cuesta?: "))
        cantidad = int(input("cuantos son?: "))

        conexion_pg.insertar_panaderia(nombre_articulo, cantidad, precio)
        
        print("ARTICULO AGREGADO!!!\n")
        print("\n********************************")       
        print('\n[a] Para agregar al mas articulos')
        print('[m] Para regresar al menu principal')
        print('[s] Para salir')
        opcion = input("\nElija una opcion: ")

        if opcion == "s":
            sys.exit()
        elif opcion == "a":
            continuar = True
        elif opcion == "m":
            continuar = False
            os.system("clear")

def insertar_cuidado(conexion_pg):
    continuar = True
    while continuar:
        os.system("clear")
        print("*****Almacen******\n")

        nombre_articulo = input("Que articulo es?: ")
        precio = float(input("cuanto cuesta?: "))
        cantidad = int(input("cuantos son?: "))

        conexion_pg.insertar_cuidado(nombre_articulo, cantidad, precio)
        
        print("ARTICULO AGREGADO!!!\n")
        print("\n********************************")       
        print('\n[a] Para agregar al mas articulos')
        print('[m] Para regresar al menu principal')
        print('[s] Para salir')
        opcion = input("\nElija una opcion: ")

        if opcion == "s":
            sys.exit()
        elif opcion == "a":
            continuar = True
        elif opcion == "m":
            continuar = False
            os.system("clear")

def insertar_limpieza(conexion_pg):
    continuar = True
    while continuar:
        os.system("clear")
        print("*****Almacen******\n")

        nombre_articulo = input("Que articulo es?: ")
        precio = float(input("cuanto cuesta?: "))
        cantidad = int(input("cuantos son?: "))

        conexion_pg.insertar_limpieza(nombre_articulo, cantidad, precio)
        
        print("ARTICULO AGREGADO!!!\n")
        print("\n********************************")       
        print('\n[a] Para agregar al mas articulos')
        print('[m] Para regresar al menu principal')
        print('[s] Para salir')
        opcion = input("\nElija una opcion: ")

        if opcion == "s":
            sys.exit()
        elif opcion == "a":
            continuar = True
        elif opcion == "m":
            continuar = False
            os.system("clear")

def insertar_mascotas(conexion_pg):
    continuar = True
    while continuar:
        os.system("clear")
        print("*****Almacen******\n")

        nombre_articulo = input("Que articulo es?: ")
        precio = float(input("cuanto cuesta?: "))
        cantidad = int(input("cuantos son?: "))

        conexion_pg.insertar_mascotas(nombre_articulo, cantidad, precio)
        
        print("ARTICULO AGREGADO!!!\n")
        print("\n********************************")       
        print('\n[a] Para agregar al mas articulos')
        print('[m] Para regresar al menu principal')
        print('[s] Para salir')
        opcion = input("\nElija una opcion: ")

        if opcion == "s":
            sys.exit()
        elif opcion == "a":
            continuar = True
        elif opcion == "m":
            continuar = False
            os.system("clear")

###################### FUNCION VER PRODUCTOS #######################
def ver_articulos(conexion_pg):
    continuar = True
    while continuar:
        os.system("clear")
        print("*****Articulos en carrito******\n")
        print("--- --------- -------------------------------    ----- -------------   ---------------- -----------------")
        print("nro articulo               fecha                 cant.    subtotal            igv        total a pagar") 
        print("--- --------- -------------------------------    ----- -------------   ---------------- -----------------")    
        print(conexion_pg.ver_articulos())     
        print('\n[m] Para regresar al menu principal')
        print('\n[s] Para salir')
        opcion = input("\nElija una opcion: ")
        if opcion == "m":
            continuar = False
            os.system("clear")
        elif opcion == "s":
            sys.exit()
        else:
            opcion == input("\nDigite una seleccion valida: ")

############ FUNCION PARA MODIFICAR ARTICULOS """ALMACEN""" ###############
def modificar_verduras(conexion_pg):
    continuar = True
    os.system("clear")

    print("*****Modifica el articulos con su ID******\n")
    print("*****Articulos en lista******\n")
    print("--  -------   -------------------------------    ----- -------------")
    print("ID  nombre                 fecha                 cant.    precio") 
    print("--  -------   -------------------------------    ----- -------------")    
    print(conexion_pg.ver_vegetales())

    codigo_articulo = int(input("\nintroduce el id del articulo a modificar\n"))
    nombre_articulo = input("el nuevo articulo es: ")
    precio = float(input("cuesta: "))
    cantidad = int(input("cantidad: "))
        
    pregunta = input('\nEstas seguro que quieres modificarlo? [s] o [n]: ')
    
    if pregunta == "s": 
        conexion_pg.modificar_verduras(nombre_articulo, cantidad, precio, codigo_articulo)
        print("ARTICULO MODIFICADO!!!")
        
    elif pregunta == "n":
        continuar = False

    print("\n********************************")
    print('[m] Para regresar al menu principal')
    print('\n[s] Para salir')
    opcion = input("\nElija una opcion: ")

    if opcion == "m":
        continuar = False
        os.system("clear")
    elif opcion == "s":
        sys.exit()
    else:
        opcion == input("elija una seleccion valida: ")

def modificar_carnes(conexion_pg):
    continuar = True
    os.system("clear")

    print("*****Modifica el articulos con su ID******\n")
    print("*****Articulos en lista******\n")
    print("--  -------   -------------------------------    ----- -------------")
    print("ID  nombre                 fecha                 cant.    precio") 
    print("--  -------   -------------------------------    ----- -------------")    
    print(conexion_pg.ver_carnes())

    codigo_articulo = int(input("\nintroduce el id del articulo a modificar\n"))
    nombre_articulo = input("el nuevo articulo es: ")
    precio = float(input("cuesta: "))
    cantidad = int(input("cantidad: "))
        
    pregunta = input('\nEstas seguro que quieres modificarlo? [s] o [n]: ')
    
    if pregunta == "s": 
        conexion_pg.modificar_carnes(nombre_articulo, cantidad, precio, codigo_articulo)
        print("ARTICULO MODIFICADO!!!")
        
    elif pregunta == "n":
        continuar = False

    print("\n********************************")
    print('[m] Para regresar al menu principal')
    print('\n[s] Para salir')
    opcion = input("\nElija una opcion: ")

    if opcion == "m":
        continuar = False
        os.system("clear")
    elif opcion == "s":
        sys.exit()
    else:
        opcion == input("elija una seleccion valida: ")

def modificar_congelados(conexion_pg):
    continuar = True
    os.system("clear")

    print("*****Modifica el articulos con su ID******\n")
    print("*****Articulos en lista******\n")
    print("--  -------   -------------------------------    ----- -------------")
    print("ID  nombre                 fecha                 cant.    precio") 
    print("--  -------   -------------------------------    ----- -------------")    
    print(conexion_pg.ver_congelados())

    codigo_articulo = int(input("\nintroduce el id del articulo a modificar\n"))
    nombre_articulo = input("el nuevo articulo es: ")
    precio = float(input("cuesta: "))
    cantidad = int(input("cantidad: "))
        
    pregunta = input('\nEstas seguro que quieres modificarlo? [s] o [n]: ')
    
    if pregunta == "s": 
        conexion_pg.modificar_congelados(nombre_articulo, cantidad, precio, codigo_articulo)
        print("ARTICULO MODIFICADO!!!")
        
    elif pregunta == "n":
        continuar = False

    print("\n********************************")
    print('[m] Para regresar al menu principal')
    print('\n[s] Para salir')
    opcion = input("\nElija una opcion: ")

    if opcion == "m":
        continuar = False
        os.system("clear")
    elif opcion == "s":
        sys.exit()
    else:
        opcion == input("elija una seleccion valida: ")

def modificar_lacteos(conexion_pg):
    continuar = True
    os.system("clear")

    print("*****Modifica el articulos con su ID******\n")
    print("*****Articulos en lista******\n")
    print("--  -------   -------------------------------    ----- -------------")
    print("ID  nombre                 fecha                 cant.    precio") 
    print("--  -------   -------------------------------    ----- -------------")    
    print(conexion_pg.ver_lacteos())

    codigo_articulo = int(input("\nintroduce el id del articulo a modificar\n"))
    nombre_articulo = input("el nuevo articulo es: ")
    precio = float(input("cuesta: "))
    cantidad = int(input("cantidad: "))
        
    pregunta = input('\nEstas seguro que quieres modificarlo? [s] o [n]: ')
    
    if pregunta == "s": 
        conexion_pg.modificar_lacteos(nombre_articulo, cantidad, precio, codigo_articulo)
        print("ARTICULO MODIFICADO!!!")
        
    elif pregunta == "n":
        continuar = False

    print("\n********************************")
    print('[m] Para regresar al menu principal')
    print('\n[s] Para salir')
    opcion = input("\nElija una opcion: ")

    if opcion == "m":
        continuar = False
        os.system("clear")
    elif opcion == "s":
        sys.exit()
    else:
        opcion == input("elija una seleccion valida: ")

def modificar_quesos(conexion_pg):
    continuar = True
    os.system("clear")

    print("*****Modifica el articulos con su ID******\n")
    print("*****Articulos en lista******\n")
    print("--  -------   -------------------------------    ----- -------------")
    print("ID  nombre                 fecha                 cant.    precio") 
    print("--  -------   -------------------------------    ----- -------------")    
    print(conexion_pg.ver_quesos())

    codigo_articulo = int(input("\nintroduce el id del articulo a modificar\n"))
    nombre_articulo = input("el nuevo articulo es: ")
    precio = float(input("cuesta: "))
    cantidad = int(input("cantidad: "))
        
    pregunta = input('\nEstas seguro que quieres modificarlo? [s] o [n]: ')
    
    if pregunta == "s": 
        conexion_pg.modificar_quesos(nombre_articulo, cantidad, precio, codigo_articulo)
        print("ARTICULO MODIFICADO!!!")
        
    elif pregunta == "n":
        continuar = False

    print("\n********************************")
    print('[m] Para regresar al menu principal')
    print('\n[s] Para salir')
    opcion = input("\nElija una opcion: ")

    if opcion == "m":
        continuar = False
        os.system("clear")
    elif opcion == "s":
        sys.exit()
    else:
        opcion == input("elija una seleccion valida: ")

def modificar_abarrotes(conexion_pg):
    continuar = True
    os.system("clear")

    print("*****Modifica el articulos con su ID******\n")
    print("*****Articulos en lista******\n")
    print("--  -------   -------------------------------    ----- -------------")
    print("ID  nombre                 fecha                 cant.    precio") 
    print("--  -------   -------------------------------    ----- -------------")    
    print(conexion_pg.ver_abarrotes())

    codigo_articulo = int(input("\nintroduce el id del articulo a modificar\n"))
    nombre_articulo = input("el nuevo articulo es: ")
    precio = float(input("cuesta: "))
    cantidad = int(input("cantidad: "))
        
    pregunta = input('\nEstas seguro que quieres modificarlo? [s] o [n]: ')
    
    if pregunta == "s": 
        conexion_pg.modificar_abarrotes(nombre_articulo, cantidad, precio, codigo_articulo)
        print("ARTICULO MODIFICADO!!!")
        
    elif pregunta == "n":
        continuar = False

    print("\n********************************")
    print('[m] Para regresar al menu principal')
    print('\n[s] Para salir')
    opcion = input("\nElija una opcion: ")

    if opcion == "m":
        continuar = False
        os.system("clear")
    elif opcion == "s":
        sys.exit()
    else:
        opcion == input("elija una seleccion valida: ")

def modificar_bebidas(conexion_pg):
    continuar = True
    os.system("clear")

    print("*****Modifica el articulos con su ID******\n")
    print("*****Articulos en lista******\n")
    print("--  -------   -------------------------------    ----- -------------")
    print("ID  nombre                 fecha                 cant.    precio") 
    print("--  -------   -------------------------------    ----- -------------")    
    print(conexion_pg.ver_bebidas())

    codigo_articulo = int(input("\nintroduce el id del articulo a modificar\n"))
    nombre_articulo = input("el nuevo articulo es: ")
    precio = float(input("cuesta: "))
    cantidad = int(input("cantidad: "))
        
    pregunta = input('\nEstas seguro que quieres modificarlo? [s] o [n]: ')
    
    if pregunta == "s": 
        conexion_pg.modificar_bebidas(nombre_articulo, cantidad, precio, codigo_articulo)
        print("ARTICULO MODIFICADO!!!")
        
    elif pregunta == "n":
        continuar = False

    print("\n********************************")
    print('[m] Para regresar al menu principal')
    print('\n[s] Para salir')
    opcion = input("\nElija una opcion: ")

    if opcion == "m":
        continuar = False
        os.system("clear")
    elif opcion == "s":
        sys.exit()
    else:
        opcion == input("elija una seleccion valida: ")


def modificar_panaderia(conexion_pg):
    continuar = True
    os.system("clear")

    print("*****Modifica el articulos con su ID******\n")
    print("*****Articulos en lista******\n")
    print("--  -------   -------------------------------    ----- -------------")
    print("ID  nombre                 fecha                 cant.    precio") 
    print("--  -------   -------------------------------    ----- -------------")    
    print(conexion_pg.ver_panaderia())

    codigo_articulo = int(input("\nintroduce el id del articulo a modificar\n"))
    nombre_articulo = input("el nuevo articulo es: ")
    precio = float(input("cuesta: "))
    cantidad = int(input("cantidad: "))
        
    pregunta = input('\nEstas seguro que quieres modificarlo? [s] o [n]: ')
    
    if pregunta == "s": 
        conexion_pg.modificar_panaderia(nombre_articulo, cantidad, precio, codigo_articulo)
        print("ARTICULO MODIFICADO!!!")
        
    elif pregunta == "n":
        continuar = False

    print("\n********************************")
    print('[m] Para regresar al menu principal')
    print('\n[s] Para salir')
    opcion = input("\nElija una opcion: ")

    if opcion == "m":
        continuar = False
        os.system("clear")
    elif opcion == "s":
        sys.exit()
    else:
        opcion == input("elija una seleccion valida: ")

def modificar_cuidado_personal(conexion_pg):
    continuar = True
    os.system("clear")

    print("*****Modifica el articulos con su ID******\n")
    print("*****Articulos en lista******\n")
    print("--  -------   -------------------------------    ----- -------------")
    print("ID  nombre                 fecha                 cant.    precio") 
    print("--  -------   -------------------------------    ----- -------------")    
    print(conexion_pg.ver_cuidado())

    codigo_articulo = int(input("\nintroduce el id del articulo a modificar\n"))
    nombre_articulo = input("el nuevo articulo es: ")
    precio = float(input("cuesta: "))
    cantidad = int(input("cantidad: "))
        
    pregunta = input('\nEstas seguro que quieres modificarlo? [s] o [n]: ')
    
    if pregunta == "s": 
        conexion_pg.modificar_verduras(nombre_articulo, cantidad, precio, codigo_articulo)
        print("ARTICULO MODIFICADO!!!")
        
    elif pregunta == "n":
        continuar = False

    print("\n********************************")
    print('[m] Para regresar al menu principal')
    print('\n[s] Para salir')
    opcion = input("\nElija una opcion: ")

    if opcion == "m":
        continuar = False
        os.system("clear")
    elif opcion == "s":
        sys.exit()
    else:
        opcion == input("elija una seleccion valida: ")

def modificar_limpieza(conexion_pg):
    continuar = True
    os.system("clear")

    print("*****Modifica el articulos con su ID******\n")
    print("*****Articulos en lista******\n")
    print("--  -------   -------------------------------    ----- -------------")
    print("ID  nombre                 fecha                 cant.    precio") 
    print("--  -------   -------------------------------    ----- -------------")    
    print(conexion_pg.ver_limpieza())

    codigo_articulo = int(input("\nintroduce el id del articulo a modificar\n"))
    nombre_articulo = input("el nuevo articulo es: ")
    precio = float(input("cuesta: "))
    cantidad = int(input("cantidad: "))
        
    pregunta = input('\nEstas seguro que quieres modificarlo? [s] o [n]: ')
    
    if pregunta == "s": 
        conexion_pg.modificar_verduras(nombre_articulo, cantidad, precio, codigo_articulo)
        print("ARTICULO MODIFICADO!!!")
        
    elif pregunta == "n":
        continuar = False

    print("\n********************************")
    print('[m] Para regresar al menu principal')
    print('\n[s] Para salir')
    opcion = input("\nElija una opcion: ")

    if opcion == "m":
        continuar = False
        os.system("clear")
    elif opcion == "s":
        sys.exit()
    else:
        opcion == input("elija una seleccion valida: ")

def modificar_mascotas(conexion_pg):
    continuar = True
    os.system("clear")

    print("*****Modifica el articulos con su ID******\n")
    print("*****Articulos en lista******\n")
    print("--  -------   -------------------------------    ----- -------------")
    print("ID  nombre                 fecha                 cant.    precio") 
    print("--  -------   -------------------------------    ----- -------------")    
    print(conexion_pg.ver_mascotas())

    codigo_articulo = int(input("\nintroduce el id del articulo a modificar\n"))
    nombre_articulo = input("el nuevo articulo es: ")
    precio = float(input("cuesta: "))
    cantidad = int(input("cantidad: "))
        
    pregunta = input('\nEstas seguro que quieres modificarlo? [s] o [n]: ')
    
    if pregunta == "s": 
        conexion_pg.modificar_verduras(nombre_articulo, cantidad, precio, codigo_articulo)
        print("ARTICULO MODIFICADO!!!")
        
    elif pregunta == "n":
        continuar = False

    print("\n********************************")
    print('[m] Para regresar al menu principal')
    print('\n[s] Para salir')
    opcion = input("\nElija una opcion: ")

    if opcion == "m":
        continuar = False
        os.system("clear")
    elif opcion == "s":
        sys.exit()
    else:
        opcion == input("elija una seleccion valida: ")

###################### MENU PRINCIPAL #######################
def menu_comprador(conexion_pg):
    continuar = True
    while continuar:
        os.system("clear")
        print("""\t\t\t© Store Hackathon
        \t\t█║▌│█│║▌║││█║▌║▌║\n""")
        print("***************************BIENVENIDO***************************\n")
        print('SI DESEA COMPRAR NUESTROS PORDUCTOS EN STOCK DIGITE "1"\n')
        print('[1] Comprar articulos')
        print('[0] Ver articulos a pagar')
        print('[d] Eliminar articulos a pagar')
        print('[a] Administrador')
        print('\n[s] Salir')
        print("\n**************************************************************\n")
        opcion = input('Digite su seleccion: ')
    
        if opcion == "1":
            agregar_articulos_clientes(conexion_pg)
        elif opcion == "0":
            ver_articulos(conexion_pg)
        elif opcion == "d":
            eliminar_articulo_clientes(conexion_pg)
        elif opcion == "a":
            menu_administrador(conexion_pg)
        elif opcion == "s":
            sys.exit()
        else:
            opcion == input("elija una seleccion valida: ")

###################### MENU ADMINISTRADOR #######################        
def menu_administrador(conexion_pg):
    os.system("clear")
    continuar = True
    while continuar:
        print("\n********** ADMINISTRADOR **********\n")
        print('[1] Agregar articulos al almacen')
        print('[2] Ver articulos en almacen')
        print('[3] Modificar articulos en el almacen')
        print('[4] Eliminar articulos del almacen')
        print('\n[b] Ir al menu principal')
        print('[s] Salir del sistema')
        print("\n**********************************\n")
        opcion = input('Digite su seleccion: ')
        

        if opcion == "1":
            menu_productos(conexion_pg)
        elif opcion == "2":
            ver_articulos(conexion_pg)
        elif opcion == "3":
            modificar_articulo_almacen(conexion_pg)
        elif opcion == "4":
            eliminar_articulo(conexion_pg)
        elif opcion == "s":
            sys.exit()
        elif opcion == "b":
            menu_comprador(conexion_pg)
        else:
            opcion == input("elija una seleccion valida: ")

###################### MENU PRODUCTOS #######################
def menu_productos(conexion_pg):
    os.system("clear")
    continuar = True
    while continuar:
        print("\n********** AGREGAR O MODIFICAR PRODUCTOS **********\n")
        print('[1] Agregar Frutas o Verduras')
        print('[1m] Modificar Frutas o Verduras')
        print('\n[2] Agregar Carnes, Pescados o Aves')
        print('[2m] Modificar Frutas o Verduras')
        print('\n[3] Agregar Congelados')
        print('[3m] Modificar Frutas o Verduras')
        print('\n[4] Agregar Lacteos o Huevos')
        print('[4m] Modificar Frutas o Verduras')
        print('\n[5] Agregar Quesos o Fiambres')
        print('[5m] Modificar Frutas o Verduras')
        print('\n[6] Agregar Abarrotes')
        print('[6m] Modificar Frutas o Verduras')
        print('\n[7] Agregar Bebidas, Cervezas o Licores')
        print('[7m] Modificar Frutas o Verduras')
        print('\n[8] Agregar Panaderia, Pasteleria o Comidas')
        print('[8m] Modificar Frutas o Verduras')
        print('\n[9] Agregar Cuidado Personal')
        print('[9m] Modificar Frutas o Verduras')
        print('\n[0] Agregar Limpieza')
        print('[0m] Modificar Frutas o Verduras')
        print('\n[m] Agregar Mascotas')
        print('[mm] Modificar Frutas o Verduras')
        print('\n\n[b] Ir a menu de admistrador')
        print('[s] Salir del sistema')
        print("\n**********************************\n")
        opcion = input('Digite su seleccion: ')
        

        if opcion == "1":
            insertar_verduras(conexion_pg)
        elif opcion == "2":
            insertar_carnes(conexion_pg)
        elif opcion == "3":
            insertar_congelados(conexion_pg)
        elif opcion == "4":
            insertar_lacteos(conexion_pg)
        elif opcion == "5":
            insertar_quesos(conexion_pg)
        elif opcion == "6":
            insertar_abarrotes(conexion_pg)
        elif opcion == "7":
            insertar_bebidas(conexion_pg)
        elif opcion == "8":
            insertar_panaderia(conexion_pg)
        elif opcion == "9":
            insertar_cuidado(conexion_pg)
        elif opcion == "0":
            insertar_limpieza(conexion_pg)
        elif opcion == "m":
            insertar_mascotas(conexion_pg)
        
        elif opcion == "1m":
            insertar_carnes(conexion_pg)
        elif opcion == "2m":
            insertar_congelados(conexion_pg)
        elif opcion == "3m":
            insertar_lacteos(conexion_pg)
        elif opcion == "4m":
            insertar_quesos(conexion_pg)
        elif opcion == "5m":
            insertar_abarrotes(conexion_pg)
        elif opcion == "6m":
            insertar_bebidas(conexion_pg)
        elif opcion == "7m":
            insertar_panaderia(conexion_pg)
        elif opcion == "8m":
            insertar_cuidado(conexion_pg)
        elif opcion == "9m":
            insertar_limpieza(conexion_pg)
        elif opcion == "0m":
            insertar_mascotas(conexion_pg)
        elif opcion == "mm":
        
        elif opcion == "b":
            menu_administrador(conexion_pg)
        elif opcion == "s":
            sys.exit()
        else:
            opcion == input("elija una seleccion valida: ")
        
#########################################################################

main()

