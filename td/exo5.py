def trouver_sous_ensemble(L, S):
    ensemble = []
    for i in range(len(L)):
        for j in range(i, len(L)):
            if L[i] + L[j] < S:
                for e in range(j, len(L)):
                    if L[i] + L[j] + L[e]  == S:
                        ensemble.append((L[i], L[j], L[e]))
            if i != j:
                if L[i] + L[j] == S:
                    ensemble.append((L[i], L[j]))
    print(ensemble)
trouver_sous_ensemble([2, 3, 5, 7], 10)