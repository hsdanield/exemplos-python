# Introdução - SQLAlchemy

## 1. O que é ORM  (Object Relational Mapper) ?

É uma técnica de desenvolvimento utilizada para produzir a impedância da POO. Basicamente oferece aos desenvolvedores todo o poder e flexibidade do SQL.
<center>

| Banco de Dados Relacional | Programação Orientada a Objetos |
| ------------------------- | ------------------------------- |
| Tabela                    | Classe                          |
| Coluna                    | Atributo                        |
| Registro                  | Objeto                          |


<h2>Interação Gerenciada Pela ORM</h2>

```mermaid
flowchart TB
    
    id1["Classes e Sintaxe Padrão"]  --- Codigo

    subgraph Codigo
        LogicaProgramacao--->ORM
    end


    subgraph Database
        ORM --Gerência de Conexão e Conection Pool----> idDB[(Database)] 
    end


```

</center>
<hr>

### Engine Configuration

* Dialect: especificar qual banco estamos trabalhando, por exemplo postgres, mysql. 
* Poll: Usada para manter conexões de longa execução na memória para reutilização eficiente, bem como para fornecer gerenciamento para o número total de conexões que um aplicativo pode usar simultaneamente. Um Query para cada pull (1-1). Número default do SQLAlchemy é 5 (pool_size).

 
<br><br><br>

## 2. Mapeando Classes

Documentação SQLAlchemy: <https://www.sqlalchemy.org/>
