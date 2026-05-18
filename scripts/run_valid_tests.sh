#!/bin/bash

echo "==========================================="
echo " EJECUTANDO PRUEBAS VÁLIDAS DEL COMPILADOR"
echo "==========================================="

contador = 1

for file in ../inputs/validos/*.txt
do
    echo "==================================="
    echo "PRUEBA: #$contador"
    echo "Archivo: $file"
    echo "==================================="
    
    python3 ../main.py "$file"
    
    echo ""
    echo "==================================="
    echo "FIN DE LA PRUEBA: #$contador"

    contador = $((contador + 1))
    
    sleep 10
done

echo "====================================="
echo "TODAS LAS PRUEBAS VÁLIDAS EJECUTADAS"