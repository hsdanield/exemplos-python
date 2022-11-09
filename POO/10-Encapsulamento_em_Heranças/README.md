<p>Teoricamente atributos protected não deveriam ser acessados pelo objeto, mas o python acaba
mas parece não existir o tipo protected, então é uma convensão colocar um underline para
 indicar que o atributo é do "tipo" protected</p>
<center>

```mermaid
classDiagram
     DabaseConn <|-- Repository

     class DabaseConn {
       -database: str
       #conn: str
       +user: str
       -get_database(): None
       #testing_connection(): None
     }

     class Repository {

     }

```

</center>
