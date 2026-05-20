import customtkinter as ctk

class BasePage(ctk.CTkFrame):
    def __init__(self, master, controller, config, title="page", navigation_back=None):
        super().__init__(
            master=master, 
            fg_color=config["mainframe_color"])
        
        self.controller = controller
        self.config = config
        self.title = title
        self.navigation_back = navigation_back
        
        if navigation_back or title:
            self.sub_header_frame = ctk.CTkFrame(self, fg_color=self.config["mainframe_color"])
            self.sub_header_frame.pack(fill="x", pady=(0, 10)) 
        
        self.base_widget_builder()
        
    def base_widget_builder(self):
        if self.navigation_back:
            self.back_button = ctk.CTkButton(
                self.sub_header_frame, 
                text="<Back", 
                width=30, 
                corner_radius=10, 
                fg_color=self.config["card_main_color"], 
                text_color=self.config["card_secondary_color"],
                font=tuple(self.config["card_label_font"]),
                command=None,
                anchor="w")
            self.back_button.pack(side="left", padx=(10, 0), pady=(10, 0))
        if self.title:
            self.title_label = ctk.CTkLabel(
                self.sub_header_frame, 
                text=self.title, 
                font=tuple(self.config["general_title_font"]), 
                anchor="w",
                justify="left")
            self.title_label.pack(side="left", fill="x", padx=20, pady=(10, 0))
            
    def set_back_button(self, target):
        if self.back_button:
            self.back_button.configure(command=target)
        else:
            print(f"Warning: Back button is not initialized for {self.title_text}")
        
    def create_button(self, master, text, command, width, height):
        button = ctk.CTkButton(
            master,
            text=text,
            command=command,
            width=width,
            height=height,
            corner_radius=5,
            font=tuple(self.config["sidebar_btn_font"]),
            fg_color=self.config["sidebar_color"],
            text_color=self.config["sidebar_btn_secondary_color"],
            anchor="w",
        )
        button.pack(anchor="nw", padx=(15, 30), pady=10)
        
        return button
    
    def create_input_fields(self, parent, field_name, row, column):
        frame = ctk.CTkFrame(parent, fg_color=self.config["mainframe_color"])
        frame.grid_columnconfigure(1, weight=1)
        frame.grid(row=row, column=column, sticky="nsew", padx=20, pady=20)
        
        label = ctk.CTkLabel(frame, text=field_name, font=tuple(self.config["sidebar_btn_font"]), anchor="w")
        label.grid(row=0, column=0, sticky="nsew")
        
        entry = ctk.CTkEntry(frame, placeholder_text=f"Enter {field_name}...")
        entry.grid(row=0, column=1, sticky="nsew")
        
        return frame, entry
