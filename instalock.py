import json
import requests
from valclient import *

agents = json.loads(requests.get(
    "https://python-valorant-api.onrender.com/agents").content)

client = Client(region="br")
client.activate()


def init():
    agente_input = input("Qual agente você deseja dar instalock? ")
    instalock(agente_input)


def instalock(agente_input):
    partida_iniciou = int(
        input('Digite "1" (Sem as aspas né) quando sua partida for iniciar para dar instalock ou "2" (Támbem sem as aspas né) Para mudar o agente que você dará instalock '))
    if partida_iniciou == 1:
        pick(agente_input.title())
        instalock(agente_input)
    elif partida_iniciou == 2:
        init()
    else:
        instalock(agente_input)


def pick(agent):
    agent = coloca_id(agent)
    client.pregame_select_character(agent)
    client.pregame_lock_character(agent)


def coloca_id(agent):
    if agent in agents.keys():
        agent = agents.get(agent)
    return agent


if __name__ == '__main__':
    init()
