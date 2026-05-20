import customtkinter as ctk
from base_frame import BasePage
import core.tech_funcs as tech_funcs
from customtkinter import filedialog
from PIL import Image
import os

class ConverterMenuPage(BasePage):
    def __init__(self, parrent, controller, config, title="Converter Select Menu", navigation_back=True):
        super().__init__(
            master=parrent, 
            controller=controller,
            config=config, 
            title=title,
            navigation_back=navigation_back)
        
        self.created_pages = {}
        
        img_path = "assets\document.png"
        pil_image = Image.open(img_path)
        self.document_icon = ctk.CTkImage(light_image=pil_image, dark_image=pil_image, size=(50, 50))
        
        self.build_widgets()
        self.set_back_button(self.controller.go_back)
    
    def build_widgets(self):
        # Left Side bar
        self.sidebar_frame = ctk.CTkFrame(
            self, 
            fg_color=self.config["sidebar_color"],
            corner_radius=0)
        self.sidebar_frame.pack(fill="y", side="left")
        
        # - Navigatioin buttons
        self.create_button(self.sidebar_frame, "Change image format", lambda p="convert_image": self.switch_widget_content(p), 100, 1)
        self.create_button(self.sidebar_frame, "Change video format", None, 100, 1)
        self.create_button(self.sidebar_frame, "Change image format", None, 100, 1)
        
        # Main Content
        self.main_frame = ctk.CTkFrame(
            self, 
            fg_color=self.config["mainframe_color"])
        self.main_frame.pack(fill="both", expand=True, side="right")
    
    def switch_widget_content(self, page_key):
        for frame in self.created_pages.values():
            frame.pack_forget()
        
        if page_key not in self.created_pages:
            new_frame = ctk.CTkFrame(self.main_frame, fg_color=self.config["mainframe_color"])
            
            if page_key == "convert_image":
                self.build_convert_image_ui(new_frame)
            
            self.created_pages[page_key] = new_frame
        
        self.created_pages[page_key].pack(fill="both", expand=True)
                    
                    # == Для jpg
                    # quality   від 1 до 95. За замовчувванням - 75
                    # optimize    Якщо true - стиснення без втрати якості
                    # progressive Якщо true - зображення буде завантажуватися поступово (розмите - чітке)
                    # subsampling налаштування колірної субдискретизації (наприклад, 0 для максимальної чіткості кольорів).
                    #     0 = висока чіткість кольорів (4:4:4)
                    #     1 = середнє (4:2:2)
                    #     2 = стандартне (4:2:0)
                    
                    # == для png
                    # optimize    Якщо True, робить файл меншим за розміром.
                    # compress_level Рівень стиснення від 0 до 9 (де 9 — найменший розмір файлу, але найповільніше збереження).

    def build_convert_image_ui(self, parent):
        parent.grid_columnconfigure(0, weight=1)
        parent.grid_columnconfigure(1, weight=2)
        parent.grid_rowconfigure(0, weight=1)
        
        # Import image side (LEFT)
        self.import_side = ctk.CTkFrame(parent, fg_color=self.config["mainframe_color"])
        self.import_side.grid(row=0, column=0, sticky="nsew")
        
        self.image_display_label = ctk.CTkLabel(self.import_side, image=self.document_icon, text="")
        self.image_display_label.pack(fill="both", pady=10, anchor="center")
        
        self.image_info_label = ctk.CTkLabel(self.import_side, text="Image wasn't imported yet.", fg_color="grey")
        self.image_info_label.pack(anchor="center")
                    
        self.image_import_btn = ctk.CTkButton(self.import_side, text="Import image", command=lambda l=self.image_info_label, d=self.image_display_label: self.import_image(l, d))
        self.image_import_btn.pack(pady=10, anchor="center")
        
        # Parameters selection and formatting side (RIGHT)
        self.parameters_side = ctk.CTkFrame(parent, fg_color=self.config["sidebar_color"])
        
        self.parameters_side.grid_columnconfigure(0, weight=1)
        self.parameters_side.grid_columnconfigure(1, weight=1)
        
        self.parameters_side.grid(row=0, column=1, sticky="nsew")
        
        self.name_frame, self.name_entry = self.create_input_fields(self.parameters_side, "name", 0, 0)
        self.res_frame, self.res_entry = self.create_input_fields(self.parameters_side, "resolution", 0, 1)
    
    def import_image(self, label, display):
        file_types = [
            ("Images", "*.jpg *.png"),
            ("All files", "*.*")
        ]
        
        file_path = filedialog.askopenfilename(title="Choose the picture", filetypes=file_types)
        
        if file_path:
            print(f"File chosen: {file_path}")
            self.process_selected_image(file_path, label, display)
    
    def process_selected_image(self, path, target_label, target_display):
        pil_image = Image.open(path)
        file_name = os.path.basename(pil_image.filename)
        
        original_width, original_height = pil_image.size
        max_size = 250
        ratio = min(max_size / original_width, max_size / original_height)
        new_width = int(original_width * ratio)
        new_height = int(original_height * ratio)
        
        target_label.configure(text=f"Name: {file_name}\nFormat: {pil_image.format}\nSize: {original_width}x{original_height}")
        
        new_ctk_image = ctk.CTkImage(
            light_image=pil_image,
            dark_image=pil_image,
            size=(new_width, new_height)
        )
        
        target_display.configure(image=new_ctk_image)
        target_display.image = new_ctk_image
        
                    
                    