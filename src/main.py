import customtkinter as ctk
from datetime import datetime
import core.tech_funcs as tech_funcs
from home_frame import HomePage

class MainWindow():
    def __init__(self):
        self.mainwindow = ctk.CTk()
        self.mainwindow.title("Makapopka's Toolbox")
        self.mainwindow.geometry("1024x600")
        self.mainwindow.update_idletasks()
        
        self.config = tech_funcs.load_config()
        
        self.build_header()
        
        self.current_frame = None
        self.switch_container(HomePage)
        
        self.mainwindow.mainloop()
        
    
    def update_clock(self):
        now = datetime.now().strftime("%H:%M:%S")
        self.label.configure(text=now)
        self.mainwindow.after(1000, self.update_clock)
    
    def build_header(self):
        self.mainframe = ctk.CTkFrame(
            self.mainwindow, 
            fg_color=self.config["header_color"], 
            height=100,
            corner_radius=0)
        self.label = ctk.CTkLabel(
            self.mainframe, font=("Helvetica", 28), 
            text_color=self.config["time_color"])
        
        self.mainframe.pack(fill="x")
        self.label.pack(pady=10)
        
        self.update_clock()
    
    def switch_container(self, frame_class):
        if self.current_frame is not None:
            self.current_frame.destroy()
        
        self.current_frame = frame_class(self.mainwindow, self.config)
        self.current_frame.pack(fill="both", expand=True)
    
if __name__ == "__main__":
    MainWindow()