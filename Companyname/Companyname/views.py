class Medida(object):
    def __init__(self, habis,banos ):
        self.habis = habis     
        self.banos = banos
    
    def tipoCasa(self):
        if (self.habis + self.banos == 2):
            tipo = "living, comedor, cocina, amplias ventanas, " + self.habis + " habitaciones, " + self.banos + " baños"
            precio = " $3.000.000 "
        elif (self.habis + self.banos == 3):
            tipo = "living, comedor, cocina, amplias ventanas, " + self.habis + " habitaciones, " + self.banos +" baños"
            precio = " $3.800.000 "
        elif (self.habis + self.banos == 4):
            tipo = "living, comedor, cocina, amplias ventanas, Chimenea(opcional), "+ self.habis + " habitaciones, "+ self.banos + " baños"
            precio = " $4.450.000 "
        elif (self.habis + self.banos == 5):
            tipo = "living, comedor, cocina, ventanales, Chimenea(opcional), "+ self.habis +" habitaciones, "+ self.banos + " baños"
            precio = " $5.200.000 "
        elif (self.habis + self.banos == 6):
            tipo = "living, comedor, cocina, ventanales, Chimenea(opcional), " + self.habis +" habitaciones, "+ self.banos +" baños"
            precio = " $6.000.000 "
        else:
            tipo = "INGRESE VALORES VALIDOS"
            precio = "INGRESE VALORES VALIDOS"
        return(tipo,precio)


from django.http import HttpResponse 
from django.template.loader import get_template


def modeloMedida(request,valor_habis):
    medidas = Medida(valor_habis,1)
    doc_externo = get_template("Medida.html")
    documento = doc_externo.render({"<int:tipcas>":medidas.tipoCasa})	
    return HttpResponse(documento)