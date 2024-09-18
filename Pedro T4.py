import tkinter as tk
from tkinter import messagebox, filedialog
import time 

# Função para verificar o login
def verificar_login():
    usuario = entrada_usuario.get()
    senha = entrada_senha.get()
    
    if usuario == "admin" and senha == "1234":  # Login simples para exemplo
        messagebox.showinfo("Sucesso","Login realizado com êxito")
        abrir_menu_principal()
    elif usuario == "pedro" and senha == "4321":
        messagebox.showinfo("Sucesso", "Login realizado com sucesso!")
        abrir_menu_principal()
    else:
        messagebox.showerror("Erro", "Usuário ou senha incorretos")

# Função para abrir a tela principal com opções de Calculadora e Bloco de Notas e cronômetro
def abrir_menu_principal():
    login_janela.destroy()  # Fecha a tela de login
    menu_janela = tk.Tk()
    menu_janela.title("Menu Principal")
    menu_janela.geometry("400x350")

    label_menu = tk.Label(menu_janela, text="Escolha uma aplicação:", font=("Arial", 16))
    label_menu.pack(pady=20)

    botao_calculadora = tk.Button(menu_janela, text="Calculadora", font=("Arial", 14), command=abrir_calculadora)
    botao_calculadora.pack(pady=10)

    botao_bloco_notas = tk.Button(menu_janela, text="Bloco de Notas", font=("Arial", 14), command=abrir_bloco_notas)
    botao_bloco_notas.pack(pady=10)

    botao_cronometro = tk.Button(menu_janela, text="Cronômetro", font=("Arial", 14), command=abrir_cronometro)
    botao_cronometro.pack(pady=10)

    menu_janela.mainloop()

# Função para abrir o cronometro
def abrir_cronometro():
    cronometro_janela = tk.Toplevel()
    cronometro_janela.title("Cronômetro")

    tempo_inicial = [0]  # Lista para armazenar o tempo

    def iniciar_cronometro():
        if tempo_inicial[0] == 0:
            tempo_inicial[0] = time.time()
        atualizar_cronometro()

    def pausar_cronometro():
        tempo_inicial[0] = 0

    def zerar_cronometro():
        tempo_inicial[0] = 0
        label_cronometro.config(text="Tempo: 0.00 segundos")

    def atualizar_cronometro():
        if tempo_inicial[0] != 0:
            tempo_decorrido = time.time() - tempo_inicial[0]
            label_cronometro.config(text="Tempo: {:.2f} segundos".format(tempo_decorrido))
            cronometro_janela.after(100, atualizar_cronometro)

    label_cronometro = tk.Label(cronometro_janela, text="Tempo: 0.00 segundos", font=("Arial", 14))
    label_cronometro.pack(pady=10)

    botao_iniciar = tk.Button(cronometro_janela, text="Iniciar", font=("Arial", 14), command=iniciar_cronometro)
    botao_iniciar.pack(pady=5)

    botao_pausar = tk.Button(cronometro_janela, text="Pausar", font=("Arial", 14), command=pausar_cronometro)
    botao_pausar.pack(pady=5)
    
    botao_zerar = tk.Button(cronometro_janela, text="Zerar", font=("Arial", 14), command=zerar_cronometro)
    botao_zerar.pack(pady=5)

    botao_voltar = tk.Button(cronometro_janela, text="Voltar", font=("Arial", 14), command=cronometro_janela.destroy)
    botao_voltar.pack(pady=10)
    botao_voltar.config(bg="light blue", fg="black")

