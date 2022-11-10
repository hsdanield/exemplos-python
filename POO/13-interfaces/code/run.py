from terrenos.quadrado import TerrenoQuadrado
from terrenos.retangular import TerrenoRetangular
from engenheiro.engenheiro import Engenheiro


engenheiro = Engenheiro("Antonio")
terrenoQuadrado = TerrenoQuadrado(4)
terrenoRetangular = TerrenoRetangular(2, 3)

# Medidas do Terreno Quadrado
print("--Medindo o Terreno Quadrado--")
engenheiro.medir_area(terrenoQuadrado)
engenheiro.medir_perimetro(terrenoQuadrado)

# Medidas do Terreno Retangular
print("\n--Medindo o Terreno Retangular--")
engenheiro.medir_area(terrenoRetangular)
engenheiro.medir_perimetro(terrenoRetangular)
