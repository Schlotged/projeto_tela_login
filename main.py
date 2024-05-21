from login import LoginWindow

# Classe que inicia a aplicação

class MainWindow(LoginWindow):

    def __init__(self):
        self.show_login_window()  # Verifica o status de login ao iniciar

    def show_login_window(self):
        login_window = LoginWindow()
        login_window.janela.mainloop()


if __name__ == "__main__":
    app = MainWindow()
