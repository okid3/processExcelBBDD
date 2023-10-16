import tkinter as tk
from tkinter import ttk, filedialog


def select_file(entry):
    """Función para seleccionar un fichero y mostrar la ruta en el campo de entrada asociado."""
    file_path = filedialog.askopenfilename()
    entry.delete(0, tk.END)  # Limpia el campo de entrada
    entry.insert(0, file_path)  # Inserta la ruta del fichero seleccionado


def select_save_location(entry):
    """Función para seleccionar una ubicación y nombre de archivo para guardar y mostrar la ruta en el campo de entrada asociado."""
    file_path = filedialog.asksaveasfilename()
    entry.delete(0, tk.END)  # Limpia el campo de entrada
    entry.insert(0, file_path)  # Inserta la ruta del fichero seleccionado

def process_files(entry):
    print('hey')

def main():
    root = tk.Tk()
    var_seleccion = tk.StringVar()

    root.title("PANTALLA SELECCIÓN")

    # Creación de los labels y entradas de los ficheros
    ttk.Label(root, text="Estructura de fichero: Proveedor, CN, descr, dto, stock, PVL prov").grid(row=0, column=0, columnspan=2, pady=10, padx=10)

    for i in range(1, 16):
        ttk.Label(root, text=f"Fichero {i}").grid(row=i, column=0, pady=2)
        entry = ttk.Entry(root)
        entry.grid(row=i, column=1, padx=5)
        ttk.Button(root, text="Examinar", command=lambda e=entry: select_file(e)).grid(row=i, column=2)

    ttk.Label(root, text="Fichero DB arts").grid(row=16, column=0, pady=2)
    db_entry = ttk.Entry(root)
    db_entry.grid(row=16, column=1, padx=5)
    ttk.Button(root, text="Examinar", command=lambda: select_file(db_entry)).grid(row=16, column=2)

    ttk.Label(root, text="CN / Descr /PVL/Lab").grid(row=17, column=0, columnspan=2, pady=10)

    # Sección de criterio
    ttk.Label(root, text="Criterio").grid(row=18, column=0, pady=10)
    tk.Radiobutton(root, text="Menor dto", value=1, variable=var_seleccion).grid(row=18, column=1)
    tk.Radiobutton(root, text="Mayor dto", value=2, variable=var_seleccion).grid(row=18, column=2)
    var_seleccion.set(1)

    # Sección de ruta salida
    ttk.Label(root, text="Ruta salida").grid(row=19, column=0, pady=10)
    output_entry = ttk.Entry(root)
    output_entry.grid(row=19, column=1)
    ttk.Button(root, text="Examinar", command=lambda: select_save_location(output_entry)).grid(row=19, column=2)

    # Botón de ejecutar
    ttk.Button(root, text="Ejecutar", command=lambda e=entry: process_files(e)).grid(row=20, column=2, pady=15)

    root.mainloop()


if __name__ == "__main__":
    main()
