
# Implementação MySQL

## Stack
- Python (feito na 3.13.2)

## Organização de Pastas
Na raiz do projeto temos a página de Apresentação, nomeada de "HomePage", e um documento com todas as bibliotecas necessárias chamada "requirements".

A pasta com o nome "pages" possui as páginas do CRUD e visualização  de todas as tabelas do BD.

Já a pasta "MySQL" possui os documentos para criação, preenchimento e trigger do Banco de Dados.

## Como rodar e preencher o BD

Abra seu VisualStudio, abra o terminal e clone todo o repositório do github através do comando "github clone https://github.com/DanielSantana47/iaad-streamlit.git"
Com todo repositório clonado, abra seu MySQLWorkbench e para criar o BD, abra a pasta "MySQL" e rode:

- Criar_Banco.sql
- Trigger.sql 
- Preencher_Banco.sql

O primeiro código e responsável pela criação e estruturação de todas as tabelas, o segundo é um trigger que não permite que programadores com menos de 18 anos sejam adicionados, já o terceiro serve para popular com dados as tabelas criadas.

## Como rodar o projeto

Como mostrado no Stack, o usuário já deve possuir a versão do Python ( 3.13.2), pode ser um pouco mais recente ou avançada.

### 1º Passo - Criar um Ambiente Virtual

Abra seu VisualStudio e abra um novo terminal, digite nele o comando "python -m venv venv"

Este comando é responsável por criar um ambiente virutal nele todas as bibliotecas necessárias serão instaladas sem interferir diretamente nas bibliotecas da máquina.

### 2º Passo - Acessar o Ambiente Virtual 

__Caso ocorra erro no próximo comando, vá para o passo 3º e volte para o segundo passo. Caso não ocorra erro vá para o passo 4º.__

Com o terminal aberto digite o código " .\venv\Scripts\activate "

Esse comando vai ser responsável por referenciar que agora estamos trabalhando com as dependências do ambiente virutal.

### 3º Passo - Correção de Erro no Acesso ao Ambiente Virtual

Caso seja sua primeira vez acessando e criando um ambiente virtual é necessário alterar a permissão para que isso possa ser feito, por padrão vem desligado.

Vá na barra de pesquisa do Windows e acesse o PowerShell, então digite os comandos: 

- cd /
- cd .\Windows\system32
- Set-ExecutionPolicy -Scope CurrentUser -ExecutionPolicy RemoteSigned

Aparecerá uma confirmação, então digite "s", para confirmar.

O primeiro código é um comando para mudar o cursor até a raiz do usuário. O segundo é responsável por navegar até a pasta de Administrador, a qual possui a configuração. O terceiro é o código responsável por mudar a configuração padrão assim permitindo criação de ambientes virtuais.

__Caso tenha ocorrido este erro, após essa correção não esqueça de voltar ao passo 2º para acessar o Ambiente Virtual.__

### 4º Passo - Baixar todas as dependências necessárias

Após estar no ambiente virtual, escreva no mesmo terminal o seguinte comando:

- pip install - r requirements.txt

Este comando é responsável por baixar todas as bibliotecas que serão usadas no projeto, e todas estão descritas no arquivo.

### 5º Passo - Por suas informações do MySQL

Acesse o arquivo .env na raiz do projeto, ele terá uma estruta semelhante a esta:

DB_HOST= 000.0.0.1

DB_USER=root

DB_PASSWORD=

DB_DATABASE= normalizacao

Para preencher as informações, abra seu MySQL e preencha assim:

![Infos](https://github.com/user-attachments/assets/3f163e2d-f205-4d3b-aa09-a5cf60a4d395)


Caso tenha colocado uma senha na conexão coloque em "DB_PASSWORD", caso não pode deixar vazio.

Para preencher o ultimo basta nomear com o esquema no qual as tabelas foram adicionadas. Como exemplo: 

![image](https://github.com/user-attachments/assets/0c81a847-45e3-4829-8bc7-e242274e154c)


DB_DATABASE= startup

Não esqueça de salvar todo o arquivo.

### 6º Passo - Acessar o streamlit


Com o ambiente virtual acessado, os requirements baixados e conexões feitas é possível agora rodar o streamlit para visualização.

Não esqueça de estar no ambiente virtual acessado com o comando ".\venv\Scripts\activate "

Escreva no terminal o seguinte comando: 
- streamlit run '.\HomePage 🏠.py'

Não se preocupe caso o emote não apareça no terminal, irá funcionar da mesma forma. 

## Time

- Guilherme Leonardo
- Daniel Santana
- Ronaldo Ribeiro
- Hivison Santos
- Diego Clebson
- Guilherme Salgueiro

### Obrigado pela atenção 🤝
