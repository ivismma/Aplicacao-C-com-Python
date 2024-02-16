# Programa em Python que porta o C.

Repositório onde pratico o uso de duas linguagens de Programação em uma aplicação. Nesse caso: Um programa em Python com portabilidade em C. Apesar dessa prática ser muito útil em diversos casos em desenvolvimento com necessidade de desempenho crítico/Herança de código (advindo de outra linguagem) e outros, eu criei o repositório como experiência para explorar essas possibilidades, além de praticar a biblioteca "ctypes" e, futuramente outras mais eficientes e que fornecem mais ferramentas.

O primeiro código é um pouco simples: Possui um código em C com algumas funções básicas: Só utilizei a função de multiplicar um número (obtido do teclado pelo Python) e a de obter uma string do C (que aguçou minha curiosidade em como o Python conseguiria ler uma string do C), além disso, no Python foi declarada uma variável para manter controlo do ponteiro da alocação dinâmica realizada na main() do C para poder liberar (free) a memória após o uso.

Arquivos:<br>
codigoC.c --> Código em C contendo as funções.;<br>
codigoPython.py --> Código principal (Executar ele);<br>
funcoesC.dll --> C compilado pronto para ser lido pelo Python;<br>
compilarC.bat --> Utilizei para compilar o código para dll.
