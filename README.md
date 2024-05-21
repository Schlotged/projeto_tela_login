<!DOCTYPE html>
<html lang="pt-BR">
<head>

<body>
    <h1>Projeto de Tela de Login com Python e MongoDB</h1>

  <p>Este projeto implementa uma tela de login utilizando Python e a biblioteca tkinter para a interface gráfica. A validação do usuário é realizada através de um banco de dados MongoDB. O projeto inclui funcionalidades de login e cadastro de novos usuários.</p>

  <h2>Funcionalidades</h2>
  <ul>
      <li><strong>Tela de Login:</strong>
          <ul>
              <li>Usuário insere o nome de usuário e a senha.</li>
              <li>Validação de credenciais utilizando MongoDB.</li>
              <li>Botão "Entrar" para avançar para a próxima tela em caso de sucesso.</li>
              <li>Botão "Cadastre-se" para abrir a tela de cadastro.</li>
          </ul>
      </li>
      <li><strong>Tela de Cadastro:</strong>
          <ul>
              <li>Formulário para inserção de novos dados de usuário.</li>
              <li>Botão para salvar o novo usuário no banco de dados MongoDB.</li>
          </ul>
      </li>
  </ul>

  <h2>Tecnologias Utilizadas</h2>
  <ul>
      <li><strong>Python:</strong> Linguagem de programação principal.</li>
      <li><strong>tkinter:</strong> Biblioteca padrão do Python para interfaces gráficas.</li>
      <li><strong>pymongo:</strong> Biblioteca para interagir com o MongoDB.</li>
  </ul>

  <h2>Como Executar o Projeto</h2>
  <h3>Pré-requisitos</h3>
  <ul>
      <li>Python 3 instalado.</li>
      <li>MongoDB instalado e em execução.</li>
      <li>Bibliotecas necessárias instaladas:
          <pre><code>pip install pymongo</code></pre>
      </li>
  </ul>

  <h3>Instruções</h3>
  <ol>
      <li><strong>Clone o repositório:</strong>
          <pre><code>git clone https://github.com/seu_usuario/seu_repositorio.git
cd seu_repositorio</code></pre>
        </li>
        <li><strong>Configurar o MongoDB:</strong>
            <ul>
                <li>Inicie seu servidor MongoDB localmente.</li>
                <li>Crie um banco de dados e uma coleção para armazenar os usuários.</li>
            </ul>
        </li>
        <li><strong>Executar o script:</strong>
            <pre><code>python main.py</code></pre>
        </li>
    </ol>

  <h3>Estrutura do Projeto</h3>
  <pre><code>seu_repositorio/
│
├── main.py                # Script principal para a tela de login e cadastro
├── login.py               # Script para a tela de login
├── validacao_usuario.py   # Script para a conexão e operações com MongoDB
├── README.md              # Documentação do projeto
    
</code></pre>

  <h2>Contribuição</h2>
  <p>Contribuições são bem-vindas! Sinta-se à vontade para abrir issues e pull requests.</p>

  <h2>Licença</h2>
  <p>Este projeto está licenciado sob a licença MIT. Veja o arquivo <code>LICENSE</code> para mais detalhes.</p>
  <p>Tela do Login</p>
  
  ![image](https://github.com/Schlotged/projeto_tela_login/assets/86088828/09042101-adc4-4063-9b3f-745ea0bb403c)

  <p>Tela para Registrar-se</p>
  
  ![image](https://github.com/Schlotged/projeto_tela_login/assets/86088828/f7371077-877c-4fc6-99dd-6bda56bf56cc)

</body>
</html>

