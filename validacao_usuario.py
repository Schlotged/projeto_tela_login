import jwt
import datetime
import pymongo
import tkinter as tk
from tkinter import messagebox
from jwt.exceptions import InvalidTokenError


class MongoDatabase():
    def __init__(self, uri, db_name):
        self.client = pymongo.MongoClient(uri)
        self.db = self.client[db_name]
        self.users = self.db['usuarios']  # coleção de usuários
        self.tokens = self.db['tokens']  # coleção de tokens
        self.logs = self.db['logs']  # coleção de logs

    def get_user(self, username, password):
        return self.users.find_one({'usuario': username, 'password': password})

    def add_user(self, username, password, date_created):
        existing_user = self.get_user(username, password)
        if existing_user:
            messagebox.showerror("Erro", "Usuário já existe!")
            return False
        else:
            self.users.insert_one({'usuario': username, 'password': password, 'data_criacao': date_created})
            messagebox.showinfo("Sucesso", "Usuário criado com sucesso!")
            return True
        
    def set_logged_in(self, username, status):
        self.users.update_one({'usuario': username}, {'$set': {'logged_in': status}})
        if status:  # Se estiver fazendo login
            # Registra o log de login
            self.logs.insert_one({'usuario': username, 'data_hora': datetime.datetime.now().strftime('%d/%m/%Y, %H:%M:%S')})

    def create_token(self, username, secret_key):
        payload = {
            'username': username,
            'exp': datetime.datetime.utcnow() + datetime.timedelta(hours=1)  # Token expira em 1 hora
        }
        token = jwt.encode(payload, secret_key, algorithm='HS256').decode('utf-8')
        self.tokens.insert_one({'username': username, 'token': token})
        return token

    def validate_token(self, token, secret_key):
        try:
            payload = jwt.decode(token, secret_key, algorithms=['HS256'])
            return payload['username']
        except InvalidTokenError:
            return None
    
class ValidationLogin():
    def __init__(self):
        super().__init__()
        self.current_user = None
    
    def validacao_dados(self, screen_login, db_uri, db_name):
        self.screen_login = screen_login
        self.db = MongoDatabase(db_uri, db_name)
    
    def login(self, usuario, senha, secret_password, screen):
        user = self.db.get_user(usuario, senha)
        if user:
            self.current_user = usuario  # Define o usuário atual
            # self.db.set_logged_in(usuario, True)
            print("Login bem-sucedido!")
            # token = self.db.create_token(usuario, secret_password)
            messagebox.showinfo("Login", "Login bem sucedido!")
            screen.destroy()
            self.current_user = usuario
            self.screen_login()
        else:
            messagebox.showerror("Erro de Login", "Credenciais inválidas!")

    def register(self, usuario, senha, data_criação, screen):
        if self.db.add_user(usuario, senha, data_criação):
            screen.destroy()
            self.screen_login()
    
    def logout_screen(self, screen, secret_password):
        screen.destroy()
        print("Deslogado com sucesso!")