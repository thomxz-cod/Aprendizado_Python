# Desafio: Sistema de Cadastro de Notas

## Objetivo

Você foi contratado para criar um pequeno programa que ajude um professor a cadastrar alunos, calcular suas médias e exibir um relatório completo.

---

# Regras

O programa deve:

1. Perguntar quantos alunos serão cadastrados.
2. Para cada aluno:
   - Pedir o nome.
   - Pedir duas notas.
   - Calcular a média.
   - Guardar as informações em uma lista.

Após o cadastro de todos os alunos, exibir um relatório.

---

# Relatório esperado

```text
===== RELATÓRIO =====

Aluno: João
Média: 8.5
Situação: Aprovado

Aluno: Maria
Média: 5.0
Situação: Recuperação

Aluno: Pedro
Média: 3.2
Situação: Reprovado
```

---

# Regras da média

A situação do aluno deve ser definida da seguinte forma:

- Média **maior ou igual a 7** → **Aprovado**
- Média **entre 5 e 6.9** → **Recuperação**
- Média **menor que 5** → **Reprovado**

---

# Estatísticas finais

Após exibir o relatório, mostre também:

- Total de aprovados
- Total de recuperação
- Total de reprovados

Exemplo:

```text
Aprovados: 10
Recuperação: 4
Reprovados: 2
```

---

# Desafio Extra 1

Mostre também:

- Maior média
- Menor média

Exemplo:

```text
Maior média: 9.8
Menor média: 2.5
```

---

# Desafio Extra 2

Pergunte ao usuário o nome de um aluno.

Se o aluno existir:

```text
Aluno encontrado!

Nome: João
Média: 8.5
Situação: Aprovado
```

Caso contrário:

```text
Aluno não encontrado.
```

---

# Exemplo de execução

```text
Quantos alunos? 3

Nome: Ana
Nota 1: 8
Nota 2: 9

Nome: Lucas
Nota 1: 6
Nota 2: 5

Nome: Carla
Nota 1: 2
Nota 2: 4

===== RELATÓRIO =====

Ana
Média: 8.5
Situação: Aprovado

Lucas
Média: 5.5
Situação: Recuperação

Carla
Média: 3.0
Situação: Reprovado

Aprovados: 1
Recuperação: 1
Reprovados: 1

Maior média: 8.5
Menor média: 3.0

Pesquisar aluno: Lucas

Aluno encontrado!
Média: 5.5
Situação: Recuperação
```

---

# O que esse desafio treina

- ✔ Entrada e saída (`input` e `print`)
- ✔ Conversão de tipos (`int` e `float`)
- ✔ Variáveis
- ✔ Operadores matemáticos
- ✔ Operadores lógicos
- ✔ Estruturas condicionais (`if`, `elif`, `else`)
- ✔ Laços de repetição (`while` ou `for`)
- ✔ Listas
- ✔ Percorrer listas
- ✔ Comparações
- ✔ Acumular valores em variáveis

---

# Nível de dificuldade

**⭐⭐⭐☆☆ (Intermediário para quem está no início do Módulo 3)**

Este desafio é suficientemente completo para consolidar os conteúdos dos Módulos 1 e 2 e praticar boa parte do início do Módulo 3, sem depender de conceitos mais avançados.


# Desafio Extra 3 – Pesquisa Contínua de Alunos

## Objetivo

Após finalizar o cadastro e exibir o relatório, permita que o usuário pesquise vários alunos sem precisar reiniciar o programa.

A pesquisa deve continuar até que o usuário digite **`sair`**.

---

## Regras

1. Após exibir o relatório, pergunte o nome de um aluno.
2. Se o aluno existir:
   - Exiba:
     - Nome
     - Média
     - Situação
3. Se o aluno não existir:
   - Exiba a mensagem:
     ```
     Aluno não encontrado.
     ```
4. Após cada pesquisa, pergunte novamente o nome do aluno.
5. O programa só deve encerrar quando o usuário digitar:
   ```
   sair
   ```

---

## Exemplo de execução

```text
Pesquisar aluno: Lucas

Aluno encontrado!

Nome: Lucas
Média: 5.5
Situação: Recuperação

Pesquisar aluno: Ana

Aluno encontrado!

Nome: Ana
Média: 8.5
Situação: Aprovado

Pesquisar aluno: Pedro

Aluno não encontrado.

Pesquisar aluno: sair

Encerrando programa...
```

---

## Desafio Bônus (Opcional)

Faça com que a pesquisa **não diferencie letras maiúsculas e minúsculas**.

Exemplo:

```text
Pesquisar aluno: lucas
```

deve encontrar:

```text
Lucas
```

> **Dica:** pesquise sobre o método `lower()`.

---

## Objetivos de Aprendizagem

Ao concluir este desafio, você praticará:

- Laços de repetição (`while`)
- Busca em listas
- Estruturas condicionais (`if/elif/else`)
- Controle de fluxo com `break`
- Comparação de strings
- Organização de lógica em programas maiores

---

## Nível de Dificuldade

**⭐⭐⭐☆☆ (Intermediário)**

Este desafio exige combinar vários conceitos básicos em um único programa, simulando uma funcionalidade comum em sistemas de cadastro reais.