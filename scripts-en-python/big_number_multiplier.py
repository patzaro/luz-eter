def multiplicar_números(a, b):
    """
    Multiplica dos números de cualquier tamaño.
    Python maneja automáticamente números grandes.
    
    Args:
        a: Primer número (int o string)
        b: Segundo número (int o string)
    
    Returns:
        El producto de a * b
    """
    # Convertir a enteros si son strings
    a = int(a)
    b = int(b)
    
    # Realizar la multiplicación
    resultado = a * b
    return resultado


def main():
    print("=== Multiplicador de Números Grandes ===\n")
    
    while True:
        try:
            # Solicitar entrada del usuario
            num1 = input("Ingresa el primer número (o 'salir' para terminar): ").strip()
            
            if num1.lower() == 'salir':
                print("¡Hasta luego!")
                break
            
            num2 = input("Ingresa el segundo número: ").strip()
            
            # Realizar la multiplicación
            resultado = multiplicar_números(num1, num2)
            
            # Mostrar resultado
            print(f"\n{num1} × {num2} = {resultado}\n")
            
        except ValueError:
            print("Error: Por favor ingresa números válidos.\n")
        except Exception as e:
            print(f"Error: {e}\n")


# Ejemplo de uso con números muy grandes
if __name__ == "__main__":
    # Descomentar para ver ejemplos automáticos
    # print("Ejemplos:")
    # print(f"123456789 × 987654321 = {multiplicar_números(123456789, 987654321)}")
    # print(f"10^100 × 10^100 = {multiplicar_números(10**100, 10**100)}")
    # print()
    
    main()