# Sistema de Gestión de Inventario
Un programa sencillo en Python que permite administrar productos desde consola.
Incluye funciones para agregar productos, mostrar el inventario y calcular estadísticas del valor total almacenado.

## Características principales
- Agregar múltiples productos
- Mostrar inventario completo en orden inverso
- Calcular el valor total del inventario
- Interfaz por consola con menú interactivo
- Validación básica de errores

## ¿Cómo funciona?
El programa es un sistema de inventario simple, que permite:
- Agregar producto
- Mostrar los productos registrados
- Calcular estadísticas del inventari
- Salir del programa
Todo funciona mediante un menú interactivo que se repite hasta que el usuario elige salir.

## Estructura del codigo
El sistema está dividido en tres funciones principales:
- agregar_producto() Pide cuántos productos agregar, Solicita nombre, precio y cantidad, Añade cada producto como diccionario dentro de inventario
- mostrar_inventario() Muestra todos los productos,  Indica si el inventario está vacío
- calcular_estadisticas() Recorre el inventario, Suma el valor total de todos los productos, Muestra los resultados
