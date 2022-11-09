## SOLID - (L) - Principio da Substituição de Liskov

<p> Mesma funcionalidade para o mesmo método! </p>
<p> Herança como complementação. </p>

<p> Especificar o mais genérico em cima da árvore. </p>

<center>

<hr>
Mesma funcionalidade para o mesmo método!

```mermaid
classDiagram
     Objeto 1 <-- Objeto 2
     Objeto 1 --> MESMO_COMPORTAMENTO_METODO
     Objeto 2 --> MESMO_COMPORTAMENTO_METODO
     
     alt mesmo
```

</center>

<center>

<hr>

<h3>Zoologico</h3>

```mermaid
classDiagram
     Pessoa --> Animal
     Aves --|> Animal
     Lobos --|> Animal
     Pinguim --|> Aves
     Falcao --|> Aves
     
     class Pessoa {
         +observador(animal:Animal): None
     }

     class Animal {
         +comer(): None
         +andar(): None
         +dormir(): None
     }

     class Aves {
         +cantar(): None
     }

     class Lobos {
         +uivar(): None
     }

     class Pinguim {
         +escorregar(): None
     }

     class Falcao {
         +voar(): None
     }
```

</center>

<center>

<hr>

<h3>Conexão</h3>

```mermaid
classDiagram
     Conexao <|-- MySQLRepo
     Conexao <|-- PostgresRepo
     CasoDeUso --> MySQLRepo
     
     class Conexao {
         +conectar(): any
         +desconectar(): any
     }

     class MySQLRepo {
         +select(): any
         +insert(): any
     }

     class PostgresRepo {
        +select(): any
        +insert(): any
     }

     class CasoDeUso {
        +buscar(db_repo:MysqlRepo): any
     }


```

</center>
