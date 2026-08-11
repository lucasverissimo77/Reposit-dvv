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



  ============================================================
MINHAS ANOTAÇÕES DE PYTHON - CALCULADORA DE MÉDIA (V2.0)
============================================================

1. CRIAÇÃO DE FUNÇÕES
------------------------------------------------------------
* def calcular_medias():
  -> O "def" serve para definir (criar) uma função personalizada.
  -> Uma função é como um bloco de código guardado que você pode 
     chamar para rodar a qualquer momento.
  
* calcular_medias()
  -> Executa (chama) a função que foi criada lá em cima para o 
     programa começar a rodar de fato.


2. TRATAMENTO DE ERROS (EVITA QUE O PROGRAMA FECHE SE ERRAR)
------------------------------------------------------------
* try:
  -> Significa "Tente". O Python vai tentar rodar o código que está 
     aqui dentro. Se o usuário digitar um texto onde deveria ser um 
     número, o programa não vai "quebrar" (dar erro).

* except ValueError:
  -> Significa "Exceção para Erro de Valor". Se o código de dentro do 
     "try" falhar porque o usuário digitou uma letra em vez de número, 
     o Python desvia para cá e roda o aviso de erro.


3. ESTRUTURAS DE DADOS (LISTAS)
------------------------------------------------------------
* medias = []
  -> Cria uma Lista vazia usando colchetes [ ].
  -> Listas servem para guardar vários valores na ordem em que foram 
     digitados (como uma fileira de gavetas).

* medias.append(nota)
  -> O comando ".append()" adiciona um novo item (a nota) no final 
     da lista "medias".


4. CONVERSÃO DE TIPOS E MATEMÁTICA
------------------------------------------------------------
* int(input(...))
  -> Converte o texto que o usuário digitou em um número INTEIRO 
     (sem casas decimais, ex: 1, 2, 5).

* float(input(...))
  -> Converte o texto que o usuário digitou em um número FLUTUANTE 
     (com casas decimais, ex: 7.5, 8.0, 10.0).

* sum(medias)
  -> O comando "sum()" soma automaticamente todos os números que 
     estão guardados dentro da lista "medias".

* {media:.2f}
  -> Formata um número flutuante dentro da f-string. 
  -> O ".2f" diz ao Python para mostrar apenas 2 casas após o ponto 
     (ex: transforma 7.666666 em 7.67).


5. LAÇOS DE REPETIÇÃO E ÍNDICES (FOR / RANGE)
------------------------------------------------------------
* for i in range(1, total_notas + 1):
  -> O "range(inicio, fim)" gera uma sequência de números.
  -> Se "total_notas" for 3, ele vai contar de 1 até 3 (o +1 serve 
     porque o Python sempre para um número antes do limite final).
  -> A variável "i" guarda o número da contagem atual (1, depois 2...).

* medias[i]
  -> Acessa um valor específico dentro da lista usando o seu Índice 
     (posição). Em Python, as posições começam sempre do 0.

