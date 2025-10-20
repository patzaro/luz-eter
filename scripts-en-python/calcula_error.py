#!/usr/bin/env python3
# calcula_error.py
# Calcula el error porcentual entre dos cifras: un valor de referencia y un valor a comparar

def limpiar_numero(s):
    """Elimina separadores como puntos, comas y espacios, devuelve entero."""
    if not s:
        raise ValueError("Entrada vacía")
    s = s.replace(".", "").replace(",", "").replace(" ", "")
    if not s.isdigit():
        raise ValueError(f"Entrada no válida: {s}")
    return int(s)

def error_porcentual(ref_str, valor_str):
    """Calcula el error relativo porcentual respecto al valor de referencia."""
    ref = limpiar_numero(ref_str)
    valor = limpiar_numero(valor_str)
    error = abs(valor - ref) / ref * 100
    return error

def main():
    print("Cálculo de error porcentual entre valor de referencia y valor a comparar")
    ref_str = input("Introduce el valor de referencia: ")
    valor_str = input("Introduce el valor a comparar: ")
    try:
        error = error_porcentual(ref_str, valor_str)
        print(f"Error relativo: {error:.12f} %")
    except ValueError as e:
        print("Error:", e)

if __name__ == "__main__":
    main()
