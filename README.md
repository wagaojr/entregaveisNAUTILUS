# entregaveisNAUTILUS
Aqui constam todos os meus entregáveis do processo de capacitação da UFRJ Nautilus

Explicação dos arquivos pelas pastas:

#### Python Básico 
1 - No primeiro exercício para começar eu fiz uma funcão que recebe os dois numeros que serão utilizados, e faz a razão e descobre qual é o maior e o menor, para começar a progressão a partir do menor numero. Para identificar qual se é par ou ímpar usei o operador aritmético de "%" que informa o resto da divisão, se a divisão por 2 for igual a 0 dá para notar que é um número par, senão, é impar. E a partir disso, usando o "range" recebendo os parâmetros de onde irá começar e onde terminar com a razão "c" no caso da PA, sempre adicionando cada termo da progressão em uma lista através do "append", e a mesma coisa serve para o caso da PG, a diferença é que foi utilizada a fórmula da PG para poder realizar, com um limite de 10 itens.

2 - No segundo exercício foi feita uma função para receber um numero, e a primeira coisa feita foi transformá-lo em binário pela função "bin" e logo em seguida colocar em uma lista para facilitar a contagem dos valores, foi utilizado a função "del" para apagar números desnecessários que estavam aparecendo. E para finalizar, usado a função "find" para percorrer a lista sempre ignorando os números negativos.

4 - No quarto exercício comecei somando todos os numeros, utilizando for e o range de "1000". Em seguida transformei em uma lista para poder mexer nos ultimos valores do numero que foi formado, com o "i" negativo, sendo possível pegar os ultimos da lista dessa maneira, e adicinei esses valores encontrados em uma outra lista que é a resposta. 

#### Python Orientado a Objetos

1 - Para esse entregável eu usei como base jogadores de LOL e dois times para fazer a correlação dos dois. Primeiramente é criado o "método construtor" com init para os times e uma função que retorna as informações de cada time instanciado, da mesma maneira existe uma classe para os participantes. Os times possuem as informações do nome e da pontuação e os participantes as informações de qual time pertence, numero de abates e numero de mortes. Com os métodos mágicos foi feita uma comparação dos times e dos participantes pelo desempenho de cada um.

####  Arduino e Sensores

1 - Para o entregável de arduino foi utilizado um potenciômetro e 6 leds RGB, e a ideia da atividade é fazer os leds acenderem por meio do potenciômetro, além de ter a opção de mudar as cores do led por meio do terminal. No meu entregável foi configurado os leds como 1 = Vermelho, 2 = Verde, 3 = Azul. Após a criação das variáveis em seus respectivos pinos, no void setup coloquei apenas as funções de cada pino, se é INPUT ou OUTPUT. No void loop, para a mudança de cores foi feita através do "Serial.available()", que identifica se há alguma coisa no terminal, e esse valor é enviado para a variável "mensagem" e por meio dela define-se qual a cor, se = 1, o pino do vermelho ficará HIGH e os outros LOW, e assim por diante. Para acender os leds conforme o potenciômetro, é necessário ler o valor do potenciômetro por meio do "analogRead" e jogar para uma variável que por sua vez é jogada na função "map" para ser convertida em um valor entre 0 e 255 e novamente esse valor é jogado para outra variável que finalmente vai para os leds por meio do "digitalWrite".

OBS!! Só dá para ver o funcionamento do potenciômetro após inserir o número de seu desejo no monitor serial.

Link do entregável: https://www.tinkercad.com/things/6NNGqSUx7vd-circuito-do-entregavel-wagner/editel?sharecode=QapTVrjwu1r0CI_VGGel3O__pAMAdnDykocz4vgJUII

#### Docker

1 - Para o docker foi feito um entregável que consistia na preparação do ambiente da nautilus, por meio de uma imagem construida no dockerfile que monta todo o ROS para os containers que eu for usar. Link do dockerhub: https://hub.docker.com/repository/docker/wagaojr/entregavel

#### Controle e Localização

1 - Em controle e localização o entregável consistia em aplicar um controle PID como resposta ao erro de uma gangorra, todo o cálculo foi feito em python seguindo a fórmula "PID Kp*(erro) + Kd*(erro_derivativo) + Ki*(erro_integral)" sendo aplicada 10 vezes, através de um for. Foi feito tanto o PID acumlulado quanto o do ultimo loop.

#### ROS Básico

1 - Para o entregável de ROS básico, foi feito uma primeira aplicação de publisher e subscriber, com a ideia de velocidade e usando os vetores angular e linear, usei uma mensagem geometry do tipo "Accel" que trata justamente do tópico do entregável. Coloquei todo o pacote na pasta do ROS, para poder ser executado. 

#### ROS Tópicos Especiais

1 - No entregável de tópicos especiais foi utilizado os conceitos de launch, parâmetro, transformadas e o rviz. Nessa atividade foi feito um sistema solar, e por meio das mensagens em forma de transformadas foi possivel modificar a translação dos planetas como o tempo do ros. No meu yaml tem os nomes de cada planeta e seus respectivos raios, e através do get_param foi possível acessar esses valores. É possível visualizar todo o trabalho por meio rviz.

#### Gazebo

1 - Em Gazebo foi realizado os conceitos básicos com os conceitos de joint para montar um braço mecânico. No meu entregável possui as pastas de config padrão e o "model.sdf" onde fica todo o código do meu braço. Para rodar o funcionamento é necessário utilizar uma força no eixo Z na peça central, com o valor da força ideal sendo de 22000.  
