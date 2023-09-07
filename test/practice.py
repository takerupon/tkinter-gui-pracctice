import customtkinter

class MyFrame(customtkinter.CTkScrollableFrame):
    def __init__(self, master, **kwargs):
        super().__init__(master, **kwargs)
        # フレームにウィジェットを追加...
        self.label = customtkinter.CTkLabel(self)
        self.label.place(x=20, y=0)  # placeメソッドを使用してウィジェットを配置

class App(customtkinter.CTk):
    def __init__(self):
        super().__init__()
        self.my_frame = MyFrame(master=self, width=300, height=200)
        self.my_frame.place(x=20, y=20)  # placeメソッドを使用してウィジェットを配置

app = App()
app.mainloop()
