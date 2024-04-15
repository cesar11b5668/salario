import mysql.connector
import tkinter as tk
import pandas as pd  # Importar Pandas (opcional)

# Definir la ventana principal
ventana = tk.Tk()
ventana.title("Registro de Salarios")

# Definir variables para almacenar datos
nombre = tk.StringVar()
puesto_trabajo = tk.StringVar()
salario = tk.StringVar()
datos = []  # Lista para almacenar datos de todos los trabajadores

# Función para agregar un nuevo trabajador
def agregar_trabajador():
    # Obtener datos de los cuadros de texto
    nombre_trabajador = nombre.get()
    puesto_trabajo_trabajador = puesto_trabajo.get()
    salario_trabajador = float(salario.get())

    # Validar entrada (opcional)
    # ...

    # Agregar datos a la lista
    datos.append({
        "Nombre": nombre_trabajador,
        "Puesto de trabajo": puesto_trabajo_trabajador,
        "Salario": salario_trabajador
    })

    # Limpiar los cuadros de texto
    nombre.set("")
    puesto_trabajo.set("")
    salario.set("")

    # Actualizar la lista de trabajadores mostrada
    actualizar_lista_trabajadores()

# Función para actualizar la lista de trabajadores mostrada
def actualizar_lista_trabajadores():
    lista_trabajadores.delete(0, tk.END)  # Borrar la lista actual
    for trabajador in datos:
        lista_trabajadores.insert(tk.END, f"{trabajador['Nombre']}: {trabajador['Puesto de trabajo']}, ${trabajador['Salario']:.2f}")

# Función para guardar datos en un archivo CSV (opcional)
def guardar_datos_csv():
    # Convertir la lista de datos a un DataFrame de Pandas
    if pd:
        df = pd.DataFrame(datos)

        # Guardar el DataFrame en un archivo CSV
        df.to_csv("datos_salarios.csv", index=False)
    else:
        print("Se requiere la librería Pandas para guardar datos en CSV. Instale Pandas para usar esta función.")
 
# Función para eliminar un trabajador
def eliminar_trabajador():
    # Obtener el índice del trabajador seleccionado en la lista
    indice_trabajador_seleccionado = lista_trabajadores.curselection()

    # Verificar si hay un trabajador seleccionado
    if not indice_trabajador_seleccionado:
        print("No hay ningún trabajador seleccionado para eliminar.")
        return

    # Obtener el índice del trabajador seleccionado
    indice_trabajador = indice_trabajador_seleccionado[0]

    # Eliminar el trabajador de la lista de datos
    del datos[indice_trabajador]

    # Actualizar la lista de trabajadores mostrada
    actualizar_lista_trabajadores()

# Función para actualizar la lista de trabajadores mostrada
def actualizar_lista_trabajadores():
    # Borrar la lista actual
    lista_trabajadores.delete(0, tk.END)

    # Agregar cada trabajador a la lista
    for indice, trabajador in enumerate(datos):
        lista_trabajadores.insert(tk.END, f"{indice+1}. {trabajador['Nombre']}: {trabajador['Puesto de trabajo']}, ${trabajador['Salario']:.2f}") 
  
# Crear etiquetas y cuadros de texto
etiqueta_nombre = tk.Label(ventana, text="Nombre:")
etiqueta_nombre.grid(row=0, column=0, padx=5, pady=5)

cuadro_texto_nombre = tk.Entry(ventana, textvariable=nombre)
cuadro_texto_nombre.grid(row=0, column=1, padx=5, pady=5)

etiqueta_puesto_trabajo = tk.Label(ventana, text="Puesto de trabajo:")
etiqueta_puesto_trabajo.grid(row=1, column=0, padx=5, pady=5)

cuadro_texto_puesto_trabajo = tk.Entry(ventana, textvariable=puesto_trabajo)
cuadro_texto_puesto_trabajo.grid(row=1, column=1, padx=5, pady=5)

etiqueta_salario = tk.Label(ventana, text="Salario:")
etiqueta_salario.grid(row=2, column=0, padx=5, pady=5)

cuadro_texto_salario = tk.Entry(ventana, textvariable=salario)
cuadro_texto_salario.grid(row=2, column=1, padx=5, pady=5)

# Crear botón para agregar trabajador
boton_agregar_trabajador = tk.Button(ventana, text="Agregar Trabajador", command=agregar_trabajador)
boton_agregar_trabajador.grid(row=3, column=0, columnspan=2, padx=5, pady=5)

# Crear lista para mostrar trabajadores
lista_trabajadores = tk.Listbox(ventana, width=30, height=10)
lista_trabajadores.grid(row=4, column=0, columnspan=2, padx=5, pady=5)

# Crear botón para eliminar trabajador
boton_eliminar_trabajador = tk.Button(ventana, text="Eliminar Trabajador", command=eliminar_trabajador)
boton_eliminar_trabajador.grid(row=6, column=0, columnspan=2, padx=5, pady=5)

# Crear botón para guardar datos en CSV
boton_guardar_csv = tk.Button(ventana, text="Guardar en CSV", command=guardar_datos_csv)
boton_guardar_csv.grid(row=5, column=0, columnspan=2, padx=5, pady=5)

# Iniciar el bucle principal de la ventana
ventana.mainloop()
