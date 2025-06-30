import yaml

from dataclasses import dataclass

@dataclass
class Planeta:
    nombre: str
    masa: float
    radio: float

    def __post_init__(self):
        self.radio = float(self.radio)
        self.masa = float(self.masa)

    @property
    def gravedad(self):
        g_constante = 6.673e-11
        return g_constante * self.masa / (self.radio ** 2)
    
class PlanetaYaml(Planeta, yaml.YAMLObject):
    yaml_tag = '!Planeta'

    def __init__(self, nombre, masa, radio):
        super(PlanetaYaml, self).__init__(nombre, masa, radio)
        self.__dict__['gravedad'] = self.gravedad


if __name__ == '__main__':
    planetas = []
    planetas.append(PlanetaYaml(nombre='Mercurio', masa=3.303e+23, radio=2439700.0))
    planetas.append(PlanetaYaml(nombre='Venus', masa=4.869e+24, radio=6051000.0))
    planetas.append(PlanetaYaml(nombre='Tierra', masa=5.976e+24, radio=6378140.0))
    with open('planetas_con_gravedad.yaml', 'w') as fw:
        yaml.dump(planetas, fw)
