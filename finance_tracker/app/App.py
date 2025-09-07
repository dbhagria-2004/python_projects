import tkinter as tk

class App(tk.Tk):
    def __init__(self):
        try:
            super().__init__()
            self.title("This is test GUI")
            self.geometry("500x500")
            self.current_frame = None

            self.switch_frame(LoginScreen)
            
        except Exception as e:
            print(e)

    def switch_frame(self, frame_class):
        new_frame = frame_class(self)
        if self.current_frame is not None:
            self.current_frame.destroy()
        self.current_frame = new_frame
        self.current_frame.pack()


class LoginScreen(tk.Frame):
    
    def __init__(self, master):
        super().__init__(master)
        tk.Label(self, text="UserId:").pack()
        self.user_id_entry = tk.Entry(self)
        self.user_id_entry.pack()
        
        tk.Label(self, text="Name:").pack()
        self.name_entry = tk.Entry(self)
        self.name_entry.pack()

        tk.Button(self, text="Login", command=lambda: master.switch_frame(Dashboard)).pack()


class Dashboard(tk.Frame):
    
    def __init__(self, master):
        super().__init__(master)
        tk.Label(self, text="DashBoard", font="Arial").pack()

        tk.Button(self, text="Add Trans", command=lambda : master.switch_frame(AddTransaction)).pack()
        tk.Button(self, text="View Trans", command=lambda : master.switch_frame(ViewTransaction)).pack()


class AddTransaction(tk.Frame):
    def __init__(self, master):
        super().__init__(master)
        tk.Label(self, text="DashBoard", font="Arial").pack()
        
        tk.Button(self, text="back_to_dashboard ", command=lambda : master.switch_frame(Dashboard)).pack()


class ViewTransaction(tk.Frame):
        def __init__(self, master):
            super().__init__(master)
            tk.Label(self, text="DashBoard", font="Arial").pack()
            tk.Button(self, text="back_to_dashboard ", command=lambda : master.switch_frame(Dashboard)).pack()
    