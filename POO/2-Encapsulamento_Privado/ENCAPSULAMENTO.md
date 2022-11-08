#Encapsulamento 
##UMLs
| Pessoas                       |
| ----------------------------- |
| +nome: string                 |
| +idade: number                |
| -cpf: string                  |
|                               |
| -correr: None                 |
| +beber(bebida:string)         |
| -apresentar_documento(): None |

| Calculadora                                    |
| ---------------------------------------------- |
| -resultado: number                             |
|                                                |
| +calcular(op:string, num: number): None        |
| -adicionar(num1:number, num2:number):number    |
| -subtrair(num1:number, num2:number): number    |
| -multiplicar(num1:number, num2:number): number |
| -dividir(num1:number, num2:number): number     |
| +print_resultado(): None                       |


* (+) publico.
* (-) privado.
* apresentar_documento: só é visivel dentro da classe.