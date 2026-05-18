from antlr4 import *
from generated.HuertoLexer import HuertoLexer
from generated.HuertoParser import HuertoParser
from generated.HuertoVisitor import HuertoVisitor

class HuertoCustomVisitor(HuertoVisitor):

    def __init__(self):
        self.cultivos = set()
        self.tareas = set()
        self.llamadas = []
        self.hay_main = False
        self.usar_time = False
        self.codigo = ""

    # ---- CULTIVO DE TOMATE ---- 
    def visitDeclaration(self,ctx):
        nombre = ctx.ID().getText()
        self.cultivos.add(nombre)
        self.codigo += f"{nombre} = 0\n"
    
    def visitRoutine(self,ctx):
        nombre = ctx.ID().getText()
        self.tareas.add(nombre)
        
        if nombre == "main":
            self.hay_main = True 
        
        self.codigo += f"\ndef {nombre}(): \n"

        for stmt in ctx.statement():
            linea = self.visit(stmt)
            if linea:
                lineas = linea.split("\n")
                for l in lineas:
                    self.codigo += "    " + l + "\n"


    def visitCultivoAction(self,ctx):
        nombre = ctx.ID().getText()
        accion = ctx.getChild(0).getText()
        linea = ctx.start.line 
        columna = ctx.start.column

        if nombre not in self.cultivos:
            raise Exception(
                f"Error semántico (línea {linea}, columna {columna})"
                f"cultivo '{nombre}' no declarado antes de usarlo en acción"
            )

        if accion == "regar":
            return f"print('Regando {nombre}')"
        elif accion == "abonar":
            return f"print('Abonando {nombre} ')"
        elif accion == "podar":
            return f"print('Podando {nombre}')"

    def visitEsperarAction(self,ctx):

        numero = ctx.NUMBER()

        if numero is None:
            linea = ctx.start.line
            columna = ctx.start.column
            raise Exception(
                f"Error sintáctico (línea {linea}, columna {columna})"
                f"la instrucción esperar requiere un número de días"
            )

        dias = int(numero.getText())

        if dias == 0:
            raise Exception(
                f"Error semántico: (línea {linea}, columna {columna})"
                f"'esperar' no puede recibir 0 días"
            )

        self.usar_time = True
        return f"time.sleep({dias})"

    
    def visitCall(self,ctx):
        nombre = ctx.ID().getText()
        self.llamadas.append(nombre)
        return f"{nombre}()"

    def visitCondition(self,ctx):
        nombre = ctx.ID().getText()
        linea = ctx.start.line 
        columna = ctx.start.column

        if not nombre in self.cultivos:
            raise Exception(
                f"Errror semántico (línea {linea}, columna {columna}) "
                f"cultivo '{nombre}' no declarado antes de usarlo en 'regar'"
            )
        
        comp = ctx.comparator().getText()
        num = ctx.NUMBER().getText()

        return f"{nombre} {comp} {num}"

    def visitIfControl(self,ctx):
        cond = self.visit(ctx.condition())

        stmt_if = self.visit(ctx.statement(0))
        stmt_if = stmt_if.split("\n")
        
        codigo = f"if {cond}: \n"
        for linea in stmt_if:
            codigo += "    " + linea + "\n"

        if ctx.getChildCount() > 4:
            stmt_else = self.visit(ctx.statement(1))
            stmt_else = stmt_else.split("\n")

            codigo += "else:\n"
            for linea in stmt_else:
                codigo += "    " + linea + "\n"

        
        return codigo.strip()