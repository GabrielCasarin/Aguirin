## Aguirin I

Essa é a primeira tentativa de fazer acontecer a proposta do Casarin.

# O quê? Por quê?

O Aguirin é a proposta de implementar um processador com uma abordagem neuromórfica.

Começou com uma leitura (On Intelligence - Jeff Hawkins, Sandra Blakeslee) onde os modelos atuais de processamento são questionados. O que é mais instigante na leitura é a inadequação do modelo atual e a proposta de um modelo baseado em memória, sendo descrito no livro o funcionamento de um cérebro biológico, e também comparado com tecnologias existentes.

A partir daí ficou na cabeça "e se fizermos um processador baseado em memória?" Talvez a simplicidade ajude, certo?

Começaram as pesquisas e compartilhamento de materiais. Finalmente a proposta está começando a ter estrutura suficiente para ser feita alguma coisa.

# Como?

A princípio vamos tentar implementar os modelos em VHDL, pelo conhecimento prévio e não-necessidade de aprender mais uma ferramenta. VHDL é a ferramenta em comum entre nós.

Num primeiro momento estão sendo estudadas possibilidades, e tudo é provisório.

## Abordagem

Como vai ser feita a abordagem pra esse projeto?

- Fase de estudos: está sendo feito um levantamento do que já foi feito, e o que encontramos está sendo lido.
- Fase de planejamento: precisamos definir como o projeto vai ser implementado, para que consigamos fazer juntos.
- Fase de implementação
- Fase de simulação
- Fase de testes

## O que é um neurônio biológico?

Um neurônio biológico é como se fosse o bloco essencial do cérebro de qualquer animal. Ele tem a mesma cara para quase todos animais, então o que varia, geralmente, é como esses blocos se organizam.

Na imagem abaixo temos uma ilustração da estrutura básica de um neurônio. As principais partes que vamos olhar são o soma, o dendrito e o axônio. (De forma simplificada esses são os coponentes do nosso bloco básico)

- Soma: é o corpo do neurônio, é onde está o núcleo da célula, e onde estão conectadas todas as outras partes do neurônio.
- Dendrito: São ramos que transmitem as informações de outros neurônios ao Soma.
- Axônio: É a parte comprida, que transmite também as informações, na forma de diferença de potencial.

![alt text](http://2.bp.blogspot.com/-MxB_DNy6yVQ/T7Iash0k3zI/AAAAAAAAAZo/1_-jCVzzIBM/s1600/neurónio.jpg)

Quase do mesmo jeito que diferentes circuitos digitais são combinações diferentes de blocos básicos, nesse caso, existem muito menos blocos básicos. Na imagem a seguir temos os blocos que podem ser usados.

![alt text](http://neuronios.pbworks.com/f/brain-neuron-types.gif)


## Fase de planejamento

Nessa etapa vamos tentar descobrir qual a melhor estratégica para começar.

## Leituras
- On Intelligence (Jeff Hawkins, Sandra Blakeslee)
- O conhecimento do cérebro (John C. Eccles, Editora USP)
- Principles of Neural Science (Kandel, Schwartz, Jessell)
- Implementation of a feed-forward Artificial Neural Network in VHDL on FPGA ( Philippe Dondon ;  Julien Carvalho ;  Rémi Gardere ;  Paul Lahalle ;  Georgi Tsenov ;  Valeri Mladenov)
- Implementation of an artificial neuron in VHDL (Javier Gómez Casado)
