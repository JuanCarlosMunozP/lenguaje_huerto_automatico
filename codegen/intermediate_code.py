def generar_tac(visitor):

    tac = []

    for cultivo in visitor.cultivos:
        tac.append(f"DECLARAR: {cultivo}")

    for tarea in visitor.tareas:
        tac.append(f"FUNCION {tarea}")

    for llamada in visitor.llamadas:
        tac.append(f"CALL {llamada}")

    return tac