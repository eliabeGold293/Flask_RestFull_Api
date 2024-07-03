from flask_restful import Resource
from flask import jsonify, request
import json

lista_habilidades = [
    {
        "habilidade": "Java"
    },
    {
        "habilidade": "PHP"
    },

    {
        "habilidade": "Python"
    },

    {
        "habilidade": "MysQL"
    },
    {
        "habilidade": "JavaScript"
    }
]

# função que faz um tratamento do id escrito pelo usuário
def ID(id):
    new_id = id - 1
    if new_id <= 0:
        new_id = 0
    return new_id

class Habilidades(Resource):
    def get(self):
        return lista_habilidades

    def post(self):
        dados = json.loads(request.data)
        lista_habilidades.append(dados)
        posicao = len(lista_habilidades)
        dados['ID'] = posicao

        mensagem = 'habilidade criada com sucesso!'
        return jsonify({'status': 'sucesso!'}, mensagem)

class Operacoes(Resource):

    def get(self, id):
        new_id = ID(id)
        try:
            response = lista_habilidades[new_id]
        except IndexError:
            mensagem = 'Habilidade de id: {} nõa encontrada na lista.'.format(new_id)
            response = mensagem
        except Exception:
            mensagem = 'Erro desconhecido, por favor contatatar Desenvolvedor da Api.'
            response = mensagem
        return jsonify(response)
    def put(self, id):
        new_id = ID(id)
        dados = json.loads(request.data)
        lista_habilidades[new_id] = dados
        return jsonify(dados)
    def delete(self, id):
        new_id = ID(id)
        lista_habilidades.pop(new_id)
        mensagem = 'Habilidade de id: {} deletada com sucesso!'.format(new_id+1)
        return jsonify({'status': 'sucesso !'}, mensagem)
