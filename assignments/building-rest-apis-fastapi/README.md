# 📘 Atividade: Construindo APIs REST com FastAPI

## 🎯 Objetivo

Aprenda a construir uma API REST em Python usando o framework FastAPI. Ao final, você terá uma API de livros com rotas para consultar, criar, atualizar e remover dados, além de validação de entradas e respostas HTTP apropriadas.

## 📝 Tarefas

### 🛠️ Criar a Primeira Rota da API

#### Descrição

Complete o starter code para criar uma API FastAPI e uma rota inicial que confirme que o serviço está funcionando. Execute a aplicação com Uvicorn e consulte a rota no navegador ou em uma ferramenta como o Swagger UI.

#### Requisitos

O programa concluído deve:

- Criar uma instância de `FastAPI` na variável `app`
- Implementar uma rota `GET /` que retorne um objeto JSON com uma mensagem de boas-vindas
- Iniciar a aplicação com `uvicorn starter-code:app --reload`
- Disponibilizar a documentação interativa em `/docs`

### 🛠️ Implementar Rotas de Livros

#### Descrição

Adicione uma coleção de livros armazenada em memória e implemente as operações principais de uma API REST. Cada livro deve possuir um identificador, um título e um autor.

#### Requisitos

O programa concluído deve:

- Implementar `GET /books` para retornar todos os livros
- Implementar `GET /books/{book_id}` para retornar um livro específico
- Implementar `POST /books` para adicionar um novo livro
- Implementar `PUT /books/{book_id}` para atualizar um livro existente
- Implementar `DELETE /books/{book_id}` para remover um livro existente
- Usar os códigos `200`, `201` e `204` quando apropriado

### 🛠️ Validar Dados e Tratar Erros

#### Descrição

Melhore a API para rejeitar dados inválidos e informar claramente quando um livro não for encontrado. Use modelos Pydantic para validar as requisições e exceções HTTP do FastAPI para produzir respostas consistentes.

#### Requisitos

O programa concluído deve:

- Definir modelos Pydantic para representar os dados de entrada e saída de um livro
- Exigir que `title` e `author` sejam textos não vazios
- Retornar `404 Not Found` quando o `book_id` não existir
- Retornar `422 Unprocessable Entity` quando o corpo da requisição for inválido
- Testar as rotas usando a documentação em `/docs` ou uma ferramenta HTTP

Exemplo de requisição para criar um livro:

```json
{
  "title": "The Hobbit",
  "author": "J. R. R. Tolkien"
}
```

Exemplo de resposta:

```json
{
  "id": 1,
  "title": "The Hobbit",
  "author": "J. R. R. Tolkien"
}
```
