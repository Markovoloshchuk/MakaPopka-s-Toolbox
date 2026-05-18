import customtkinter as ctk
from base_frame import BasePage
import core.tech_funcs as tech_funcs

class HomePage(BasePage):
    def __init__(self, master, config):
        super().__init__(
            master, 
            config, title="Home Page")
        self.config = tech_funcs.load_config()
        
        self.build_widgets()
        self.build_cards()
    
    def build_widgets(self):
        self.label = ctk.CTkLabel(self, text="Home page dayo")
        self.label.pack()
        
        self.item_frame = ctk.CTkFrame(self, width=1000, fg_color=self.config["mainframe_color"])
        # self.item_frame.grid_propagate(False)
        self.item_frame.pack(fill="both", padx=20)
        
        for i in range(3):
            self.item_frame.grid_columnconfigure(i, weight=1)
        
        for i in range(2):
            self.item_frame.grid_rowconfigure(i, weight=1)
        
    def on_card_click(self, name):
        print(f"You've pressed {name} card, my congrats")
        
    def create_card(self, master, title, description, command, row, column, progress):
        card_color = ""
        if progress:
            card_color = self.config["card_in_progress"]
        else:
            card_color = self.config["card_done"]
        
        
        card = ctk.CTkFrame(
            master, 
            corner_radius=10, 
            border_width=2, 
            border_color=self.config["card_secondary_color"],
            fg_color=self.config["card_main_color"],
            cursor="hand2")
        card.grid(row=row, column=column, padx=10, pady=10, sticky="nsew")
        
        label_title = ctk.CTkLabel(
            card, 
            text=title, 
            font=tuple(self.config["card_label_font"]), 
            text_color=card_color)    
        label_title.pack(pady=(5,10), padx=15, anchor="w")
        
        label_desc = ctk.CTkLabel(
            card, 
            text=description,
            font=tuple(self.config["card_desc_font"]),
            text_color=self.config["card_secondary_color"],
            wraplength=280,
            justify="left",
            anchor="w"
            
        )
        label_desc.pack(pady=(5, 10), padx=15, anchor="w")
        
        for widget in (card, label_title, label_desc):
            widget.bind("<Button-1>", lambda e: command())
            
        return card
        
    def build_cards(self):
        data = [
            ("Media Convertion", "Formats: \n - .png -> .jpg\n - .png -> .bin\n - .bin -> .png\n - .mvp -> .mp4\n - .mkv -> .mp4 \nChange media size (res, bitrate, upscale, etc.).", lambda t="Convertion":self.on_card_click(t), True),
            ("Cipher", "Coding vatious data using DES, AES, SHA-250, etc.", self.on_card_click, True),
            ("Zip viewer", "Most obscure one. Used to view media on zip files, including mangas.", self.on_card_click, True),
            ("Mini Game", "Didn't make up my mind of what exactly there should be.", self.on_card_click, True),
            ("Drawing", "Simple drawing program with ability to post results on makaboard or export in various formats.", self.on_card_click, True),
            ("Coming soon", "Waiting for my idea generator to work...", self.on_card_click, True)
        ]
        
        columns = 3
        for index, (title, desc, command, progress) in enumerate(data):
            r = index // columns
            c = index % columns
            
            self.create_card(self.item_frame, title, desc, command, r, c, progress)
    
    