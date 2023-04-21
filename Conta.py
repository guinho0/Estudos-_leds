class Conta:

    def __init__(self, numero, titular, saldo, limite):#criando os atributos, o init é o construtor usado no python especificamente para isso.
        print("Construindo objeto ... {}".format(self))
        self.__numero = numero# o duplo undeline é usado para atributo privado, ou seja , ele não é visto de fora do objeto.
        self.__titular = titular
        self.__saldo = saldo
        self.__limite = limite

    def extrato(self):#metódo que permite saber o extrato da conta
        print("Saldo de {} do titular {}".format(self.__saldo, self.__titular))

    def deposita(self, valor):#metodo deposita, acrescenta valor a conta.
        self.__saldo += valor

    def __pode_sacar(self, valor_a_sacar):#criando um método privado para saber se a conta está propensa ao saque.metodo privado só poderá ser usado nessa classe. caso eu crie uma subclasse, esse metodo não poderá ser usado.
        valor_disponivel_a_sacar = self.__saldo + self.__limite
        return valor_a_sacar <= valor_disponivel_a_sacar

    def saca(self, valor): # se o metodo pode_sacar for atendido, voce pode sacar.
        if(self.__pode_sacar(valor)):
            self.__saldo -= valor
        else:
            print("O valor {} passou o limite".format(valor))

    def transfere(self, valor, destino):#metodo de tranferência.
        self.saca(valor)
        destino.deposita(valor)

    @property #propriedade, a maneira como o python define os "getters, setters e deleters". assim voce pode acessar e alterar um atributo sem chamar essas funcoes.
    def saldo(self):
        return self.__saldo

    @property
    def get_titular(self):#o get sempre retorna algo, sem receber nenhum argumento
        return self.__titular

    @property
    def limite(self):
        return self.__limite

    @limite.setter #perceba a importancia do @property vc aplica o set ou o get no mesmo metodo.
    def limite(self, limite):
        self.__limite = limite

    @staticmethod#método estático será atribuido a uma classe sem a necessidade de criação de um objeto, normalmente valores fixos. e podem ser chamados diretamente na classe. ex.Conta.codigo_banco()
    def codigo_banco():
        return "001"

    @staticmethod
    def codigos_bancos():
        return {'BB':'001', 'Caixa':'104', 'Bradesco':'237'}
