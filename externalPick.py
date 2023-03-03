import json
import requests
from valclient import *

agentsIDs = json.loads(requests.get("https://python-valorant-api.onrender.com/agentsIds").content)
agents = json.loads(requests.get("https://python-valorant-api.onrender.com/agents").content)

class ExternalPick:

    def __init__(self):
        self.logado = False
        self.logarValorant()

    def logarValorant(self):
        try:
            self.client = Client(region="br")
            self.client.activate()
            self.logado = True
        except:
            self.logado = False

    def select(self, agent):
        agent = self.coloca_id(agent)
        self.client.pregame_select_character(agent)

    def lock(self, agent):
        agent = self.coloca_id(agent)
        self.client.pregame_lock_character(agent)

    def instalock(self, agent):
        agent = self.coloca_id(agent)
        self.client.pregame_select_character(agent)
        self.client.pregame_lock_character(agent)

    def coloca_id(self, agent):
        if agent in agentsIDs.keys(): agent = agentsIDs.get(agent)
        return agent