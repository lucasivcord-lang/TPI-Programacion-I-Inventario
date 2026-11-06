
def main():
    inventario = []
    opcion = 0

    while opcion != 7:    
        print("""\n===== SISTEMA DE INVENTARIO =====
1. Cargar herramientas
2. Mostrar inventario
3. Consultar stock
4. Reporte de agotados
5. Alta de producto
6. Actualizar stock
7. Salir""")
        try:
            entrada = input("Seleccione una opcion (1 a 7): ")
            opcion = int(entrada)
            if opcion < 1 or opcion > 7:
                raise ValueError ("Opción fuera de rango")
            elif opcion == 1:
                cargar_herramientas(inventario)
            elif opcion == 2:
                mostrar_inventario(inventario)
            elif opcion == 3:
                consultar_stock(inventario)
            elif opcion == 4:
                reporte_agotados(inventario)
            elif opcion == 5:
                alta_producto(inventario)
            elif opcion == 6:
                actualizar_stock(inventario)
            else:
                print("Fin del programa")
        except ValueError as e:
            print(f"Error: {e}. Intente nuevamente.")
            continue

def cargar_herramientas(inventario):
    while True:
        try:
            entrada = input("Ingrese la cantidad a cargar: ")
            cantidad = int(entrada)
            if cantidad <= 0:
                raise ValueError ("Cantidad no valida")
            break
        except ValueError as e:
            print(f"Error: {e}. Intente nuevamente.")
    print(f"Se cargaran {cantidad} herramientas")
    for i in range(cantidad):
        while True:
            try:
                nombre = input(f"Ingrese el nombre de la herramienta {i+1}: ").strip()
                if not nombre:
                    raise ValueError("El nombre no puede estar vacío")
                for herramienta in inventario:
                    if nombre.lower() == herramienta["herramienta"].lower():
                        raise ValueError("La herramienta ya existe")
                break
            except ValueError as e:
                print(f"Error: {e}. Intente nuevamente.")
        while True:
            try: 
                stock = int(input("Ingrese stock: "))
                if stock < 0:
                    raise ValueError ("El stock no puede ser negativo")
                break
            except ValueError as e:
                print(f"Error: {e}. Intente nuevamente.")          
        inventario.append({"herramienta": nombre,"cantidad": stock})
        print(f"Herramienta {nombre} cargada correctamente.")
  
def mostrar_inventario(inventario):
    if len(inventario) == 0:
        print("El inventario esta vacio")
        return
    print("\n===== INVENTARIO =====")
    for herramientas in inventario:
        print(f"Herramienta: {herramientas['herramienta']} | Stock: {herramientas['cantidad']}")

def consultar_stock(inventario):
    if len(inventario) == 0:
        print("El inventario esta vacio")
        return
    nombre = input("Ingrese la herramienta a consultar: ").strip()
    if not nombre:
        raise ValueError("El nombre no puede estar vacío")
    for herramienta in inventario:
           if nombre.lower() == herramienta["herramienta"].lower():
                print(f"Herramientas en Stock: {herramienta['herramienta']} | Stock: {herramienta['cantidad']}")
                return
    print("La herramienta no existe")
    
def reporte_agotados(inventario):
    if len(inventario) == 0:
            print("El inventario esta vacio")
            return
    encontrado = False
    for herramienta in inventario:
        if herramienta["cantidad"] == 0:
            print(f"Herramientas agotadas: {herramienta["herramienta"]}")
            encontrado = True
    if not encontrado:
        print("No hay herramientas agotadas")

def alta_producto(inventario):
        nombre = input("Ingrese el nombre de la herramienta: ").strip()
        if not nombre:
            raise ValueError("El nombre no puede estar vacío")
        for herramienta in inventario:
            if nombre.lower() == herramienta["herramienta"].lower():
                raise ValueError("La herramienta ya existe")
        stock = int(input("Ingrese el stock inicial: "))
        if stock < 0:
            raise ValueError("El stock no puede ser negativo")
        inventario.append({"herramienta": nombre,"cantidad": stock})
        print("Producto ingresado con exito")

def actualizar_stock(inventario):
    if len(inventario) == 0:
        print("El inventario esta vacio") 
        return
    nombre = input("Ingrese la herramienta a consultar: ").strip()
    if not nombre:
        raise ValueError("El nombre no puede estar vacío")    
    for herramienta in inventario:
        if nombre.lower() == herramienta["herramienta"].lower():
            print(f"Herramienta: {herramienta['herramienta']} | Stock: {herramienta['cantidad']}")
            print("""\n===== OPCIONES =====
1. Venta
2. Ingreso""")
            movimiento = input("Seleccione una opcion: ").strip()
            if movimiento != "1" and movimiento != "2":
                print("Movimiento inválido")
                return
            if movimiento == "1": # Venta
                unidades = int(input("Ingrese la cantidad de unidades: "))
                if unidades <= 0:
                    raise ValueError("Las unidades deben ser mayores que cero")
                if unidades > herramienta["cantidad"]:
                    raise ValueError("Las unidades solicitadas superan el stock disponible")
                herramienta["cantidad"] -= unidades   
            elif movimiento == "2": # Ingreso
                unidades = int(input("Ingrese la cantidad de unidades: "))
                if unidades <= 0:
                    raise ValueError("Las unidades deben ser mayores que cero")
                herramienta["cantidad"] += unidades
            return
    print("Herramienta no encontrada")

main()