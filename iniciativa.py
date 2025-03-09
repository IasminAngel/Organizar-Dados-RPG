import tkinter as tk
from tkinter import messagebox

class OrdemIniciativaApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Ordem de Iniciativa")
        self.root.geometry("350x400")  # Define o tamanho da janela
        self.centralizar_janela()

        self.jogadores = []

        # Entrada de nome
        tk.Label(root, text="Nome do Jogador:", font=("Arial", 10, "bold")).pack(pady=5)
        self.nome_entry = tk.Entry(root, font=("Arial", 10))
        self.nome_entry.pack(pady=5)

        # Entrada do número
        tk.Label(root, text="Número do Dado:", font=("Arial", 10, "bold")).pack(pady=5)
        self.numero_entry = tk.Entry(root, font=("Arial", 10))
        self.numero_entry.pack(pady=5)

        # Botões
        tk.Button(root, text="Adicionar", command=self.adicionar, width=15, bg="green", fg="white").pack(pady=5)
        tk.Button(root, text="Remover Selecionado", command=self.remover_selecionado, width=20, bg="red", fg="white").pack(pady=5)
        tk.Button(root, text="Apagar Lista", command=self.apagar_lista, width=15, bg="gray", fg="white").pack(pady=5)

        # Lista de jogadores (usando Listbox)
        self.lista_label = tk.Label(root, text="Lista de Iniciativa:", font=("Arial", 10, "bold"))
        self.lista_label.pack(pady=5)

        self.lista_box = tk.Listbox(root, width=40, height=10, font=("Arial", 10))
        self.lista_box.pack(pady=5)

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
        self.lista_box.delete(0, tk.END)
        for i, (numero, nome) in enumerate(self.jogadores, start=1):
            self.lista_box.insert(tk.END, f"{i}. {numero} - {nome}")

    def remover_selecionado(self):
        try:
            index = self.lista_box.curselection()[0]
            del self.jogadores[index]
            self.atualizar_lista()
        except IndexError:
            messagebox.showwarning("Aviso", "Selecione um jogador para remover.")

    def apagar_lista(self):
        self.jogadores.clear()
        self.atualizar_lista()

    def centralizar_janela(self):
        self.root.update_idletasks()
        largura = self.root.winfo_width()
        altura = self.root.winfo_height()
        x = (self.root.winfo_screenwidth() // 2) - (largura // 2)
        y = (self.root.winfo_screenheight() // 2) - (altura // 2)
        self.root.geometry(f"+{x}+{y}")

if __name__ == "__main__":
    root = tk.Tk()
    app = OrdemIniciativaApp(root)
    root.mainloop()
