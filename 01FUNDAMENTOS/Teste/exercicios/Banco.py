from datetime import datetime
import tkinter as tk
from tkinter import ttk, messagebox


#ABSTRAÇÃO

class Conta:
    """Classe base que representa uma conta bancária."""

    def __init__(self, numero, cliente, documento, saldo=0.0):
        self._numero = numero
        self._cliente = cliente
        self._documento = documento
        self._saldo = saldo
        self._extrato = []

        self._registrar_transacao("Abertura de conta", saldo)


    @property
    def numero(self):
        return self._numero

    @property
    def cliente(self):
        return self._cliente

    @property
    def documento(self):
        return self._documento

    @property
    def saldo(self):
        return self._saldo

    @property
    def tipo(self):
        return "Conta"

    #ENCAPSULAMENTO
    def _registrar_transacao(self, descricao, valor):
        agora = datetime.now().strftime("%d/%m/%Y %H:%M:%S")

        self._extrato.append(
            f"{agora} - {descricao}: R$ {valor:.2f}"
        )

    def depositar(self, valor):
        if valor <= 0:
            return False, "O valor deve ser maior que zero."

        self._saldo += valor

        self._registrar_transacao(
            "Depósito",
            valor
        )

        return True, "Depósito realizado com sucesso!"

    def sacar(self, valor):
        if valor <= 0:
            return False, "O valor deve ser maior que zero."

        if valor > self._saldo:
            return False, "Saldo insuficiente!"

        self._saldo -= valor

        self._registrar_transacao(
            "Saque",
            -valor
        )

        return True, "Saque realizado com sucesso!"

    def transferir(self, destino, valor):

        if destino.numero == self._numero:
            return False, "Não é possível transferir para a própria conta."

        if valor <= 0:
            return False, "O valor deve ser maior que zero."

        if valor > self._saldo:
            return False, "Saldo insuficiente!"

        self._saldo -= valor
        destino._saldo += valor

        self._registrar_transacao(
            f"Transferência enviada (conta {destino.numero})",
            -valor
        )

        destino._registrar_transacao(
            f"Transferência recebida (conta {self._numero})",
            valor
        )

        return True, "Transferência realizada com sucesso!"

    def obter_extrato(self):
        return self._extrato


#HERANÇA

class ContaPF(Conta):
    """Conta de Pessoa Física."""

    def __init__(self, numero, cliente, cpf, idade, saldo=0.0):
        super().__init__(numero,cliente,cpf,saldo)

        self._idade = idade

    @property
    def idade(self):
        return self._idade

    @property
    def tipo(self):
        return "PF"


class ContaPJ(Conta):
    """Conta de Pessoa Jurídica."""

    def __init__(self, numero, empresa, cnpj, saldo=0.0):
        super().__init__(
            numero,
            empresa,
            cnpj,
            saldo
        )

    @property
    def tipo(self):
        return "PJ"

# BANCO

class Banco:
    """Classe responsável pelo gerenciamento das contas."""

    LIMITE_CLIENTES = 5
    NUMERO_INICIAL = 123456

    def __init__(self):
        self._contas = []
        self._proximo_numero = self.NUMERO_INICIAL

    # ABSTRAÇÃO
    @property
    def total_contas(self):
        return len(self._contas)

    def limite_atingido(self):
        return self.total_contas >= self.LIMITE_CLIENTES

    @staticmethod
    def validar_cpf(cpf):
        cpf = cpf.replace(".", "").replace("-", "")

        if len(cpf) != 11 :
            return False
        if cpf == cpf[0] * 11:
            return False

        soma = 0

        for i in range(9):
            soma += int(cpf[i]) * (10 - i)

        resto = soma % 11

        if resto < 2:
            digito = 0
        else:
            digito = 11 - resto

        if digito != int(cpf[9]):
            return False

        soma = 0

        for i in range(10):
            soma += int(cpf[i]) * (11 - i)

        resto = soma % 11

        if resto < 2:
            segundo = 0
        else:
            segundo = 11 - resto

        if segundo != int(cpf[10]):
            return False

        return True

    @staticmethod
    def validar_cnpj(cnpj):
        return len(cnpj) == 14 and cnpj.isdigit()

    def cadastrar_pf(self, cpf, cliente, idade, saldo):

        if self.limite_atingido():
            return None

        conta = ContaPF(
            self._proximo_numero,
            cliente,
            cpf,
            idade,
            saldo
        )

        self._contas.append(conta)
        self._proximo_numero += 1

        return conta

    def cadastrar_pj(self, cnpj, empresa, saldo):

        if self.limite_atingido():
            return None

        conta = ContaPJ(
            self._proximo_numero,
            empresa,
            cnpj,
            saldo
        )

        self._contas.append(conta)
        self._proximo_numero += 1

        return conta

    def buscar_conta(self, numero):

        for conta in self._contas:

            if conta.numero == numero:
                return conta

        return None


    def listar_contas(self):
        return self._contas

