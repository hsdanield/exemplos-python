
### Injeção de Dependencia: Através de um objeto injetado para outra classe, conseguimos utilziar os metodos da classe injetada

### Principio da Inversão da Dependencia: através de uma interface molde conseguimos instanciar objetos que implementar essa interface, como no exemplo abaixo, não dependendo diretamente de uma classe

<center>

<br>

### Inversão da Dependência

```mermaid
classDiagram
    Usuario --> Repositorio
    MySqlRepositorio --|> Repositorio 
    MongoRepositorio --|> Repositorio 

    class Usuario {
        -repositorio: ~Repositorio~
        +armazenar_dados(): None
        +remover_Dados(): None
    }

    class Repositorio {
        <<Interface>>
        +inserir(): None
        +deletar(): None
    }

    class MySqlRepositorio {
        +inserir(): None
        +deletar(): None
    }

    class MongoRepositorio {
        +inserir(): None
        +deletar(): None
    }

```

</center>
