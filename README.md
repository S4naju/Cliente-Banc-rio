# Sistema Banário em Python

### Sobre o projeto:
Este projeto foi desenvolvido como parte da disciplina **Programação II** no **IFRJ - Niterói**, com o objetivo de aplicar os conceitos de **Programação Orientada a Objetos (POO)** em Python.

O trabalho consiste na **criação de um sistema bancário**, no qual o aluno deve modelar uma **classe `Cliente`** que representa um cliente bancário e fornece métodos para operações básicas (depósito, saque, extrato) e uma simulação de financiamento usando **juros compostos e tabela PRICE**.

---

### Estrutura orientada pelo professor:

O professor orientou que o projeto fosse dividido em **dois arquivos**:

1. **`clienteBancario.py`**  
   Contém **apenas a classe e os métodos** (sem `print` nem `input`), responsáveis por:
   - Calcular saldo em tempo real  
   - Registrar depósitos e saques  
   - Gerar extrato entre datas  
   - Simular financiamento com juros compostos e tabela PRICE  

2. **`clienteBancarioMenu.py`**  
   Contém **a interface com o usuário**, utilizando comandos `print()` e `input()` para interação.  
   Este arquivo **instancia a classe `Cliente`** e demonstra o funcionamento do sistema através de:
   - Criação de cliente  
   - Depósitos e saques  
   - Visualização do extrato  
   - Simulação de financiamento  

---

### Como usar:

Basta rodar o arquivo Python correspondente a cada trabalho. O programa interage com você, pedindo os itens a inserir e quantos deseja remover, mostrando sempre o estado atual da fila.

---

**Observação:** O código está cheio de comentário explicativos, pois eu estudo ele comentando cada parte para entender melhor a lógica e alguns conceitos de POO
