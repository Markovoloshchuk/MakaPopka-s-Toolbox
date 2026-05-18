import customtkinter as ctk

class BasePage(ctk.CTkFrame):
    def __init__(self, master, config, title="page"):
        super().__init__(
            master, 
            fg_color=config["mainframe_color"], 
            corner_radius=0)
        self.config = config
        self.title = title
        
