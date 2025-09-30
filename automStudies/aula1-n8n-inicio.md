### **Minhas Anotações sobre Automação - Aula 1**

**Assunto:** Entender e começar a aplicar automação de tarefas.

**Objetivo:** Dominar os conceitos para poder automatizar processos, seja usando ferramentas visuais (Low-Code) ou programação (Código).

#### **1. O Conceito Fundamental**

Meu entendimento sobre automação é que se trata, essencialmente, de criar uma "receita" de passos para que um computador execute uma tarefa repetitiva por mim. Toda automação, independentemente da ferramenta, segue uma estrutura lógica clara. Ela sempre começa com um **Gatilho (Trigger)**, que é o evento que inicia o processo. A partir daí, uma ou mais **Ações (Actions)** são executadas em sequência, utilizando **Dados (Data)** específicos para realizar a tarefa. Muitas vezes, o processo também envolve **Lógica (Logic)** para tomar decisões, como verificar uma condição antes de prosseguir. Para criar essas receitas, identifiquei duas abordagens principais: a visual e a baseada em código.

-----

#### **2. Abordagem 1: O Construtor Visual (Ex: n8n)**

A primeira abordagem é a Low-Code/No-Code, que vejo como um "Lego Digital" para conectar diferentes aplicativos e serviços. Nela, eu monto os fluxos de trabalho, ou **Workflows**, arrastando e conectando caixas em uma interface visual. Cada caixa é um **Nó (Node)**, que representa um aplicativo como o Gmail ou uma função lógica, como um IF. Cada nó executa uma micro-tarefa específica.

O fluxo sempre começa com um **Nó de Gatilho (Trigger Node)**, que fica "escutando" por um evento para iniciar a automação, seja um agendamento (Cron), um evento web (Webhook) ou uma ação manual. Para que a ferramenta possa acessar minhas contas em outros serviços, como o Google, eu preciso configurar as **Credenciais (Credentials)**, que funcionam como autorizações seguras.

A grande vantagem que eu vejo nisso é a velocidade, sendo extremamente rápido para criar e testar integrações entre serviços web que se comunicam via API. A natureza visual torna o fluxo muito intuitivo. Contudo, a principal desvantagem é a flexibilidade limitada, pois fico restrito às integrações e funções que a plataforma oferece. Portanto, essa abordagem é ideal para quando preciso conectar diferentes ferramentas da web de forma rápida, como por exemplo, criar um card no Trello sempre que um formulário específico for preenchido.

-----

#### **3. Abordagem 2: O Canivete Suíço (Ex: Python)**

A segunda abordagem é a baseada em código, utilizando uma linguagem de programação como Python. Aqui, em vez de arrastar blocos, eu escrevo a "receita" linha por linha, o que me dá controle total sobre cada detalhe do processo. O trabalho é feito escrevendo um **Script**, que é basicamente um arquivo de texto com a extensão `.py` contendo todas as instruções.

O verdadeiro poder do Python para automação vem de suas **Bibliotecas (Libraries)**, que são como caixas de ferramentas com código pronto que eu posso importar. Para automação local, manipulando arquivos e pastas no meu computador, as bibliotecas `os` e `shutil` são essenciais. Para interagir com APIs na web, a biblioteca `Requests` é o padrão. Se preciso controlar um navegador para preencher formulários ou clicar em botões, posso usar `Selenium` ou `Playwright`. E para manipular dados de planilhas, a biblioteca `Pandas` é extremamente poderosa. Para que tudo isso funcione, preciso ter um entendimento básico da **Sintaxe** da linguagem, como o uso de variáveis, laços de repetição (`for`) e condicionais (`if/else`).

Para colocar isso em prática, o script que montamos para organizar uma pasta de downloads é um exemplo perfeito. Ele verifica cada arquivo na pasta e o move para um subdiretório específico com base em sua extensão.

```python
# Importa as bibliotecas para interagir com o sistema (os) e mover arquivos (shutil)
import os
import shutil

# Define o caminho da pasta a ser organizada. É crucial alterar esta linha.
caminho_da_pasta = 'COLOQUE_O_CAMINHO_DA_SUA_PASTA_DE_DOWNLOADS_AQUI'

# Tenta listar os arquivos no caminho, tratando o erro se a pasta não existir.
try:
    lista_de_arquivos = os.listdir(caminho_da_pasta)
except FileNotFoundError:
    print(f"ERRO: A pasta '{caminho_da_pasta}' não foi encontrada.")
    print("Por favor, verifique o caminho e tente novamente.")
    exit()

# Percorre a lista, olhando um arquivo de cada vez.
for arquivo in lista_de_arquivos:
    caminho_completo_arquivo = os.path.join(caminho_da_pasta, arquivo)

    # Garante que estamos lidando com um arquivo, não uma subpasta.
    if os.path.isfile(caminho_completo_arquivo):
        
        # Lógica para mover arquivos PDF.
        if arquivo.endswith('.pdf'):
            pasta_destino = os.path.join(caminho_da_pasta, 'Documentos PDF')
            os.makedirs(pasta_destino, exist_ok=True) # Cria a pasta de destino se não existir
            shutil.move(caminho_completo_arquivo, pasta_destino)
            print(f"Movido '{arquivo}' para a pasta Documentos PDF.")

        # Lógica para mover arquivos de imagem.
        elif arquivo.endswith(('.jpg', '.png', '.gif', '.jpeg')):
            pasta_destino = os.path.join(caminho_da_pasta, 'Imagens')
            os.makedirs(pasta_destino, exist_ok=True)
            shutil.move(caminho_completo_arquivo, pasta_destino)
            print(f"Movido '{arquivo}' para a pasta Imagens.")

print("\nOrganização concluída!")
```

O poder aqui é virtualmente ilimitado; se algo pode ser feito em um computador, provavelmente posso automatizá-lo com Python. Por outro lado, a curva de aprendizado é real e o desenvolvimento inicial é mais lento do que com uma ferramenta visual. Essa abordagem é, portanto, ideal para tarefas locais no meu computador, extração de dados da web (web scraping) e qualquer automação que exija uma lógica altamente personalizada e complexa.

-----

#### **4. Meu Plano de Ação**

Primeiramente, meu plano é focar na base do código. A ideia é iniciar os estudos com esse script inicial e logo após melhorar as skills pra programar coisas mais complexas.
