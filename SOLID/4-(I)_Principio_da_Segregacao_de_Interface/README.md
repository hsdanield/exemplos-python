# Interfaces Especificas


<center>

### Interface Aves: cada classe que herdam essa interface, acaba tendo que implementar todos seus metodos, mas no caso fazendo uma analise bem rapida para o pinguim. Realmente o pinguim é uma Ave, mas ele não voa, então seriamos "forçados" a implementar esse metodo sem necessidade, deixando a arquitetura um pouco confusa. Para isso podemos criar dois "moldes de interfaces" diferentes. Uma interface AvesQueVoam, AvesQueNaoVoam, como mostrado no diagrama 2.

<hr>

<h3> Interface </h3>

```mermaid
classDiagram
    Agente --> Aves : Association
    Canario --|> Aves : Inheritance
    Pinguim --|> Aves : Inheritance

    class Aves {
        <<Interface>>
        +comer(): None
        +voar(): None
        +gritar(): None
    }

    class Canario {
        +comer(): None
        +voar(): None
        +gritar(): None
    }

    class Pinguim {
        +comer(): None
        +voar(): None
        +gritar(): None
    }

```
<hr>
<h3> Segregação de Interfaces</h3>

```mermaid
classDiagram
    Agente1 --> AvesQueVoam : Association
    Agente2 --> AvesQueNaoVoam : Association
    Pinguim --|> AvesQueNaoVoam : Inheritance
    Pinguim --|> AvesQueVoam : Inheritance

    class AvesQueVoam {
        <<Interface>>
        +comer(): None
        +voar(): None
        +gritar(): None
    }

    class AvesQueNaoVoam {
        +comer(): None
        +gritar(): None
    }

    class Pinguim {
        +comer(): None
        +voar(): None
        +gritar(): None
    }

```

</center>
