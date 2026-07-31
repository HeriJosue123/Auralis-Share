import tkinter as tk
from tkinter import messagebox, simpledialog
import subprocess
import os

# --- FUNCIONES LÓGICAS ---

def verificar_repo():
    """Revisa si la carpeta ya está conectada a GitHub"""
    if not os.path.exists(".git"):
        return False
    try:
        # Revisa si hay un origen configurado
        remotes = subprocess.check_output(["git", "remote"], text=True)
        if "origin" in remotes:
            return True
    except:
        pass
    return False

def configurar_repo():
    """Pide el link y configura git localmente"""
    url = simpledialog.askstring("Configurar Repositorio", "Pega aquí el enlace de tu repo de GitHub (https://...):")
    if url:
        try:
            if not os.path.exists(".git"):
                subprocess.run(["git", "init"], check=True)
            subprocess.run(["git", "remote", "add", "origin", url], check=True)
            subprocess.run(["git", "branch", "-M", "main"], check=True)
            messagebox.showinfo("¡Éxito!", "Repositorio vinculado localmente. Ya puedes subir tus archivos.")
            actualizar_archivos()
        except subprocess.CalledProcessError:
            messagebox.showerror("Error", "No se pudo configurar. Asegúrate de tener Git instalado.")

def actualizar_archivos():
    """Muestra qué archivos han cambiado o son nuevos"""
    lista_archivos.delete(0, tk.END)
    
    if not verificar_repo():
        lista_archivos.insert(tk.END, "⚠️ Repositorio no configurado aún.")
        return
        
    try:
        # Ejecuta 'git status' para ver los archivos pendientes
        status = subprocess.check_output(["git", "status", "-s"], text=True)
        if status.strip() == "":
            lista_archivos.insert(tk.END, "✅ Todo limpio. No hay cambios pendientes.")
        else:
            for linea in status.split("\n"):
                if linea.strip():
                    lista_archivos.insert(tk.END, linea)
    except:
        lista_archivos.insert(tk.END, "❌ Error al leer los archivos.")

def crear_archivo():
    """Permite crear un archivo rápido desde la app"""
    nombre = simpledialog.askstring("Nuevo Archivo", "Nombre del archivo (ej: index.html, main.py):")
    if nombre:
        with open(nombre, "w") as f:
            f.write("# Archivo creado desde tu Gestor\n")
        actualizar_archivos()
        messagebox.showinfo("Creado", f"Archivo '{nombre}' creado con éxito en la carpeta.")

def subir_a_github():
    """Sube todo a GitHub"""
    if not verificar_repo():
        # Si no hay repo, lo pide primero
        configurar_repo()
        # Si el usuario canceló, cortamos aquí
        if not verificar_repo():
            return 
            
    mensaje = entrada_mensaje.get()
    if not mensaje:
        messagebox.showwarning("Falta info", "¡Ey! Escribe un mensaje de lo que hicimos (Commit).")
        return

    try:
        subprocess.run(["git", "add", "."], check=True)
        # Hacemos commit
        subprocess.run(["git", "commit", "-m", mensaje], check=True)
        # Subimos (usamos -u para asegurar que se ancle la rama main)
        subprocess.run(["git", "push", "-u", "origin", "main"], check=True)

        messagebox.showinfo("¡Éxito!", "¡Código subido a GitHub correctamente! 🚀")
        entrada_mensaje.delete(0, tk.END)
        actualizar_archivos()
        
    except subprocess.CalledProcessError:
        messagebox.showerror("Error", "Hubo un problema al subir. ¿Seguro que hay archivos nuevos para subir?")

# --- DISEÑO DE LA PANTALLA ---
ventana = tk.Tk()
ventana.title("Gestor de GitHub 🚀")
ventana.geometry("450x550")
ventana.config(bg="#1e1e1e")

# Título
tk.Label(ventana, text="Gestor de Proyecto", font=("Arial", 16, "bold"), fg="#00ff00", bg="#1e1e1e").pack(pady=15)

# --- APARTADO DE ARCHIVOS ---
frame_archivos = tk.Frame(ventana, bg="#1e1e1e")
frame_archivos.pack(pady=10, fill="x", padx=20)

tk.Label(frame_archivos, text="Archivos con cambios pendientes:", font=("Arial", 11, "bold"), fg="white", bg="#1e1e1e").pack(anchor="w")

# Lista visual de archivos
lista_archivos = tk.Listbox(frame_archivos, height=6, bg="#2d2d2d", fg="#ffcc00", font=("Consolas", 10), selectbackground="#4CAF50")
lista_archivos.pack(fill="x", pady=5)

# Botones de archivos
frame_botones_archivos = tk.Frame(frame_archivos, bg="#1e1e1e")
frame_botones_archivos.pack(fill="x")
tk.Button(frame_botones_archivos, text="🔄 Refrescar", bg="#444", fg="white", command=actualizar_archivos).pack(side="left", padx=5)
tk.Button(frame_botones_archivos, text="📄 Crear Archivo", bg="#008cba", fg="white", command=crear_archivo).pack(side="right", padx=5)

tk.Label(ventana, text="-"*50, bg="#1e1e1e", fg="#555").pack(pady=10)

# --- APARTADO DE SUBIDA ---
tk.Label(ventana, text="¿Qué cambios hicimos hoy? (Commit):", font=("Arial", 11), fg="white", bg="#1e1e1e").pack(pady=5)
entrada_mensaje = tk.Entry(ventana, width=40, font=("Arial", 12))
entrada_mensaje.pack(pady=5)

tk.Button(ventana, text="🚀 Subir a GitHub", font=("Arial", 13, "bold"), bg="#4CAF50", fg="white", cursor="hand2", command=subir_a_github, pady=5).pack(pady=20)

# Botón extra por si quieres reconfigurar el repo a la fuerza
tk.Button(ventana, text="⚙️ Configurar/Cambiar Repo", bg="#333", fg="white", command=configurar_repo).pack(side="bottom", pady=10)

# Al abrir, revisamos qué archivos hay
actualizar_archivos()

ventana.mainloop()