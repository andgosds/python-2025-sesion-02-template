import json

from ddataclass import dataclass

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

def como_planetas(dct):
    return Planeta(dct['nombre'], dct['masa'], dct['radio'])


class PlanetaEncoder(json.JSONEncoder):
    def default(self, obj):
        if isinstance(obj, Planeta):
            return dict(nombre=obj.nombre, masa=obj.masa, radio=int(obj.radio), gravedad=obj.gravedad)
        return json.JSONEncoder.default(self, obj)


if __name__ == '__main__':
    with open('planetas.json', 'r') as fr:
        planetas = json.load(fr, object_hook=como_planetas)
        print(planetas[0])

    with open('planetas_con_gravedad.json', 'w') as fw:
        json.dump(planetas, fw, cls=PlanetaEncoder, indent=4)
