class NodeNonBinary:
    def __init__(self, value, weight=[], parent=None):
        self.value = value
        self.weight = weight
        self.children = []  # Lista dei figli
        self.parent = parent


def binary_search(arr, target):
    if len(arr) == 1:  # Caso in cui l'array ha un solo elemento
        return arr[0] if arr[0] >= target else -1  # Restituisce l'indice se il valore è >= target
    left, right = 0, len(arr) - 1
    result = -1  # Inizialmente, supponiamo che non ci sia un valore valido

    while left <= right:
        mid = (left + right) // 2
        
        if arr[mid] >= target:
            result = mid  # Salviamo l'indice come potenziale risultato
            right = mid - 1  # Continuiamo a cercare nella metà sinistra
        else:
            left = mid + 1  # Cerchiamo nella metà destra
    if result == -1:
        return -1
    else:
        return arr[result]
    
def binary_search_leq(arr, target):
    if len(arr) == 1:  # Caso in cui l'array ha un solo elemento
        return arr[0] if arr[0] <= target else -1  # Restituisce l'elemento se è ≤ target
    
    left, right = 0, len(arr) - 1
    result = -1  # Inizialmente, supponiamo che non ci sia un valore valido

    while left <= right:
        mid = (left + right) // 2
        
        if arr[mid] <= target:
            result = mid  # Salviamo l'indice come potenziale risultato
            left = mid + 1  # Continuiamo a cercare nella metà destra
        else:
            right = mid - 1  # Cerchiamo nella metà sinistra

    if result == -1:
        return -1  # Nessun valore trovato ≤ target
    else:
        return arr[result]

def dfs_EA_tmax_spazioN_NonBinary(root):
    # Caso base: nodo nullo
    if root is None:
        return {}

    # Caso base: foglia
    if not root.children:
        print(f"EA e tempo max visita per il sottoalbero radicato nel nodo {root.value} (foglia): {root.weight[0], root.weight[-1]}")
        return {root.value: (root.weight[0], root.weight[-1])}

    # Variabili per raccogliere i valori EA e Tmax per ogni sottoalbero
    sottoalberi = {}

    # Calcolo ricorsivo per ogni figlio
    # ea_vals = []
    # t_max_vals = []
    ea_tmax = []
    for child in root.children:
        sottoalberi.update(dfs_EA_tmax_spazioN_NonBinary(child))
        ea, t_max = sottoalberi[child.value]
        # ea_vals.append(ea)
        # t_max_vals.append(t_max)
        ea_tmax.append((ea, t_max))

    
    # min_tmax = min(t_max_vals)
    # pos_min = t_max_vals.index(min_tmax)
    # #first_ea = ea_vals[pos_min]
    # for i in range(len(ea_vals)):
    #     if ea_vals.index(ea_vals[i]) == pos_min:
    #         continue
    #     elif ea_vals[i] > min_tmax:
    #         return {root.value: (float("inf"), float("inf"))}
    
    # Controllo di consistenza tra i nodi
    ea_tmax.sort(key=lambda x: x[1]) # Step 1

    if ea_tmax[0][0] > ea_tmax[1][1]: # Step 2
        return {root.value: (float("inf"), float("inf"))}
    
    for i in range(1, len(ea_tmax)): # Step 3
        if ea_tmax[i][0] > ea_tmax[0][1]:
            return {root.value: (float("inf"), float("inf"))}
        
    # # Iterare su ogni EA nell'array
    # for i, (ea, tmax) in enumerate(ea_tmax):
    #     # Metto a +inf il valore di Tmax associato a EA
    #     # cerco min
    #     # check
    #     # rimetto al valore precedente il tmax

    #     # Salvo il valore del Tmax associato all'EA attuale
    #     original_tmax = ea_tmax[i][1]
    #     # Imposto il Tmax attuale a +inf
    #     ea_tmax[i] = (ea, float("inf"))
    #     # Cerco il minimo Tmax nell'array
    #     min_tmax = min(ea_tmax, key=lambda x: x[1])[1]
    #     # Check tra EA e Tmax minimo
    #     check = ea <= min_tmax
    #     print(f"EA: {ea}, Tmin: {min_tmax}, Check: {check}")
    #     if check == False:
    #         return {root.value: (float("inf"), float("inf"))}
    #     # Ripristino il valore originale di Tmax
    #     ea_tmax[i] = (ea, original_tmax)
        
    

    # Calcolo EA e Tmax per il nodo corrente
    EA = max(ea_tmax, key=lambda x: x[0])[0]
    t_max_visita = min(ea_tmax, key=lambda x: x[1])[1]
    
    k = binary_search(root.weight, EA)
    nextTimeMax = binary_search_leq(root.weight, t_max_visita)  # Binary search per trovare il predecessore
    if nextTimeMax == -1 and root.value != "A":
        return {root.value: (float("inf"), float("inf"))}
    print(f"Valore di nextTimeMax: {nextTimeMax} per il nodo {root.value}")
    print(f"Valore di k: {k} per il nodo {root.value}")
    print(f"EA e tempo max visita per il sottoalbero radicato nel nodo {root.value} (nodo interno): {k, nextTimeMax}")
    minTime = min(t_max_visita, nextTimeMax)

    # Aggiornamento del nodo corrente nei risultati
    sottoalberi[root.value] = (k, minTime)

    return sottoalberi

