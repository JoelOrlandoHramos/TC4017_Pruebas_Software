'''EJERCICIO DE PROGRAMACION 2'''
# pylint: disable = invalid-name
import sys
import json
import time


def cargar_json(ruta_archivo):
    '''Función para cargar un archivo JSON'''
    try:
        with open(ruta_archivo, 'r', encoding='utf8') as archivo:
            datos = json.load(archivo)
        return datos
    except FileNotFoundError:
        print(f"ERROR: El archivo {ruta_archivo} no se encontró.")
        sys.exit(1)
    except json.JSONDecodeError:
        print(f"ERROR: El archivo {ruta_archivo} no es un JSON válido.")
        sys.exit(1)


def diccionario_precios(catalogo_precios):
    '''Funcion para crear un diccionario sea más sencillo accesar
    a los datos'''
    dicc_precios = {}
    for registro in catalogo_precios:
        dicc_precios[registro['title']] = registro['price']
    return dicc_precios


def calcular_costo_total(catalogo_precios, registro_ventas):
    '''Función para calcular el costo total de las ventas'''
    costo_total = 0
    dicc_precios = diccionario_precios(catalogo_precios)
    for venta in registro_ventas:
        id_producto = venta['Product']
        cantidad = venta['Quantity']
        if id_producto in dicc_precios:
            costo_total += dicc_precios[id_producto] * cantidad
        else:
            print(f"ADVERTENCIA: El producto con ID {id_producto}"
                  f" no está en el catálogo de precios.")
    return costo_total


def main():
    '''Función principal'''
    # Verificar si se pasaron los argumentos esperados
    if len(sys.argv) != 3:
        print("Uso: python computeSales.py "
              "priceCatalogue.json salesRecord.json")
        sys.exit(1)

    # Obtener los nombres de los archivos de entrada
    archivo_catalogo_precios = sys.argv[1]
    archivo_registro_ventas = sys.argv[2]

    # Cargar los datos de los archivos JSON
    catalogo_precios = cargar_json(archivo_catalogo_precios)
    registro_ventas = cargar_json(archivo_registro_ventas)

    # Calcular el costo total de las ventas
    tiempo_inicio = time.time()
    costo_total = calcular_costo_total(catalogo_precios, registro_ventas)
    tiempo_fin = time.time()

    # Calcular el tiempo transcurrido
    tiempo_transcurrido = tiempo_fin - tiempo_inicio

    # Imprimir el costo total y el tiempo transcurrido
    print(f"Costo total de las ventas: ${costo_total:.2f}")
    print(f"Tiempo transcurrido: {tiempo_transcurrido:.2f} segundos")

    # Escribir los resultados en un archivo
    with open(f"SalesResults_{archivo_registro_ventas}.txt",
              'w', encoding='utf8') as archivo_resultados:
        archivo_resultados.write(f"Costo total de las ventas: "
                                 f"${costo_total:.2f}\n")
        archivo_resultados.write(f"Tiempo transcurrido:"
                                 f" {tiempo_transcurrido:.2f} segundos")


if __name__ == "__main__":
    main()
