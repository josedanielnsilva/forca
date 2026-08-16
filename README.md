# 🎮 Jogo da Forca

Jogo da forca desenvolvido em Python para execução no terminal. O jogador deve descobrir a palavra sorteada antes de completar o desenho da forca.

## Funcionalidades

- Sorteio aleatório de palavras
- Validação das letras digitadas
- Identificação de letras repetidas
- Desenho da forca conforme os erros
- Sistema de pontuação
- Armazenamento do histórico de partidas
- Ranking ordenado pela maior pontuação

## Tecnologias utilizadas

- Python 3
- Manipulação de arquivos `.txt`
- Estruturas condicionais e de repetição
- Funções e módulos
- Tratamento de exceções

## Estrutura do projeto

```text
forca/
├── main.py
├── jogo.py
├── desenhos.py
├── fileHandler.py
├── palavras.txt
├── score.txt
└── .gitignore
```

## Como executar

1. Clone o repositório:

```bash
git clone https://github.com/josedanielnsilva/forca.git
```

2. Entre na pasta do projeto:

```bash
cd forca
```

3. Execute o jogo:

```bash
python main.py
```

> É necessário ter o Python 3.10 ou uma versão mais recente instalada.

## Como jogar

1. Escolha a opção **Jogar** no menu.
2. Digite seu nome.
3. Informe uma letra por tentativa.
4. Descubra a palavra antes de atingir seis erros.
5. Consulte sua pontuação na opção **Score**.

## Autor

Desenvolvido por [José Daniel Silva](https://github.com/josedanielnsilva).