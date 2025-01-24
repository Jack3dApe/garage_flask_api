# Garage Flask API - Desenvolvido por Alexandre Rocha e Vasile Zbireanu

O **Garage Flask API** é um sistema modular e escalável desenvolvido para gerenciar uma garagem de reparação automóvel. O sistema foi projetado para realizar operações de CRUD para diversos recursos, incluindo:

- **Clientes**
- **Funcionários**
- **Veículos**
- **Trabalhos**
- **Tarefas**
- **Faturas**
- **Itens de Faturas**
- **Configurações Globais**

A estrutura do projeto foi organizada com base em boas práticas de desenvolvimento, garantindo consistência, reutilização de código e facilidade de manutenção. Além disso, o sistema conta com uma documentação interativa via **Swagger**, facilitando o entendimento e a integração com as APIs.

---

## Estrutura do Projeto

O projeto é organizado em diferentes diretórios e arquivos para manter a separação de responsabilidades:

### 1. Diretório `api/`

Contém as implementações das APIs RESTful para cada recurso. As APIs são registradas e documentadas automaticamente pelo **Flask-RESTx**.

### 2. Diretório `models/`

Define os modelos de dados utilizando **SQLAlchemy**, representando as tabelas do banco de dados e suas relações. Modelos principais incluem:

- **Client**: Informações sobre clientes.
- **Employee**: Dados de funcionários.
- **Vehicle**: Detalhes de veículos.
- **Work**: Serviços realizados.
- **Invoice** e **Invoice Item**: Gestão de faturas e itens de faturas.

### 3. Diretório `services/`

Encapsula a lógica de negócios do sistema, como operações CRUD e interações com o banco de dados. Cada serviço corresponde a um recurso da aplicação.

### 4. Script SQL

Um arquivo SQL inicializa a estrutura do banco de dados e popula as tabelas com dados de exemplo para testes.

### 5. Frontend

O frontend foi desenvolvido como uma interface funcional e dinâmica, utilizando **HTML**, **CSS** (Tabler e Bootstrap) e **JavaScript**. Ele consome as APIs para exibir e gerenciar os dados dos recursos.

---

## Preparação para Executar a Aplicação

### 1. Pré-requisitos

Certifique-se de ter instalados:

- **Python 3.10+**
- **pip**
- **Banco de Dados SQLite** ou outro compatível configurado no projeto

### 2. Configuração do Ambiente

1. Clone este repositório:

   ```bash
   git clone https://github.com/Jack3dApe/garage_flask_api
   cd garage-flask-api
   ```

2. Crie um ambiente virtual e ative-o:

   ```bash
   python -m venv venv
   source venv/bin/activate   # Linux/Mac
   venv\Scripts\activate      # Windows
   ```

3. Instale as dependências:

   ```bash
   pip install -r requirements.txt
   ```

4. Inicialize o banco de dados:

   ```bash
   flask db upgrade  # Se usar migrations
   python scripts.sql
   ```

5. Execute o servidor:
   ```bash
   flask run
   ```
   O servidor estará disponível em [http://127.0.0.1:5000](http://127.0.0.1:5000).

---

## Preparção do Frontend

1. Certifique-se de que o backend está em execução.
2. Abra o diretório do frontend (como `dashboard/`) e configure um servidor local. Por exemplo:
   ```bash
   python -m http.server
   ```
3. Abra o navegador em [http://127.0.0.1:8000](http://127.0.0.1:8000).

---

## Funcionalidades Implementadas

- **Clientes**: Gerenciamento de cadastro, visualização e exclusão.
- **Funcionários**: Gestão de papéis, contato e estado de contratação.
- **Veículos**: Associação com clientes e gerenciamento de informações.
- **Trabalhos**: Registros detalhados de serviços realizados.
- **Tarefas**: Controle de atividades atribuídas aos funcionários.
- **Faturas**: Emissão e detalhamento de pagamentos.

---
