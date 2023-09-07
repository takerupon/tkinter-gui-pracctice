import tkinter as tk
import customtkinter
from PIL import Image, ImageTk
import os

FONT_TYPE = "meiryo"

class App(customtkinter.CTk):

    def __init__(self):
        super().__init__()

        # メンバー変数の設定
        self.fonts = (FONT_TYPE, 15)

        # フォームのセットアップをする
        self.setup_form()

    def setup_form(self):
        # CustomTkinter のフォームデザイン設定
        customtkinter.set_appearance_mode("light")  # Modes: system (default), light, dark
        customtkinter.set_default_color_theme("blue")  # Themes: blue (default), dark-blue, green

        # フォームサイズ設定
        self.geometry("960x640")
        self.title("Airshop")

        # 行方向のマスのレイアウトを設定する。リサイズしたときに一緒に拡大したい行をweight 1に設定。
        self.grid_rowconfigure(1, weight=1)
        # 列方向のマスのレイアウトを設定する
        self.grid_columnconfigure(0, weight=1)

        # 1つ目のフレームの設定
        self.navigation_frame = NavigationFrame(master=self, width=940, height=60, corner_radius=0, fg_color="#FFFFFF")
        self.navigation_frame.place(x=10, y=10)

        #2つ目のフレームの設定
        self.search_frame = SearchFrame(master=self, corner_radius=0, width=940, height=60, fg_color="#AEC2B4")
        self.search_frame.place(x=10, y=80)

        #3つ目のフレームの設定
        self.info_frame = InfoFrame(master=self, width=450, height=469, fg_color="#EAEEEB")
        self.info_frame.place(x=10, y=150)

        #4つ目のフレームの設定
        self.product_frame=ProductFrame(master=self, width=465, height=480, fg_color="#EAEEEB")
        self.product_frame.place(x=485, y=150)

        self.resizable(False, False)



class NavigationFrame(customtkinter.CTkFrame):
    def __init__(self, *args, header_name="NavigationFrame", **kwargs):
        super().__init__(*args, **kwargs)

        self.fonts = (FONT_TYPE, 15)
        self.header_name = header_name

        # フォームのセットアップをする
        self.setup_form()

    def setup_form(self):
        # 設定ボタン
        self.original_image=Image.open("C:\\Users\\樋口剛琉\\Git\\tkinter-gui-pracctice\\img\\setting_icon.png")
        self.resized_image = self.original_image.resize((30, 30))
        self.font_setting=("setting", 10)
        self.button_setting = customtkinter.CTkButton(
            master=self,
            text="設定",
            text_color="#646A64",
            font=self.font_setting,
            fg_color="#FFFFFF",
            hover_color="#dcdcdc",
            compound="top",
            image=ImageTk.PhotoImage(self.resized_image), width=34, height=60)
        self.button_setting.place(x=32, y=2)

        # ホームボタン
        self.icon_home=Image.open("C:\\Users\\樋口剛琉\\Git\\tkinter-gui-pracctice\\img\\home2.png").resize((30, 30))
        self.font_home=("home", 10)
        self.button_home = customtkinter.CTkButton(
            master=self,
            text="ホーム",
            text_color="#646A64",
            compound="top",
            fg_color="#FFFFFF",
            hover_color="#dcdcdc",
            image=ImageTk.PhotoImage(self.icon_home), font=self.font_home, width=34, height=60)
        self.button_home.place(x=122, y=3)

        #画面状態表示
        self.label_screen=customtkinter.CTkLabel(master=self, text="販売", text_color="#000000", font=("販売", 20), fg_color="#FFFFFF")
        self.label_screen.place(x=456, y=21)

        #管理者選択ボタン
        self.button_manager_serect = customtkinter.CTkOptionMenu(
            master=self,
            values=["山田花子", "山口友也", "樋口剛琉"],
            text_color="#000000",
            fg_color="#FFFFFF",
            button_color="#FFFFFF",
            button_hover_color="#dcdcdc",
            width=147,
            height=40.16)
        self.button_manager_serect.place(x=786, y=12)


class SearchFrame(customtkinter.CTkFrame):
    def __init__(self, *args, header_name="SearchFrame", **kwargs):
        super().__init__(*args, **kwargs)

        self.fonts = (FONT_TYPE, 15)
        self.header_name = header_name

        # フォームのセットアップをする
        self.setup_form()

    def setup_form(self):
        #検索バー
        self.entry = customtkinter.CTkEntry(self, placeholder_text="入力してください", width=400, height=40)
        self.entry.place(x=20, y=10)


class InfoFrame(customtkinter.CTkScrollableFrame):
    def __init__(self, *args, header_name="InfoFrame", **kwargs):
        super().__init__(*args, **kwargs)

        self.fonts = (FONT_TYPE, 15)
        self.header_name = header_name

        # フォームのセットアップをする
        self.setup_form()

    def setup_form(self):
        #購入者情報
        self.purchaser_info = customtkinter.CTkLabel(self, width=373, height=144, fg_color="#AEC2B4")
        self.purchaser_info.grid(row=0, column=0, padx=32, pady=15)

        #スキャン商品一覧
        self.scanned_product = customtkinter.CTkLabel(self, width=373, height=72, fg_color="#D9D9D9")
        self.scanned_product.grid(row=1, column=0, padx=32, pady=205)


class ProductFrame(customtkinter.CTkFrame):
    def __init__(self, *args, header_name="ProductFrame", **kwargs):
        super().__init__(*args, **kwargs)

        self.fonts = (FONT_TYPE, 15)
        self.header_name = header_name

        # フォームのセットアップをする
        self.setup_form()

    def setup_form(self):
        #商品一覧
        self.product_list = customtkinter.CTkTextbox(self, width=440, height=296)
        self.product_list.place(x=10, y=10)
        self.product_list.insert("0.0", "商品一覧\n\n")

        #購入ボタン
        self.button_buy = customtkinter.CTkButton(
            master=self,
            width=152,
            height=48,
            text="購入",
            font=self.fonts,
            text_color="black",
            hover_color="#B9D0B4",
            fg_color="#478A56")
        self.button_buy.place(x=300, y=418)


if __name__ == "__main__":
    app = App()
    app.mainloop()
