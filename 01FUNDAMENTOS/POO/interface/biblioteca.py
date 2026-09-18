import tkinter as tk
from tkinter import ttk, messagebox

# POO - SISTEMA DE BIBLIOTECA
# 4 pilares: Abstração, Encapsulamento, Herança e Polimorfismo


# ABSTRAÇÃO

class Livro:
    def __init__(self, titulo, autor, ano):
        self.titulo = titulo
        self.autor = autor
        self.ano = ano
        self.__disponivel = True  # Encapsulamento

    # Encapsulamento: controlar a disponibilidade por métodos
    def emprestar(self):
        if self.__disponivel:
            self.__disponivel = False
            return True, "Empréstimo realizado com sucesso!"
        return False, "Este livro já está emprestado."

    def devolver(self):
        if not self.__disponivel:
            self.__disponivel = True
            return True, "Devolução realizada com sucesso!"
        return False, "Este livro já está disponível."

    def verificar_disponibilidade(self):
        return self.__disponivel

    def exibir_dados(self):
        status = "Disponível" if self.__disponivel else "Emprestado"
        return f"{self.titulo} | {self.autor} | {self.ano} | {status}"

# HERANÇA

class Usuario:
    def __init__(self, nome, matricula):
        self.nome = nome
        self.matricula = matricula

    # POLIMORFISMO: as classes filhas sobrescrevem este método
    def apresentar(self):
        return f"Usuário: {self.nome} | Matrícula: {self.matricula}"


class Aluno(Usuario):
    def __init__(self, nome, matricula, curso):
        super().__init__(nome, matricula)
        self.curso = curso

    def apresentar(self):
        return f"Aluno: {self.nome} | Matrícula: {self.matricula} | Curso: {self.curso}"


class Professor(Usuario):
    def __init__(self, nome, matricula, disciplina):
        super().__init__(nome, matricula)
        self.disciplina = disciplina

    def apresentar(self):
        return (
            f"Professor: {self.nome} | Matrícula: {self.matricula} | "
            f"Disciplina: {self.disciplina}"
        )


# DESAFIO EXTRA
class Funcionario(Usuario):
    def __init__(self, nome, matricula, cargo):
        super().__init__(nome, matricula)
        self.cargo = cargo

    def apresentar(self):
        return (
            f"Funcionário: {self.nome} | Matrícula: {self.matricula} | "
            f"Cargo: {self.cargo}"
        )

# ABSTRAÇÃO / GERENCIAMENTO

class Biblioteca:
    def __init__(self):
        self.livros = []
        self.usuarios = []

    def adicionar_livro(self, livro):
        self.livros.append(livro)

    def adicionar_usuario(self, usuario):
        self.usuarios.append(usuario)

    def listar_livros(self):
        return self.livros

    def listar_usuarios(self):
        return self.usuarios

    def encontrar_livro(self, indice):
        if 0 <= indice < len(self.livros):
            return self.livros[indice]
        return None

    def encontrar_usuario(self, indice):
        if 0 <= indice < len(self.usuarios):
            return self.usuarios[indice]
        return None

    def realizar_emprestimo(self, indice_livro):
        livro = self.encontrar_livro(indice_livro)
        if livro is None:
            return False, "Livro não encontrado."
        return livro.emprestar()

    def realizar_devolucao(self, indice_livro):
        livro = self.encontrar_livro(indice_livro)
        if livro is None:
            return False, "Livro não encontrado."
        return livro.devolver()

# INTERFACE GRÁFICA

