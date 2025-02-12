import random
import flet as ft

def main(page: ft.Page):
    palabras = ["manzana", "banana", "cherry", "sociales", "perro", "elefante", "montaña", "casa", "isla", "limón", "oceano", "flores", "aditia", "queso", 
                "cuaderno", "tigre", "chocolate", "vainilla", "juneilis"]
    random.shuffle(palabras)
    palabras = palabras[:15]

    index = 0 
    errores = 0
    palabrasTotales = len(palabras)

    palabraLabel = ft.Text(palabras[index], size=16)
    estadoLabel = ft.Text("", size=20)
    aciertosLabel = ft.Text("Precisión: 100.00%", size=16)
    progresoLabel = ft.Text(f"Progreso: {index}/{palabrasTotales}", size=16)

    page.update()

    page.add(palabraLabel, estadoLabel, aciertosLabel, progresoLabel)

ft.app(target=main)

