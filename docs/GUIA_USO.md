# Guía de uso del laboratorio

## 1. Abrir el laboratorio

Ejecutar `iniciar.bat` o iniciar `server.py` manualmente.

La pantalla principal permite seleccionar uno de los diez ejercicios.

## 2. Seleccionar un ejercicio

Al seleccionar un ejercicio se cargan:

- título;
- conceptos principales;
- parámetros modificables;
- código Python del ejercicio.

## 3. Modificar valores

Los formularios cambian según el ejercicio.

Ejemplos:

- ejercicio 2: capacidad y nombres de personas;
- ejercicio 3: dimensiones geométricas;
- ejercicio 4: saldos, ingreso, retirada y transferencia;
- ejercicio 6: precio, stock, venta y reposición;
- ejercicio 8: orden `D(B, C)` o `D(C, B)`;
- ejercicio 10: precios, envío, meses y descuento.

## 4. Ejecutar paso a paso

La ejecución interactiva devuelve:

- salida resultante;
- pasos realizados;
- explicación de por qué se produce cada cambio;
- estado relevante del objeto.

El objetivo es seguir este orden mental:

```text
1. Predecir
2. Ejecutar
3. Comparar
4. Explicar
```

## 5. Consultar el código Python

La interfaz carga el archivo `.py` correspondiente desde `ejercicios/`.

Ese código es el mismo que puede ejecutarse directamente desde la consola.

## 6. Editar el código

Antes de guardar por primera vez una modificación, el servidor genera una copia:

```text
archivo.py.bak
```

Los `.bak` son archivos de trabajo y están excluidos de Git mediante `.gitignore`.

## 7. Ejecutar el `.py` real

La opción de ejecución directa lanza el ejercicio mediante el intérprete de Python.

La ejecución está limitada a 5 segundos para evitar que un bucle infinito bloquee la herramienta.

## 8. Restaurar

Si existe una copia `.bak`, puede restaurarse desde la interfaz.

## 9. Uso recomendado para estudiar

Para cada ejercicio:

1. ejecutar con los valores por defecto;
2. explicar las clases;
3. localizar encapsulación, herencia, composición o polimorfismo;
4. modificar un valor;
5. predecir el resultado;
6. comprobarlo;
7. realizar una pequeña modificación del código;
8. volver a explicar por qué sigue funcionando o por qué cambia.
