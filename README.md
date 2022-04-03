# entregaveisNAUTILUS
Aqui constam todos os meus entregáveis do processo de capacitação da UFRJ Nautlius

Explicação dos arquivos pelas pastas:

#### Python Básico 
1 - No primeiro exercício para começar eu fiz uma funcão que recebe os dois numeros que serão utilizados, e faz a razão e descobre qual é o maior e o menor, para começar a progressão a partir do menor numero. Para identificar qual se é par ou ímpar usei o operador aritmético de "%" que informa o resto da divisão, se a divisão por 2 for igual a 0 dá para notar que é um número par, senão, é impar. E a partir disso, usando o "range" recebendo os parâmetros de onde irá começar e onde terminar com a razão "c" no caso da PA, sempre adicionando cada termo da progressão em uma lista através do "append", e a mesma coisa serve para o caso da PG, a diferença é que foi utilizada a fórmula da PG para poder realizar, com um limite de 10 itens.

2 - No segundo exercício foi feita uma função para receber um numero, e a primeira coisa feita foi transformá-lo em binário pela função "bin" e logo em seguida colocar em uma lista para facilitar a contagem dos valores, foi utilizado a função "del" para apagar números desnecessários que estavam aparecendo. E para finalizar, usado a função "find" para percorrer a lista sempre ignorando os números negativos.

4 - No quarto exercício comecei somando todos os numeros, utilizando for e o range de "1000". Em seguida transformei em uma lista para poder mexer nos ultimos valores do numero que foi formado, com o "i" negativo, sendo possível pegar os ultimos da lista dessa maneira, e adicinei esses valores encontrados em uma outra lista que é a resposta. 

#### Python Orientado a Objetos

1 - Para esse entregável eu usei como base jogadores de LOL e dois times para fazer a correlação dos dois. Primeiramente é criado o "método construtor" com init para os times e uma função que retorna as informações de cada time instanciado, da mesma maneira existe uma classe para os participantes. Os times possuem as informações do nome e da pontuação e os participantes as informações de qual time pertence, numero de abates e numero de mortes. Com os métodos mágicos foi feita uma comparação dos times e dos participantes pelo desempenho de cada um.

####  Arduino e Sensores

1 - Para o entregável de arduino foi utilizado um potenciômetro e 6 leds RGB, e a ideia da atividade é fazer os leds acenderem por meio do potenciômetro, além de ter a opção de mudar as cores do led por meio do terminal. No meu entregável foi configurado os leds como 1 = Vermelho, 2 = Verde, 3 = Azul. Após a criação das variáveis em seus respectivos pinos, no void setup coloquei apenas as funções de cada pino, se é INPUT ou OUTPUT. No void loop, para a mudança de cores foi feita através do "Serial.available()", que identifica se há alguma coisa no terminal, e esse valor é enviado para a variável "mensagem" e por meio dela define-se qual a cor, se = 1, o pino do vermelho ficará HIGH e os outros LOW, e assim por diante. Para acender os leds conforme o potenciômetro, é necessário ler o valor do potenciômetro por meio do "analogRead" e jogar para uma variável que por sua vez é jogada na função "map" para ser convertida em um valor entre 0 e 255 e novamente esse valor é jogado para outra variável que finalmente vai para os leds por meio do "digitalWrite".

Link do entregável: https://www.tinkercad.com/things/6NNGqSUx7vd-circuito-do-entregavel-wagner/editel?sharecode=QapTVrjwu1r0CI_VGGel3O__pAMAdnDykocz4vgJUII

#### Controle e Localização
