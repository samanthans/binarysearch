# Agenda Telefônica Flask

Esta é uma aplicação Flask simples que funciona como uma agenda telefônica. Permite aos usuários adicionar contatos e procurar por eles usando busca binária.

## Funcionalidades

- Adicionar novos contatos à agenda telefônica.
- Buscar contatos existentes usando busca binária.
- Estilização básica com CSS.

## Estrutura do Projeto

```
flask-phonebook
├── app.py               # Ponto de entrada principal da aplicação Flask
├── static
│   └── style.css        # Estilos CSS para a aplicação
├── templates
│   ├── index.html       # Página principal para adicionar contatos e exibir resultados da busca
└── README.md            # Documentação do projeto
```

## Requisitos

Para executar esta aplicação, você precisa ter Python e Flask instalados. Você pode instalar os pacotes necessários usando o seguinte comando:

```
pip install -r requirements.txt # use uv sync
```

## Executando a Aplicação

1. Clone o repositório ou baixe os arquivos.
2. Navegue até o diretório do projeto.
3. Execute a aplicação com o seguinte comando:

```
python app.py
```

4. Abra seu navegador web e vá para `http://127.0.0.1:5000` para acessar a agenda telefônica.
