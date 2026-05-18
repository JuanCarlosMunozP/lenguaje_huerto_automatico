def generar_codigo(visitor):

    codigo_final = ""

    if visitor.usar_time:
        codigo_final += "import time \n\n"

    codigo_final += visitor.codigo
    codigo_final += "\nmain()\n"

    return codigo_final