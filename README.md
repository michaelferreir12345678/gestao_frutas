# Portal da Folha

Bem-vindo ao Portal da Folha! Este é um sistema para gerenciamento de folha de pagamento e visualização de dados relacionados.

## Funcionalidades

- Login e Autenticação de Usuários
- Visualização e Gerenciamento de Frutas
- Gerenciamento de Vendas
- Relatórios de Vendas
- Controle de Acessos

## Tecnologias Utilizadas

- **Frontend**: React, PrimeReact, Axios
- **Backend**: Django, Django REST Framework
- **Banco de Dados**: SQLite (pode ser alterado para outro SGBD)
- **Autenticação**: JWT (JSON Web Token)

## Requisitos

- Node.js (v14 ou superior)
- Python (v3.8 ou superior)
- Django (v3.2 ou superior)

## Instalação

### Backend

1. Clone o repositório:
    ```bash
    git clone https://github.com/seu-usuario/seu-repositorio.git
    cd seu-repositorio
    ```

2. Crie e ative um ambiente virtual:
    ```bash
    python -m venv venv
    source venv/bin/activate  # No Windows: venv\Scripts\activate
    ```

3. Instale as dependências:
    ```bash
    pip install -r requirements.txt
    ```

4. Configure o banco de dados e aplique as migrações:
    ```bash
    python manage.py migrate
    ```

5. Crie um superusuário:
    ```bash
    python manage.py createsuperuser
    ```

6. Inicie o servidor de desenvolvimento:
    ```bash
    python manage.py runserver
    ```

### Frontend

1. Vá para o diretório `frontend`:
    ```bash
    cd frontend
    ```

2. Instale as dependências:
    ```bash
    npm install
    ```

3. Inicie o servidor de desenvolvimento:
    ```bash
    npm start
    ```

## Uso

### Autenticação

Para acessar as rotas protegidas, primeiro faça login no sistema. Use as credenciais criadas durante a configuração do superusuário.

### Lista de Frutas

Após logar, você poderá acessar a lista de frutas na aplicação. Vá para a página `Lista de Frutas` para visualizar todas as frutas cadastradas no sistema.

## Rotas da API

### Autenticação

- **POST /api/token/**: Obtém tokens de acesso e refresh.
    ```json
    {
        "username": "seu-usuario",
        "password": "sua-senha"
    }
    ```

### Frutas

- **GET /api/frutas/**: Lista todas as frutas.
- **POST /api/frutas/**: Cria uma nova fruta.
- **GET /api/frutas/{id}/**: Obtém detalhes de uma fruta específica.
- **PUT /api/frutas/{id}/**: Atualiza uma fruta específica.
- **DELETE /api/frutas/{id}/**: Deleta uma fruta específica.

### Vendas

- **GET /api/vendas/**: Lista todas as vendas.
- **POST /api/vendas/**: Cria uma nova venda.
- **GET /api/vendas/{id}/**: Obtém detalhes de uma venda específica.

## Testes

Para rodar os testes automatizados, utilize o comando:
```bash
python manage.py test
