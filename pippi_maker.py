import tkinter as tk
from tkinter import ttk, colorchooser, filedialog
from PIL import Image, ImageTk
import os

class PippidonCustomizer:
    def __init__(self, root):
        self.root = root
        self.root.title("Pippidon Customizer")
        
        # Directories
        self.base_path = "resources/base/"
        self.face_path = "resources/face/"
        self.legs_path = "resources/legs/"
        self.outfit_path = "resources/outfit/"
        self.front_path = "resources/outfit/"
        self.pet_path = "resources/pet/"
        self.hat_path = "resources/hat/"
        self.accessory_path = "resources/accessory/"

        # Initialize variables for images
        self.base_images = {}
        self.legs_images = {}
        self.face_images = {}
        self.hat_images = {}
        self.outfit_images = {}
        self.pet_images = {}
        self.accessory_images = {}
        self.modified_images = {}

        # Initialize variables for selected accessories
        self.selected_face = None
        self.selected_hat = None
        self.selected_outfit = None
        self.selected_pet = None
        self.selected_accessory = None

        self.params_face = {
            "pippidonidle0@2x.png": {"position": (152, 666), "size": (670, 670), "rotation": 0},
            "pippidonidle1@2x.png": {"position": (150, 676), "size": (670, 670), "rotation": -1},
            "pippidonidle2@2x.png": {"position": (152, 666), "size": (670, 670), "rotation": 0},
            "pippidonidle3@2x.png": {"position": (150, 676), "size": (670, 670), "rotation": -1},
            "pippidonidle4@2x.png": {"position": (152, 666), "size": (670, 670), "rotation": 0},
            "pippidonidle5@2x.png": {"position": (150, 676), "size": (670, 670), "rotation": -1},
            "pippidonkiai0@2x.png": {"position": (74, 520), "size": (670, 670), "rotation": 16},
            "pippidonkiai1@2x.png": {"position": (112, 584), "size": (670, 670), "rotation": 7},
            "pippidonkiai2@2x.png": {"position": (74, 520), "size": (670, 670), "rotation": 16},
            "pippidonkiai3@2x.png": {"position": (112, 584), "size": (670, 670), "rotation": 7},
            "pippidonfail0@2x.png": {"position": (152, 666), "size": (670, 670), "rotation": 0},
            "pippidonfail1@2x.png": {"position": (150, 676), "size": (670, 670), "rotation": -1},
            "pippidonclear0@2x.png": {"position": (134, 550), "size": (670, 670), "rotation": 14},
            "pippidonclear1@2x.png": {"position": (134, 508), "size": (670, 670), "rotation": 14},
            "pippidonclear2@2x.png": {"position": (134, 466), "size": (670, 670), "rotation": 14},
            "pippidonclear3@2x.png": {"position": (134, 446), "size": (670, 670), "rotation": 14},
            "pippidonclear4@2x.png": {"position": (134, 426), "size": (670, 670), "rotation": 14},
            "pippidonclear5@2x.png": {"position": (134, 416), "size": (670, 670), "rotation": 14},
            "pippidonclear6@2x.png": {"position": (134, 402), "size": (670, 670), "rotation": 14},
        }
        
        self.params_hat = {
            "pippidonidle0@2x.png": {"position": (152, 666), "size": (670, 670), "rotation": 0},
            "pippidonidle1@2x.png": {"position": (150, 676), "size": (670, 670), "rotation": -1},
            "pippidonidle2@2x.png": {"position": (152, 666), "size": (670, 670), "rotation": 0},
            "pippidonidle3@2x.png": {"position": (150, 676), "size": (670, 670), "rotation": -1},
            "pippidonidle4@2x.png": {"position": (152, 666), "size": (670, 670), "rotation": 0},
            "pippidonidle5@2x.png": {"position": (150, 676), "size": (670, 670), "rotation": -1},
            "pippidonkiai0@2x.png": {"position": (74, 520), "size": (670, 670), "rotation": 16},
            "pippidonkiai1@2x.png": {"position": (112, 584), "size": (670, 670), "rotation": 7},
            "pippidonkiai2@2x.png": {"position": (74, 520), "size": (670, 670), "rotation": 16},
            "pippidonkiai3@2x.png": {"position": (112, 584), "size": (670, 670), "rotation": 7},
            "pippidonfail0@2x.png": {"position": (152, 666), "size": (670, 670), "rotation": 0},
            "pippidonfail1@2x.png": {"position": (150, 676), "size": (670, 670), "rotation": -1},
            "pippidonclear0@2x.png": {"position": (134, 550), "size": (670, 670), "rotation": 14},
            "pippidonclear1@2x.png": {"position": (134, 508), "size": (670, 670), "rotation": 14},
            "pippidonclear2@2x.png": {"position": (134, 466), "size": (670, 670), "rotation": 14},
            "pippidonclear3@2x.png": {"position": (134, 446), "size": (670, 670), "rotation": 14},
            "pippidonclear4@2x.png": {"position": (134, 426), "size": (670, 670), "rotation": 14},
            "pippidonclear5@2x.png": {"position": (134, 416), "size": (670, 670), "rotation": 14},
            "pippidonclear6@2x.png": {"position": (134, 402), "size": (670, 670), "rotation": 14},
        }

        self.params_outfit = {
            "pippidonidle0@2x.png": {"position": (152, 666), "size": (670, 670), "rotation": 0},
            "pippidonidle1@2x.png": {"position": (150, 676), "size": (670, 670), "rotation": -1},
            "pippidonidle2@2x.png": {"position": (152, 666), "size": (670, 670), "rotation": 0},
            "pippidonidle3@2x.png": {"position": (150, 676), "size": (670, 670), "rotation": -1},
            "pippidonidle4@2x.png": {"position": (152, 666), "size": (670, 670), "rotation": 0},
            "pippidonidle5@2x.png": {"position": (150, 676), "size": (670, 670), "rotation": -1},
            "pippidonkiai0@2x.png": {"position": (74, 520), "size": (670, 670), "rotation": 16},
            "pippidonkiai1@2x.png": {"position": (112, 584), "size": (670, 670), "rotation": 7},
            "pippidonkiai2@2x.png": {"position": (74, 520), "size": (670, 670), "rotation": 16},
            "pippidonkiai3@2x.png": {"position": (112, 584), "size": (670, 670), "rotation": 7},
            "pippidonfail0@2x.png": {"position": (152, 666), "size": (670, 670), "rotation": 0},
            "pippidonfail1@2x.png": {"position": (150, 676), "size": (670, 670), "rotation": -1},
            "pippidonclear0@2x.png": {"position": (134, 550), "size": (670, 670), "rotation": 14},
            "pippidonclear1@2x.png": {"position": (134, 508), "size": (670, 670), "rotation": 14},
            "pippidonclear2@2x.png": {"position": (134, 466), "size": (670, 670), "rotation": 14},
            "pippidonclear3@2x.png": {"position": (134, 446), "size": (670, 670), "rotation": 14},
            "pippidonclear4@2x.png": {"position": (134, 426), "size": (670, 670), "rotation": 14},
            "pippidonclear5@2x.png": {"position": (134, 416), "size": (670, 670), "rotation": 14},
            "pippidonclear6@2x.png": {"position": (134, 402), "size": (670, 670), "rotation": 14},
        }

        self.params_pet = {
            "pippidonidle0@2x.png": {"position": (0, 1006), "size": (340, 340), "rotation": 0},
            "pippidonidle1@2x.png": {"position": (0, 992), "size": (340, 340), "rotation": 0},
            "pippidonidle2@2x.png": {"position": (0, 1006), "size": (340, 340), "rotation": 0},
            "pippidonidle3@2x.png": {"position": (0, 992), "size": (340, 340), "rotation": 0},
            "pippidonidle4@2x.png": {"position": (0, 1006), "size": (340, 340), "rotation": 0},
            "pippidonidle5@2x.png": {"position": (0, 992), "size": (340, 340), "rotation": 0},
            "pippidonkiai0@2x.png": {"position": (0, 1006), "size": (340, 340), "rotation": 0},
            "pippidonkiai1@2x.png": {"position": (0, 992), "size": (340, 340), "rotation": 0},
            "pippidonkiai2@2x.png": {"position": (0, 1006), "size": (340, 340), "rotation": 0},
            "pippidonkiai3@2x.png": {"position": (0, 992), "size": (340, 340), "rotation": 0},
            "pippidonfail0@2x.png": {"position": (0, 1006), "size": (340, 340), "rotation": 0},
            "pippidonfail1@2x.png": {"position": (0, 992), "size": (340, 340), "rotation": 0},
            "pippidonclear0@2x.png": {"position": (0, 1006), "size": (340, 340), "rotation": 0},
            "pippidonclear1@2x.png": {"position": (0, 992), "size": (340, 340), "rotation": 0},
            "pippidonclear2@2x.png": {"position": (0, 1006), "size": (340, 340), "rotation": 0},
            "pippidonclear3@2x.png": {"position": (0, 992), "size": (340, 340), "rotation": 0},
            "pippidonclear4@2x.png": {"position": (0, 1006), "size": (340, 340), "rotation": 0},
            "pippidonclear5@2x.png": {"position": (0, 992), "size": (340, 340), "rotation": 0},
            "pippidonclear6@2x.png": {"position": (0, 1006), "size": (340, 340), "rotation": 0},
        }

        self.params_accessory = {
            "pippidonidle0@2x.png": {"position": (0, 0), "size": (1400, 1400), "rotation": 0},
            "pippidonidle1@2x.png": {"position": (-10, 4), "size": (1400, 1400), "rotation": -2},
            "pippidonidle2@2x.png": {"position": (0, 0), "size": (1400, 1400), "rotation": 0},
            "pippidonidle3@2x.png": {"position": (-10, 4), "size": (1400, 1400), "rotation": -2},
            "pippidonidle4@2x.png": {"position": (0, 0), "size": (1400, 1400), "rotation": 0},
            "pippidonidle5@2x.png": {"position": (-10, 4), "size": (1400, 1400), "rotation": -2},
            "pippidonkiai0@2x.png": {"position": (-270, -300), "size": (1400, 1400), "rotation": 16},
            "pippidonkiai1@2x.png": {"position": (-120, -176), "size": (1400, 1400), "rotation": 7},
            "pippidonkiai2@2x.png": {"position": (-270, -300), "size": (1400, 1400), "rotation": 16},
            "pippidonkiai3@2x.png": {"position": (-120, -176), "size": (1400, 1400), "rotation": 7},
            "pippidonfail0@2x.png": {"position": (0, 0), "size": (1400, 1400), "rotation": 0},
            "pippidonfail1@2x.png": {"position": (-10, 4), "size": (1400, 1400), "rotation": -2},
            "pippidonclear0@2x.png": {"position": (-180, -250), "size": (1400, 1400), "rotation": 13},
            "pippidonclear1@2x.png": {"position": (-180, -292), "size": (1400, 1400), "rotation": 13},
            "pippidonclear2@2x.png": {"position": (-180, -334), "size": (1400, 1400), "rotation": 13},
            "pippidonclear3@2x.png": {"position": (-180, -354), "size": (1400, 1400), "rotation": 13},
            "pippidonclear4@2x.png": {"position": (-180, -374), "size": (1400, 1400), "rotation": 13},
            "pippidonclear5@2x.png": {"position": (-180, -384), "size": (1400, 1400), "rotation": 13},
            "pippidonclear6@2x.png": {"position": (-180, -398), "size": (1400, 1400), "rotation": 13},
        }

        # Left frame (Preview)
        self.preview_frame = tk.Frame(root)
        self.preview_frame.pack(side=tk.LEFT, padx=10, pady=10)
        
        self.canvas = tk.Canvas(self.preview_frame, width=600, height=500, bg="white")
        self.canvas.pack()
        
        # Right frame (Options)
        self.options_frame = tk.Frame(root)
        self.options_frame.pack(side=tk.RIGHT, padx=10, pady=10, anchor="n")
        
        self.notebook = ttk.Notebook(self.options_frame)
        self.notebook.pack(side=tk.TOP, fill=tk.X)
        
        # Create tabs for customization
        self.tabs = {}
        for category in ["Body", "Face", "Hat", "Outfit", "Pet", "Accessory"]:
            frame = tk.Frame(self.notebook)
            self.notebook.add(frame, text=category)
            self.tabs[category] = frame
        
        # Color controls for body, face and border on the same tab
        self.body_color = "#6ac1c1"
        self.face_color = "#fc4729"
        self.border_color = "#faf1d9"
        
        # Create color buttons for body, face and border
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
        
        # Display thumbnails in tabs
        self.display_face_options()
        self.display_hat_options()
        self.display_outfit_options()
        self.display_pet_options()
        self.display_accessory_options()

        # Save button
        self.save_button = tk.Button(self.options_frame, text="Save", command=self.save_customized_sprites)
        self.save_button.pack(pady=10)

        # Load images from directories
        self.load_base_images()
        self.load_legs_images()
        self.load_face_images()
        self.load_hat_images()
        self.load_outfit_images()
        self.load_pet_images()
        self.load_accessory_images()
        
        # Display current preview
        self.update_preview()

    def apply_color_change(self, image, target_color, new_color):
        image = image.convert("RGBA")
        data = image.getdata()
        new_data = []
        
        target_color = tuple(int(target_color[i:i+2], 16) for i in (1, 3, 5))
        new_color = tuple(int(new_color[i:i+2], 16) for i in (1, 3, 5))
        
        for item in data:
            if abs(item[0] - target_color[0]) < 60 and abs(item[1] - target_color[1]) < 60 and abs(item[2] - target_color[2]) < 60:
                new_data.append(new_color + (item[3],))
            else:
                new_data.append(item)
        
        image.putdata(new_data)
        return image
    
    def change_body_color(self):
        color = colorchooser.askcolor(title="Select body color")[1]
        if color:
            self.body_color = color
            self.body_color_button.config(bg=color)
            self.update_preview()
    
    def change_face_color(self):
        color = colorchooser.askcolor(title="Select face color")[1]
        if color:
            self.face_color = color
            self.face_color_button.config(bg=color)
            self.update_preview()
    
    def change_border_color(self):
        color = colorchooser.askcolor(title="Select border color")[1]
        if color:
            self.border_color = color
            self.border_color_button.config(bg=color)
            self.update_preview()

    def display_face_options(self):
        # Create a frame with scrollbar
        canvas = tk.Canvas(self.tabs["Face"])
        scrollbar = tk.Scrollbar(self.tabs["Face"], orient="vertical", command=canvas.yview)
        scrollable_frame = tk.Frame(canvas)
    
        # Configure scrollbar
        scrollable_frame.bind(
            "<Configure>",
            lambda e: canvas.configure(scrollregion=canvas.bbox("all"))
        )
        canvas.create_window((0, 0), window=scrollable_frame, anchor="nw")
        canvas.configure(yscrollcommand=scrollbar.set)
    
        # Pack canvas and scrollbar
        canvas.pack(side="left", fill="both", expand=True)
        scrollbar.pack(side="right", fill="y")
    
        # Create buttons in grid
        max_columns = 5
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
                if col >= max_columns:
                    col = 0
                    row += 1

    def display_hat_options(self):
        canvas = tk.Canvas(self.tabs["Hat"])
        scrollbar = tk.Scrollbar(self.tabs["Hat"], orient="vertical", command=canvas.yview)
        scrollable_frame = tk.Frame(canvas)
    
        scrollable_frame.bind(
            "<Configure>",
            lambda e: canvas.configure(scrollregion=canvas.bbox("all"))
        )
        canvas.create_window((0, 0), window=scrollable_frame, anchor="nw")
        canvas.configure(yscrollcommand=scrollbar.set)
    
        canvas.pack(side="left", fill="both", expand=True)
        scrollbar.pack(side="right", fill="y")
    
        max_columns = 5
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
                if col >= max_columns:
                    col = 0
                    row += 1

    def display_outfit_options(self):
        canvas = tk.Canvas(self.tabs["Outfit"])
        scrollbar = tk.Scrollbar(self.tabs["Outfit"], orient="vertical", command=canvas.yview)
        scrollable_frame = tk.Frame(canvas)
    
        scrollable_frame.bind(
            "<Configure>",
            lambda e: canvas.configure(scrollregion=canvas.bbox("all"))
        )
        canvas.create_window((0, 0), window=scrollable_frame, anchor="nw")
        canvas.configure(yscrollcommand=scrollbar.set)
    
        canvas.pack(side="left", fill="both", expand=True)
        scrollbar.pack(side="right", fill="y")
    
        max_columns = 5
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
                if col >= max_columns:
                    col = 0
                    row += 1

    def display_pet_options(self):
        canvas = tk.Canvas(self.tabs["Pet"])
        scrollbar = tk.Scrollbar(self.tabs["Pet"], orient="vertical", command=canvas.yview)
        scrollable_frame = tk.Frame(canvas)
    
        scrollable_frame.bind(
            "<Configure>",
            lambda e: canvas.configure(scrollregion=canvas.bbox("all"))
        )
        canvas.create_window((0, 0), window=scrollable_frame, anchor="nw")
        canvas.configure(yscrollcommand=scrollbar.set)
    
        canvas.pack(side="left", fill="both", expand=True)
        scrollbar.pack(side="right", fill="y")
    
        max_columns = 5
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
                if col >= max_columns:
                    col = 0
                    row += 1

    def display_accessory_options(self):
        canvas = tk.Canvas(self.tabs["Accessory"])
        scrollbar = tk.Scrollbar(self.tabs["Accessory"], orient="vertical", command=canvas.yview)
        scrollable_frame = tk.Frame(canvas)
    
        scrollable_frame.bind(
            "<Configure>",
            lambda e: canvas.configure(scrollregion=canvas.bbox("all"))
        )
        canvas.create_window((0, 0), window=scrollable_frame, anchor="nw")
        canvas.configure(yscrollcommand=scrollbar.set)
    
        canvas.pack(side="left", fill="both", expand=True)
        scrollbar.pack(side="right", fill="y")
    
        max_columns = 5
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
                if col >= max_columns:
                    col = 0
                    row += 1
        
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
        face_params = self.params_face
        hat_params = self.params_hat
        outfit_params = self.params_outfit
        pet_params = self.params_pet
        accessory_params = self.params_accessory
    
        filename = "pippidonidle0@2x.png"
        if filename in self.base_images:
            img = self.base_images[filename]
            modified_img = img.copy()
            modified_img = self.apply_color_change(modified_img, "#6ac1c1", self.body_color)
            modified_img = self.apply_color_change(modified_img, "#fc4729", self.face_color)
            modified_img = self.apply_color_change(modified_img, "#faf1d9", self.border_color)
    
            # Apply "Face"
            if self.selected_face:
                params = face_params.get(filename, {"position": (0, 0), "size": (50, 50), "rotation": 0})
                position = params["position"]
                size = params["size"]
                rotation = params["rotation"]
                accessory = self.selected_face.resize(size).rotate(rotation, expand=True)
                modified_img.paste(accessory, position, accessory)
    
            # Apply "Hat"
            if self.selected_hat:
                params = hat_params.get(filename, {"position": (0, 0), "size": (50, 50), "rotation": 0})
                position = params["position"]
                size = params["size"]
                rotation = params["rotation"]
                accessory = self.selected_hat.resize(size).rotate(rotation, expand=True)
                modified_img.paste(accessory, position, accessory)
    
            # Apply "Outfit"
            if self.selected_outfit:
                params = outfit_params.get(filename, {"position": (0, 0), "size": (50, 50), "rotation": 0})
                position = params["position"]
                size = params["size"]
                rotation = params["rotation"]
                accessory = self.selected_outfit.resize(size).rotate(rotation, expand=True)
                modified_img.paste(accessory, position, accessory)

            # Apply "Accessory"
            if self.selected_accessory:
                params = accessory_params.get(filename, {"position": (0, 0), "size": (50, 50), "rotation": 0})
                position = params["position"]
                size = params["size"]
                rotation = params["rotation"]
                accessory = self.selected_accessory.resize(size).rotate(rotation, expand=True)
                modified_img.paste(accessory, position, accessory)

            # Add legs if available
            if filename in self.legs_images:
                legs_img = self.legs_images[filename]
                modified_img.paste(legs_img, (0, 0), legs_img)
    
            # Apply "Pet" (render after legs)
            if self.selected_pet:
                params = pet_params.get(filename, {"position": (0, 0), "size": (50, 50), "rotation": 0})
                position = params["position"]
                size = params["size"]
                rotation = params["rotation"]
                accessory = self.selected_pet.resize(size).rotate(rotation, expand=True)
                modified_img.paste(accessory, position, accessory)
    
            # Update preview (scale down 4x for display)
            preview_img = modified_img.resize((int(modified_img.width / 2), int(modified_img.height / 2)))
            img_tk = ImageTk.PhotoImage(preview_img)
            self.canvas.create_image(450, 140, image=img_tk)
            self.canvas.image = img_tk
        else:
            print(f"Warning: {filename} not found in base images.")
    
    def save_customized_sprites(self):
        self.apply_changes_to_all_sprites()

        folder_selected = filedialog.askdirectory()
        if not folder_selected:
            return
        for filename, image in self.modified_images.items():
            image.save(os.path.join(folder_selected, filename))

    def apply_changes_to_all_sprites(self):
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
    
            # Apply "Face"
            if self.selected_face:
                params = face_params.get(filename, {"position": (0, 0), "size": (50, 50), "rotation": 0})
                position = params["position"]
                size = params["size"]
                rotation = params["rotation"]
                accessory = self.selected_face.resize(size).rotate(rotation, expand=True)
                modified_img.paste(accessory, position, accessory)
    
            # Apply "Hat"
            if self.selected_hat:
                params = hat_params.get(filename, {"position": (0, 0), "size": (50, 50), "rotation": 0})
                position = params["position"]
                size = params["size"]
                rotation = params["rotation"]
                accessory = self.selected_hat.resize(size).rotate(rotation, expand=True)
                modified_img.paste(accessory, position, accessory)
    
            # Apply "Outfit"
            if self.selected_outfit:
                params = outfit_params.get(filename, {"position": (0, 0), "size": (50, 50), "rotation": 0})
                position = params["position"]
                size = params["size"]
                rotation = params["rotation"]
                accessory = self.selected_outfit.resize(size).rotate(rotation, expand=True)
                modified_img.paste(accessory, position, accessory)

            # Apply "Accessory"
            if self.selected_accessory:
                params = accessory_params.get(filename, {"position": (0, 0), "size": (50, 50), "rotation": 0})
                position = params["position"]
                size = params["size"]
                rotation = params["rotation"]
                accessory = self.selected_accessory.resize(size).rotate(rotation, expand=True)
                modified_img.paste(accessory, position, accessory)

            # Add legs if available (render first)
            if filename in self.legs_images:
                legs_img = self.legs_images[filename]
                modified_img.paste(legs_img, (0, 0), legs_img)

            # Apply "Pet" (render after legs)
            if self.selected_pet:
                params = pet_params.get(filename, {"position": (0, 0), "size": (50, 50), "rotation": 0})
                position = params["position"]
                size = params["size"]
                rotation = params["rotation"]
                accessory = self.selected_pet.resize(size).rotate(rotation, expand=True)
                modified_img.paste(accessory, position, accessory)

            # Save modified image
            self.modified_images[filename] = modified_img

if __name__ == "__main__":
    root = tk.Tk()
    app = PippidonCustomizer(root)
    root.mainloop()
