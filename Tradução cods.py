============================================================
MINHAS ANOTAÇÕES DE PYTHON - SISTEMA DE LOGIN (VERSÃO 2.0)
============================================================

1. COMANDOS DE TEXTO E EXIBIÇÃO (PRINT / INPUT)
------------------------------------------------------------
* print("\n")
  -> O "\n" é um comando invisível que pula uma linha na tela.
  -> Ajuda a espaçar o texto e deixar o terminal organizado.

* print("=" * 40)
  -> Multiplica o caractere dentro das aspas.
  -> Cria uma linha com exatamente 40 sinais de igual.

* print(f"Olá, {usuario}!")
  -> A letra "f" antes do texto avisa ao Python que é uma "f-string".
  -> Permite colocar variáveis direto dentro do texto usando chaves { }.

* .strip()
  -> Apaga espaços em branco invisíveis antes e depois do texto.
  -> Evita que o usuário erre digitando " lucas " com espaços.

* .lower()
  -> Transforma todas as letras digitadas em minúsculas.
  -> Garante que "LUCAS", "Lucas" e "lucas" sejam lidos iguais.


2. BIBLIOTECAS E COMANDOS DO SISTEMA OPERACIONAL
------------------------------------------------------------
* import os
  -> Importa os comandos do Sistema Operacional (Windows/Linux).

* os.system('cls' if os.name == 'nt' else 'clear')
  -> Limpa a tela do terminal para sumir com textos antigos.
  -> Usa 'cls' se for Windows (nt) ou 'clear' se for Linux/Mac.

* import time
  -> Importa comandos relacionados ao tempo e relógio.

* time.sleep(1)
  -> Faz o programa pausar ("dormir") pelo tempo indicado em segundos.


3. ESTRUTURAS DE DADOS (DICIONÁRIOS)
------------------------------------------------------------
* usuarios_cadastrados = {"lucas": "lucas777"}
  -> Cria um Dicionário usando chaves { }.
  -> Guarda informações associadas no modelo Chave: Valor.
  -> No código: o Nome do usuário é a Chave e a Senha é o Valor.


4. OPERADORES ESPECIAIS E LÓGICA
------------------------------------------------------------
* response := resposta == "sair"
  -> Operador Walrus (:=). Faz duas coisas ao mesmo tempo.
  -> Testa se a resposta é igual a "sair" e já salva isso na variável.

* while True:
  -> Cria um laço de repetição infinito.
  -> O código roda para sempre até encontrar o comando "break".

* break
  -> Força o programa a sair imediatamente de um laço (while ou for).

* while resposta != "sim" and resposta != "nao":
  -> O símbolo "!=" significa "Diferente de".
  -> O "and" significa "E". Só roda se for diferente das duas opções.

* while usuario in usuarios_cadastrados:
  -> O comando "in" significa "Dentro de".
  -> Procura se o nome digitado já existe nas chaves do dicionário.

* while not cadastro_valido:
  -> O "not" inverte o valor lógico. Significa "Enquanto NÃO for válido".


5. LAÇO DE REPETIÇÃO (FOR)
------------------------------------------------------------
* for user in usuarios_cadastrados:
  -> O laço "for" passa de linha em linha pelo dicionário.
  -> Ele pega o nome de cada usuário cadastrado, um por um.
