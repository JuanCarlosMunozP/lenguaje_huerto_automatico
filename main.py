from antlr4 import * 
from generated.HuertoLexer import HuertoLexer 
from generated.HuertoParser import HuertoParser

from semantic_analyzer.visitor import HuertoCustomVisitor
from codegen.generator import generar_codigo
import sys
import os

def main():

    if len(sys.argv) < 2:
        print("Uso python3 main.py <ruta/archivo_entrada>")
        print("Ejemplo: python3 main.py inputs/validos/input1.txt")
        return 

    input_file = sys.argv[1]

    if not os.path.exists(input_file):
        print(f"Error el archivo '{input_file}' no existe")
        return 

    try:

        input_stream = FileStream(input_file)

        lexer = HuertoLexer(input_stream)
        stream = CommonTokenStream(lexer)
        parser = HuertoParser(stream)

        tree = parser.program()

        visitor = HuertoCustomVisitor()
        visitor.visit(tree)

        for llamada in visitor.llamadas:
            if llamada not in visitor.tareas:
                raise Exception(f"Error semántico: la tarea '{llamada}' fue llamada pero no está definida")

        if not visitor.hay_main:
            raise Exception("Error no semántico: no se encontró la tarea obligatoria 'main()'")

        codigo_final = generar_codigo(visitor)

    except Exception as e:
        print("\n ERROR DETECTADO: \n")
        print(e)

    
if __name__ == "__main__":
    main()

