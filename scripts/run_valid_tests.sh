#!/bin/bash

echo "=== EJECUTANDO PRUEBAS VALIDAS ==="

for file in ../inputs/validos/*.txt
do
    echo ""
    echo "Probando: $file"
    echo "-----------------------------------"
    
    python3 ../main.py "$file"
    
    echo "-----------------------------------"

    sleep 10
done

echo ""
echo "Todas las pruebas válidas ejecutadas"