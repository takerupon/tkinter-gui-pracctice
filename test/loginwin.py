import tkinter as tk
import customtkinter
from PIL import Image, ImageTk
import os

FONT_TYPE = "meiryo"
FONT_SIZE = 15
FONT_SETTING = (FONT_TYPE, FONT_SIZE)

class App(customtkinter.CTk):
    def __init__(self):
        super().__init__()
        self.setup_form()

    def setup_form(self):
        customtkinter.set_appearance_mode("light")
        customtkinter.set_default_color_theme("blue")
        self.geometry("960x640")
        self.title("Airshop")
        self.grid_rowconfigure(1, weight=1)
        self.grid_columnconfigure(0, weight=1)

        self.login_frame = LoginFrame(self, 960, 640, 0, 0, "#D9D9D9")

        self.resizable(False, False)

class BaseFrame(customtkinter.CTkFrame):
    def __init__(self, master, width, height, x, y, fg_color):
        super().__init__(master=master, width=width, height=height, fg_color=fg_color)
        self.place(x=x, y=y)

class LoginFrame(BaseFrame):
    def __init__(self, master, width, height, x, y, fg_color):
        super().__init__(master, width, height, x, y, fg_color)
        self.setup_form()

    def setup_form(self):
        label_logo = customtkinter.CTkLabel(self, fg_color="#FFFFFF", width=120, height=120)
        label_logo.place(x=420, y=100)

        button_manager_select = customtkinter.CTkOptionMenu(self, values=["山田花子", "山口友也", "樋口剛琉"],
                                                            text_color="#000000",
                                                            fg_color="#FFFFFF",
                                                            button_color="#FFFFFF",
                                                            button_hover_color="#dcdcdc",
                                                            width=280, height=40)
        button_manager_select.place(x=349, y=243)

        entry = customtkinter.CTkEntry(self, placeholder_text="パスワード", width=280, height=40)
        entry.place(x=349, y=307)

        button_login = customtkinter.CTkButton(self, width=280, height=40, text="ログイン", font=FONT_SETTING, text_color="black", hover_color="#B9D0B4", fg_color="#478A56")
        button_login.place(x=349, y=379)


if __name__ == "__main__":
    app = App()
    app.mainloop()