# Urna Eletrônica

Projeto acadêmico de simulação de votação eletrônica, desenvolvido individualmente utilizando Python e Django.

A aplicação simula o funcionamento de uma urna eletrônica, permitindo registrar votos em candidatos e votos em branco, além de visualizar os resultados da votação.

## Funcionalidades

- Exibição dos candidatos cadastrados.
- Identificação dos candidatos pelo número.
- Registro de votos.
- Opção de voto em branco.
- Exibição dos resultados da votação.
- Cálculo da quantidade e porcentagem de votos.

## Candidatos para teste

Para realizar uma simulação de votação, utilize os seguintes números de identificação:

| Número |
|:---:|
| 40 |
| 70 |
| 13 |

Os números acima correspondem aos candidatos cadastrados no projeto e podem ser utilizados durante os testes da aplicação.

## Tecnologias utilizadas

- Python
- Django
- SQLite
- HTML
- CSS
- JavaScript

## Estrutura do projeto

```text
Urna_Eletronica/
├── urna/
├── UrnaEletronica/
├── manage.py
├── requirements.txt
├── .gitignore
└── README.md
```

## Como executar o projeto

### 1. Clone o repositório

```bash
git clone URL_DO_SEU_REPOSITORIO
```

### 2. Acesse a pasta do projeto

```bash
cd Urna_Eletronica
```

### 3. Crie um ambiente virtual

```bash
python -m venv venv
```

### 4. Ative o ambiente virtual

No Windows:

```bash
venv\Scripts\activate
```

### 5. Instale as dependências

```bash
pip install -r requirements.txt
```

### 6. Execute as migrações

```bash
python manage.py migrate
```

### 7. Inicie o servidor

```bash
python manage.py runserver
```

Acesse no navegador:

```text
http://127.0.0.1:8000/
```

## Sobre o projeto

Este projeto foi desenvolvido individualmente como prática de desenvolvimento web, com o objetivo de aplicar conhecimentos de programação em Python, desenvolvimento com Django e construção de interfaces utilizando HTML, CSS e JavaScript.

Trata-se de uma simulação acadêmica de votação eletrônica, não de um sistema oficial de eleições.

## Autoria

Desenvolvido por **Kaila Evelin**.
