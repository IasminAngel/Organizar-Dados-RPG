import customtkinter as ctk
from tkinter import messagebox

class OrdemIniciativaApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Ordem de Iniciativa")
        self.root.geometry("500x900")
        ctk.set_appearance_mode("dark")  
        ctk.set_default_color_theme("blue")

        self.jogadores = []
        self.ordem_atual = []
        self.rodada = 1
        self.indice_atual = 0
        self.efeitos = {}

        # Entrada de Nome
        self.label_nome = ctk.CTkLabel(root, text="Nome do Jogador:", font=("Arial", 14, "bold"))
        self.label_nome.pack(pady=5)
        self.nome_entry = ctk.CTkEntry(root, width=250)
        self.nome_entry.pack(pady=5)

        # Entrada do Número do Dado
        self.label_numero = ctk.CTkLabel(root, text="Número do Dado:", font=("Arial", 14, "bold"))
        self.label_numero.pack(pady=5)
        self.numero_entry = ctk.CTkEntry(root, width=250)
        self.numero_entry.pack(pady=5)

        # Botões
        self.btn_adicionar = ctk.CTkButton(root, text="Adicionar", command=self.adicionar, width=200, fg_color="green")
        self.btn_adicionar.pack(pady=5)

        self.btn_proximo = ctk.CTkButton(root, text="Próximo Jogador", command=self.proximo_jogador, width=200, fg_color="orange")
        self.btn_proximo.pack(pady=5)
        
        self.btn_remover = ctk.CTkButton(root, text="Remover Selecionado", command=self.remover_selecionado, width=200, fg_color="red")
        self.btn_remover.pack(pady=5)

        self.btn_apagar = ctk.CTkButton(root, text="Apagar Lista", command=self.apagar_lista, width=200, fg_color="blue")
        self.btn_apagar.pack(pady=5)

        # Lista de Jogadores
        self.lista_label = ctk.CTkLabel(root, text="Lista de Iniciativa:", font=("Arial", 14, "bold"))
        self.lista_label.pack(pady=5)

        self.lista_box = ctk.CTkTextbox(root, width=350, height=150, state="disabled", font=("Arial", 12))
        self.lista_box.pack(pady=5)

        # Exibição da Rodada Atual
        self.label_rodada = ctk.CTkLabel(root, text="Rodada: 1", font=("Arial", 14, "bold"), text_color="yellow")
        self.label_rodada.pack(pady=10)

        # Seção de efeitos
        self.label_efeito = ctk.CTkLabel(root, text="Adicionar Efeito:", font=("Arial", 14, "bold"))
        self.label_efeito.pack(pady=5)

        self.efeito_nome_entry = ctk.CTkEntry(root, width=200, placeholder_text="Nome do Efeito")
        self.efeito_nome_entry.pack(pady=5)

        self.efeito_duracao_entry = ctk.CTkEntry(root, width=100, placeholder_text="Duração (rodadas)")
        self.efeito_duracao_entry.pack(pady=5)

        self.efeito_jogador_entry = ctk.CTkEntry(root, width=200, placeholder_text="Jogador(es) afetado(s)")
        self.efeito_jogador_entry.pack(pady=5)

        self.btn_adicionar_efeito = ctk.CTkButton(root, text="Aplicar Efeito", command=self.aplicar_efeito, width=200, fg_color="purple")
        self.btn_adicionar_efeito.pack(pady=5)

        # Lista de Efeitos
        self.efeitos_label = ctk.CTkLabel(root, text="Efeitos Ativos:", font=("Arial", 14, "bold"))
        self.efeitos_label.pack(pady=5)

        self.efeitos_box = ctk.CTkTextbox(root, width=350, height=100, state="disabled", font=("Arial", 12))
        self.efeitos_box.pack(pady=5)

    def adicionar(self):
        nome = self.nome_entry.get().strip()
        numero = self.numero_entry.get().strip()

        if not nome or not numero.isdigit():
            messagebox.showwarning("Entrada Inválida", "Por favor, insira um nome válido e um número inteiro.")
            return

        self.jogadores.append((int(numero), nome))
        self.jogadores.sort(reverse=True, key=lambda x: x[0])
        self.ordem_atual = self.jogadores[:]  
        self.atualizar_lista()
        self.nome_entry.delete(0, "end")
        self.numero_entry.delete(0, "end")

    def atualizar_lista(self):
        self.lista_box.configure(state="normal")
        self.lista_box.delete("1.0", "end")

        for i, (numero, nome) in enumerate(self.jogadores, start=1):
            self.lista_box.insert("end", f"{i}. {numero} - {nome}\n")

        self.lista_box.configure(state="disabled")

    def proximo_jogador(self):
        if not self.ordem_atual:
            messagebox.showwarning("Aviso", "Adicione jogadores antes de iniciar a rodada!")
            return

        jogador_atual = self.ordem_atual[self.indice_atual]
        messagebox.showinfo("Vez do Jogador", f"Agora é a vez de: {jogador_atual[1]}")

        self.indice_atual += 1

        if self.indice_atual >= len(self.ordem_atual):
            self.indice_atual = 0
            self.rodada += 1
            self.label_rodada.configure(text=f"Rodada: {self.rodada}")
            self.atualizar_efeitos()

    def aplicar_efeito(self):
        efeito_nome = self.efeito_nome_entry.get().strip()
        efeito_duracao = self.efeito_duracao_entry.get().strip()
        jogadores_afetados = self.efeito_jogador_entry.get().strip().split(",")

        if not efeito_nome or not efeito_duracao.isdigit():
            messagebox.showwarning("Entrada Inválida", "Insira um nome de efeito válido e um número inteiro de rodadas.")
            return

        efeito_duracao = int(efeito_duracao)
        for jogador in jogadores_afetados:
            jogador = jogador.strip()
            if jogador:
                if jogador not in self.efeitos:
                    self.efeitos[jogador] = []
                self.efeitos[jogador].append([efeito_nome, efeito_duracao])

        self.atualizar_efeitos()
        self.efeito_nome_entry.delete(0, "end")
        self.efeito_duracao_entry.delete(0, "end")
        self.efeito_jogador_entry.delete(0, "end")
        
    def atualizar_efeitos(self):
        self.efeitos_box.configure(state="normal")
        self.efeitos_box.delete("1.0", "end")

        for jogador, efeitos in list(self.efeitos.items()):
            self.efeitos[jogador] = [[nome, dur - 1] for nome, dur in efeitos if dur > 1]
            if self.efeitos[jogador]:
                self.efeitos_box.insert("end", f"{jogador}: {', '.join([f'{nome} ({dur}R)' for nome, dur in self.efeitos[jogador]])}\n")
            else:
                del self.efeitos[jogador]  

        self.efeitos_box.configure(state="disabled")
        
    def remover_selecionado(self):
        try:
            index = self.lista_box.index("insert").split(".")[0]  # Obtém a linha selecionada
            if index.isdigit():
                index = int(index) - 1
                if 0 <= index < len(self.jogadores):
                    del self.jogadores[index]
                    self.atualizar_lista()
        except:
            messagebox.showwarning("Aviso", "Selecione um jogador para remover.")
        
    def apagar_lista(self):
        self.jogadores.clear()
        self.efeitos.clear()
        self.rodada = 1
        self.indice_atual = 0
        self.atualizar_lista()
        self.atualizar_efeitos()
        self.label_rodada.configure(text="Rodada: 1")

if __name__ == "__main__":
    root = ctk.CTk()
    app = OrdemIniciativaApp(root)
    root.mainloop()
