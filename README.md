# 🖱️ Automação de Cadastro de Produtos com PyAutoGUI

Este projeto tem como objetivo automatizar o processo de cadastro de produtos em um sistema web, utilizando a biblioteca **PyAutoGUI** em Python. A automação interage com o navegador, realiza o login e preenche os formulários de produtos com dados extraídos de um arquivo `.csv`.

## ✅ Funcionalidades

- Abre o navegador e acessa o sistema.
- Realiza o login automaticamente com e-mail e senha.
- Lê uma planilha de produtos (`produtos.csv`).
- Cadastra automaticamente cada produto no sistema.
- Fecha pop-ups, caso apareçam.
- Exibe no terminal o tempo total de execução.

## 📁 Estrutura do Projeto

````plaintext
automacao_cadastro/
├── imgs/
│   ├── campo_email.png
│   ├── campo_codigo.png
│   ├── campo_codigo_apos_cadastro.png
│   └── popup_ok.png
├── produtos.csv
├── cadastro.py
└── README.md
````

## 📦 Requisitos

- Python 3.7 ou superior
- Google Chrome
- Resolução de tela compatível com os pontos de clique definidos no script
- Bibliotecas Python:
  - `pyautogui`
  - `pandas`
  - `pillow`

### 🚀 Como Usar

- Clone o repositório
  ````
  git clone https://github.com/fmota-dev/automacao_cadastro_py.git
  cd automacao-cadastro
  ````

- Instalação das bibliotecas

  ````bash
  pip install pyautogui pandas pillow
  ````

- Execute o script:
  python cadastro.py

- Observe o processo de automação. O terminal mostrará os dados da planilha e, ao final, o tempo total da execução.

## ✅ Resultado

Ao final da execução, o terminal exibirá algo como:

✅ Cadastro finalizado! Tempo total: 2m 45s.
