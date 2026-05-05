import tkinter as tk
from tkinter import ttk, colorchooser, filedialog
from PIL import Image, ImageTk
import os

class PippidonCustomizer:
    def __init__(self, root):
        self.root = root
        self.root.title("Pippidon Customizer")

        # Set the window icon
        icon_path = "resources/app/tc.ico"  # Replace with the path to your icon file
        icon_image = ImageTk.PhotoImage(file=icon_path)
        self.root.iconphoto(False, icon_image)
        
        # Directorios
        self.base_path = "resources/base/"
        self.face_path = "resources/face/"
        self.legs_path = "resources/legs/"
        self.outfit_path = "resources/outfit/"
        self.front_path = "resources/outfit/"
        self.pet_path = "resources/pet/"
        self.hat_path = "resources/hat/"
        self.accessory_path = "resources/accessory/"

        # Inicializar variables para las imágenes
        self.base_images = {}
        self.legs_images = {}
        self.face_images = {}
        self.hat_images = {}
        self.outfit_images = {}
        self.pet_images = {}
        self.accessory_images = {}
        self.modified_images = {}

        # Inicializar variables para los accesorios seleccionados
        self.selected_face = None
        self.selected_hat = None
        self.selected_outfit = None
        self.selected_pet = None
        self.selected_accessory = None

        self.params_face = {
            "pippidonidle0@2x.png": {"position":  (76*2, 333*2), "size": (335*2, 335*2), "rotation": 0},
            "pippidonidle1@2x.png": {"position":  (75*2, 338*2), "size": (335*2, 335*2), "rotation": -1},
            "pippidonidle2@2x.png": {"position":  (76*2, 333*2), "size": (335*2, 335*2), "rotation": 0},
            "pippidonidle3@2x.png": {"position":  (75*2, 338*2), "size": (335*2, 335*2), "rotation": -1},
            "pippidonidle4@2x.png": {"position":  (76*2, 333*2), "size": (335*2, 335*2), "rotation": 0},
            "pippidonidle5@2x.png": {"position":  (75*2, 338*2), "size": (335*2, 335*2), "rotation": -1},
            "pippidonkiai0@2x.png": {"position":  (37*2, 260*2), "size": (335*2, 335*2), "rotation": 16},
            "pippidonkiai1@2x.png": {"position":  (56*2, 292*2), "size": (335*2, 335*2), "rotation": 7},
            "pippidonkiai2@2x.png": {"position":  (37*2, 260*2), "size": (335*2, 335*2), "rotation": 16},
            "pippidonkiai3@2x.png": {"position":  (56*2, 292*2), "size": (335*2, 335*2), "rotation": 7},
            "pippidonfail0@2x.png": {"position":  (76*2, 333*2), "size": (335*2, 335*2), "rotation": 0},
            "pippidonfail1@2x.png": {"position":  (75*2, 338*2), "size": (335*2, 335*2), "rotation": -1},
            "pippidonclear0@2x.png": {"position": (67*2, 275*2), "size": (335*2, 335*2), "rotation": 14},
            "pippidonclear1@2x.png": {"position": (67*2, 254*2), "size": (335*2, 335*2), "rotation": 14},
            "pippidonclear2@2x.png": {"position": (67*2, 233*2), "size": (335*2, 335*2), "rotation": 14},
            "pippidonclear3@2x.png": {"position": (67*2, 223*2), "size": (335*2, 335*2), "rotation": 14},
            "pippidonclear4@2x.png": {"position": (67*2, 213*2), "size": (335*2, 335*2), "rotation": 14},
            "pippidonclear5@2x.png": {"position": (67*2, 208*2), "size": (335*2, 335*2), "rotation": 14},
            "pippidonclear6@2x.png": {"position": (67*2, 201*2), "size": (335*2, 335*2), "rotation": 14},
        }
        
        self.params_hat = {
            "pippidonidle0@2x.png": {"position":  (76*2, 333*2), "size": (335*2, 335*2), "rotation": 0},
            "pippidonidle1@2x.png": {"position":  (75*2, 338*2), "size": (335*2, 335*2), "rotation": -1},
            "pippidonidle2@2x.png": {"position":  (76*2, 333*2), "size": (335*2, 335*2), "rotation": 0},
            "pippidonidle3@2x.png": {"position":  (75*2, 338*2), "size": (335*2, 335*2), "rotation": -1},
            "pippidonidle4@2x.png": {"position":  (76*2, 333*2), "size": (335*2, 335*2), "rotation": 0},
            "pippidonidle5@2x.png": {"position":  (75*2, 338*2), "size": (335*2, 335*2), "rotation": -1},
            "pippidonkiai0@2x.png": {"position":  (37*2, 260*2), "size": (335*2, 335*2), "rotation": 16},
            "pippidonkiai1@2x.png": {"position":  (56*2, 292*2), "size": (335*2, 335*2), "rotation": 7},
            "pippidonkiai2@2x.png": {"position":  (37*2, 260*2), "size": (335*2, 335*2), "rotation": 16},
            "pippidonkiai3@2x.png": {"position":  (56*2, 292*2), "size": (335*2, 335*2), "rotation": 7},
            "pippidonfail0@2x.png": {"position":  (76*2, 333*2), "size": (335*2, 335*2), "rotation": 0},
            "pippidonfail1@2x.png": {"position":  (75*2, 338*2), "size": (335*2, 335*2), "rotation": -1},
            "pippidonclear0@2x.png": {"position": (67*2, 275*2), "size": (335*2, 335*2), "rotation": 14},
            "pippidonclear1@2x.png": {"position": (67*2, 254*2), "size": (335*2, 335*2), "rotation": 14},
            "pippidonclear2@2x.png": {"position": (67*2, 233*2), "size": (335*2, 335*2), "rotation": 14},
            "pippidonclear3@2x.png": {"position": (67*2, 223*2), "size": (335*2, 335*2), "rotation": 14},
            "pippidonclear4@2x.png": {"position": (67*2, 213*2), "size": (335*2, 335*2), "rotation": 14},
            "pippidonclear5@2x.png": {"position": (67*2, 208*2), "size": (335*2, 335*2), "rotation": 14},
            "pippidonclear6@2x.png": {"position": (67*2, 201*2), "size": (335*2, 335*2), "rotation": 14},
        }

        self.params_outfit = {
            "pippidonidle0@2x.png":  {"position":    (0*2,    0*2), "size": (700*2, 700*2), "rotation": 0},
            "pippidonidle1@2x.png":  {"position":   (-5*2,    2*2), "size": (700*2, 700*2), "rotation": -2},
            "pippidonidle2@2x.png":  {"position":    (0*2,    0*2), "size": (700*2, 700*2), "rotation": 0},
            "pippidonidle3@2x.png":  {"position":   (-5*2,    2*2), "size": (700*2, 700*2), "rotation": -2},
            "pippidonidle4@2x.png":  {"position":    (0*2,    0*2), "size": (700*2, 700*2), "rotation": 0},
            "pippidonidle5@2x.png":  {"position":   (-5*2,    2*2), "size": (700*2, 700*2), "rotation": -2},
            "pippidonkiai0@2x.png":  {"position": (-200*2, -182*2), "size": (700*2, 700*2), "rotation": 27},
            "pippidonkiai1@2x.png":  {"position": (-151*2, -132*2), "size": (700*2, 700*2), "rotation": 18},
            "pippidonkiai2@2x.png":  {"position": (-200*2, -182*2), "size": (700*2, 700*2), "rotation": 27},
            "pippidonkiai3@2x.png":  {"position": (-151*2, -132*2), "size": (700*2, 700*2), "rotation": 18},
            "pippidonfail0@2x.png":  {"position":    (0*2,    0*2), "size": (700*2, 700*2), "rotation": 0},
            "pippidonfail1@2x.png":  {"position":   (-5*2,    2*2), "size": (700*2, 700*2), "rotation": -2},
            "pippidonclear0@2x.png": {"position":  (-83*2, -112*2), "size": (700*2, 700*2), "rotation": 13},
            "pippidonclear1@2x.png": {"position":  (-83*2, -133*2), "size": (700*2, 700*2), "rotation": 13},
            "pippidonclear2@2x.png": {"position":  (-83*2, -154*2), "size": (700*2, 700*2), "rotation": 13},
            "pippidonclear3@2x.png": {"position":  (-83*2, -164*2), "size": (700*2, 700*2), "rotation": 13},
            "pippidonclear4@2x.png": {"position":  (-83*2, -174*2), "size": (700*2, 700*2), "rotation": 13},
            "pippidonclear5@2x.png": {"position":  (-83*2, -179*2), "size": (700*2, 700*2), "rotation": 13},
            "pippidonclear6@2x.png": {"position":  (-83*2, -186*2), "size": (700*2, 700*2), "rotation": 13},
        }

        self.params_pet = {
            "pippidonidle0@2x.png": {"position":  (0*2, 503*2), "size": (170*2, 170*2), "rotation": 0},
            "pippidonidle1@2x.png": {"position":  (0*2, 496*2), "size": (170*2, 170*2), "rotation": 0},
            "pippidonidle2@2x.png": {"position":  (0*2, 503*2), "size": (170*2, 170*2), "rotation": 0},
            "pippidonidle3@2x.png": {"position":  (0*2, 496*2), "size": (170*2, 170*2), "rotation": 0},
            "pippidonidle4@2x.png": {"position":  (0*2, 503*2), "size": (170*2, 170*2), "rotation": 0},
            "pippidonidle5@2x.png": {"position":  (0*2, 496*2), "size": (170*2, 170*2), "rotation": 0},
            "pippidonkiai0@2x.png": {"position":  (0*2, 503*2), "size": (170*2, 170*2), "rotation": 0},
            "pippidonkiai1@2x.png": {"position":  (0*2, 496*2), "size": (170*2, 170*2), "rotation": 0},
            "pippidonkiai2@2x.png": {"position":  (0*2, 503*2), "size": (170*2, 170*2), "rotation": 0},
            "pippidonkiai3@2x.png": {"position":  (0*2, 496*2), "size": (170*2, 170*2), "rotation": 0},
            "pippidonfail0@2x.png": {"position":  (0*2, 503*2), "size": (170*2, 170*2), "rotation": 0},
            "pippidonfail1@2x.png": {"position":  (0*2, 496*2), "size": (170*2, 170*2), "rotation": 0},
            "pippidonclear0@2x.png": {"position": (0*2, 503*2), "size": (170*2, 170*2), "rotation": 0},
            "pippidonclear1@2x.png": {"position": (0*2, 496*2), "size": (170*2, 170*2), "rotation": 0},
            "pippidonclear2@2x.png": {"position": (0*2, 503*2), "size": (170*2, 170*2), "rotation": 0},
            "pippidonclear3@2x.png": {"position": (0*2, 496*2), "size": (170*2, 170*2), "rotation": 0},
            "pippidonclear4@2x.png": {"position": (0*2, 503*2), "size": (170*2, 170*2), "rotation": 0},
            "pippidonclear5@2x.png": {"position": (0*2, 496*2), "size": (170*2, 170*2), "rotation": 0},
            "pippidonclear6@2x.png": {"position": (0*2, 503*2), "size": (170*2, 170*2), "rotation": 0},
        }

        self.params_accessory = {
            "pippidonidle0@2x.png":  {"position":    (0*2,    0*2), "size": (700*2, 700*2), "rotation": 0},
            "pippidonidle1@2x.png":  {"position":   (-5*2,    2*2), "size": (700*2, 700*2), "rotation": -2},
            "pippidonidle2@2x.png":  {"position":    (0*2,    0*2), "size": (700*2, 700*2), "rotation": 0},
            "pippidonidle3@2x.png":  {"position":   (-5*2,    2*2), "size": (700*2, 700*2), "rotation": -2},
            "pippidonidle4@2x.png":  {"position":    (0*2,    0*2), "size": (700*2, 700*2), "rotation": 0},
            "pippidonidle5@2x.png":  {"position":   (-5*2,    2*2), "size": (700*2, 700*2), "rotation": -2},
            "pippidonkiai0@2x.png":  {"position": (-135*2, -150*2), "size": (700*2, 700*2), "rotation": 16},
            "pippidonkiai1@2x.png":  {"position":  (-60*2,  -88*2), "size": (700*2, 700*2), "rotation": 7},
            "pippidonkiai2@2x.png":  {"position": (-135*2, -150*2), "size": (700*2, 700*2), "rotation": 16},
            "pippidonkiai3@2x.png":  {"position":  (-60*2,  -88*2), "size": (700*2, 700*2), "rotation": 7},
            "pippidonfail0@2x.png":  {"position":    (0*2,    0*2), "size": (700*2, 700*2), "rotation": 0},
            "pippidonfail1@2x.png":  {"position":   (-5*2,    2*2), "size": (700*2, 700*2), "rotation": -2},
            "pippidonclear0@2x.png": {"position":  (-90*2, -125*2), "size": (700*2, 700*2), "rotation": 13},
            "pippidonclear1@2x.png": {"position":  (-90*2, -146*2), "size": (700*2, 700*2), "rotation": 13},
            "pippidonclear2@2x.png": {"position":  (-90*2, -167*2), "size": (700*2, 700*2), "rotation": 13},
            "pippidonclear3@2x.png": {"position":  (-90*2, -177*2), "size": (700*2, 700*2), "rotation": 13},
            "pippidonclear4@2x.png": {"position":  (-90*2, -187*2), "size": (700*2, 700*2), "rotation": 13},
            "pippidonclear5@2x.png": {"position":  (-90*2, -192*2), "size": (700*2, 700*2), "rotation": 13},
            "pippidonclear6@2x.png": {"position":  (-90*2, -199*2), "size": (700*2, 700*2), "rotation": 13},
        }

        # Marco izquierdo (Vista previa)
        self.preview_frame = tk.Frame(root)
        self.preview_frame.pack(side=tk.LEFT, padx=10, pady=10)
        
        self.canvas = tk.Canvas(self.preview_frame, width=600, height=500, bg="white")
        self.canvas.pack()
        
        # Marco derecho (Opciones)
        self.options_frame = tk.Frame(root)
        self.options_frame.pack(side=tk.RIGHT, padx=10, pady=10, anchor="n")
        
        self.notebook = ttk.Notebook(self.options_frame)
        self.notebook.pack(side=tk.TOP, fill=tk.X)
        
        # Crear pestañas para personalización
        self.tabs = {}
        for category in ["Body", "Face", "Hat", "Outfit", "Pet", "Accessory", "Info"]:  # Agregar "Info"
            frame = tk.Frame(self.notebook)
            self.notebook.add(frame, text=category)
            self.tabs[category] = frame

        # Controles de color para el cuerpo, cara y borde en la misma pestaña
        self.body_color = "#6ac1c1"
        self.face_color = "#fc4729"
        self.border_color = "#faf1d9"

        # Agregar contenido a la pestaña "Info"
        if "Info" in self.tabs:
            info_label = tk.Label(self.tabs["Info"], text="Made by lanelanelane\ndiscord:lanelanelane\ngmail:pm04034@gmail.com\nforked by h3oCharles\nosu!: h3oCharles", font=("Arial", 20), justify="center")
            info_label.pack(pady=20)
        
        # Crear botones de color para el cuerpo, cara y borde
        if "Body" in self.tabs:
            tk.Label(self.tabs["Body"], text="Body Color:").pack()
            self.body_color_button = tk.Button(self.tabs["Body"], bg=self.body_color, width=10, command=self.change_body_color)
            self.body_color_button.pack()
            
            tk.Label(self.tabs["Body"], text="Face Color:").pack()
            self.face_color_button = tk.Button(self.tabs["Body"], bg=self.face_color, width=10, command=self.change_face_color)
            self.face_color_button.pack()
            
            tk.Label(self.tabs["Body"], text="Border Color:").pack()
            self.border_color_button = tk.Button(self.tabs["Body"], bg=self.border_color, width=10, command=self.change_border_color)
            self.border_color_button.pack()

            # Botón para restablecer colores
            reset_colors_button = tk.Button(self.tabs["Body"], text="Reset Colors", command=self.reset_colors)
            reset_colors_button.pack(pady=10)
        
        # Mostrar miniaturas en las pestañas
        self.display_face_options()
        self.display_hat_options()
        self.display_outfit_options()
        self.display_pet_options()
        self.display_accessory_options()

        # Botón de Save Pippidon
        self.save_button = tk.Button(self.options_frame, text="Save Pippidon", command=self.save_customized_sprites)
        self.save_button.pack(pady=10)

         # Cargar imágenes de los directorios
        self.load_base_images()
        self.load_legs_images()
        self.load_face_images()
        self.load_hat_images()
        self.load_outfit_images()
        self.load_pet_images()
        self.load_accessory_images()
        
        # Imagen actual
        self.update_preview()

    def reset_colors(self):
        self.body_color = "#6ac1c1"
        self.face_color = "#fc4729"
        self.border_color = "#faf1d9"
        self.body_color_button.config(bg=self.body_color)
        self.face_color_button.config(bg=self.face_color)
        self.border_color_button.config(bg=self.border_color)
        self.update_preview()

    def remove_face(self):
        self.selected_face = None
        self.update_preview()

    def remove_hat(self):
        self.selected_hat = None
        self.update_preview()

    def remove_outfit(self):
        self.selected_outfit = None
        self.update_preview()

    def remove_pet(self):
        self.selected_pet = None
        self.update_preview()

    def remove_accessory(self):
        self.selected_accessory = None
        self.update_preview()

    def apply_color_change(self, image, target_color, new_color):
        image = image.convert("RGBA")
        data = image.getdata()
        new_data = []
        
        target_color = tuple(int(target_color[i:i+2], 16) for i in (1, 3, 5))
        new_color = tuple(int(new_color[i:i+2], 16) for i in (1, 3, 5))
        
        for item in data:
            #   
            if abs(item[0] - target_color[0]) < 60 and abs(item[1] - target_color[1]) < 60 and abs(item[2] - target_color[2]) < 60:
                new_data.append(new_color + (item[3],))
            else:
                new_data.append(item)
        
        image.putdata(new_data)
        return image
    
    def change_body_color(self):
        color = colorchooser.askcolor(title="Select the body color")[1]
        if color:
            self.body_color = color
            self.body_color_button.config(bg=color)
            self.update_preview()
    
    def change_face_color(self):
        color = colorchooser.askcolor(title="Select the face color")[1]
        if color:
            self.face_color = color
            self.face_color_button.config(bg=color)
            self.update_preview()
    
    def change_border_color(self):
        color = colorchooser.askcolor(title="Select the border color")[1]
        if color:
            self.border_color = color
            self.border_color_button.config(bg=color)
            self.update_preview()

    def display_face_options(self):
        # Crear un marco con desplazador
        canvas = tk.Canvas(self.tabs["Face"])
        scrollbar = tk.Scrollbar(self.tabs["Face"], orient="vertical", command=canvas.yview)
        scrollable_frame = tk.Frame(canvas)
    
        # Configurar el desplazador
        scrollable_frame.bind(
            "<Configure>",
            lambda e: canvas.configure(scrollregion=canvas.bbox("all"))
        )
        canvas.create_window((0, 0), window=scrollable_frame, anchor="nw")
        canvas.configure(yscrollcommand=scrollbar.set)
    
        # Empaquetar el canvas y el desplazador
        canvas.pack(side="left", fill="both", expand=True)
        scrollbar.pack(side="right", fill="y")
    
        # Crear botones en una cuadrícula
        max_columns = 5  # Número máximo de columnas por fila
        row = 0
        col = 0
    
        for file in os.listdir(self.face_path):
            if file.endswith(".png"):
                path = os.path.join(self.face_path, file)
                img_original = Image.open(path)
                img_preview = img_original.resize((50, 50))
                img_tk = ImageTk.PhotoImage(img_preview)
    
                self.face_images[file] = img_original
                btn = tk.Button(scrollable_frame, image=img_tk, command=lambda f=file: self.select_face(f))
                btn.image = img_tk
                btn.grid(row=row, column=col, padx=5, pady=5)
    
                col += 1
                if col >= max_columns:  # Si alcanzamos el número máximo de columnas, pasamos a la siguiente fila
                    col = 0
                    row += 1
        # Botón para quitar el objeto de "Face"
        remove_face_button = tk.Button(self.tabs["Face"], text="❌", command=self.remove_face)
        remove_face_button.pack(pady=10)

    def display_hat_options(self):
        # Crear un marco con desplazador
        canvas = tk.Canvas(self.tabs["Hat"])
        scrollbar = tk.Scrollbar(self.tabs["Hat"], orient="vertical", command=canvas.yview)
        scrollable_frame = tk.Frame(canvas)
    
        # Configurar el desplazador
        scrollable_frame.bind(
            "<Configure>",
            lambda e: canvas.configure(scrollregion=canvas.bbox("all"))
        )
        canvas.create_window((0, 0), window=scrollable_frame, anchor="nw")
        canvas.configure(yscrollcommand=scrollbar.set)
    
        # Empaquetar el canvas y el desplazador
        canvas.pack(side="left", fill="both", expand=True)
        scrollbar.pack(side="right", fill="y")
    
        # Crear botones en una cuadrícula
        max_columns = 5  # Número máximo de columnas por fila
        row = 0
        col = 0
    
        for file in os.listdir(self.hat_path):
            if file.endswith(".png"):
                path = os.path.join(self.hat_path, file)
                img_original = Image.open(path)
                img_preview = img_original.resize((50, 50))
                img_tk = ImageTk.PhotoImage(img_preview)
    
                self.hat_images[file] = img_original
                btn = tk.Button(scrollable_frame, image=img_tk, command=lambda f=file: self.select_hat(f))
                btn.image = img_tk
                btn.grid(row=row, column=col, padx=5, pady=5)
    
                col += 1
                if col >= max_columns:  # Si alcanzamos el número máximo de columnas, pasamos a la siguiente fila
                    col = 0
                    row += 1
        # Botón para quitar el objeto de "Hat"
        remove_hat_button = tk.Button(self.tabs["Hat"], text="❌", command=self.remove_hat)
        remove_hat_button.pack(pady=10)

    def display_outfit_options(self):
        # Crear un marco con desplazador
        canvas = tk.Canvas(self.tabs["Outfit"])
        scrollbar = tk.Scrollbar(self.tabs["Outfit"], orient="vertical", command=canvas.yview)
        scrollable_frame = tk.Frame(canvas)
    
        # Configurar el desplazador
        scrollable_frame.bind(
            "<Configure>",
            lambda e: canvas.configure(scrollregion=canvas.bbox("all"))
        )
        canvas.create_window((0, 0), window=scrollable_frame, anchor="nw")
        canvas.configure(yscrollcommand=scrollbar.set)
    
        # Empaquetar el canvas y el desplazador
        canvas.pack(side="left", fill="both", expand=True)
        scrollbar.pack(side="right", fill="y")
    
        # Crear botones en una cuadrícula
        max_columns = 5  # Número máximo de columnas por fila
        row = 0
        col = 0
    
        for file in os.listdir(self.outfit_path):
            if file.endswith(".png"):
                path = os.path.join(self.outfit_path, file)
                img_original = Image.open(path)
                img_preview = img_original.resize((50, 50))
                img_tk = ImageTk.PhotoImage(img_preview)
    
                self.outfit_images[file] = img_original
                btn = tk.Button(scrollable_frame, image=img_tk, command=lambda f=file: self.select_outfit(f))
                btn.image = img_tk
                btn.grid(row=row, column=col, padx=5, pady=5)
    
                col += 1
                if col >= max_columns:  # Si alcanzamos el número máximo de columnas, pasamos a la siguiente fila
                    col = 0
                    row += 1
        # Botón para quitar el objeto de "Outfit"
        remove_outfit_button = tk.Button(self.tabs["Outfit"], text="❌", command=self.remove_outfit)
        remove_outfit_button.pack(pady=10)

    def display_pet_options(self):
        # Crear un marco con desplazador
        canvas = tk.Canvas(self.tabs["Pet"])
        scrollbar = tk.Scrollbar(self.tabs["Pet"], orient="vertical", command=canvas.yview)
        scrollable_frame = tk.Frame(canvas)
    
        # Configurar el desplazador
        scrollable_frame.bind(
            "<Configure>",
            lambda e: canvas.configure(scrollregion=canvas.bbox("all"))
        )
        canvas.create_window((0, 0), window=scrollable_frame, anchor="nw")
        canvas.configure(yscrollcommand=scrollbar.set)
    
        # Empaquetar el canvas y el desplazador
        canvas.pack(side="left", fill="both", expand=True)
        scrollbar.pack(side="right", fill="y")
    
        # Crear botones en una cuadrícula
        max_columns = 5  # Número máximo de columnas por fila
        row = 0
        col = 0
    
        for file in os.listdir(self.pet_path):
            if file.endswith(".png"):
                path = os.path.join(self.pet_path, file)
                img_original = Image.open(path)
                img_preview = img_original.resize((50, 50))
                img_tk = ImageTk.PhotoImage(img_preview)
    
                self.pet_images[file] = img_original
                btn = tk.Button(scrollable_frame, image=img_tk, command=lambda f=file: self.select_pet(f))
                btn.image = img_tk
                btn.grid(row=row, column=col, padx=5, pady=5)
    
                col += 1
                if col >= max_columns:  # Si alcanzamos el número máximo de columnas, pasamos a la siguiente fila
                    col = 0
                    row += 1
        # Botón para quitar el objeto de "Pet"
        remove_pet_button = tk.Button(self.tabs["Pet"], text="❌", command=self.remove_pet)
        remove_pet_button.pack(pady=10)

    def display_accessory_options(self):
        # Crear un marco con desplazador
        canvas = tk.Canvas(self.tabs["Accessory"])
        scrollbar = tk.Scrollbar(self.tabs["Accessory"], orient="vertical", command=canvas.yview)
        scrollable_frame = tk.Frame(canvas)
    
        # Configurar el desplazador
        scrollable_frame.bind(
            "<Configure>",
            lambda e: canvas.configure(scrollregion=canvas.bbox("all"))
        )
        canvas.create_window((0, 0), window=scrollable_frame, anchor="nw")
        canvas.configure(yscrollcommand=scrollbar.set)
    
        # Empaquetar el canvas y el desplazador
        canvas.pack(side="left", fill="both", expand=True)
        scrollbar.pack(side="right", fill="y")
    
        # Crear botones en una cuadrícula
        max_columns = 5  # Número máximo de columnas por fila
        row = 0
        col = 0
    
        for file in os.listdir(self.accessory_path):
            if file.endswith(".png"):
                path = os.path.join(self.accessory_path, file)
                img_original = Image.open(path)
                img_preview = img_original.resize((50, 50))
                img_tk = ImageTk.PhotoImage(img_preview)
    
                self.accessory_images[file] = img_original
                btn = tk.Button(scrollable_frame, image=img_tk, command=lambda f=file: self.select_accessory(f))
                btn.image = img_tk
                btn.grid(row=row, column=col, padx=5, pady=5)
    
                col += 1
                if col >= max_columns:  # Si alcanzamos el número máximo de columnas, pasamos a la siguiente fila
                    col = 0
                    row += 1
        # Botón para quitar el objeto de "Accessory"
        remove_accessory_button = tk.Button(self.tabs["Accessory"], text="❌", command=self.remove_accessory)
        remove_accessory_button.pack(pady=10)
        
    def select_face(self, face_file):
        self.selected_face = self.face_images.get(face_file)
        self.update_preview()

    def select_hat(self, hat_file):
        self.selected_hat = self.hat_images.get(hat_file)
        self.update_preview()

    def select_outfit(self, outfit_file):
        self.selected_outfit = self.outfit_images.get(outfit_file)
        self.update_preview()

    def select_pet(self, pet_file):
        self.selected_pet = self.pet_images.get(pet_file)
        self.update_preview()
        
    def select_accessory(self, accessory_file):
        self.selected_accessory = self.accessory_images.get(accessory_file)
        self.update_preview()

    def load_base_images(self):
        for file in os.listdir(self.base_path):
            if file.endswith(".png"):
                path = os.path.join(self.base_path, file)
                self.base_images[file] = Image.open(path).convert("RGBA")

    def load_legs_images(self):
        for file in os.listdir(self.legs_path):
            if file.endswith(".png"):
                path = os.path.join(self.legs_path, file)
                self.legs_images[file] = Image.open(path).convert("RGBA")

    def load_face_images(self):
        for file in os.listdir(self.face_path):
            if file.endswith(".png"):
                path = os.path.join(self.face_path, file)
                self.face_images[file] = Image.open(path).convert("RGBA")
            
    def load_hat_images(self):
        for file in os.listdir(self.hat_path):
            if file.endswith(".png"):
                path = os.path.join(self.hat_path, file)
                self.hat_images[file] = Image.open(path).convert("RGBA")

    def load_outfit_images(self):
        for file in os.listdir(self.front_path):
            if file.endswith(".png"):
                path = os.path.join(self.front_path, file)
                self.outfit_images[file] = Image.open(path).convert("RGBA")

    def load_pet_images(self):
        for file in os.listdir(self.pet_path):
            if file.endswith(".png"):
                path = os.path.join(self.pet_path, file)
                self.pet_images[file] = Image.open(path).convert("RGBA")

    def load_accessory_images(self):
        for file in os.listdir(self.accessory_path):
            if file.endswith(".png"):
                path = os.path.join(self.accessory_path, file)
                self.accessory_images[file] = Image.open(path).convert("RGBA")
    
    def update_preview(self):
        # Parámetros predeterminados para los accesorios
        face_params = self.params_face
        hat_params = self.params_hat
        outfit_params = self.params_outfit
        pet_params = self.params_pet
        accessory_params = self.params_accessory
    
        # Trabajar solo con el sprite de previsualización
        filename = "pippidonidle0@2x.png"
        if filename in self.base_images:
            img = self.base_images[filename]
            modified_img = img.copy()
            modified_img = self.apply_color_change(modified_img, "#6ac1c1", self.body_color)
            modified_img = self.apply_color_change(modified_img, "#fc4729", self.face_color)
            modified_img = self.apply_color_change(modified_img, "#faf1d9", self.border_color)
    
            # Aplicar "Outfit"
            if self.selected_outfit:
                params = outfit_params.get(filename, {"position": (0, 0), "size": (50, 50), "rotation": 0})
                position = params["position"]
                size = params["size"]
                rotation = params["rotation"]
                accessory = self.selected_outfit.resize(size).rotate(rotation, expand=True)
                modified_img.paste(accessory, position, accessory)

            # Aplicar "Accessory"
            if self.selected_accessory:
                params = accessory_params.get(filename, {"position": (0, 0), "size": (50, 50), "rotation": 0})
                position = params["position"]
                size = params["size"]
                rotation = params["rotation"]
                accessory = self.selected_accessory.resize(size).rotate(rotation, expand=True)
                modified_img.paste(accessory, position, accessory)

            # Aplicar "Face"
            if self.selected_face:
                params = face_params.get(filename, {"position": (0, 0), "size": (50, 50), "rotation": 0})
                position = params["position"]
                size = params["size"]
                rotation = params["rotation"]
                accessory = self.selected_face.resize(size).rotate(rotation, expand=True)
                modified_img.paste(accessory, position, accessory)
    
            # Aplicar "Hat"
            if self.selected_hat:
                params = hat_params.get(filename, {"position": (0, 0), "size": (50, 50), "rotation": 0})
                position = params["position"]
                size = params["size"]
                rotation = params["rotation"]
                accessory = self.selected_hat.resize(size).rotate(rotation, expand=True)
                modified_img.paste(accessory, position, accessory)

            # Agregar las piernas si están disponibles
            if filename in self.legs_images:
                legs_img = self.legs_images[filename]
                legs_img = self.apply_color_change(legs_img, "#faf1d9", self.border_color)
                modified_img.paste(legs_img, (0, 0), legs_img)  # Pegar en la posición original
    
            # Aplicar "Pet" (renderizar después de las piernas)
            if self.selected_pet:
                params = pet_params.get(filename, {"position": (0, 0), "size": (50, 50), "rotation": 0})
                position = params["position"]
                size = params["size"]
                rotation = params["rotation"]
                accessory = self.selected_pet.resize(size).rotate(rotation, expand=True)
                modified_img.paste(accessory, position, accessory)
    
            # Actualizar la previsualización
            preview_img = modified_img.resize((int(modified_img.width / 2), int(modified_img.height / 2)))
            img_tk = ImageTk.PhotoImage(preview_img)
            self.canvas.create_image(450, 140, image=img_tk)
            self.canvas.image = img_tk
        else:
            # Manejar el caso en el que el archivo no esté en self.base_images
            print(f"Warning: {filename} is not found in the base images.")
    
    def save_customized_sprites(self):
        # Aplicar los cambios a todos los sprites antes de Save Pippidon
        self.apply_changes_to_all_sprites()

        folder_selected = filedialog.askdirectory()
        if not folder_selected:
            return
        for filename, image in self.modified_images.items():
            image.save(os.path.join(folder_selected, filename))

    def apply_changes_to_all_sprites(self):
        # Parámetros predeterminados para los accesorios
        face_params = self.params_face
        hat_params = self.params_hat
        outfit_params = self.params_outfit
        pet_params = self.params_pet
        accessory_params = self.params_accessory
    
        for filename, img in self.base_images.items():
            modified_img = img.copy()
            modified_img = self.apply_color_change(modified_img, "#6ac1c1", self.body_color)
            modified_img = self.apply_color_change(modified_img, "#fc4729", self.face_color)
            modified_img = self.apply_color_change(modified_img, "#faf1d9", self.border_color)

             # Aplicar "Outfit"
            if self.selected_outfit:
                params = outfit_params.get(filename, {"position": (0, 0), "size": (50, 50), "rotation": 0})
                position = params["position"]
                size = params["size"]
                rotation = params["rotation"]
                accessory = self.selected_outfit.resize(size).rotate(rotation, expand=True)
                modified_img.paste(accessory, position, accessory)

            # Aplicar "Accessory"
            if self.selected_accessory:
                params = accessory_params.get(filename, {"position": (0, 0), "size": (50, 50), "rotation": 0})
                position = params["position"]
                size = params["size"]
                rotation = params["rotation"]
                accessory = self.selected_accessory.resize(size).rotate(rotation, expand=True)
                modified_img.paste(accessory, position, accessory)

            # Aplicar "Face"
            if self.selected_face:
                params = face_params.get(filename, {"position": (0, 0), "size": (50, 50), "rotation": 0})
                position = params["position"]
                size = params["size"]
                rotation = params["rotation"]
                accessory = self.selected_face.resize(size).rotate(rotation, expand=True)
                modified_img.paste(accessory, position, accessory)
    
            # Aplicar "Hat"
            if self.selected_hat:
                params = hat_params.get(filename, {"position": (0, 0), "size": (50, 50), "rotation": 0})
                position = params["position"]
                size = params["size"]
                rotation = params["rotation"]
                accessory = self.selected_hat.resize(size).rotate(rotation, expand=True)
                modified_img.paste(accessory, position, accessory)

             # Agregar las piernas si están disponibles (renderizar primero)
            if filename in self.legs_images:
                legs_img = self.legs_images[filename]
                legs_img = self.apply_color_change(legs_img, "#faf1d9", self.border_color)
                modified_img.paste(legs_img, (0, 0), legs_img)  # Pegar en la posición original

            # Aplicar "Pet" (renderizar después de las piernas)
            if self.selected_pet:
                params = pet_params.get(filename, {"position": (0, 0), "size": (50, 50), "rotation": 0})
                position = params["position"]
                size = params["size"]
                rotation = params["rotation"]
                accessory = self.selected_pet.resize(size).rotate(rotation, expand=True)
                modified_img.paste(accessory, position, accessory)

    
            # Save Pippidon la imagen modificada
            self.modified_images[filename] = modified_img

if __name__ == "__main__":
    root = tk.Tk()
    app = PippidonCustomizer(root)
    root.mainloop()
