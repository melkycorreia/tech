+---------------------+            +------------------------+
|      Cliente        |            |      ContaBancaria      |
+---------------------+            +------------------------+
| - nome: str         |            | - numero: str           |
| - endereco: str     |            | - titular: Cliente      |
| - telefone: str     |            | - saldo: float          |
| - email: str        |            | - limite: float         |
+---------------------+            +------------------------+
| + atualizar_info()  |            | + depositar(valor:float)|
|                     |            | + sacar(valor:float)    |
+---------------------+            +------------------------+
                                        ^             ^
                                        |             |
                           +------------+  +----------+
                           |                            |
                    +------------+             +----------------+
                    |    ContaCorrente     |             |    ContaPoupanca |
                    +------------+             +----------------+
                    | - agencia: str       |             | - juros: float   |
                    | - saldo_especial: float|            |                |
                    |                        |            | + atualizar_juros()|
                    +------------------------+            +-----------------+
