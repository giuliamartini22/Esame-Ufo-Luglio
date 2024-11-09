import flet as ft
from UI.view import View
from model.modello import Model


class Controller:
    def __init__(self, view: View, model: Model):
        # the view, with the graphical elements of the UI
        self._view = view
        # the model, which implements the logic of the program and holds the data
        self._model = model

        self._listYear = None
        self._listStates = None
        self._anno = None
        self._state = None

    def read_anno(self, e):
        """event handler che legge l'anno scelto dal menu a tendina ogniqualvolta viene cambiata
        la scelta, e lo memorizza in una variabile di instanza. L'anno è un intero, se si tratta di un anno,
        oppure un None se viene scelta l'opzione nessun filtro sull'anno"""
        if e.control.value == "None":
            self._anno = None
        else:
            self._anno = e.control.value

            # Svuota le opzioni attuali del dropdown degli stati
            self._view.ddstate.options.clear()
            # Popola il dropdown degli stati con i nuovi valori basati sull'anno selezionato
            self.populate_dd_state(self._anno)


    def populate_dd_anno(self):
        """methodo che popola la tendina con tutti gli anni in cui ci sono state vendite,
        prendendo le informazioni dal database"""
        self._listYear = self._model.getYears()
        for anno in self._listYear:
            self._view.ddyear.options.append(ft.dropdown.Option(anno))
        self._view.update_page()

    def read_state(self, e):
        if e.control.value == "None":
            self._state = None
        else:
            self._state = e.control.value
        print(self._state)

    def populate_dd_state(self, anno):
        self._listStates = []
        self._listState = self._model.getStates(anno)
        for s in self._listState:
            self._view.ddstate.options.append(ft.dropdown.Option(s))
        self._view.update_page()

    def handle_graph(self, e):
        anno = self._anno
        stato = self._state
        if anno is None:
            self._view.create_alert("Anno non inserito")
            return
        if stato is None:
            self._view.create_alert("Stato non inserito")
            return

        self._model.buildGraph(anno, stato)
        self._view.txt_result1.controls.clear()
        self._view.txt_result1.controls.append(ft.Text(f"Numero di nodi {self._model.getNumNodi()}"))
        self._view.txt_result1.controls.append(ft.Text(f"Numero di archi {self._model.getNumArchi()}"))

        components = self._model.get_connected_components()
        num_components = len(components)
        self._view.txt_result1.controls.append(
            ft.Text(f"Numero totale di componenti connesse: {num_components}"))

        # 2. Identificare la componente di dimensione maggiore
        largest_component = max(components, key=len)
        largest_size = len(largest_component)

        self._view.txt_result1.controls.append(
            ft.Text(f"La componente più grande contiene {largest_size} nodi."))
        self._view.txt_result1.controls.append(
            ft.Text(f"Nodi della componente più grande: "))
        for component in largest_component:
            self._view.txt_result1.controls.append(ft.Text(component))

        self._view.update_page()


    def handle_path(self, e):
        pass

