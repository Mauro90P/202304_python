
    #1_haz que este método reduzca el balance del usuario en la cantidad especificada 

hacer_retiro (self, amount);

     #2_haz que este método imprima el nombre del usuario y el balance de cuenta en la terminal (#Ej.: “Usuario: Guido van Rossum, Balance: $150)

mostrar_balance_usuario(self): 


     #3_BONUS: haz que este método reduzca el balance del usuario por el monto y agrega esa cantidad al balance de otro_usuario 

transfer_dinero(self, other_user, amount): 

class Usuario:
    def __init__(self) -> None:
        self.name = "Roberto"
        self.balance_cuenta = 0