def algoritmo3_NonBinary(root):
    print("\nQuesto è per alberi non binari\n")
    
    # Esegui DFS-EA-Tmax una sola volta
    risultati = dfs_EA_tmax_spazioN_NonBinary(root)

    # Ottieni i risultati per i figli della radice
    figli = root.children
    if not figli:
        return False

    
    ea_tmax = []
    if risultati[root.value][0] == float("inf") or risultati[root.value][1] == float("inf"):
        return False
    
    for child in figli:
        ea, t_max = risultati[child.value]
        ea_tmax.append((ea, t_max))

    print("------------------------------------------------")
    for i, child in enumerate(figli):
        print(f"EA e tempo max visita del figlio {child.value}: {ea_tmax[i][0], ea_tmax[i][1]}")
        
    
    ea_tmax.sort(key=lambda x: x[1]) # Step 1

    if ea_tmax[0][0] > ea_tmax[1][1]: # Step 2
        return False
    
    for i in range(1, len(ea_tmax)): # Step 3
        if ea_tmax[i][0] > ea_tmax[0][1]:
            return False
    
    
    # # Iterare su ogni EA nell'array
    # for i, (ea, tmax) in enumerate(ea_tmax):
    #     # Metto a +inf il valore di Tmax associato a EA
    #     # cerco min
    #     # check
    #     # rimetto al valore precedente il tmax

    #     # Salvo il valore del Tmax associato all'EA attuale
    #     original_tmax = ea_tmax[i][1]
    #     # Imposto il Tmax attuale a +inf
    #     ea_tmax[i] = (ea, float("inf"))
    #     # Cerco il minimo Tmax nell'array
    #     min_tmax = min(ea_tmax, key=lambda x: x[1])[1]
    #     # Check tra EA e Tmax minimo
    #     check = ea <= min_tmax
    #     if check == False:
    #         return False
    #     # Ripristino il valore originale di Tmax
    #     ea_tmax[i] = (ea, original_tmax)
    
    return True
    

def print_tree(root, level=0):
    if root is not None:
        print("  " * level + f"Node {root.value}, Weight: {root.weight}")
        for child in root.children:
            print_tree(child, level + 1)

# root = NodeNonBinary("A")
# node_b = NodeNonBinary("B", weight=[1,5,7], parent=root)
# node_c = NodeNonBinary("C", weight=[2,5,8], parent=root)
# node_d = NodeNonBinary("D", weight=[2,5,10], parent=root)
# node_e = NodeNonBinary("E", weight=[1,5,6], parent=node_b)
# node_f = NodeNonBinary("F", weight=[2,7,9], parent=node_c)
# node_g = NodeNonBinary("G", weight=[2,8], parent=node_c)
# node_h = NodeNonBinary("H", weight=[1,11], parent=node_d)
# node_i = NodeNonBinary("I", weight=[1,15], parent=node_d)
# node_j = NodeNonBinary("J", weight=[1,17], parent=node_d)

# root.children = [node_b, node_c,node_d]
# node_b.children = [node_e]
# node_c.children = [node_f, node_g]
# node_d.children = [node_h, node_i, node_j]

# root = NodeNonBinary("A")
# node_b = NodeNonBinary("B", weight=[2,6], parent=root)
# node_c = NodeNonBinary("C", weight=[2,11], parent=root)
# node_d = NodeNonBinary("D", weight=[2,5], parent=root)
# node_e = NodeNonBinary("E", weight=[2,4,5], parent=node_b)
# node_f = NodeNonBinary("F", weight=[1,3], parent=node_b)
# node_g = NodeNonBinary("G", weight=[1,11], parent=node_c)
# node_h = NodeNonBinary("H", weight=[1,11], parent=node_d)
# node_i = NodeNonBinary("I", weight=[1,15], parent=node_d)
# node_j = NodeNonBinary("J", weight=[1,22], parent=node_d)

# root.children = [node_b, node_c,node_d]
# node_b.children = [node_e, node_f]
# node_c.children = [node_g]
# node_d.children = [node_h, node_i, node_j]

# root = NodeNonBinary("A")
# node_b = NodeNonBinary("B", weight=[1,3], parent=root)
# node_c = NodeNonBinary("C", weight=[2,4], parent=root)
# node_d = NodeNonBinary("D", weight=[3,7], parent=root)

# root.children = [node_b, node_c, node_d]

# root = NodeNonBinary("A")
# node_b = NodeNonBinary("B", weight=[2,4], parent=root)
# node_c = NodeNonBinary("C", weight=[3,5], parent=root)
# node_d = NodeNonBinary("D", weight=[1,15], parent=node_b)
# node_e = NodeNonBinary("E", weight=[3,6], parent=node_b)
# node_f = NodeNonBinary("F", weight=[1,2], parent=node_c)
# node_g = NodeNonBinary("G", weight=[1,3], parent=node_c)
# node_h = NodeNonBinary("H", weight=[1,4], parent=node_c)
# node_i = NodeNonBinary("I", weight=[2,11], parent=node_c)
# node_j = NodeNonBinary("J", weight=[2], parent=node_f)
# node_k = NodeNonBinary("K", weight=[2], parent=node_f)
# node_l = NodeNonBinary("L", weight=[3], parent=node_g)

# root.children = [node_b, node_c]
# node_b.children = [node_d, node_e]
# node_c.children = [node_f, node_g, node_h, node_i]
# node_f.children = [node_j, node_k]
# node_g.children = [node_l]

root = NodeNonBinary("A")
node_b = NodeNonBinary("B", weight=[1,3], parent=root)
node_c = NodeNonBinary("C", weight=[2,4], parent=root)
node_d = NodeNonBinary("D", weight=[4,7], parent=root)
node_e = NodeNonBinary("E", weight=[1,2], parent=node_c)
node_f = NodeNonBinary("F", weight=[2], parent=node_c)

root.children = [node_b, node_c, node_d]
node_c.children = [node_e, node_f]
print_tree(root)
print(f"\nAlbero non binario temporalmente connesso? : {algoritmo3_NonBinary(root)}")