class Envio:

    def __init__(self, codigo, destino, peso, coste_base):
        self.codigo = codigo
        self.destino = destino
        self.peso = peso
        self.coste_base = coste_base


    def get_coste_total(self):
        return self.coste_base

    def es_pesado(self):
        if self.peso > 10 :
            return True
        else :
            return False

    def __str__ (self):
        return f'Envío {self.codigo} con destino {self.destino}'




class EnvioNacional(Envio):

    def __init__(self, iva):
        super().__init__(codigo, destino, peso, coste_base)
        self.iva = iva


    def get_coste_Total(self):
        return f'{self.coste_base} * '