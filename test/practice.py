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
        self.search_frame = SearchFrame(self, 940, 60, 10, 80, "#AEC2B4")
        self.info_frame = InfoFrame(self, 450, 469, 10, 150, "#EAEEEB")
        self.product_frame = ProductFrame(self, 465, 480, 485, 150, "#EAEEEB")

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
        icons = [("img/setting_icon.png", "設定", 32, 2), ("img/home2.png", "ホーム", 122, 3)]
        for icon_path, text, x, y in icons:
            icon = Image.open(icon_path).resize((30, 30))
            btn = customtkinter.CTkButton(self, text=text, text_color="#000000", compound="top", fg_color="#FFFFFF", hover_color="#dcdcdc", image=ImageTk.PhotoImage(icon), font=("meiryo", 10), width=34, height=60)
            btn.place(x=x, y=y)

        label_screen = customtkinter.CTkLabel(self, text="販売", text_color="#000000", font=("販売", 20), fg_color="#FFFFFF")
        label_screen.place(x=456, y=21)

        button_manager_select = customtkinter.CTkOptionMenu(self, values=["山田花子", "山口友也", "樋口剛琉"], text_color="#000000", fg_color="#FFFFFF", button_color="#FFFFFF", button_hover_color="#dcdcdc", width=147, height=40.16)
        button_manager_select.place(x=786, y=12)

class SearchFrame(BaseFrame):
    def __init__(self, master, width, height, x, y, fg_color):
        super().__init__(master, width, height, x, y, fg_color)
        self.setup_form()

    def setup_form(self):
        entry = customtkinter.CTkEntry(self, placeholder_text="入力してください", width=400, height=40)
        entry.place(x=20, y=10)

class InfoFrame(customtkinter.CTkScrollableFrame):
    def __init__(self, master, width, height, x, y, fg_color):
        super().__init__(master=master, width=width, height=height, fg_color=fg_color)
        self.place(x=x, y=y)
        self.setup_form()

    def setup_form(self):
        self.purchaser_info = customtkinter.CTkLabel(self, width=373, height=144, fg_color="#AEC2B4")
        self.purchaser_info.grid(row=0, column=1, padx=32, pady=15)

        self.button_add_label = customtkinter.CTkButton(self, width=152, height=48, text="add_label", font=FONT_SETTING, text_color="black", hover_color="#B9D0B4", fg_color="#478A56", command=self.add_label)
        self.button_add_label.grid(row=1, column=1, padx=10, pady=10)
        self.label_count = 1

    def add_label(self):
        new_label = customtkinter.CTkLabel(self, width=373, height=72, text=f"Label {self.label_count + 1}", fg_color="#FFFFFF")
        new_label.grid(row=self.label_count + 1, column=1, pady=10)
        self.label_count += 1

class ProductFrame(BaseFrame):
    def __init__(self, master, width, height, x, y, fg_color):
        super().__init__(master, width, height, x, y, fg_color)
        self.setup_form()

    def setup_form(self):
        product_list = customtkinter.CTkTextbox(self, width=440, height=296)
        product_list.place(x=10, y=10)
        product_list.insert("0.0", "商品一覧\n\n")

        button_buy = customtkinter.CTkButton(self, width=152, height=48, text="購入", font=FONT_SETTING, text_color="black", hover_color="#B9D0B4", fg_color="#478A56")
        button_buy.place(x=300, y=418)

if __name__ == "__main__":
    app = App()
    app.mainloop()
