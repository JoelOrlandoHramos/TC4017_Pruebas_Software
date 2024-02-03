'''Código para Problema 2'''
# pylint: disable=invalid-name
# este comentario fue deshabilitado debido
# a que en los requerimiento se especifica que
# el nombre debe de ser converNumbers
import sys
import time



def convert_to_binary(numbers):
    '''Funcion para convertir a binario'''
    if numbers < 0:
        numbers = 2 ** 32 + numbers  # conversion de numeros negativos a representacion de 32 bits

    binary_result = ""
    while numbers > 0:
        remainder = numbers % 2  # matematicamente lo que vamos a buscar es los residuos
        # al dividir el numero siempre entre dos.
        binary_result = str(remainder) + binary_result
        numbers //= 2
    return binary_result


def convert_to_hexadecimal(numbers):
    '''Funcion para convertir a binario'''
    if numbers < 0:
        numbers = 2 ** 32 + numbers  # conversion de numeros negativos a representacion de 32 bits

    hex_chars = "0123456789ABCDEF"  # En la notación hexadecimal, los números
    # se representan utilizando los dígitos
    # del 0 al 9 y las letras A-F, donde A representa 10, B representa 11,
    # y así sucesivamente hasta que F representa 15.
    hex_result = ""
    while numbers > 0:
        remainder = numbers % 16  # en este caso tambien nos interesa el residuo.
        # No obstante, aqui dividiremos el numero
        # siempre entre 16.
        hex_result = hex_chars[remainder] + hex_result
        numbers //= 16
    return hex_result


def convert_numbers(file_path):
    '''Funcion para comenzar a evaluar los numeros en los
    txt files y llamar a las funciones de conversión'''
    try:
        with open(file_path, 'r', encoding='utf8') as file:
            numbers = file.read().splitlines()
    except FileNotFoundError:
        print(f"Error: Archivo '{file_path}' no ha sido encontrado.")
        return None

    binary_results = []
    hex_results = []
    decimal_numbers = []

    for number in numbers:
        try:
            num = int(number)
            decimal_numbers.append(num)
            binary_results.append(convert_to_binary(num))
            hex_results.append(convert_to_hexadecimal(num))
        except ValueError:
            print(f"Error: El tipo de dato '{number}' no es un número.")
            decimal_numbers.append('NA')
            binary_results.append('NA')
            hex_results.append('NA')

    return binary_results, hex_results, decimal_numbers


def main():
    '''Principal'''
    if len(sys.argv) != 2:
        print("El input no es valido. La línea de comando debe "
              "de ser: python convertNumbers.py fileWithData.txt")
        sys.exit(1)

    filename = sys.argv[1]

    start_time = time.time()

    results = convert_numbers(filename)

    if results:
        binary_results, hex_results, decimal_numbers = results

        print("RESULTADOS")
        print(f"{'Decimal':<12} {'Binary':<40} {'Hexadecimal':<20}")
        print("-" * 60)
        for binary, hex_val, decimal in zip(binary_results, hex_results, decimal_numbers):
            print(f"{decimal:<12} {binary:<40} {hex_val:<20}")

        with open(f'ConversionResults_{filename}.txt', 'w', encoding='utf8') as results_file:
            results_file.write(f"{'Decimal':<80} {'Binary':<80} {'Hexadecimal':<80}\n")
            results_file.write("-" * 160 + "\n")

            for binary, hex_val, decimal in zip(binary_results, hex_results, decimal_numbers):
                results_file.write(f"{decimal:<80} {binary:<80} {hex_val:<80}")

        elapsed_time = time.time() - start_time

        print(f"\nTime elapsed: {elapsed_time:.6f} seconds")

        with open(f'ConversionResults_{filename}.txt', 'a', encoding='utf8') as results_file:
            results_file.write(f"\nTime elapsed: {elapsed_time:.6f} seconds")


if __name__ == "__main__":
    main()
