# Cálculadora
# Johan Danilo Gómez Bocanegra

# importando librerías
from tkinter import *
import tkinter as tk
from tkinter import ttk
from tkinter import messagebox

def init_window():
    """
    Crea interfaz gráfica.
    """
    # Crear ventana o raíz
    window = tk.Tk()
    window.title("Mi primera aplicacion")
    window.config(bg="gray")
    window.geometry("500x250")

    # Crear título
    label = tk.Label(window, text="Calculadora", font=("Arial bold", 15), bg="gray")
    label.grid(row=0, column=0)

    # Agregar dos campos de texto
    Uresultado2 = StringVar()
    Uresultado3 = StringVar()
    entrada1 = tk.Entry(window, width=10, textvariable=Uresultado2)
    entrada2 = tk.Entry(window, width=10, textvariable=Uresultado3)
    entrada1.grid(row=1, column=1)
    entrada2.grid(row=2, column=1)

    # Texto de entrada1 y entrada2
    label_entrada1 = tk.Label(window, text="Ingrese primer numero", bg="gray", font=("Arial bold", 10))
    label_entrada2 = tk.Label(window, text="Ingrese segundo numero", bg="gray", font=("Arial bold", 10))
    label_entrada1.grid(row=1, column=0)
    label_entrada2.grid(row=2, column=0)

    # Crear etiqueta para el seleccionadox (combobox)
    label_operador = tk.Label(window, text="Escoja un operador", bg="gray", font=("Arial bold", 10))
    label_operador.grid(row=3, column=0)

    # Crear un seleccionador (combobox)
    combo_operadores = ttk.Combobox(window)
    # Asignar los valores del seleccionador a traves de su atributo values
    combo_operadores["values"] = ["+", "-", "*", "/", "pow"]
    # Asignar por defecto una opción seleccionada: 0 es el índice de los valores
    combo_operadores.current(0)
    # Ubicar el seleccionador
    combo_operadores.grid(row=3, column=1)

    # agregar etiqueta para mostrar el resultado de la operación en pantalla
    label_resultado = tk.Label(window, text="Resultado", bg="gray", font=("Arial bold", 15))
    label_resultado.grid(row=6, column=0, sticky="s")

    # Boton calcular
    boton = tk.Button(window, command=lambda: click_calcular(label_resultado, entrada1.get(), entrada2.get(), combo_operadores.get(), Uresultado), text="Calcular", bg="purple", fg="white")
    boton.grid(row=4, column=1)

    # Radio botones para selecionar el tema
    select = IntVar()
    rad1 = tk.Radiobutton(window, text="Tema 1", bg="gray", value=1, variable=select)
    rad2 = tk.Radiobutton(window, text="Tema 2", bg="gray", value=2, variable=select)
    rad3 = tk.Radiobutton(window, text="Tema 3", bg="gray", value=3, variable=select)
    rad1.grid(row=1, column=3, padx=20)
    rad2.grid(row=2, column=3, padx=20)
    rad3.grid(row=3, column=3, padx=20)

    # Boton cambiar tema
    boton_tema = tk.Button(window, text="Cambiar", command=lambda: cambiar_tema(select.get(), window, label, label_entrada1, label_entrada2, label_operador, label_resultado, rad1, rad2, rad3, boton_check1))
    boton_tema.grid(row=4, column=3)

    # Checkbutton para usar el último valor obtenido en el resultado
    val_check = BooleanVar()
    val_check.set(False)
    boton_check1 = Checkbutton(window, text="Ultimo resultado", bg="gray", var=val_check) 
    boton_check1.grid(row=5, column=1)

    # Botones para usar último resultado
    Uresultado = StringVar()
    boton_check2 = Button(window, text="Resultado", command=lambda:poner_ultimo_resultado(val_check.get(), Uresultado2, Uresultado))
    boton_check3 = Button(window, text="Resultado", command=lambda:poner_ultimo_resultado(val_check.get(), Uresultado3, Uresultado))
    boton_check2.grid(row=1, column=2)
    boton_check3.grid(row=2, column=2)

    # Hacer que el programa esté a la escucha del usuario
    window.mainloop()

