import datetime
import json

fecha_hora = datetime.datetime.now()
formato_personalizado = "%Y-%m-%d %H:%M:%S"
ruta_archivo = 'C:\\Users\\Pamela\\OneDrive\\Escritorio\\pame prueba.json'
ventas = []

precio_pizzas = {
    'cuatro quesos': {'pequeña': 6000, 'mediana': 9000, 'familiar': 12000},
    'hawaiana': {'pequeña': 6000, 'mediana': 9000, 'familiar': 12000},
    'napolitana': {'pequeña': 5500, 'mediana': 8500, 'familiar': 11000},
    'peperoni': {'pequeña': 7000, 'mediana': 10000, 'familiar': 13000}
}

def menu():
    print('\nVentas de pizza Duoc')
    print('1. Registrar una venta')
    print('2. Mostrar todas las ventas')
    print('3. Buscar ventas por cliente')
    print('4. Guardar ventas en un archivo')
    print('5. Cargar las ventas desde un archivo')
    print('6. Generar boleta')
    print('7. Anular Venta')
    print('8. Salir del programa')

def registrar_ventas():
    cliente = input('Ingrese el nombre del cliente: ').lower()
    tipo_cliente = input('Ingrese el tipo de cliente (diurno, vespertino, administrativo): ').lower()
    tipo_pizza = input('Ingrese tipo de pizza (cuatro quesos, hawaiana, napolitana, peperoni): ').lower()
    tamaño_pizza = input('Ingrese el tamaño de la pizza (pequeña, mediana, familiar): ').lower()
    cantidad = int(input('Ingrese la cantidad de pizzas: '))

    precio_unitario = precio_pizzas[tipo_pizza][tamaño_pizza]
    
    descuento = 0
    
    if tipo_cliente == 'diurno':
        descuento = 0.12
    elif tipo_cliente == 'vespertino':
        descuento = 0.14
    elif tipo_cliente == 'administrativo':
        descuento = 0.10
        
    precio_total = precio_unitario * cantidad
    precio_final = precio_total * (1 - descuento)

    # Registro de la venta
    venta = {
        'cliente': cliente,
        'tipo_cliente': tipo_cliente,
        'tipo_pizza': tipo_pizza,
        'tamaño_pizza': tamaño_pizza,
        'cantidad': cantidad,
        'precio_final': precio_final,
        'fecha': fecha_hora.strftime(formato_personalizado)
    }
    ventas.append(venta)
    print('Venta registrada exitosamente')

def mostrar_ventas():
    for venta in ventas:
        print(f"Cliente: {venta['cliente']}, Tipo de cliente: {venta['tipo_cliente']}, "
              f"Pizza: {venta['tipo_pizza']} ({venta['tamaño_pizza']}), "
              f"Cantidad: {venta['cantidad']}, Precio final: ${venta['precio_final']}")

def buscar_venta_cliente():
    buscar_cliente = input('Ingrese el nombre del cliente para buscar las ventas: ').lower()
    ventas_encontradas = [venta for venta in ventas if venta['cliente'] == buscar_cliente]

    if ventas_encontradas:
        for venta in ventas_encontradas:
            print(f"Cliente: {venta['cliente']}, Tipo de cliente: {venta['tipo_cliente']}, "
                  f"Pizza: {venta['tipo_pizza']} ({venta['tamaño_pizza']}), "
                  f"Cantidad: {venta['cantidad']}, Precio final: ${venta['precio_final']}")
    else:
        print(f"No se encontraron ventas para el cliente '{buscar_cliente}'.")

def guardar_venta():
    archivo = 'C:\\Users\\Pamela\\OneDrive\\Escritorio\\pame prueba.json'
    with open('ventas.json', 'w') as archivo:
        json.dump(ventas, archivo, indent=4)
    print('Ventas guardadas con éxito en el archivo "ventas.json".')

def cargar_ventas():
    archivo = 'C:\\Users\\Pamela\\OneDrive\\Escritorio\\pame prueba.json'
    global ventas
    try:
        with open('ventas.json', 'r') as archivo:
            ventas = json.load(archivo)
        print('Ventas cargadas desde el archivo "ventas.json".')
    except FileNotFoundError:
        print('No se encontró el archivo "ventas.json".')

def generar_boleta():
    cliente = input('Ingrese el nombre del cliente para generar la boleta: ').lower()
    ventas_cliente = [venta for venta in ventas if venta['cliente'] == cliente]

    if ventas_cliente:
        total = sum(venta['precio_final'] for venta in ventas_cliente)
        print('\nBoleta:')
        print(f'Cliente: {cliente}')
        print(f'Fecha: {fecha_hora.strftime(formato_personalizado)}')
        print('Detalle de compras:')
        for venta in ventas_cliente:
            print(f"- {venta['tipo_pizza']} ({venta['tamaño_pizza']}): ${venta['precio_final']}")
        print(f'Total a pagar: ${total}')
    else:
        print(f"No se encontraron ventas para el cliente '{cliente}'.")

def anular_venta():
    cliente = input("Ingrese el nombre del cliente de la venta a anular: ").lower()
    tipo_pizza = input("Ingrese el tipo de pizza de la venta a anular: ").lower()
    tamaño_pizza = input("Ingrese el tamaño de la pizza de la venta a anular: ").lower()

    venta_a_anular = None
    for venta in ventas:
        if (venta['cliente'] == cliente and venta['tipo_pizza'] == tipo_pizza and venta['tamaño_pizza'] == tamaño_pizza):
            venta_a_anular = venta
            break

    if venta_a_anular:
        ventas.remove(venta_a_anular)
        print("Venta anulada con éxito.")
    else:
        print("No se encontró la venta a anular.")

# Bucle principal del programa
while True:
    menu()
    op = input('Seleccione una opción: ')

    if op == '1':
        registrar_ventas()
    elif op == '2':
        mostrar_ventas()
    elif op == '3':
        buscar_venta_cliente()
    elif op == '4':
        guardar_venta()
    elif op == '5':
        cargar_ventas()
    elif op == '6':
        generar_boleta()
    elif op == '7':
        anular_venta()
    elif op == '8':
        print('Saliendo del programa.')
        break
    else:
        print('Opción no válida. Por favor, ingrese un número del 1 al 8.')
