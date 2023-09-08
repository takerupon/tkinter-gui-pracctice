import tkinter as tk
import customtkinter
from PIL import Image, ImageTk

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

        self.navigation_frame = NavigationFrame(self, 940, 60, 10, 10, "#FFFFFF")
        self.home_frame = HomeFrame(self, 940, 560, 10, 100, "#EAEEEB")

        self.resizable(False, False)

class BaseFrame(customtkinter.CTkFrame):
    def __init__(self, master, width, height, x, y, fg_color):
        super().__init__(master=master, width=width, height=height, fg_color=fg_color)
        self.place(x=x, y=y)


class NavigationFrame(BaseFrame):
    def __init__(self, master, width, height, x, y, fg_color):
        super().__init__(master, width, height, x, y, fg_color)
        self.setup_form()

    def setup_form(self):
        icon_setting = Image.open("img/setting_icon.png").resize((30, 30))
        btn_setting = customtkinter.CTkButton(self, text="設定", text_color="#000000", compound="top", fg_color="#FFFFFF", hover_color="#dcdcdc", image=ImageTk.PhotoImage(icon_setting), font=("meiryo", 10), width=34, height=60)
        btn_setting.place(x=32, y=2)

        label_screen = customtkinter.CTkLabel(self, text="ホーム", text_color="#000000", font=("ホーム", 20), fg_color="#FFFFFF")
        label_screen.place(x=456, y=21)

        button_manager_select = customtkinter.CTkOptionMenu(self, values=["山田花子", "山口友也", "樋口剛琉"], text_color="#000000", fg_color="#FFFFFF", button_color="#FFFFFF", button_hover_color="#dcdcdc", width=147, height=40.16)
        button_manager_select.place(x=786, y=12)


class HomeFrame(BaseFrame):
    def __init__(self, master, width, height, x, y, fg_color):
        super().__init__(master, width, height, x, y, fg_color)
        self.setup_form()

    def setup_form(self):
        state_icons = [("img/hanbai2.png", "販売", 96, 39), ("img/uriage.png", "売上", 509, 39), ("img/packin.png", "取り寄せ依頼", 96, 304), ("img/zaikokanri.png", "在庫管理", 509, 304)]
        for icon_path, text, x, y in state_icons:
            icon = Image.open(icon_path).resize((40, 40))
            btn_state = customtkinter.CTkButton(self, text=text, text_color="#FFFFFF", compound="left", fg_color="#478A56", hover_color="#B9D0B4", image=ImageTk.PhotoImage(icon), font=("meiryo", 20), width=359, height=207)
            btn_state.place(x=x, y=y)


if __name__ == "__main__":
    app = App()
    app.mainloop()