#!/bin/bash

echo "=== EJECUTANDO PRUEBAS DE ERROR ==="

for file in inputs/errores/*.txt
do
    echo ""
    echo "Probando: $file"
    echo "-----------------------------------"
    
    python3 main.py "$file"
    
    echo "-----------------------------------"

    sleep 10
done

echo ""
echo "Pruebas de error finalizadas"