class Aplicacao:
    def __init__(self, janela):
        self.janela = janela
        self.janela.title("BIBLIOTECA POO - Python")
        self.janela.geometry("900x620")
        self.janela.minsize(820, 560)

        self.biblioteca = Biblioteca()

        # Alguns dados iniciais para a tela já aparecer preenchida
        self.biblioteca.adicionar_livro(
            Livro("Dom Casmurro", "Machado de Assis", 1899)
        )
        self.biblioteca.adicionar_livro(
            Livro("O Hobbit", "J. R. R. Tolkien", 1937)
        )

        self.biblioteca.adicionar_usuario(
            Aluno("João", "001", "Desenvolvimento de Sistemas")
        )
        self.biblioteca.adicionar_usuario(
            Professor("Maria", "002", "Programação")
        )

        self.criar_estilo()
        self.tela_principal()

    def criar_estilo(self):
        estilo = ttk.Style()
        try:
            estilo.theme_use("clam")
        except tk.TclError:
            pass

        estilo.configure("Titulo.TLabel", font=("Arial", 24, "bold"))
        estilo.configure("Subtitulo.TLabel", font=("Arial", 12))
        estilo.configure("Botao.TButton", font=("Arial", 11, "bold"), padding=10)
        estilo.configure("Treeview", rowheight=30, font=("Arial", 10))
        estilo.configure("Treeview.Heading", font=("Arial", 10, "bold"))

    def limpar(self):
        for widget in self.janela.winfo_children():
            widget.destroy()

    def cabecalho(self, titulo, subtitulo=""):
        frame = ttk.Frame(self.janela, padding=(25, 20))
        frame.pack(fill="x")

        ttk.Label(frame, text=titulo, style="Titulo.TLabel").pack(anchor="w")
        if subtitulo:
            ttk.Label(frame, text=subtitulo, style="Subtitulo.TLabel").pack(
                anchor="w", pady=(5, 0)
            )

    def botao_voltar(self):
        ttk.Button(
            self.janela,
            text="← Voltar ao menu",
            command=self.tela_principal,
            style="Botao.TButton"
        ).pack(pady=15)


    # TELA PRINCIPAL

    def tela_principal(self):
        self.limpar()

        self.cabecalho(
            "BIBLIOTECA POO",
            "Sistema de Biblioteca desenvolvido com Python e Programação Orientada a Objetos"
        )

        principal = ttk.Frame(self.janela, padding=30)
        principal.pack(expand=True)

        botoes = [
            ("1 - Cadastrar livro", self.tela_cadastrar_livro),
            ("2 - Cadastrar aluno", self.tela_cadastrar_aluno),
            ("3 - Cadastrar professor", self.tela_cadastrar_professor),
            ("4 - Listar livros", self.tela_listar_livros),
            ("5 - Listar usuários", self.tela_listar_usuarios),
            ("6 - Emprestar livro", self.tela_emprestar),
            ("7 - Devolver livro", self.tela_devolver),
            ("8 - Cadastrar funcionário", self.tela_cadastrar_funcionario)
        ]

        for texto, comando in botoes:
            ttk.Button(
                principal,
                text=texto,
                command=comando,
                width=35,
                style="Botao.TButton"
            ).pack(pady=5)

        ttk.Separator(principal).pack(fill="x", pady=12)

        ttk.Button(
            principal,
            text="0 - Sair",
            command=self.janela.destroy,
            width=35,
            style="Botao.TButton"
        ).pack(pady=5)

        ttk.Label(
            self.janela,
            text="POO: Abstração • Encapsulamento • Herança • Polimorfismo",
            font=("Arial", 10, "bold")
        ).pack(side="bottom", pady=12)

    # FUNÇÕES AUXILIARES

    def formulario(self, titulo, campos, salvar_callback):
        self.limpar()
        self.cabecalho(titulo)

        area = ttk.Frame(self.janela, padding=30)
        area.pack(fill="both", expand=True)

        entradas = {}

        for linha, campo in enumerate(campos):
            ttk.Label(
                area, text=campo + ":", font=("Arial", 11, "bold")
            ).grid(row=linha, column=0, sticky="w", pady=10)

            entrada = ttk.Entry(area, width=55, font=("Arial", 11))
            entrada.grid(row=linha, column=1, sticky="ew", pady=10, padx=15)
            entradas[campo] = entrada

        area.columnconfigure(1, weight=1)

        ttk.Button(
            area,
            text="Salvar",
            command=lambda: salvar_callback(entradas),
            style="Botao.TButton"
        ).grid(row=len(campos), column=0, columnspan=2, pady=20)

        self.botao_voltar()

        return entradas

    def valor(self, entradas, nome):
        return entradas[nome].get().strip()


    # CADASTROS

    def tela_cadastrar_livro(self):
        self.formulario(
            "CADASTRAR LIVRO",
            ["Título", "Autor", "Ano"],
            self.salvar_livro
        )

    def salvar_livro(self, entradas):
        titulo = self.valor(entradas, "Título")
        autor = self.valor(entradas, "Autor")
        ano = self.valor(entradas, "Ano")

        if not titulo or not autor or not ano:
            messagebox.showwarning("Atenção", "Preencha todos os campos.")
            return

        try:
            ano = int(ano)
        except ValueError:
            messagebox.showerror("Erro", "O ano deve ser um número.")
            return

        self.biblioteca.adicionar_livro(Livro(titulo, autor, ano))
        messagebox.showinfo("Sucesso", "Livro cadastrado com sucesso!")
        self.tela_principal()

    def tela_cadastrar_aluno(self):
        self.formulario(
            "CADASTRAR ALUNO",
            ["Nome", "Matrícula", "Curso"],
            self.salvar_aluno
        )

    def salvar_aluno(self, entradas):
        nome = self.valor(entradas, "Nome")
        matricula = self.valor(entradas, "Matrícula")
        curso = self.valor(entradas, "Curso")

        if not nome or not matricula or not curso:
            messagebox.showwarning("Atenção", "Preencha todos os campos.")
            return

        self.biblioteca.adicionar_usuario(Aluno(nome, matricula, curso))
        messagebox.showinfo("Sucesso", "Aluno cadastrado com sucesso!")
        self.tela_principal()

    def tela_cadastrar_professor(self):
        self.formulario(
            "CADASTRAR PROFESSOR",
            ["Nome", "Matrícula", "Disciplina"],
            self.salvar_professor
        )

    def salvar_professor(self, entradas):
        nome = self.valor(entradas, "Nome")
        matricula = self.valor(entradas, "Matrícula")
        disciplina = self.valor(entradas, "Disciplina")

        if not nome or not matricula or not disciplina:
            messagebox.showwarning("Atenção", "Preencha todos os campos.")
            return

        self.biblioteca.adicionar_usuario(
            Professor(nome, matricula, disciplina)
        )
        messagebox.showinfo("Sucesso", "Professor cadastrado com sucesso!")
        self.tela_principal()

    def tela_cadastrar_funcionario(self):
        self.formulario(
            "CADASTRAR FUNCIONÁRIO - DESAFIO EXTRA",
            ["Nome", "Matrícula", "Cargo"],
            self.salvar_funcionario
        )

    def salvar_funcionario(self, entradas):
        nome = self.valor(entradas, "Nome")
        matricula = self.valor(entradas, "Matrícula")
        cargo = self.valor(entradas, "Cargo")

        if not nome or not matricula or not cargo:
            messagebox.showwarning("Atenção", "Preencha todos os campos.")
            return

        self.biblioteca.adicionar_usuario(
            Funcionario(nome, matricula, cargo)
        )
        messagebox.showinfo("Sucesso", "Funcionário cadastrado com sucesso!")
        self.tela_principal()

    # LISTAGENS

    def tela_listar_livros(self):
        self.limpar()
        self.cabecalho("LISTA DE LIVROS", "Livros cadastrados na biblioteca")

        frame = ttk.Frame(self.janela, padding=25)
        frame.pack(fill="both", expand=True)

        tabela = ttk.Treeview(
            frame,
            columns=("titulo", "autor", "ano", "status"),
            show="headings"
        )

        tabela.heading("titulo", text="Título")
        tabela.heading("autor", text="Autor")
        tabela.heading("ano", text="Ano")
        tabela.heading("status", text="Status")

        tabela.column("titulo", width=240)
        tabela.column("autor", width=220)
        tabela.column("ano", width=100)
        tabela.column("status", width=150)

        tabela.pack(fill="both", expand=True)

        for livro in self.biblioteca.livros:
            status = (
                "Disponível"
                if livro.verificar_disponibilidade()
                else "Emprestado"
            )
            tabela.insert(
                "", "end",
                values=(livro.titulo, livro.autor, livro.ano, status)
            )

        self.botao_voltar()

    def tela_listar_usuarios(self):
        self.limpar()
        self.cabecalho("LISTA DE USUÁRIOS", "Alunos, professores e funcionários")

        frame = ttk.Frame(self.janela, padding=25)
        frame.pack(fill="both", expand=True)

        tabela = ttk.Treeview(
            frame,
            columns=("tipo", "nome", "matricula", "informacao"),
            show="headings"
        )

        tabela.heading("tipo", text="Tipo")
        tabela.heading("nome", text="Nome")
        tabela.heading("matricula", text="Matrícula")
        tabela.heading("informacao", text="Curso / Disciplina / Cargo")

        tabela.column("tipo", width=130)
        tabela.column("nome", width=180)
        tabela.column("matricula", width=120)
        tabela.column("informacao", width=300)

        tabela.pack(fill="both", expand=True)

        for usuario in self.biblioteca.usuarios:
            if isinstance(usuario, Aluno):
                tipo = "Aluno"
                info = usuario.curso
            elif isinstance(usuario, Professor):
                tipo = "Professor"
                info = usuario.disciplina
            elif isinstance(usuario, Funcionario):
                tipo = "Funcionário"
                info = usuario.cargo
            else:
                tipo = "Usuário"
                info = "-"

            tabela.insert(
                "", "end",
                values=(tipo, usuario.nome, usuario.matricula, info)
            )

        self.botao_voltar()

    # EMPRÉSTIMO E DEVOLUÇÃO

    def escolher_livro(self, titulo, callback):
        self.limpar()
        self.cabecalho(titulo)

        frame = ttk.Frame(self.janela, padding=30)
        frame.pack(fill="both", expand=True)

        if not self.biblioteca.livros:
            ttk.Label(
                frame, text="Nenhum livro cadastrado.",
                font=("Arial", 12)
            ).pack(pady=30)
            self.botao_voltar()
            return

        ttk.Label(
            frame, text="Selecione o livro:",
            font=("Arial", 11, "bold")
        ).pack(anchor="w", pady=5)

        lista = tk.Listbox(frame, font=("Arial", 11), height=10)
        lista.pack(fill="both", expand=True, pady=10)

        for i, livro in enumerate(self.biblioteca.livros):
            status = (
                "Disponível"
                if livro.verificar_disponibilidade()
                else "Emprestado"
            )
            lista.insert(
                "end",
                f"{i + 1} - {livro.titulo} ({status})"
            )

        ttk.Button(
            frame,
            text="Confirmar",
            command=lambda: callback(lista),
            style="Botao.TButton"
        ).pack(pady=10)

        self.botao_voltar()

    def tela_emprestar(self):
        self.escolher_livro(
            "EMPRESTAR LIVRO",
            self.confirmar_emprestimo
        )

    def confirmar_emprestimo(self, lista):
        selecionado = lista.curselection()
        if not selecionado:
            messagebox.showwarning("Atenção", "Selecione um livro.")
            return

        indice = selecionado[0]
        sucesso, mensagem = self.biblioteca.realizar_emprestimo(indice)

        if sucesso:
            messagebox.showinfo("Sucesso", mensagem)
            self.tela_principal()
        else:
            messagebox.showwarning("Atenção", mensagem)

    def tela_devolver(self):
        self.escolher_livro(
            "DEVOLVER LIVRO",
            self.confirmar_devolucao
        )

    def confirmar_devolucao(self, lista):
        selecionado = lista.curselection()
        if not selecionado:
            messagebox.showwarning("Atenção", "Selecione um livro.")
            return

        indice = selecionado[0]
        sucesso, mensagem = self.biblioteca.realizar_devolucao(indice)

        if sucesso:
            messagebox.showinfo("Sucesso", mensagem)
            self.tela_principal()
        else:
            messagebox.showwarning("Atenção", mensagem)


# INICIAR O PROGRAMA
if __name__ == "__main__":
    janela = tk.Tk()
    app = Aplicacao(janela)
    janela.mainloop()