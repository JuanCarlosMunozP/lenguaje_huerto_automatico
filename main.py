from antlr4 import * 
from gen.HuertoLexer import HuertoLexer 
from gen.HuertoParser import HuertoParser
from visitor import HuertoCustomVisitor
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

        codigo_final = ""

        if visitor.usar_time: 
            codigo_final += "import time\n\n"

        codigo_final += visitor.codigo
        codigo_final += "\nmain()\n"

        print("\n--- CODIGO GENERADO ---\n")
        print(codigo_final)

        with open("output.py","w") as f:
            f.write(codigo_final)

    except Exception as e:
        print("\n ERROR DETECTADO: \n")
        print(e)

    
if __name__ == "__main__":
    main()