def poner_ultimo_resultado(val_check, entrada, Uresultado):
    """
    Pone el último resultado obtenido en algún entry.
    :param BooleanVar val_check: Estado (True | False) del boton "boton_check1".
    :param StringVar entrada: Variable asociada al entry a modificar.
    :param StringVar Uresultado: Último resultado obtenido.
    """
    if val_check:
        # Ajustando el último valor de resultado en el Entry seleccionado
        entrada.set(Uresultado.get())

def cambiar_tema(tema, window, label, label_entrada1, label_entrada2, label_operador, label_resultado, rad1, rad2, rad3, boton_check1):
    """
    Cambia el tema o color de la interfaz.
    :param int tema: Color de la interfaz (1 a 3).
    :param Tk window: Raíz.
    :param Label label: Label de título.
    :param Label label_entrada1: Label descripción entry1.
    :param Label label_entrada2: Label descripción entry2.
    :param Label label_operador: Label descripción combobox.
    :param Label label_resultado: Label del resultado.
    :param Radiobutton rad1: Radiobutton "tema 1".
    :param Radiobutton rad2: Radiobutton "tema 2".
    :param Radiobutton rad3: Radiobutton "tema 3".
    :param Checkbutton boton_check1: Checkbutton de "último resultado".
    """
    if tema == 1:
        # Tema 1
        window.config(bg="white")
        label.config(bg="white", fg="black")
        label_entrada1.config(bg="white", fg="black")
        label_entrada2.config(bg="white", fg="black")
        label_operador.config(bg="white", fg="black")
        label_resultado.config(bg="white", fg="black")
        rad1.config(bg="white", fg="black")
        rad2.config(bg="white", fg="black")
        rad3.config(bg="white", fg="black")
        boton_check1.config(bg="white")
    elif tema == 2:
        # Tema 2
        window.config(bg="gray")
        label.config(bg="gray", fg="black")
        label_entrada1.config(bg="gray", fg="black")
        label_entrada2.config(bg="gray", fg="black")
        label_operador.config(bg="gray", fg="black")
        label_resultado.config(bg="gray", fg="black")
        rad1.config(bg="gray", fg="black")
        rad2.config(bg="gray", fg="black")
        rad3.config(bg="gray", fg="black")
        boton_check1.config(bg="gray")
    else:
        # Tema 3
        window.config(bg="#5BBEB3")
        label.config(bg="#5BBEB3", fg="black")
        label_entrada1.config(bg="#5BBEB3", fg="black")
        label_entrada2.config(bg="#5BBEB3", fg="black")
        label_operador.config(bg="#5BBEB3", fg="black")
        label_resultado.config(bg="#5BBEB3", fg="black")
        rad1.config(bg="#5BBEB3")
        rad2.config(bg="#5BBEB3")
        rad3.config(bg="#5BBEB3")
        boton_check1.config(bg="#5BBEB3")

def calculadora(num1, num2, operador):
    """
    Calcula el resultado de una operación determinada y saber si fue exitosa.
    :param float num1:
    :param float num2:
    :param str operador:
    :return: int, True | False.
    """
    if operador == "+":
        resultado = num1+num2
    elif operador == "-":
        resultado = num1-num2
    elif operador == "*":
        resultado = num1*num2
    elif operador == "/":
        if num2 == 0:
            # Generando un mensaje de error de división entre cero
            mensaje = messagebox.showerror("Error matemático", "La división entre cero no es posible")
            return 0, False
        resultado = round(num1/num2, 2)
    else:
        resultado = num1**num2
    return resultado, True

def click_calcular(label, num1, num2, operador, Uresultado):
    """
    Ajusta el resultado en el label en el label.
    :param Label label: Label del resultado.
    :param str num1: Valor en entry 1.
    :param str num2: Valor en entry 2.
    :param str operador: Operador de combobox.
    :param StringVar Uresultado: Resultado de operación.
    """
    # Conversión de valores
    valor1 = float(num1)
    valor2 = float(num2)

    # Cálculo dados los valores y el operador
    res, estado = calculadora(valor1, valor2, operador)

    if estado == False:
        return
    Uresultado.set(str(res))

    # Actualización del texto en la etiqueta
    label.configure(text = "Resultado: " + str(res))

def main():
    """
    Ejecuta todo el programa.
    """
    init_window()

# Llamando función principal
main()

