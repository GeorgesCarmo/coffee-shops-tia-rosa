# ☕ Coffee Shops Tia Rosa

Sistema simples de terminal feito em Python para gerenciar **pedidos**, **cardápio** e **clientes** de uma cafeteria fictícia chamada *Tia Rosa*.

---

## 📁 Estrutura de Pastas

```
.
├── main.py                   # Ponto de entrada do programa
└── lib/
    ├── __init__.py          # Módulo principal com lógica de negócios
    ├── archive/             # Lida com arquivos e registros
    │   └── __init__.py
    └── interface/           # Interface de texto com o usuário
        └── __init__.py
```

---

## 🧩 Funcionalidades

### ✅ Módulo de Pedidos
- Adicionar novo pedido com nome, item, preço e data
- Listar todos os pedidos
- Listar apenas pedidos pendentes
- Marcar pedidos como atendidos

### ✅ Módulo de Cardápio
- Adicionar novos itens com ingredientes e preço
- Listar todos os itens disponíveis
- Desativar itens do cardápio

### ✅ Módulo de Clientes
- Cadastrar novos clientes com nome, e-mail, telefone e endereço
- Listar todos os clientes cadastrados

---

## 🛠️ Como rodar o projeto

1. Clone este repositório ou baixe os arquivos:

```bash
git clone https://github.com/seu-usuario/coffee-shops-tia-rosa.git
cd coffee-shops-tia-rosa
```

2. Certifique-se de ter o Python 3 instalado:

```bash
python3 --version
```

3. Rode o sistema com:

```bash
python3 main.py
```

---

## 📝 Estrutura dos arquivos gerados

- **`pedidos.txt`** – Contém os pedidos feitos:
  ```
  Nome;Produto;Preço;Status;DataHora
  ```

- **`cardapio.txt`** – Contém os itens do cardápio:
  ```
  Nome;Ingredientes;Preço;Status
  ```

- **`clientes.txt`** – Contém os clientes cadastrados:
  ```
  Nome;Email;Telefone;Endereço
  ```

---

## 💡 Exemplo de uso

Ao rodar o projeto, você verá menus como:

```
--------------------------
         MENU
--------------------------
[1] PEDIDOS
[2] CARDÁPIO
[3] CLIENTES
[4] SAIR
```

Você pode navegar entre as opções digitando o número correspondente.

---

## 🧪 Tecnologias utilizadas

- Python 3.x
- Manipulação de arquivos `.txt`
- Interface via terminal (CLI)
- Boas práticas de organização modular

---

## 📌 Melhorias futuras (sugestões)

- Adicionar persistência em banco de dados (SQLite ou PostgreSQL)
- Interface gráfica com Tkinter ou web com Flask
- Autenticação de usuários (admin/atendentes)
- Exportação de relatórios em `.csv` ou `.pdf`

---

## 👨‍💻 Autor

Georges do Carmo Pereira
