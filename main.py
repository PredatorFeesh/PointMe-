import tkinter as tk
import src.Application

if __name__ == '__main__':
    root = tk.Tk()
    #root.geometry("1600x900")
    root.title("Operation Event Hub")
    app = src.Application.App(master=root)
    app.mainloop()