# INTERFACE GRÁFICA

class InterfaceGrafica:
    """Classe responsável pela interface gráfica do sistema."""

    def __init__(self, banco):

        self.banco = banco

        self.janela = tk.Tk()

        self.janela.title("Sistema Bancário")
        self.janela.geometry("900x620")
        self.janela.minsize(820, 560)

        self.configurar_estilo()
        self.criar_interface()

    # CONFIGURAÇÃO

    def configurar_estilo(self):

        estilo = ttk.Style()

        estilo.theme_use("clam")

        estilo.configure("Titulo.TLabel",font=("Arial", 24, "bold"),foreground="#ffffff",background="#17365D")
        estilo.configure("Subtitulo.TLabel",font=("Arial", 13, "bold"),foreground="#17365D")
        estilo.configure("Botao.TButton",font=("Arial", 11, "bold"),padding=10)

    # TELA PRINCIPAL

    def criar_interface(self):

        # Cabeçalho
        cabecalho = tk.Frame(self.janela,bg="#17365D",height=90)

        cabecalho.pack(fill="x")

        titulo = tk.Label(cabecalho,text="🏦 SISTEMA BANCÁRIO",font=("Arial", 24, "bold"),fg="white",bg="#17365D")
        titulo.pack(pady=25)

        conteudo = tk.Frame(self.janela,bg="#F2F5F9")

        conteudo.pack(fill="both",expand=True)

        texto = tk.Label(conteudo,text="Escolha uma operação",font=("Arial", 18, "bold"),bg="#F2F5F9",fg="#17365D")
        texto.pack(pady=30)

        botoes = tk.Frame(conteudo,bg="#F2F5F9")

        botoes.pack()

        self.criar_botao(botoes,"👤 Cadastro PF/PJ",self.tela_cadastro,0,0)
        self.criar_botao(botoes,"💰 Operações",self.tela_operacoes,0,1)
        self.criar_botao(botoes,"📋 Contas cadastradas",self.tela_contas,1,0)
        self.criar_botao(botoes,"📄 Extrato",self.tela_extrato,1,1)
        self.criar_botao(botoes,"❌ Sair",self.janela.destroy,2,0)

        rodape = tk.Label(conteudo,text="Sistema desenvolvido utilizando Programação Orientada a Objetos",
            font=("Arial", 9),bg="#F2F5F9",fg="#777777")
        rodape.pack(side="bottom",pady=15)

    def criar_botao(self,frame,texto,comando,linha,coluna):

        botao = tk.Button(frame,text=texto,command=comando,width=25,height=3,
            font=("Arial", 11, "bold"),bg="#1F5A94",fg="white",activebackground="#17446F",
            activeforeground="white",relief="flat",cursor="hand2")

        botao.grid(row=linha,column=coluna,padx=15,pady=15)

    # TELA DE CADASTRO

    def tela_cadastro(self):

        janela = tk.Toplevel(self.janela)

        janela.title("Cadastro de Conta")
        janela.geometry("500x550")
        janela.configure(bg="#F2F5F9")

        tk.Label(janela,text="Cadastro de Conta",font=("Arial", 20, "bold"),bg="#F2F5F9",fg="#17365D").pack(pady=20)

        tk.Label(janela,text="Tipo de conta:",bg="#F2F5F9",font=("Arial", 11)).pack()

        tipo = ttk.Combobox(janela,values=["PF", "PJ"],state="readonly",width=30)

        tipo.pack(pady=5)
        tipo.set("PF")

        tk.Label(janela,text="CPF/CNPJ:",bg="#F2F5F9").pack()

        documento = tk.Entry(janela,width=33)

        documento.pack(pady=5)

        # Nome
        tk.Label(
            janela,
            text="Nome/Empresa:",
            bg="#F2F5F9"
        ).pack()

        nome = tk.Entry(
            janela,
            width=33
        )

        nome.pack(pady=5)

        # Idade
        label_idade = tk.Label(
            janela,
            text="Idade:",
            bg="#F2F5F9"
        )

        label_idade.pack()

        idade = tk.Entry(
            janela,
            width=33
        )

        idade.pack(pady=5)

        # Saldo
        tk.Label(
            janela,
            text="Saldo inicial:",
            bg="#F2F5F9"
        ).pack()

        saldo = tk.Entry(
            janela,
            width=33
        )

        saldo.pack(pady=5)

        def atualizar_campos(event=None):

            if tipo.get() == "PF":

                label_idade.pack()
                idade.pack(pady=5)

            else:

                label_idade.pack_forget()
                idade.pack_forget()

        tipo.bind(
            "<<ComboboxSelected>>",
            atualizar_campos
        )

        def cadastrar():

            if self.banco.limite_atingido():

                messagebox.showerror(
                    "Erro",
                    "Limite de 5 contas atingido."
                )

                return

            tipo_conta = tipo.get()
            doc = documento.get().strip()
            cliente = nome.get().strip()

            if not doc or not cliente:

                messagebox.showerror(
                    "Erro",
                    "Preencha todos os campos obrigatórios."
                )

                return

            try:
                valor_saldo = float(
                    saldo.get().replace(",", ".")
                )

                if valor_saldo < 0:
                    raise ValueError

            except ValueError:

                messagebox.showerror(
                    "Erro",
                    "Informe um saldo válido."
                )

                return

            if tipo_conta == "PF":

                if not Banco.validar_cpf(doc):

                    messagebox.showerror(
                        "Erro",
                        "CPF deve possuir exatamente 11 números."
                    )

                    return

                try:
                    valor_idade = int(
                        idade.get()
                    )

                except ValueError:

                    messagebox.showerror(
                        "Erro",
                        "Informe uma idade válida."
                    )

                    return

                if valor_idade < 18:

                    messagebox.showerror(
                        "Erro",
                        "O cliente deve ser maior de 18 anos."
                    )

                    return

                conta = self.banco.cadastrar_pf(
                    doc,
                    cliente,
                    valor_idade,
                    valor_saldo
                )

            else:

                if not Banco.validar_cnpj(doc):

                    messagebox.showerror(
                        "Erro",
                        "CNPJ deve possuir exatamente 14 números."
                    )

                    return

                conta = self.banco.cadastrar_pj(
                    doc,
                    cliente,
                    valor_saldo
                )

            messagebox.showinfo(
                "Sucesso",
                f"Conta cadastrada!\n\n"
                f"Número: {conta.numero}\n"
                f"Cliente: {conta.cliente}"
            )

            janela.destroy()

        tk.Button(
            janela,
            text="CADASTRAR",
            command=cadastrar,
            bg="#198754",
            fg="white",
            font=("Arial", 11, "bold"),
            width=25,
            height=2
        ).pack(pady=25)

    # TELA DE OPERAÇÕES

    def tela_operacoes(self):

        janela = tk.Toplevel(self.janela)

        janela.title("Operações Bancárias")
        janela.geometry("500x500")
        janela.configure(bg="#F2F5F9")

        tk.Label(
            janela,
            text="Operações Bancárias",
            font=("Arial", 20, "bold"),
            bg="#F2F5F9",
            fg="#17365D"
        ).pack(pady=20)

        # Conta
        tk.Label(
            janela,
            text="Número da conta:",
            bg="#F2F5F9"
        ).pack()

        numero = tk.Entry(
            janela,
            width=30
        )

        numero.pack(pady=5)

        # Operação
        tk.Label(
            janela,
            text="Operação:",
            bg="#F2F5F9"
        ).pack()

        operacao = ttk.Combobox(
            janela,
            values=[
                "Depósito",
                "Saque",
                "Transferência"
            ],
            state="readonly",
            width=28
        )

        operacao.pack(pady=5)
        operacao.set("Depósito")

        # Destino
        label_destino = tk.Label(
            janela,
            text="Conta de destino:",
            bg="#F2F5F9"
        )

        destino = tk.Entry(
            janela,
            width=30
        )

        # Valor
        tk.Label(
            janela,
            text="Valor:",
            bg="#F2F5F9"
        ).pack(pady=(15, 0))

        valor = tk.Entry(
            janela,
            width=30
        )

        valor.pack(pady=5)

        def alterar_campos(event=None):

            if operacao.get() == "Transferência":

                label_destino.pack()
                destino.pack(pady=5)

            else:

                label_destino.pack_forget()
                destino.pack_forget()

        operacao.bind(
            "<<ComboboxSelected>>",
            alterar_campos
        )

        def executar():

            try:

                numero_conta = int(
                    numero.get()
                )

                valor_operacao = float(
                    valor.get().replace(",", ".")
                )

            except ValueError:

                messagebox.showerror(
                    "Erro",
                    "Digite números válidos."
                )

                return

            conta = self.banco.buscar_conta(
                numero_conta
            )

            if conta is None:

                messagebox.showerror(
                    "Erro",
                    "Conta não encontrada."
                )

                return

            escolha = operacao.get()

            if escolha == "Depósito":

                sucesso, mensagem = conta.depositar(
                    valor_operacao
                )

            elif escolha == "Saque":

                sucesso, mensagem = conta.sacar(
                    valor_operacao
                )

            else:

                try:

                    numero_destino = int(
                        destino.get()
                    )

                except ValueError:

                    messagebox.showerror(
                        "Erro",
                        "Conta de destino inválida."
                    )

                    return

                conta_destino = self.banco.buscar_conta(
                    numero_destino
                )

                if conta_destino is None:

                    messagebox.showerror(
                        "Erro",
                        "Conta de destino não encontrada."
                    )

                    return

                sucesso, mensagem = conta.transferir(
                    conta_destino,
                    valor_operacao
                )

            if sucesso:

                messagebox.showinfo(
                    "Sucesso",
                    f"{mensagem}\n\n"
                    f"Saldo atual: R$ {conta.saldo:.2f}"
                )

                janela.destroy()

            else:

                messagebox.showerror(
                    "Erro",
                    mensagem
                )

        tk.Button(
            janela,
            text="REALIZAR OPERAÇÃO",
            command=executar,
            bg="#1F5A94",
            fg="white",
            font=("Arial", 11, "bold"),
            width=25,
            height=2
        ).pack(pady=25)

    # TELA DE CONTAS

    def tela_contas(self):

        janela = tk.Toplevel(self.janela)

        janela.title("Contas Cadastradas")
        janela.geometry("750x450")

        tk.Label(
            janela,
            text="Contas Cadastradas",
            font=("Arial", 20, "bold"),
            fg="#17365D"
        ).pack(pady=15)

        colunas = (
            "Número",
            "Tipo",
            "Cliente",
            "Documento",
            "Saldo"
        )

        tabela = ttk.Treeview(
            janela,
            columns=colunas,
            show="headings"
        )

        for coluna in colunas:

            tabela.heading(
                coluna,
                text=coluna
            )

            tabela.column(
                coluna,
                width=130
            )

        tabela.pack(
            fill="both",
            expand=True,
            padx=20,
            pady=10
        )

        for conta in self.banco.listar_contas():

            tabela.insert(
                "",
                "end",
                values=(
                    conta.numero,
                    conta.tipo,
                    conta.cliente,
                    conta.documento,
                    f"R$ {conta.saldo:.2f}"
                )
            )

    # TELA DE EXTRATO

    def tela_extrato(self):

        janela = tk.Toplevel(self.janela)

        janela.title("Extrato Bancário")
        janela.geometry("700x500")

        tk.Label(
            janela,
            text="Extrato Bancário",
            font=("Arial", 20, "bold"),
            fg="#17365D"
        ).pack(pady=15)

        frame_topo = tk.Frame(janela)
        frame_topo.pack()

        tk.Label(
            frame_topo,
            text="Número da conta:"
        ).pack(side="left")

        numero = tk.Entry(
            frame_topo,
            width=20
        )

        numero.pack(
            side="left",
            padx=10
        )

        texto = tk.Text(
            janela,
            width=80,
            height=20,
            font=("Courier New", 10)
        )

        texto.pack(
            padx=20,
            pady=20
        )

        def consultar():

            try:

                numero_conta = int(
                    numero.get()
                )

            except ValueError:

                messagebox.showerror(
                    "Erro",
                    "Número da conta inválido."
                )

                return

            conta = self.banco.buscar_conta(
                numero_conta
            )

            if conta is None:

                messagebox.showerror(
                    "Erro",
                    "Conta não encontrada."
                )

                return

            texto.delete(
                "1.0",
                tk.END
            )

            texto.insert(
                tk.END,
                f"EXTRATO DA CONTA {conta.numero}\n"
            )

            texto.insert(
                tk.END,
                "=" * 70 + "\n\n"
            )

            for movimentacao in conta.obter_extrato():

                texto.insert(
                    tk.END,
                    movimentacao + "\n"
                )

            texto.insert(
                tk.END,
                "\n"
                + "=" * 70
                + "\n"
            )

            texto.insert(
                tk.END,
                f"SALDO ATUAL: R$ {conta.saldo:.2f}"
            )

        tk.Button(
            frame_topo,
            text="Consultar",
            command=consultar,
            bg="#1F5A94",
            fg="white",
            font=("Arial", 10, "bold")
        ).pack(
            side="left"
        )

    # EXECUTAR

    def executar(self):

        self.janela.mainloop()

# PROGRAMA PRINCIPAL

if __name__ == "__main__":

    banco = Banco()

    sistema = InterfaceGrafica(
        banco
    )

    sistema.executar()
