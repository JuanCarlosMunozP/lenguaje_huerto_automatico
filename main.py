from antlr4 import * 
from antlr4.tree.Tree import TerminalNodeImpl

from generated.HuertoLexer import HuertoLexer 
from generated.HuertoParser import HuertoParser

from semantic_analyzer.visitor import HuertoCustomVisitor
from codegen.generator import generar_codigo
import sys
import os

def imprimir_arbol(node,parser,indent=0):

    espacio = "  " * indent 

    if isinstance(node,TerminalNodeImpl):

        print(f"{espacio}TerminalNodeImp: '{node.getText()}'")

    else:

        nombre_regla = type(node).__name__

        texto = node.getText()

        if len(texto):

            texto = texto[:30] + "..."

        print(f"{espacio}{nombre_regla}: '{texto}'")

        for i in range(node.getChildCount()):

            hijo = node.getChild(i)

            imprimir_arbol(hijo, parser, indent + 1)


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

        TOKENS = {
            1: "CULTIVO",
            2: "PUNTO_Y_COMA",
            3: "TAREA",
            4: "PARENTESIS_IZQ",
            5: "PARENTESIS_DER",
            6: "LLAVE_IZQ",
            7: "LLAVE_DER",
            8: "SI",
            9: "DOS_PUNTOS",
            10: "SINO",
            11: "REGAR",
            12: "ABONAR",
            13: "PODAR",
            14: "ESPERAR",
            15: "DIAS",
            16: "MENOR_QUE",
            17: "MAYOR_QUE",
            18: "IGUAL_IGUAL",
            19: "IDENTIFICADOR",
            20: "NUMERO",
            21: "ESPACIO"
        }

        for i, token in enumerate(tokens,start=1):

            if token.type == -1:
                continue

            token_name = TOKENS.get(token.type, "TOKEN")                
            print(f"{i:4}. {token_name:<20} '{token.text}'")

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

        imprimir_arbol(tree,parser)
        
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

