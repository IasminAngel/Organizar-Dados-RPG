# Ordem de Iniciativa App

Este é um aplicativo de desktop desenvolvido em Python com a biblioteca **CustomTkinter** para gerenciar a ordem de iniciativa de jogadores em jogos de RPG. O aplicativo permite adicionar jogadores, definir a ordem de iniciativa com base nos números sorteados e gerenciar efeitos que afetam os jogadores ao longo das rodadas.

## Funcionalidades

- **Adicionar Jogadores:** Insira o nome do jogador e o número sorteado no dado para determinar a ordem de iniciativa.
- **Próximo Jogador:** Avance para o próximo jogador na ordem de iniciativa.
- **Remover Jogador:** Remova um jogador da lista.
- **Efeitos:** Aplique efeitos em jogadores, com duração em rodadas. Os efeitos diminuem a cada rodada até chegar a 0.
- **Rodadas:** O aplicativo avança automaticamente a cada ação de um jogador e informa quando uma rodada se passa.

## Requisitos

- Python 3.x
- CustomTkinter
- Tkinter
- PyInstaller (para gerar o executável)

## Instalação

### 1. Clone o repositório ou faça o download do código

```
git clone https://seu-repositorio-url.git
```

## 2. Instale as dependências necessárias
Se você ainda não tem as bibliotecas necessárias, instale-as com o seguinte comando:

```
pip install customtkinter
```
## Como Executar
1. Abra o terminal ou prompt de comando.
2. Navegue até o diretório onde o arquivo iniciativa.py está localizado.
3. Execute o seguinte comando:
```
pip install pyinstaller
```
## Como Criar o Executável
Se você deseja criar um arquivo executável para rodar sem precisar de Python instalado, siga as instruções abaixo:

1. Crie o executável com PyInstaller
No terminal ou prompt de comando, execute o seguinte comando:

```
pyinstaller --onefile --windowed iniciativa.py
```

2. Localize o Executável
Após a execução do comando, o arquivo executável será gerado na pasta dist. O arquivo será nomeado como iniciativa.exe (ou o nome do seu script).


## Personalização
Você pode personalizar o comportamento do aplicativo alterando os parâmetros no código. Por exemplo, você pode modificar as cores, fontes e até mesmo a lógica de gerenciamento dos jogadores e efeitos.

## Contribuição
Se você deseja contribuir para o projeto, sinta-se à vontade para fazer um fork e enviar um pull request.

## Licença
Este projeto está licenciado sob a Licença MIT. Veja o arquivo LICENSE para mais detalhes.
```
Esse código contém todos os detalhes para a instalação das dependências, execução, criação do executável e informações sobre personalização, contribuição e licença. Basta copiar e colar diretamente no seu arquivo `README.md`.
```

