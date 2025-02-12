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