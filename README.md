
# Projeto - EcoMares
## Participantes
```http
• Beatriz Vieira de Novais        | rm554746
• Mariana Neugebauer Dourado      | rm550494
```

## Como acessar:
1. Certifique-se de ter o código-fonte do projeto em mãos, abrindo-o no ambiente de desenvolvimento como o Visual Studio Code. 

2. Verifique se as dependências necessárias estão instaladas e execute o projeto conforme as instruções específicas, podendo ser um projeto web ou de linha de comando.

3. Interaja com as opções fornecidas no menu principal, como visualizar informações sobre a preservação dos oceanos, soluções ambientais e benefícios da preservação marinha.

4. Consulte a documentação do projeto para mais detalhes sobre as dependências.


## Explicação: 
Nosso código "Projeto EcoMares" tem seu objetivo de fornecer informações sobre a importância da preservação de oceanos e dá própria vida marinha. 
Nosso programa utiliza um menu com seis funções para o nosso usuário escolher. 

Explicando funções: 

exibir_programa()
Sendo responsável por exibir uma mensagem de boas-vindas ao programa, juntamente com um logotipo do projeto EcoMares. 
Essa função não recebe nenhum argumento e simplesmente imprime as mensagens na tela.

exibir_opcoes(opcoes) 
Responsável por exibir as opções do menu principal para o usuário e solicitar que ele escolha uma opção válida. Utilizamos uma lista de opções que junto de um loop while True para garantir que o usuário escolha uma o
pção válida.
Dentro do loop, as opções são exibidas na tela e a escolha do usuário é lida através da função input().
Se a escolha do usuário for válida, o loop é interrompido e a função retorna o índice da opção escolhida. Caso contrário, uma mensagem de erro é exibida e o loop continua.

função main() sendo a função principal do programa. Ela chama todas as funções.. 
A função exibir_programa() ⭣
Exibe uma função de boas-vindas e imprime um texto estilizado. 
Site para pegar fonte: https://fsymbols.com/pt/letras/

A função exibir_opcoes(opcoes) ⭣
Exibe as opções do menu principal para o usuário escolher. Ela recebe um loop em while para garantir que o usuário escolha entre as seis opções dadas. 

Existem outras funções no código, como problema_020() | solucao_ecomares() | beneficios_ecomares() | 
como_ajudar() | equipe_ecomares() | sair()
sendo chamadas de acordo com a escolha do usuário no menu. Cada uma das funções exibe informações sobre o projeto. 

Utilizando a lógica de programação nosso código usa while/ for para o controle de exibição do menu e a leitura do usuário.
Utilizamos listas para armazenar as opções do menu e suas funções. 
E por fim utilizamos condicionais para verificar se a escolha do usuário é válida e para decidir qual função chamar com base na escolha.
