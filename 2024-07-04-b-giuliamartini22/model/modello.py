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



Permettere all’utente di scrivere in un campo di testo un valore intero compreso fra la durata minima e 
massima degli avvistamenti registrati nel database. I valori minimi e massimi vanno letti dal database e non 
specificati a mano. Inoltre, si permetta all’utente di selezionare un anno desiderato tramite un menù a 
tendina che contiene tutti gli anni registrati nel database ordinati in senso decrescente (fare riferimento alla 
colonna datetime del database). 
b. Facendo click sul bottone Crea Grafo, creare un grafo diretto non pesato, i cui vertici siano tutti gli 
avvistamenti presenti nella tabella “sighting” che siano avvenuti nell’anno selezionato (fare riferimento alla 
colonna datetime del database) dall’utente e con una durata compresa fra gli estremi specificati 
(strettamente).
• Un arco fra due avvistamenti esiste se e solo se tali avvistamenti hanno la stessa forma (colonna 
“shape” del db). 
• L’arco è uscente dall’avvistamento che ha durata minore ed entrante nell’avvistamento con durata 
maggiore. Se i due avvistamenti hanno la stessa durata, l’arco va aggiunto in entrambe le direzioni!
c. Analizzare il grafo, verificando le diverse durate di avvistamenti presenti nel grafo e per ognuna di esse 
stampare il numero di nodi corrispondenti (vedere screenshot di sotto per maggiore chiarezza).
Inoltre, stampare anche la durata media degli avvistamenti presenti nel grafo
