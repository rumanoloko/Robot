import json

data = {
    "city": {"rows": 4,
             "columns": 4,
             "blocked": [[0, 3], [1, 2], [3, 2]]
             },
    "departure": [0, 0],
    "dangers": [[0, 2], [3, 1]],
    "trapped": [[2, 1], [1, 1]]
}
data_json = json.dumps(data)
loaded_data = json.loads(data_json)
class Robot:

    def __init__(self, my_dictionary):
        if isinstance(my_dictionary, dict):
            self.my_dictionary = my_dictionary
            self.rutasMasCortas = []
        else:
            raise ValueError("No pasaste un diccionario al constructor")

    def iniciador(self):
        print(len(loaded_data["trapped"]))
        posicionInicial = loaded_data["departure"]
        personaAtrapada = loaded_data["dangers"][0]
        barreras = loaded_data["city"]["blocked"]
        pisadasDejadas = loaded_data[]
        self.rutasMasCortas += self.preparacionBusquedaRamificada(self.my_dictionary)

    def preparacionBusquedaRamificada(self, biblioteca):
        #print(personaBuscada)
        rutaProhibida = []
        rutas = [[1, 2, 3], [3, 2, 1], [2, 2, 2]]
        #for x in "nesw":
            #print(x);

    def busquedaRamificada(self):
        pass


robot = Robot(loaded_data)
robot.iniciador()