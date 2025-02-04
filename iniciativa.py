import tkinter as tk
from tkinter import messagebox

class OrdemIniciativaApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Ordem de Iniciativa")
        
        self.jogadores = []

        tk.Label(root, text="Nome do Jogador:").grid(row=0, column=0, padx=5, pady=5)
        self.nome_entry = tk.Entry(root)
        self.nome_entry.grid(row=0, column=1, padx=5, pady=5)

        tk.Label(root, text="Número do Dado:").grid(row=1, column=0, padx=5, pady=5)
        self.numero_entry = tk.Entry(root)
        self.numero_entry.grid(row=1, column=1, padx=5, pady=5)

        tk.Button(root, text="Adicionar", command=self.adicionar).grid(row=2, column=0, columnspan=2, pady=5)
        tk.Button(root, text="Apagar Lista", command=self.apagar_lista).grid(row=3, column=0, columnspan=2, pady=5)

        
        self.lista_frame = tk.Frame(root)
        self.lista_frame.grid(row=4, column=0, columnspan=2, pady=5)
        self.lista_label = tk.Label(self.lista_frame, text="Lista de Iniciativa:")
        self.lista_label.pack()
        self.lista_box = tk.Text(self.lista_frame, width=30, height=10, state="disabled")
        self.lista_box.pack()

    def adicionar(self):
        nome = self.nome_entry.get().strip()
        numero = self.numero_entry.get().strip()

        if not nome or not numero.isdigit():
            messagebox.showwarning("Entrada Inválida", "Por favor, insira um nome válido e um número inteiro.")
            return

        self.jogadores.append((int(numero), nome))
        self.jogadores.sort(reverse=True, key=lambda x: x[0])
        self.atualizar_lista()
        self.nome_entry.delete(0, tk.END)
        self.numero_entry.delete(0, tk.END)

    def atualizar_lista(self):
        self.lista_box.config(state="normal")
        self.lista_box.delete(1.0, tk.END)

        for i, (numero, nome) in enumerate(self.jogadores, start=1):
            self.lista_box.insert(tk.END, f"{i}. {numero} - {nome}\n")

        self.lista_box.config(state="disabled")

    def apagar_lista(self):
        self.jogadores.clear()
        self.atualizar_lista()


if __name__ == "__main__":
    root = tk.Tk()
    app = OrdemIniciativaApp(root)
    root.mainloop()
