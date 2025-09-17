# Analisador Léxico – Python

Projeto desenvolvido para a disciplina de Compiladores.  
Objetivo: implementar um analisador léxico em Python capaz de transformar código-fonte em uma lista de *tokens*.

---

## ⚡ Funcionalidades
- Leitura de arquivos `.txt` como entrada.
- Reconhecimento de:
  - Identificadores e palavras reservadas
  - Números inteiros e decimais
  - Strings
  - Operadores e símbolos (`+ - * / = ; , ( ) { } ...`)
  - Comentários de linha e de bloco
- Registro da posição do token (linha e coluna).
- Tratamento de erros léxicos (caracteres inválidos, strings/comentários não fechados).
- Saída em **JSON**.

---
