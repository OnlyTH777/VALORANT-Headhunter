import customtkinter
from instalockOOP import *

main = Main()


class InitialFrame(customtkinter.CTkFrame):
    def __init__(self, parent):
        super().__init__(parent)

        customtkinter.CTkLabel(master=self, text="Bem Vindo ao Valorant Headhunter", font=("Roboto", 24)).pack(padx=10, pady=10)
        customtkinter.CTkLabel(master=self, text="Este projeto é um projeto em constante desenvolvimento e bugs podem aparecer no decorrer deste processo.", font=("Roboto", 16)).pack(padx=10, pady=10)
        customtkinter.CTkLabel(master=self, text="Não me responsabilizo por banimentos devido ao uso deste aplicativo.", font=("Roboto", 16)).pack(padx=10, pady=10)

        if main.logado == False:
            self.labelOpenValorant = customtkinter.CTkLabel(master=self, text="Para continuar pressione o botão abaixo com o VALORANT aberto.", font=("Roboto", 12))
            self.labelOpenValorant.pack(padx=10, pady=10)

            self.buttonLogin = customtkinter.CTkButton(master=self, text="Conectar com o VALORANT", command=self.conectWithValorant)
            self.buttonLogin.pack(padx=10, pady=10)


    def conectWithValorant(self):
        main.logarValorant()
        if main.logado == True:
            self.buttonLogin.destroy()
            self.labelOpenValorant.destroy()


class ExternalPickFrame(customtkinter.CTkFrame):
    def __init__(self, parent):
        super().__init__(parent)

        self.label = customtkinter.CTkLabel(master=self, text="Instalock System", font=("Roboto", 24))
        self.label.pack(padx=10, pady=10)

        self.agent = customtkinter.CTkOptionMenu(master=self, values=agents)
        self.agent.pack(padx=10, pady=10)
        self.agent.set("Selecione um agente")

        self.buttonPick = customtkinter.CTkButton(master=self, text="Pickar", command=self.agenteskk, state="normal")
        self.buttonPick.pack(padx=10, pady=10)

    def agenteskk(self):
        main.instalock(self.agent.get())


class SupportFrame(customtkinter.CTkFrame):
    def __init__(self, parent):
        super().__init__(parent)
        customtkinter.CTkLabel(self, text="Baixou pq quis, não tem galantia").pack(padx="10", pady="10")


class MainWindow():
    def __init__(self, master):

        self.index = 0
        self.frameList = [InitialFrame(master), ExternalPickFrame(master), SupportFrame(master)]

        customtkinter.set_default_color_theme("dark-blue")

        master.title("VALORANT Headhunter")
        master.grid_rowconfigure(0, weight=1)
        master.grid_columnconfigure(9, weight=1)

        initialFrame = InitialFrame(master)
        initialFrame.grid(row=0, column=1, columnspan=9, padx=20, pady=20, sticky="nsew")

        bottomFrame = customtkinter.CTkFrame(master)
        bottomFrame.grid(row=0, column=0, columnspan=1, padx=20, pady=20, sticky="nsew")

        label = customtkinter.CTkLabel(bottomFrame, text="Valorant Headhunter")
        label.pack(padx="10", pady="10")

        switch = customtkinter.CTkButton(bottomFrame, text="Home", command=lambda: self.switchFrame("Home"))
        switch.pack(padx="10", pady="10")

        switch = customtkinter.CTkButton(bottomFrame, text="External Pick", command=lambda: self.switchFrame("ExternalPick"))
        switch.pack(padx="10", pady="10")

        switch = customtkinter.CTkButton(bottomFrame, text="Support", command=lambda: self.switchFrame("Support"))
        switch.pack(padx="10", pady="10")

    def switchFrame(self, ID):
        IDs = {"Home": 0, "ExternalPick": 1, "Support": 2}
        if ID in IDs.keys():
            IDf = IDs.get(ID)
        self.frameList[self.index].forget()
        self.index = IDf
        self.frameList[self.index].tkraise()
        self.frameList[self.index].grid(row=0, column=1, columnspan=9, padx=20, pady=20, sticky="nsew")
