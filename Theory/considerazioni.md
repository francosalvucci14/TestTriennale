- per dire che fra due nodi u e v esiste un percorso temporale, basta vedere solo u->v e non il viceversa,perchè i tempi di attivazione sono in ordine crescente
    - Si potrebbe fare che le etichette siano scelte random???
- Oppure serve un'approccio sia top-down che bottom-up?? **da chiedere**
    - I percorsi temporali devono essere intesi come bidirezionali, quindi da U a V e da V a U, oppure solo da una direzione?
- Posso dire che un albero è temporalmente connesso se, facendo partire la BFS temporale dalla radice dell'albero, si toccano tutti i nodi??? **da chiedere**
- Se aun solo percorso da u a v non rispetta la proprietà temporale, posso affermare con certezza che l'albero non è temporalmente connesso? prob. si perchè se esiste un percorso di questo tipo, allora esisterà un nodo singolo che non si può connettere con gli altri, in teoria
- Proabile approccio DP??
- Il costo deve essere $O(M)$ con M= numero di archi, Oppure M= numero di percorsi temporali totali?
    - Con la seconda, prob. problema NP-Hard 

