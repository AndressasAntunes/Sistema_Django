# 📚 Sistema de Gerenciamento de Biblioteca (Django-main)

Este é um projeto **Django** dedicado à criação de um sistema robusto e eficiente para a **administração completa de uma biblioteca**. O sistema foi arquitetado para simplificar as operações diárias, desde o **cadastro e controle do acervo** até a **gestão dos usuários** e o acompanhamento das interações.

---

## ✨ Módulos e Funcionalidades Principais

O projeto está estruturado em módulos claros (`sgb_livros` e `sgb_usuarios`) para garantir organização e escalabilidade:

### 📖 Gerenciamento de Livros (`sgb_livros`)

Este módulo centraliza todas as operações relacionadas ao acervo da biblioteca:
* **Cadastro Completo**: Inclusão de novos títulos com informações detalhadas (autor, ISBN, editora, ano, etc.).
* **Controle de Estoque**: Visualização e atualização da quantidade de cópias disponíveis.
* **Edição e Atualização**: Permite corrigir ou atualizar os dados de qualquer item do acervo.
* **Listagem e Pesquisa**: Interface para listar e realizar buscas rápidas e filtradas no catálogo de livros.

### 🧑‍💻 Gerenciamento de Usuários (`sgb_usuarios`)

Responsável pela administração da base de membros da biblioteca:
* **Cadastro de Membros**: Registro de novos leitores com informações de contato.
* **Perfil do Usuário**: Consulta e gerenciamento dos dados cadastrais dos leitores.
* **Histórico de Interações**: Futuramente, incluirá o rastreamento de empréstimos e devoluções associados a cada usuário.

---

## 🛠️ Tecnologias Envolvidas

O projeto utiliza um *stack* de desenvolvimento web moderno e amplamente reconhecido:

| Categoria | Tecnologia | Detalhes |
| :--- | :--- | :--- |
| **Backend/Core** | **Python** | Linguagem principal para toda a lógica de negócio do sistema. |
| **Framework** | **Django** | O framework web de alto nível, utilizado para o desenvolvimento rápido e seguro. |
| **Frontend** | **HTML, CSS** | Usados para a estruturação da interface de usuário e estilização. |
| **Banco de Dados** | **SQLite** (padrão) | Utilizado para desenvolvimento e testes, com possibilidade de migração para PostgreSQL ou MySQL em produção. |

---
