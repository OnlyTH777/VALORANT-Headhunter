import customtkinter
import webbrowser
from src.instalockOOP import *


class App(customtkinter.CTk):
    def __init__(self):
        super().__init__()
        self.main = Main()
        customtkinter.set_appearance_mode("dark")
        customtkinter.set_default_color_theme("dark-blue")

        self.geometry("500x500")
        self.title("VALORANT Headhunter")

        self.grid_rowconfigure(0, weight=1)
        self.grid_columnconfigure(9, weight=1)

        self.sideBar = SideBar(master=self)
        self.sideBar.grid(row=0, column=0, columnspan=1, padx=20, pady=20, sticky="nsew")

        self.frame = FrameInstalock(master=self)
        self.frame.grid(row=0, column=1, columnspan=9, padx=20, pady=20, sticky="nsew")


class SideBar(customtkinter.CTkFrame):
    def __init__(self, master, **kwargs):
        super().__init__(master, **kwargs)

        self.buttonInstalockSideBar = customtkinter.CTkButton(master=self, text="Instalock", state="disabled")
        self.buttonInstalockSideBar.pack(padx=10, pady=10)

        self.buttonSupportSideBar = customtkinter.CTkButton(master=self, text="Support", state="normal", command=self.support)
        self.buttonSupportSideBar.pack(padx=10, pady=10)

    def support(self):
        webbrowser.open('https://github.com/OnlyTH777/VALORANT-Headhunter/issues')  # Go to example.com

class FrameInstalock(customtkinter.CTkFrame):
    def __init__(self, master, **kwargs):
        super().__init__(master, **kwargs)
        self.label = customtkinter.CTkLabel(master=self, text="Instalock System", font=("Roboto", 24))
        self.label.pack(padx=10, pady=10)

        self.agent = customtkinter.CTkOptionMenu(master=self, values=agents)
        self.agent.pack(padx=10, pady=10)
        self.agent.set("Selecione um agente")

        self.buttonLogin = customtkinter.CTkButton(master=self, text="Conectar com o VALORANT", command=self.logaValorant)
        self.buttonLogin.pack(padx=10, pady=10)

        self.buttonPick = customtkinter.CTkButton(master=self, text="Pickar", command=self.agenteskk, state="disabled")
        self.buttonPick.pack(padx=10, pady=10)

    def agenteskk(self):
        self.main.instalock(self.agent.get())

    def logaValorant(self):
        self.buttonLogin.configure(state="disabled")
        self.buttonPick.configure(state="normal")
        self.main.logarValorant()
