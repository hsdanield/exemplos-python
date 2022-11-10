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


Documentação SQLAlchemy: <https://www.sqlalchemy.org/>
