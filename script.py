""" from paquete.saludos import Saludo
s=Saludo() """


from collections import Counter

""" x = [1,2,3,4,5,6,7,8]
print(Counter(x))

 """

""" 
animales = "perro gato conejo perro perro gato salamandra"
c= Counter(animales.split())

print(c)

 """

""" from collections import defaultdict

x = defaultdict(float)
print(x['algo'])
print(x)


from collections import OrderedDict

l = OrderedDict()
l["uno"] = 'one'
l ["dos "] = 'two'
l["tres"] = 'three'

print(l) """


""" from collections import namedtuple
Persona = namedtuple("Persona", "nombre apellido edad")
p = Persona(nombre = "Lucas", apellido = "Rodriguez", edad = 30)



print(p.edad)



print(p[0]) """



from datetime import datetime

""" dt = datetime.now() #Fecha y hora actual


print(dt)

print(dt.microsecond)



dt = datetime(1993,6,2)

dt = dt.replace(year=2500)

print(dt) """


import math 
""" print(math.floor(3.99))


print(math.ceil(3.10))

 """


""" numeros = [0.9999999, 1,2,3]
print(math.fsum(numeros))

 """

""" print(math.pow(2,3))

print(math.sqrt(9))





print(math.pi)

print(math.e) """




import random

print(random.random())

print(random.uniform(1,10))



print(random.randrange(10))


print(random.randrange(0,101,5))



lista = [1,2,3,4,5]

random.shuffle(lista)
print(lista)

