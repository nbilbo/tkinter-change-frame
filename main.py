from tkinter import Tk, Frame, Button, Label, Menu

class SampleApp(Tk):
    def __init__(self):
        super().__init__()
        
        #menubar
        menubar = Menu(self)
        self.config(menu=menubar)

        #menuAdicionar
        menuAdicionar = Menu(menubar, tearoff=0)
        menubar.add_cascade(label="Adicionar", menu=menuAdicionar)

        menuAdicionar.add_command(label="Usuário", command=lambda: self.showFrame("TelaUsuario"))
        menuAdicionar.add_command(label="Cliente", command=lambda: self.showFrame("TelaCliente"))
        
        
        #container
        #onde os frames vaão ficar um em cima do outro.
        self.container = Frame(self, width=300, bg = "blue")
        self.container.grid_rowconfigure(0, weight=1)
        self.container.grid_columnconfigure(0, weight=1)
        
        #um dicionario com todos os frames.
        self.frames = {}
        #percorrer todos os frames.
        for classe in (TelaUsuario, TelaCliente):
            page_name = classe.__name__
            frame = classe(parent=self.container, width=500)
            #atualizando o dicionario
            self.frames[page_name]=frame
            #colocando os frames no mesmo local.
            frame.grid(row=0, column=0, sticky="nsew")

        #pack
        self.container.pack(side="left", fill="y",  padx=5, pady=5)
        self.container.pack_propagate(False)
    
    #atulizar o frame que ficará 'na frente' dos outros.
    def showFrame(self, page_name):
        frame=self.frames[page_name]
        frame.tkraise()

class TelaUsuario(Frame):
    def __init__(self, parent, **kwargs):
        super().__init__(parent, **kwargs)
        self["background"]="red"
        self.pack_propagate(False)
        label = Label(self, text="TelaUsuario")
        label.pack()


class TelaCliente(Frame):
    def __init__(self, parent, **kwargs):
        super().__init__(parent, **kwargs)
        self["background"]="green"
        label = Label(self, text = "TelaCliente")
        label.pack()



if __name__ == "__main__":
    app = SampleApp()
    app.geometry("500x400")
    app.mainloop()

