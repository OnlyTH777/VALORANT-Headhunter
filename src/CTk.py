import customtkinter
import webbrowser
from externalPick import *

externalPick = ExternalPick()


class HomeFrame(customtkinter.CTkFrame):
    def __init__(self, parent):
        super().__init__(parent)

        customtkinter.CTkLabel(master=self, text="Bem Vindo ao Valorant Headhunter", font=("Roboto", 24)).pack(padx=10, pady=10)
        customtkinter.CTkLabel(master=self, text="Este projeto é um projeto em constante desenvolvimento e bugs podem aparecer no decorrer deste processo.", font=("Roboto", 16)).pack(padx=10, pady=10)
        customtkinter.CTkLabel(master=self, text="Não me responsabilizo por banimentos devido ao uso deste aplicativo.", font=("Roboto", 16)).pack(padx=10, pady=10)

        if externalPick.logado == False:
            self.labelOpenValorant = customtkinter.CTkLabel(master=self, text="Para que as funções funcionem pressione o botão abaixo com o VALORANT aberto.", font=("Roboto", 12))
            self.labelOpenValorant.pack(padx=10, pady=10)

            self.buttonLogin = customtkinter.CTkButton(master=self, text="Conectar com o VALORANT", command=lambda: self.conectWithValorant())
            self.buttonLogin.pack(padx=10, pady=10)

    def conectWithValorant(self):
        externalPick.logarValorant()
        if externalPick.logado == True:
            self.labelOpenValorant.destroy()
            self.buttonLogin.destroy()


class ExternalPickFrame(customtkinter.CTkFrame):
    def __init__(self, parent):
        super().__init__(parent)
        customtkinter.CTkLabel(master=self, text="External Pick System", font=("Roboto", 24)).pack(padx=10, pady=10)
        self.agent = customtkinter.CTkOptionMenu(master=self, values=agents)
        self.agent.pack(padx=10, pady=10)
        self.agent.set("Selecione um agente")
        customtkinter.CTkButton(master=self, text="Pickar Agente", command=lambda: externalPick.instalock(self.agent.get())).pack(padx=10, pady=10)


class SupportFrame(customtkinter.CTkFrame):
    def __init__(self, parent):
        super().__init__(parent)
        customtkinter.CTkLabel(self, text="Caso você tenha encontrado um bug abra uma issue no repositorio do projeto em meu GitHub").pack(padx="10", pady="10")
        customtkinter.CTkLabel(self, text="Você pode entrar em contato comigo diretamente pelo meu Discord").pack(padx="10", pady="10")
        customtkinter.CTkButton(self, text="Meu Discord", command=lambda: webbrowser.open('https://github.com/OnlyTH777')).pack(padx="10", pady="10")
        customtkinter.CTkButton(self, text="Meu GitHub", command=lambda: webbrowser.open('https://discord.com/users/410479396084908044')).pack(padx="10", pady="10")


class MainWindow():
    def __init__(self, master):
        customtkinter.set_default_color_theme("dark-blue")
        master.title("VALORANT Headhunter")
        master.grid_rowconfigure(0, weight=1)
        master.grid_columnconfigure(9, weight=1)
        self.index = 0
        self.frameList = [HomeFrame(master), ExternalPickFrame(master), SupportFrame(master)]

        HomeFrame(master).grid(row=0, column=1, columnspan=9, padx=20, pady=20, sticky="nsew")

        sideBarFrame = customtkinter.CTkFrame(master)
        sideBarFrame.grid(row=0, column=0, columnspan=1, padx=20, pady=20, sticky="nsew")

        customtkinter.CTkButton(sideBarFrame, text="Home", command=lambda: self.switchFrame("Home")).pack(padx="10", pady="10")
        customtkinter.CTkButton(sideBarFrame, text="External Pick", command=lambda: self.switchFrame("ExternalPick")).pack(padx="10", pady="10")
        customtkinter.CTkButton(sideBarFrame, text="Suporte", command=lambda: self.switchFrame("Suporte")).pack(padx="10", pady="10")

    def switchFrame(self, ID):
        IDs = {"Home": 0, "ExternalPick": 1, "Suporte": 2}
        if ID in IDs.keys():
            ID = IDs.get(ID)

        self.frameList[self.index].forget()
        self.index = ID
        self.frameList[self.index].tkraise()
        self.frameList[self.index].grid(row=0, column=1, columnspan=9, padx=20, pady=20, sticky="nsew")
