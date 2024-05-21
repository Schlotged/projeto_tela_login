from tkinter import *
import tkinter
import tkinter as tk
from tkinter import ttk
from tkinter import messagebox
# from files import WINDOW_ICON_PATH
from validacao_usuario import ValidationLogin
from tela import Window_main
from funcoes import FuncoesValidacao
from time import sleep
import os
from datetime import datetime
import requests

# Classe da janela de login

class LoginWindow(FuncoesValidacao):
    def __init__(self):
        super().__init__()
        self.janela = Tk()
        self.login()
        self.screen()
        self.loginScreen()
        self.footer()
        self.validation_password = FuncoesValidacao()

        

   
    def login(self):
        self.janela.title("Login")
        self.janela.geometry("300x200")

        self.janela.configure(background="lightblue")
        
    def screen(self):
        self.janela.title("Login")
        self.janela.resizable(True, True)
        
        largura = 680
        altura = 650
         
        x_geral = (self.janela.winfo_screenwidth() - largura) // 2
        y_geral = (self.janela.winfo_screenheight() - altura) // 2
        self.janela.geometry(f'{largura}x{altura}+{x_geral}+{y_geral}')

    def loginScreen(self):
        self.frame1 = ttk.Frame(self.janela, padding=60, border=78)
        self.frame1.pack(expand=1)
        self.frame1.configure(style='Custom.TFrame')
        
        self.style = ttk.Style()
        self.style.configure('Custom.TFrame',
        background="#FFF",
        )
                
        # Cria o rótulo e a entrada para o login
        current_dir = os.path.dirname(os.path.abspath(__file__))
        # Define o caminho completo para o arquivo de imagem
        WINDOW_ICON_PATH = os.path.join(current_dir, "assests\\LOGOPARAZIMBRA")
        
        img = tk.PhotoImage(file=f"{WINDOW_ICON_PATH}.png")  # Insira o caminho para sua imagem
        self.senha_oculta = True
        self.input_password = tk.StringVar()

        # Exibe a imagem
        image_label = ttk.Label(self.frame1, image=img, background='white')
        image_label.photo = img  # Mantém uma referência para evitar a coleta de lixo
        image_label.grid(row=0, column=0, columnspan=2, pady=10)

        label_login = ttk.Label(self.frame1, text='Login', font=("Arial", 12), background="#FFF")
        label_login.grid(row=1, column=0, pady=(10, 0), padx=10, sticky='w', columnspan=2)
        
        self.input_login = ttk.Entry(self.frame1, width=30, font=16)
        self.input_login.grid(row=2, column=0, pady=(0, 5), padx=10, sticky='news', columnspan=2)

        # Cria o rótulo e a entrada para a senha
        label_password = ttk.Label(self.frame1, text='Password', font=("Arial", 12), background="#FFF")
        label_password.grid(row=3, column=0, pady=5, padx=10, sticky='w', columnspan=2)
        
        self.input_password = ttk.Entry(self.frame1, width=30, font=16,  textvariable=self.input_password, show="*")
        self.input_password.grid(row=4, column=0, padx=10, sticky='ew', columnspan=2)
        self.input_password.bind("<Return>", self.on_enter_pressed)
        
        imagem = tk.PhotoImage(file="assests\\show-alt-regular-24.png")
        self.show_password = ttk.Button(self.frame1, width=2,image=imagem, command=self.toggle_password)
        self.show_password.image = imagem
        self.show_password.grid(row=4, column=3,padx=2)
        
        style = ttk.Style()
        style.configure("BotaoRedondo.TButton",
                borderwidth=10,
                background="blue",  # Define a cor de fundo como branco
        )
        
        self.show_password.configure(style="BotaoRedondo.TButton")

        # Cria os botões
        button_reset_password = tk.Button(self.frame1, text='Resete sua senha', background='lightblue', font=("Calibri", 13), width=15)
        button_reset_password.grid(row=5, column=0, pady=5, padx=10)
        
        button_register = tk.Button(self.frame1, text='Cadastre-se', background='lightblue', font=("Calibri", 13), width=15, command=self.window_register)
        button_register.grid(row=5, column=1, pady=5, padx=10)

        button_login = ttk.Button(self.frame1, text='Login', command=self.switch_window)
        button_login.grid(row=6, column=0, pady=5, columnspan=2, sticky='news')
        button_login.configure(style="Custom.TButton", width=20)

    def on_enter_pressed(self, event):
        self.switch_window()
    
    def footer(self):
                # Cria o rodapé
        self.frame_rodape = ttk.Frame(self.janela)
        self.frame_rodape.pack(side='bottom', fill='x')

        # Adiciona widgets ao rodapé
        self.label_status = ttk.Label(self.frame_rodape, text='Status: Conectar', anchor='w')
        self.label_status.pack(side='left', padx=5, pady=5, fill='x')

        button_fechar = ttk.Button(self.frame_rodape, text='Fechar', command=self.janela.quit)
        button_fechar.pack(side='right', padx=5, pady=5)
        
        self.style = ttk.Style()
        self.style.configure("Custom.TButton", 
        font=("Helvetica", 12),
        )


    def window_register(self):
        self.frame1.destroy()
        
        self.frame2_register = ttk.Frame(self.janela, padding=50, border=82)
        self.frame2_register.pack(expand=1)
        self.frame2_register.configure(style='Custom.TFrame')
        
        self.style = ttk.Style()
        self.style.configure('Custom.TFrame',
        background="#FFF",
        )
        
        self.input_password_register = tk.StringVar()
        # Cria o rótulo e a entrada para o login
        current_dir = os.path.dirname(os.path.abspath(__file__))
        # Define o caminho completo para o arquivo de imagem
        WINDOW_ICON_PATH = os.path.join(current_dir, "assests\\LOGOPARAZIMBRA")
        
        img = tk.PhotoImage(file=f"{WINDOW_ICON_PATH}.png")  # Insira o caminho para sua imagem
        image_label = ttk.Label(self.frame2_register, image=img, background='white')
        image_label.photo = img  # Mantém uma referência para evitar a coleta de lixo
        image_label.grid(row=0, column=0, pady=10, columnspan=2)

        label_register = ttk.Label(self.frame2_register, text='Usuário', font=("Arial", 12), background="#FFF")
        label_register.grid(row=1, column=0, pady=(10, 0), padx=10, sticky='ew', columnspan=2)

        self.input_usuario_register = ttk.Entry(self.frame2_register,  font=16)
        self.input_usuario_register.grid(row=2, column=0, pady=(0, 5), padx=10, sticky='news', columnspan=2)

        # Cria o rótulo e a entrada para a senha
        label_password_register = ttk.Label(self.frame2_register, text='Senha', font=("Arial", 12), background="#FFF")
        label_password_register.grid(row=3, column=0, pady=5, padx=10, sticky='ew', columnspan=2)

        self.input_password_register = ttk.Entry(self.frame2_register,  font=16,textvariable=self.input_password_register, show="*")
        self.input_password_register.grid(row=4, column=0, padx=10, sticky='ew', columnspan=2)
        
        # Cria o rótulo e a entrada para a senha
        label_password_confirm_register = ttk.Label(self.frame2_register, text='Confirme a Senha', font=("Arial", 12), background="#FFF")
        label_password_confirm_register.grid(row=5, column=0, pady=5, padx=10, sticky='ew', columnspan=2)

        self.input_password_confirm_register = ttk.Entry(self.frame2_register,  font=16,textvariable=self.input_password_register, show="*")
        self.input_password_confirm_register.grid(row=6, column=0, padx=10, sticky='ew', columnspan=2)
        
        imagem = tk.PhotoImage(file=r"assests\show-alt-regular-24.png")
        self.show_password_register = ttk.Button(self.frame2_register, width=2,image=imagem, command=self.toggle_password_register)
        self.show_password_register.image = imagem
        self.show_password_register.grid(row=4, column=2,padx=2)
        style = ttk.Style()
        style.configure("BotaoRedondo.TButton",
                borderwidth=10,
                background="blue",  # Define a cor de fundo como branco
        )
        
        self.show_password_register.configure(style="BotaoRedondo.TButton")
        
        list_setor = ["", "Agendamento", "Comparecimento"]
        self.setor_colaborador = ttk.Combobox(self.frame2_register, value=list_setor, font=("Arial", 12))
        self.setor_colaborador.grid(row=7, column=0, pady=5, padx=10, sticky='ew', columnspan=2)
        
        
        button_back_login = ttk.Button(self.frame2_register, text='Voltar ao Login', command=self.show_login)
        button_back_login.grid(row=8, column=0, pady=5, padx=5)
        button_back_login.configure(style="Custom.TButton", width=15, padding=(3,3))

        button_login = ttk.Button(self.frame2_register, text='Salvar', command=self.confirm_password)
        button_login.grid(row=8, column=1, pady=5)
        button_login.configure(style="Custom.TButton", width=15, padding=(3,3))
    
    def show_login(self):
        self.frame2_register.destroy()
        self.loginScreen()
    
    def toggle_password(self):
        # Alternar entre mostrar e ocultar a senha
        if self.senha_oculta:
            self.input_password.config(show="")
            self.show_password.config(text="Ocultar Senha")
        else:
            self.input_password.config(show="*")
            self.show_password.config(text="Mostrar Senha")

        # Inverter o estado da senha
        self.senha_oculta = not self.senha_oculta
    
    def toggle_password_register(self):
        # Alternar entre mostrar e ocultar a senha
        if self.senha_oculta:
            self.input_password_register.config(show="")
            self.show_password_register.config(text="Ocultar Senha")
        else:
            self.input_password_register.config(show="*")
            self.show_password_register.config(text="Mostrar Senha")

        # Inverter o estado da senha
        self.senha_oculta = not self.senha_oculta
    
    def dados_login(self):
        usuario_dado = self.input_login.get()
        senha_dada = self.input_password.get()
        
        return usuario_dado, senha_dada

    def switch_window(self):
        # mongo_uri = 'mongodb+srv://admin:Schlot28@cluster0.stloyio.mongodb.net/'
        # db_name = 'users'  # Nome do banco de dados
        # secret_password = "mqFjCeoSew5TYkyOfFOxJoW4PUgMn3V6uQA7uWt7ePI"
        
        mongo_uri,db_name,secret_password = self.validation_password.info_mongodb()
        validacao = ValidationLogin()
        
        validacao.validacao_dados(Window_main, mongo_uri, db_name)
        
        usuario, senha = self.dados_login()
        
        validacao.login(usuario, senha, secret_password, self.janela)

    def confirm_password(self):
        
        mongo_uri,db_name,secret_password = self.validation_password.info_mongodb()
        
        validacao = ValidationLogin()
        
        validacao.validacao_dados(Window_main, mongo_uri, db_name)
        
        usuario_add = self.input_usuario_register.get()
        senha_add = self.input_password_register.get()
        
        data_criado = datetime.now().strftime('%d/%m/%Y')
        
        resultado = self.validation_password.validacao_senha(self.input_password_register,self.input_password_confirm_register)
        
        if resultado:
            messagebox.showinfo('Sucesso', 'Senhas são iguais')
            
            validacao.register(usuario_add,senha_add, data_criado,self.janela)
        else:
            messagebox.showerror('Erro', 'Senhas não são iguais')

