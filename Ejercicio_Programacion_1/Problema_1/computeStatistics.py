"""" Código para el probema 1"""

# pylint: disable=invalid-name
# Se desabilito este error dado que era un requerimiento nombrar la tarea
# de esta manera computeStatistics.py

import sys
import time
import math


def calculate_count(numbers):
    """" Funcion para calcular el numero total de elementos """
    return len(numbers)


def calculate_mean(numbers):
    """" Funcion para calcular la media """
    return sum(numbers) / len(numbers)


def calculate_median(numbers):
    """" Funcion para calcular la mediana """
    sorted_numbers = sorted(numbers)
    n = len(sorted_numbers)

    if n % 2 == 0:  # pylint: disable= no-else-return
        mid_number1 = sorted_numbers[n // 2 - 1]
        mid_number2 = sorted_numbers[n // 2]
        return (mid_number1 + mid_number2) / 2
    else:
        return sorted_numbers[n // 2]


# Este error fue deshabilitado debido a que si necesitamos especificar que pasara en caso de
# que el numero total de elementos no sea par.

def calculate_mode(numbers):
    """"Funcion para calcular la moda"""
    counts = {}

    for num in numbers:
        counts[num] = counts.get(num, 0) + 1

    max_freq = max(counts.values(), default=0)

    if max_freq > 1: # pylint: disable= no-else-return
        mode = [k for k, v in counts.items() if v == max(counts.values())]
        return mode
    else:
        return "NO APLICA"
# Este error fue deshabilitado debido a que si necesitamos especificar que pasara en caso de
# que no haya una frecuencia de moda mayor a 1.

def calculate_variance(numbers, mean):
    """" Funcion para calcular la varianza """
    return sum((x - mean) ** 2 for x in numbers) / (len(numbers) - 1)


def calculate_standard_deviation(variance):
    """" Funcion para calcular la des. estandar """
    return math.sqrt(variance)


def handle_invalid_data(line, line_number):
    """" Error al encontrar un dato que no sea numerico """
    try:
        return float(line)
    except ValueError:
        print(f"Error: Invalid data at line {line_number}: {line}")
        return None


def main():
    """" Función principal"""
    if len(sys.argv) != 2:
        print('El input no esta completo. La linea de comando es: '
              'python computeStatistics.py <filename>')
        sys.exit(1)

    input_file = sys.argv[1]

    try:
        start_time = time.time()

        with open(input_file, 'r', encoding='utf-8') as file:
            lines = file.readlines()
            numbers = [handle_invalid_data(line.strip(), i + 1) for i, line in enumerate(lines)]
            numbers = [num for num in numbers if num is not None]

            if not numbers:
                print("No hay valores númericos en el archivo")
                sys.exit(1)

            count = calculate_count(numbers)
            mean = calculate_mean(numbers)
            median = calculate_median(numbers)
            mode = calculate_mode(numbers)
            variance = calculate_variance(numbers, mean)
            standard_deviation = calculate_standard_deviation(variance)

            print("CONTEO:", count)
            print("MEDIA:", mean)
            print("MEDIANA:", median)
            print("MODA:", mode)
            print("DESVIACION ESTANDAR:", standard_deviation)
            print("VARIANZA:", variance)

            with open(f"StatisticsResults_{input_file}.txt", 'w', encoding="utf-8") as result_file:
                result_file.write(f"Conteo: {count}\n")
                result_file.write(f"Media: {mean}\n")
                result_file.write(f"Mediana: {median}\n")
                result_file.write(f"Moda: {mode}\n")
                result_file.write(f"Varianza: {variance}\n")
                result_file.write(f"Desv. Estándar: {standard_deviation}\n")

        elapsed_time = time.time() - start_time
        print(f"\nTime elapsed: {elapsed_time} seconds")
        with open(f"StatisticsResults_{input_file}.txt", 'a', encoding="utf-8") as result_file:
            result_file.write(f"\nTime elapsed: {elapsed_time} seconds\n")

    except FileNotFoundError:
        print(f"Error: File '{input_file}' not found.")


if __name__ == "__main__":
    main()
