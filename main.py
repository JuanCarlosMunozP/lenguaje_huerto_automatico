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

        # ====================================
        # FASE 1: ANÁLISIS LÉXICO
        # ====================================

        print("\nFASE 1: ANALISIS LEXICO")
        print("------------------------------")

        input_stream = FileStream(input_file)

        lexer = HuertoLexer(input_stream)

        stream = CommonTokenStream(lexer)

        tokens = lexer.getAllTokens()

        for i, token in enumerate(tokens,start=1):

            if token.type == -1:
                continue

            if token.type < len(lexer.symbolicNames):
                token_name = lexer.symbolicNames[token.type]
            else:
                token_name = "TOKEN"
                
            print(f"{i:4}. {token_name:<15} '{token.text}'")

        print("\n[OK] {len(tokens)} tokens generados correctamente.")
        

        # reiniciar Lexer/input
        
        input_stream = FileStream(input_file)

        lexer = HuertoLexer(input_stream)

        # ====================================
        # FASE 2: ANÁLISIS SINTÁTICO
        # ====================================

        print("\nFASE 2: ANALISIS SINTATICO")
        print("------------------------------")

        stream = CommonTokenStream(lexer)
        
        parser = HuertoParser(stream)

        tree = parser.program()

        print("\nParse Tree:\n")

        print(tree.toStringTree(recog=parser))
        
        print("\n[OK] Analisis sintatico completado.")

        
        # ====================================
        # FASE 3: ANÁLISIS SEMÁNTICO
        # ====================================

        print("\nFASE 3: ANALISIS SEMANTICO")
        print("------------------------------")

        visitor = HuertoCustomVisitor()

        visitor.visit(tree)

        for llamada in visitor.llamadas:

            if llamada not in visitor.tareas:

                raise Exception(
                    f"Error semántico: la tarea '{llamada}' fue llamada pero no está definida"
                )

        if not visitor.hay_main:

            raise Exception("Error no semántico: no se encontró la tarea obligatoria 'main()'")

        print("\n Tabla de Cultivos: \n")

        for cultivo in visitor.cultivos:
            print(f"  - {cultivo}")

        print("\n Tabla de tareas: \n")

        for tarea in visitor.tareas:
            print(f"  - {tarea}")
        
        print("\n[OK] analisis semantico completado.")

        # ====================================
        # FASE 4: GENERACIÓN DE CODIGO
        # ====================================

        print("\nFASE 4: GENERACION DE CODIGO")
        print("------------------------------")
        
        codigo_final = generar_codigo(visitor)

        print("\n Código Python generado: \n")

        print(codigo_final)

        with open("output_program.py","w") as f:

            f.write("# === CODIGO GENERADO ===\n\n")
            f.write(codigo_final)

        with open("output.txt","w") as f:

            f.write("# FASE 4 GENERACIÓN DE CODIGO PYTHON\n")
            f.write("#----------------------------------------\n\n")
            f.write(codigo_final)

    except Exception as e:

        print("\n ERROR DETECTADO: \n")

        print(e)

    
if __name__ == "__main__":
    main()

