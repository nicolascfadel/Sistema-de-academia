# 🏋️ Sistema de Academia (CLI em Python com Persistência em JSON)

![Python](https://img.shields.io/badge/Python-3.x-blue)
![Status](https://img.shields.io/badge/status-em%20desenvolvimento-yellow)

Sistema de gerenciamento de academia desenvolvido em Python, com foco em organização de exercícios e montagem de treinos, utilizando persistência de dados em JSON.

---

## 📌 Funcionalidades

- ✅ Cadastro de exercícios
- 🔍 Busca de exercícios por nome
- 📋 Listagem de exercícios
- ✏️ Atualização de dados
- ❌ Remoção de exercícios
- 🏋️ Criação de treinos com vínculo de exercícios
- 📂 Persistência de dados em arquivo JSON

---

## 🧱 Estrutura do Projeto


📁 sistema-academia
├── index.py # Ponto de entrada do sistema
├── menu.py # Interface CLI (menu interativo)
├── exercicio.py # Regras de negócio dos exercícios
├── treino.py # Regras de negócio dos treinos
├── dados.py # Leitura e escrita em JSON
└── banco_dados.json


---

## ▶️ Como Executar

1. Clone o repositório:


https://github.com/nicolascfadel/Sistema-de-academia.git


2. Acesse a pasta do projeto:


cd seu-repositorio


3. Execute o sistema:


python index.py


---

## 💾 Persistência de Dados

Os dados são armazenados em um arquivo `banco_dados.json`, simulando um banco de dados simples.

Isso permite que as informações permaneçam salvas mesmo após encerrar o programa.

---

## 🧠 Conceitos Aplicados

- Estrutura modular em Python
- Separação de responsabilidades
- CRUD completo (Create, Read, Update, Delete)
- Manipulação de arquivos JSON
- Relacionamento entre dados (treinos e exercícios)
- Interface interativa via terminal (CLI)

---

## 🚀 Melhorias Futuras

- Interface gráfica (GUI)
- Integração com banco de dados (SQLite ou PostgreSQL)
- Criação de API REST
- Sistema de autenticação de usuários
- Melhorias na experiência do usuário (UX)

---

## 👨‍💻 Autor

Desenvolvido por **Nicolas Fadel**

🔗 LinkedIn: https://www.linkedin.com/in/nicolascfadel/
🔗 GitHub: https://github.com/nicolascfadel

---
