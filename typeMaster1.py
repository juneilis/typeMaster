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

    tituloLabel = ft.Text("Type Master", size=24, weight="bold", color="blue")
    palabraLabel = ft.Text(palabras[index], size=16)
    estadoLabel = ft.Text("", size=20)
    aciertosLabel = ft.Text("Precisión: 100.00%", size=16)
    progresoLabel = ft.Text(f"Progreso: {index}/{palabrasTotales}", size=16)

    input1 = ft.TextField(on_submit=lambda e: chequearPalabra(e, page), border_color="blue")

    def chequearPalabra(e, page):
        nonlocal index, errores
        if input1.value == palabras[index]:
            estadoLabel.value = "Correcto"
            estadoLabel.color = "green"
        else: 
            estadoLabel.value = "Incorrecto"
            estadoLabel.color = "red"
            errores +=1
            input1.focus()
        index +=1
        if index < palabrasTotales:
            palabraLabel.value = palabras[index]
            progresoLabel.value = f"Progreso: {index}/{palabrasTotales}" 
            aciertos = ((palabrasTotales - errores)/ palabrasTotales) * 100
            aciertosLabel.value = f"Precisión: {aciertos: .2f}% (Errores: {errores})" 
            input1.value = ""
            input1.focus()
        else:
            aciertos = ((palabrasTotales - errores)/ palabrasTotales) * 100
            aciertosLabel.value = f"Precisión: {aciertos: .2f}% (Errores: {errores})" 
            input1.disabled = True
        
        page.update()
        input1.focus()

    page.add(tituloLabel,palabraLabel, input1,estadoLabel, aciertosLabel, progresoLabel)

ft.app(target=main)

