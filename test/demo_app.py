import tkinter as tk
import customtkinter
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
        # stickyは拡大したときに広がる方向のこと。nsew で4方角で指定する。
        self.navigation_frame = NavigationFrame(master=self, corner_radius=0)
        self.navigation_frame.grid(row=0, column=0,padx=10, pady=10, sticky="ew")
        
        #2つ目のフレームの設定
        self.search_frame = SearchFrame(master=self, corner_radius=0,)
        self.search_frame.grid(row=1, column=0,padx=10, pady=10, sticky="ew")
        
        #3つ目のフレームの設定
        self.info_frame = InfoFrame(master=self)
        self.info_frame.grid(row=2, column=0,padx=10, pady=10, sticky="ew")
        
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
        self.button_setting = customtkinter.CTkButton(master=self, text="設定", font=self.fonts)
        self.button_setting.grid(row=1, column=0, padx=10, pady=10)
        
        # ホームボタン
        self.button_home = customtkinter.CTkButton(master=self, text="ホーム", font=self.fonts)
        self.button_home.grid(row=1, column=1, padx=10, pady=10)
        
        #管理者選択ボタン
        self.button_manager_serect = customtkinter.CTkOptionMenu(master=self, values=["山田花子", "山口友也", "樋口剛琉"])
        self.button_manager_serect.grid(row=1, column=2, padx=(460,10), pady=10,)


class SearchFrame(customtkinter.CTkFrame):
    def __init__(self, *args, header_name="SearchFrame", **kwargs):
        super().__init__(*args, **kwargs)
        
        self.fonts = (FONT_TYPE, 15)
        self.header_name = header_name

        # フォームのセットアップをする
        self.setup_form()

    def setup_form(self):
        #検索バー
        self.entry = customtkinter.CTkEntry(self, placeholder_text="入力してください", width=920)
        self.entry.grid(row=0, column=0, padx=10, pady=10, sticky="ew")


class InfoFrame(customtkinter.CTkFrame):
    def __init__(self, *args, header_name="InfoFrame", **kwargs):
        super().__init__(*args, **kwargs)
        
        self.fonts = (FONT_TYPE, 15)
        self.header_name = header_name

        # フォームのセットアップをする
        self.setup_form()

    def setup_form(self):
        #購入者情報
        self.purchaser_info = customtkinter.CTkTextbox(self, width=450)
        self.purchaser_info.grid(row=0, column=0, padx=10, pady=10, sticky="nsew")
        self.purchaser_info.insert("0.0", "購入者情報\n\n")
        
        #スキャン商品一覧
        self.scanned_product = customtkinter.CTkTextbox(self, width=450)
        self.scanned_product.grid(row=1, column=0, padx=10, pady=10, sticky="nsew")
        self.scanned_product.insert("0.0", "スキャンした商品\n\n")
        
        #商品一覧
        self.product_list = customtkinter.CTkTextbox(self, width=450)
        self.product_list.grid(row=0, column=1, rowspan=2, padx=10, pady=10, sticky="nsew")
        self.product_list.insert("0.0", "商品一覧\n\n")
        
        #購入ボタン
        self.button_buy = customtkinter.CTkButton(master=self, text="購入", font=self.fonts)
        self.button_buy.grid(row=3, column=1, padx=(300,10), pady=(0,10))
if __name__ == "__main__":
    app = App()
    app.mainloop()
