#!/bin/bash

echo "==========================================="
echo " EJECUTANDO PRUEBAS DE ERROR DEL COMPILADOR"
echo "==========================================="

contador = 1

for file in ../inputs/errores/*.txt
do
    echo "==================================="
    echo "PRUEBA: #$contador"
    echo "Archivo: $file"
    echo "==================================="
    
    python3 ../main.py "$file"
    
    echo ""
    echo "==================================="
    echo "FIN ERROR: #$contador"

    contador = $((contador + 1))
    
    sleep 10
done

echo "====================================="
echo "TODAS LAS PRUEBAS DE ERROR FINALIZARON"