def generar_codigo(visitor):

    codigo_final = ""

    if visitor.usar_time:
        codigo_final += "import time \n\n"

    codigo_final += visitor.codigo
    codigo_final += "\nmain()\n"

    print("\n--- CODIGO GENERADO ---\n")
    
    print(codigo_final)

    with open("output_program.py","w") as f:
        f.write("---CODIGO GENERADO--- \n\n")
        f.write(codigo_final)

    with open("output.txt","w") as f:
        f.write("===CODIGO GENERADO=== \n\n")
        f.write(codigo_final)
    