'''Código Problema 3'''
# pylint: disable=invalid-name
# Este comentario de pylint fue deshabilitado debido a
# que en los requerimientos de l a tarea se solicito
# que el nombre del script fuera wordCount

import sys
import time


def process_words(file_path):
    '''Funcion para procesar las palabras y contarlas'''
    word_count = {}
    try:
        with open(file_path, 'r', encoding='utf8') as file:
            for line in file:
                words = line.split()
                for word in words:
                    word = word.lower()  # Convertir todas a minusculas para evitar problemas
                    word_count[word] = word_count.get(word, 0) + 1
        grand_total = sum(word_count.values())
    except FileNotFoundError:
        print(f"Error: File '{file_path}' not found.")
        return None

    return word_count, grand_total


def main():
    '''Funcion principal que llama a las otras funciones'''
    if len(sys.argv) != 2:
        print("Error. No se dieron las variables de entrada"
              "necesarias. Usar el formato python wordCount.py fileWithData.txt")
        return

    start_time = time.time()
    file_path = sys.argv[1]

    word_count, grand_total = process_words(file_path)

    if word_count is not None:
        elapsed_time = time.time() - start_time

        # Print results on the screen
        for word, count in word_count.items():
            print(f"{word}: {count}")
        print('-' * 12)
        print(f'Cantidad Total de palabras {grand_total}')

        print(f"\nTime elapsed: {elapsed_time:.4f} seconds")

        # Save results to file
        with open(f'WordCountResults_{file_path}.txt', 'w', encoding='utf8') as result_file:
            for word, count in word_count.items():
                result_file.write(f"{word}: {count}\n")
            result_file.write('-' * 12)
            result_file.write(f'\nCantidad Total de palabras {grand_total}\n')

            result_file.write(f"\nTime elapsed: {elapsed_time:.4f} seconds\n")


if __name__ == "__main__":
    main()
