from database.DAO import DAO
import networkx as nx

class Model:
    def __init__(self):
        self._listYears = []
        self._listStates = []
        self._listSightings = []
        self._grafo = nx.Graph()
        self._idMap = {}
        self._listEdges = []
        self.largest_cc = []


    def buildGraph(self, anno, stato):
        self._grafo.clear()
        self._listSightings = DAO.get_all_sightings(anno, stato)

        for s in self._listSightings:
            self._idMap[s.id] = s

        self._grafo.add_nodes_from(self._listSightings)
        self._listEdges = DAO.getAllEdges(anno, stato)

        for e in self._listEdges:
            s1 = self._idMap[e[0]]
            s2 = self._idMap[e[3]]

            if s1.distance_HV(s2) < 100:
                self._grafo.add_edge(s1, s2)

        """for i in self._listSightings:
            for j in self._listSightings:
                distanza = i.distance_HV(j)
                if distanza < 100 and i.shape == j.shape and i.id != j.id:
                    self._grafo.add_edge(i, j)
                    #print(i, "- ", j, "- ", distanza)"""

    def getYears(self):
        self._listYears = DAO.get_all_years()
        return self._listYears

    def getStates(self, anno):
        self._listStates = DAO.get_all_states(anno)
        return self._listStates

    def getNumNodi(self):
        return len(self._grafo.nodes)

    def getNumArchi(self):
        return len(self._grafo.edges)

    def get_connected_components(self):
        # Ottiene le componenti debolmente connesse del grafo
        components = list(nx.connected_components(self._grafo))
        return components

    def getConnectedComponents(self):
        return nx.number_connected_components(self._grafo)



Ciao Eli! Spero tu riesca a vedere! Quanto fa 2+2?
