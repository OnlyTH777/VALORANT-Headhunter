import json
import requests
from valclient import *

agentsIds = json.loads(requests.get("https://python-valorant-api.onrender.com/agentsIds").content)
agents = json.loads(requests.get("https://python-valorant-api.onrender.com/agents").content)

class Main:
    def logarValorant(self):
        self.client = Client(region="br")
        self.client.activate()
        print("EITa")

    def instalock(self, agent):
        agent = self.coloca_id(agent)
        self.client.pregame_select_character(agent)
        self.client.pregame_lock_character(agent)

    def coloca_id(self, agent):
        if agent in agentsIds.keys():
            agent = agentsIds.get(agent)
        return agent
