from flask_restful import Resource

lista_hablidades = ['Python', 'Java', 'Flask', 'PHP']
class Habilidades(Resource):
    def get(self):
        return lista_hablidades