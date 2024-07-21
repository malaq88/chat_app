# Chat Application

## Descrição

Esta é uma aplicação web de chat desenvolvida em Python usando Flask e Flask-SocketIO. O aplicativo permite aos usuários criar e participar de salas de chat temáticas com mensagens em tempo real. Cada sala tem um limite de tempo definido e o layout é responsivo, adequado para acesso em dispositivos móveis.

## Funcionalidades

- **Criação de Salas**: Usuários podem criar salas de chat com temas específicos.
- **Autenticação de Usuários**: Usuários precisam criar uma conta com login e senha para participar das salas.
- **Limitação de Tempo das Salas**: As salas têm um limite de tempo, após o qual todos os usuários são removidos.
- **Mensagens em Tempo Real**: Mensagens são enviadas e recebidas em tempo real usando WebSockets.
- **Layout Responsivo**: A interface é responsiva e acessível em dispositivos móveis.
- **Persistência de Dados**: Informações de usuários e conversas são armazenadas em um banco de dados.

## Tecnologias Utilizadas

- **Python**: Linguagem de programação principal.
- **Flask**: Framework web para Python.
- **Flask-SocketIO**: Extensão para adicionar suporte a WebSockets no Flask.
- **SQLite**: Banco de dados relacional utilizado para persistência de dados.
- **HTML/CSS/JavaScript**: Tecnologias web para a interface do usuário.
- **Bootstrap**: Framework CSS para garantir a responsividade do layout.

## Instalação

1. **Clone o Repositório**

    ```bash
    git clone https://github.com/malaq88/chat_app
    cd chat_app
    ```

2. **Crie um Ambiente Virtual**

    ```bash
    python -m venv venv
    ```

3. **Ative o Ambiente Virtual**

    - No Windows:

      ```bash
      venv\Scripts\activate
      ```

    - No macOS/Linux:

      ```bash
      source venv/bin/activate
      ```

4. **Instale as Dependências**

    ```bash
    pip install -r requirements.txt
    ```

5. **Configure o Banco de Dados**

    O banco de dados será automaticamente criado na primeira execução.

6. **Inicie o Servidor**

    ```bash
    python run.py
    ```

    A aplicação estará disponível em `http://localhost:5000`.

## Uso

1. **Criar uma Conta**: Vá para a página de registro e crie uma conta com um nome de usuário e senha.
2. **Entrar em uma Sala**: Após o login, você poderá criar ou entrar em salas de chat com temas específicos.
3. **Enviar Mensagens**: Digite suas mensagens no formulário e pressione "Send" ou aperte Enter para enviar.

## Estrutura do Projeto

- **app/**: Contém a lógica da aplicação Flask.
  - **__init__.py**: Configuração do Flask e SocketIO.
  - **models.py**: Definição dos modelos de dados.
  - **routes.py**: Definição das rotas da aplicação.
  - **forms.py**: Definição dos formulários.
  - **config.py**: Configurações da aplicação.
- **templates/**: Contém os arquivos de template HTML.
- **static/**: Contém arquivos estáticos como CSS e JavaScript.
- **run.py**: Script para iniciar a aplicação.

## Contribuição

Sinta-se à vontade para contribuir com melhorias. Você pode fazer isso abrindo issues ou enviando pull requests no GitHub.

## Licença

Este projeto está licenciado sob a Licença MIT. Veja o arquivo [LICENSE](LICENSE) para mais detalhes.

## Contato

Para mais informações, entre em contato com [seu_email@dominio.com](mailto:seu_email@dominio.com).