# Função para abrir a calculadora
def abrir_calculadora():
    calculadora_janela = tk.Toplevel()  # Abre uma nova janela
    calculadora_janela.title("Calculadora")

    # Função para realizar operações matemáticas
    def calcular():
        try:
            resultado = eval(entrada_calculadora.get())
            label_resultado.config(text="Resultado: " + str(resultado))
        except:
            label_resultado.config(text="Erro de cálculo")

    entrada_calculadora = tk.Entry(calculadora_janela, font=("Arial", 14))
    entrada_calculadora.pack(pady=10)

    botao_calcular = tk.Button(calculadora_janela, text="Calcular", font=("Arial", 14), command=calcular)
    botao_calcular.pack(pady=10)

    label_resultado = tk.Label(calculadora_janela, text="Resultado: ", font=("Arial", 14))
    label_resultado.pack(pady=10)

    botao_voltar = tk.Button(calculadora_janela, text="Voltar", font=("Arial", 14), command=calculadora_janela.destroy)
    botao_voltar.pack(pady=10)
    botao_voltar.config(bg="light blue", fg="black")

# Função para abrir o bloco de notas
def abrir_bloco_notas():
    bloco_notas_janela = tk.Toplevel()  # Abre uma nova janela
    bloco_notas_janela.title("Bloco de Notas")

    # Função para salvar o conteúdo em um arquivo
    def salvar_bloco():
        conteudo = texto_bloco_notas.get("1.0", tk.END)
        caminho_arquivo = filedialog.asksaveasfilename(defaultextension=".txt", 
                                                       filetypes=[("Arquivo de Texto", "*.txt"), 
                                                                  ("Todos os arquivos", "*.*")])
        if caminho_arquivo:
            with open(caminho_arquivo, "w") as arquivo:
                arquivo.write(conteudo)
            messagebox.showinfo("Salvo", "Arquivo salvo com sucesso!")

    # Função para abrir um arquivo e carregar o conteúdo no bloco de notas
    def abrir_arquivo():
        caminho_arquivo = filedialog.askopenfilename(defaultextension=".txt", 
                                                     filetypes=[("Arquivo de Texto", "*.txt"), 
                                                                ("Todos os arquivos", "*.*")])
        if caminho_arquivo:
            with open(caminho_arquivo, "r") as arquivo:
                conteudo = arquivo.read()
                texto_bloco_notas.delete("1.0", tk.END)  # Limpa o bloco de notas
                texto_bloco_notas.insert(tk.END, conteudo)  # Insere o conteúdo no bloco de notas

    # Menu para salvar e abrir arquivos
    menu_barra = tk.Menu(bloco_notas_janela)
    bloco_notas_janela.config(menu=menu_barra)

    menu_arquivo = tk.Menu(menu_barra, tearoff=0)
    menu_barra.add_cascade(label="Arquivo", menu=menu_arquivo)
    menu_arquivo.add_command(label="Abrir", command=abrir_arquivo)
    menu_arquivo.add_command(label="Salvar", command=salvar_bloco)

    # Área de texto do bloco de notas
    texto_bloco_notas = tk.Text(bloco_notas_janela, font=("Arial", 12), wrap="word")
    texto_bloco_notas.pack(expand=True, fill="both", padx=10, pady=10)

    botao_voltar = tk.Button(bloco_notas_janela, text="Voltar", font=("Arial", 14), command=bloco_notas_janela.destroy)
    botao_voltar.pack(pady=10)
    botao_voltar.config(bg="light blue", fg="black")

# Configuração da janela de login
login_janela = tk.Tk()
login_janela.title("Login")
login_janela.geometry("350x300")

label_usuario = tk.Label(login_janela, text="Usuário:", font=("Arial", 14))
label_usuario.pack(pady=10)
entrada_usuario = tk.Entry(login_janela, font=("Arial", 14))
entrada_usuario.pack(pady=10)

label_senha = tk.Label(login_janela, text="Senha:", font=("Arial", 14))
label_senha.pack(pady=10)
entrada_senha = tk.Entry(login_janela, show="*", font=("Arial", 14))
entrada_senha.pack(pady=10)

botao_login = tk.Button(login_janela, text="Entrar", font=("Arial", 14), command=verificar_login)
botao_login.pack(pady=20)

login_janela.mainloop()
