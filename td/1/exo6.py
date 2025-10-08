def regrouper_par_cle(liste, cle):
    ensemble = {}
    for dictionnaire in liste:
        key = dictionnaire[cle]
        for k, v in dictionnaire.items():
            if k != cle:
                value = v
        if key in ensemble:
            ensemble[key].append(value)
        else:
            ensemble[key] = [value]
    print(ensemble)

regrouper_par_cle([{"ville": "Paris", "vente": 100},{"ville": "Lyon", "vente": 80},{"ville": "Paris", "vente": 50}],'ville')
regrouper_par_cle([{"ville": "Paris", "vente": 100},{"ville": "Lyon", "vente": 80},{"ville": "Paris", "vente": 50}, {"ville": "Lyon", "vente": 100}],'ville')