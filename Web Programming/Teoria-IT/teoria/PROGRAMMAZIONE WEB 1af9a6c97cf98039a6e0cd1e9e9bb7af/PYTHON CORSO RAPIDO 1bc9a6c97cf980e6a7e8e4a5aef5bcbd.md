# PYTHON CORSO RAPIDO

- **Setup** e Python basics
    
    ## Cosa sapere su Python
    
    - È un linguaggio interpretato.
    - L'indentazione è fondamentale.
    - È estremamente flessibile (non sempre un pregio).
    
    ---
    
    ## Setup dell'interprete
    
    1. **Installare**
    2. **Creare un interprete:**
        
        ```bash
        conda create --name isde
        
        ```
        
    3. **Attivare l'interprete:**
        
        ```bash
        conda activate isde
        
        ```
        
    4. **Utilizzare l'interprete**
    5. **(Opzionale) Disattivare l'interprete:**
    L'ultimo passaggio è opzionale in quanto verrà eseguito automaticamente al termine della sessione shell.
        
        ```bash
        conda deactivate
        
        ```
        
    
    **Miniconda:**
    
    Consulta [la documentazione di Miniconda](https://docs.conda.io/en/latest/miniconda.html).
    
    **Nota:**
    
    Se si utilizza un IDE, verificare le istruzioni specifiche per impostare l'interprete nel proprio progetto; questo renderà la vita più semplice!
    
- **Variabili** e Tipi in Python
    
    ```python
    # esempi di tipi
    number = 100          # intero
    another_number = 10.6 # floating point
    letter = "a"          # char
    
    # ottiene il tipo di una variabile
    type(number)
    
    str(number)  # conversione di tipo
    ```
    
    ---
    
    ### **Primo esercizio**
    
    ```python
    a = 15
    b = -20
    c = a - b
    print(c)  # Output?
    
    c = not a
    print(c)  # Output?
    
    c = (a == b) or ((a + b) == -5)
    print(c)  # Output?
    
    ```
    
    **Spiegazione:**
    
    1. `c = a - b` → `c = 15 - (-20)` → `c = 35`
        - Viene fatta la sottrazione tra `15` e `20` → risultato **35**.
    2. `c = not a`
        - `a = 15`, che è un numero diverso da `0` → considerato **True**.
        - `not True` → diventa **False**.
    3. `c = (a == b) or ((a + b) == -5)`
        - `(a == b)` → `15 == -20` → **False**.
        - `(a + b) = 15 + (-20) = -5` → `5 == -5` → **True**.
        - Quindi: `False or True` → **True**.
    
    **Risultati finali:**
    
    ```python
    35
    False
    True
    
    ```
    
    ---
    
    ### **Secondo esercizio**
    
    ```python
    print((4 > 6) and (3 > 8))        # Output?
    print((4 > 6) or (3 > 8))         # Output?
    print(1 == 1 and 2 == 1)          # Output?
    print(False and 0 != 0)           # Output?
    print(not (True and False))       # Output?
    
    ```
    
    **Spiegazione:**
    
    1. `(4 > 6) and (3 > 8)`
        - `4 > 6` → **False**
        - `3 > 8` → **False**
        - `False and False` → **False**
    2. `(4 > 6) or (3 > 8)`
        - `False or False` → **False**
    3. `1 == 1 and 2 == 1`
        - `1 == 1` → **True**
        - `2 == 1` → **False**
        - `True and False` → **False**
    4. `False and 0 != 0`
        - `False` → già False, quindi non valuta nemmeno `0 != 0` (short-circuit)
        - Risultato → **False**
    5. `not (True and False)`
        - `True and False` → **False**
        - `not False` → **True**
    
    **Risultati finali:**
    
    ```python
    False
    False
    False
    False
    True
    
    ```
    
    ---
    
    **Vuoi che te li scriva tutti insieme pronti da copiare?**
    
- Aggregazioni di Variabili
    
    ```python
    l = [0, 1, 2]       # lista
    s = "some text"     # stringa
    
    print(type(l))
    print(type(s))
    
    l = [[0, 1], [2, 3]] # liste annidate
    
    ```
    
- **Indicizzazione** di Liste e Stringhe
    
    ```python
    l = [0, 1, 2]
    
    # prendi il primo elemento (o elemento in posizione X)
    first_element = l[0]   # numerazione parte da zero!
    first_letter = s[0]
    
    # prendi l'ultimo elemento (o elemento in posizione -X)
    last_letter = s[-1]
    
    ```
    
    ```python
    # prendi una porzione di elementi (da A a B -> B non incluso)
    group_of_letters = s[1:5]  # elementi da 1 a 4
    
    # se un'estremità non è specificata, viene usato il default
    first_letters = s[:2]  # default: inizia da 0
    last_letters = s[2:]   # default: termina con -1
    
    # prendi un elemento ogni N
    reverse_string = s[::2]  # ogni 2 elementi
    
    # prendi gli elementi al contrario
    reverse_string = s[::-1]
    
    ```
    
    ```python
    l = [[1, 2], [3, 4, 5]]
    
    # accesso alle liste annidate
    sublist = l[0]
    element_of_sublist = l[0][1]
    
    ```
    
- **Modifica** degli **Elementi** delle **Liste**
    
    ```python
    l = ['a', 1, 2]
    l[0] = 0  # cambia il primo elemento in 0
    
    s = "text"
    s[0] = "n"  # NON FUNZIONA
    s = "next"  # ridefinire la stringa funziona
    
    ```
    

**ATTENZIONE:** Gli elementi delle stringhe non possono essere modificati!

- **Operazioni** con **Stringhe** e **Liste**
    
    ```python
    l = [0, 1, 2]
    l = l + [3, 4, 5]  # concatena le liste
    s = "abc" + "def"  # funziona anche con le stringhe
    
    s = '!' * 30       # crea una stringa con 30 '!'
    number_of_chars = len(s)  # lunghezza della stringa
    
    ```
    
- **Operazioni** con **Solo** le **Stringhe**: lower, upper,  “stringa” in …
    
    ```python
    s = "abCdef"
    lowercase = s.lower()
    uppercase = s.upper()
    
    # verifica se la sequenza "de" è contenuta nella stringa (case sensitive!)
    de_in_s = "de" in s
    
    ```
    
- Fancy Strings - **f”…”**
    
    Dal Python 3.6 è possibile accedere direttamente alle variabili all'interno delle stringhe.
    
    Il valore della variabile viene automaticamente convertito in stringa e concatenato all'interno della stringa.
    
    ```python
    number = 222
    s = f"The lucky number is {number}"
    print(s)
    
    ```
    
- **Tuple**
    
    Le tuple possono essere considerate come liste immutabili.
    
    ```python
    t = (0, 1, 2,)
    
    t[0] = 1  # NON FUNZIONA
    
    ```
    
- **Dizionari**
    
    Ricorda: ogni chiave è unica! Le chiavi non sono ordinate!
    
    ```python
    d = {'age': 22, 'name': 'joe'}
    age = d['age']         # accede all'elemento tramite chiave
    keys = d.keys()        # tutte le chiavi
    values = d.values()    # tutti i valori
    d['surname'] = 'doe'   # aggiunge una nuova chiave
    d['name'] = 'john'     # modifica l'elemento
    
    ```
    
- **Set**
    
    Come per i dizionari, i set non preservano l’ordine degli elementi.
    
    ```python
    # memorizza valori unici, elimina duplicati
    s = {1, 2, 3, 1, 2, 3}
    
    ```
    

Per modificare il flusso di controllo di un programma possiamo utilizzare:

- ***if***
- ***if-else***
- ***if-elif-else***
- ***while***
- ***for***
- Flusso di Controllo Normale
    
    ```python
    # instr1, instr2, instr3
    
    a = 2       # instr1
    b = a + 3   # instr2
    c = b / 2   # instr3
    
    ```
    
- Flusso di Controllo: **if**
    
    ```python
    a = 2  # instr1
    if a >= 1:               # condizione
        print("greater than or equal to 1")  # instrA
    print(a)                 # instr2
    
    ```
    

**ATTENZIONE:** Tutto ciò che è diverso da 0 o False viene considerato True!

- Flusso di Controllo: **if-Else**
    
    ```python
    a = 2  # instr1
    if a >= 1:                        # condizione
        print("greater than or equal to 1")  # instrA
    else:
        print("smaller than 1")       # instrB
    
    ```
    
- Flusso di Controllo: **if-Elif-Else**
    
    ```python
    a = 2  # instr1
    if a >= 1:                # condizione1
        print("greater than 1")   # instrA
    elif a == 1:
        print("equal to 1")     # instrB
    else:
        print("smaller than 1") # instrC
    
    ```
    
- Cicli (**Loops**): I cicli permettono di ripetere la stessa istruzione più volte, finché non viene soddisfatta una condizione di stop.
    
    ---
    
    ## Cicli: **`While`**
    
    Utilizzato per ripetere azioni fino al soddisfacimento della condizione. 
    
    Quando la condizione diventa falsa esco dal while.
    
    *CTRL + C se si rimane bloccati in un ciclo while :D*
    
    ```python
    a = 0  # instr1
    while a < 10:    # condizione,  continua finchè la condizione è vera
        a += 1     # instrA
    print(a)       # instr2
    
    ```
    
    ---
    
    ## Cicli: `For`
    
    Utilizzato per strutture basate su indice o per ripetere azioni (esattamente) N volte.
    
    ```python
    #get only items
    for item in [0, 1, 2]:
        print(item)
    
    # get index and item
    for index, item in enumerate([0, 1, 2]):
        print(index, item)
    
    # do action exactly N times
    for i in range(10):
        print("string")
    
    ```
    
    ---
    
    ## Cicli: `For con Dizionari`
    
    ```python
    d = {'A': [0, 1, 2], 'B': [3, 4, 5]}
    
    for key, value in d.items():
        print(key, value)
    
    ```
    

- **Funzioni**
    
    Le funzioni sono utili per suddividere problemi complessi in sottoproblemi più semplici e risolvibili.
    
    Esempio:
    
    **Problema principale:** Togliere un punto per ogni voto di ogni studente.
    
    **Sottoproblema:** Sottrarre uno a tutti gli elementi di una lista (da risolvere per ogni studente).
    
    **Sotto-sottoproblema:** Sottrarre uno ad un elemento.
    
    Dati gli studenti:
    
    ```python
    students = {
        'A': [20, 23, 22, 19],
        'B': [18, 22, 19, 28],
        'C': [30, 18, 22, 30]
    }
    
    ```
    
- **Definizione** di Funzioni
    
    ```python
    def subtract_one(x):
        """Sottrae un punto dal punteggio x"""
        return x - 1
    
    def subtract_one_list(x):
        """Restituisce una nuova lista con i punteggi diminuiti di 1"""
        new_list = []  # lista vuota
        for item in x:
            lower_score = subtract_one(item)
            new_list.append(lower_score)  # aggiunge l'elemento
        return new_list
    
    def subtract_one_to_all(x):
        ...  # divertiti a completare :)
    
    ```
    
- Funzioni Senza Input o Output
    
    ```python
    def no_input():
        return 10
    
    def no_return(x):
        print(x)
    
    def no_input_and_return():
        print("I will return nothing.")
    
    result = no_input_and_return()  # restituisce None
    
    ```
    
- Funzioni con Molteplici Parametri e Risultati
    
    ```python
    # due parametri di input
    def concatenate_strings(s1, s2):
        return s1 + s2
    
    # restituisce due risultati
    def sum_and_subtract_10(x):
        return 10 + 10, 10 - 10
    ```
    
- **Scope :** Le variabili all'interno di una funzione sono accessibili solo all'interno della funzione stessa (scope).
    
    ```python
    def concatenate_strings(s1, s2):
        print(s1)  # funziona
    
    a = "aa"
    b = "bb"
    concatenate_strings(a, b)
    print(s1)  # genera errore perché s1 non è definita fuori dalla funzione
    
    ```
    
- Funzioni **Built-in**
    
    Python mette a disposizione molte funzioni built-in.
    
    **RACCOMANDAZIONE:** Non utilizzare nomi di funzioni o variabili che corrispondono a funzioni built-in!
    
    ```python
    x = [0, -1, 2, -10]
    m = min(x)   # trova il minimo
    l = len(x)   # trova la lunghezza
    
    ```
    
- **Librerie**
    
    Esempio di utilizzo di librerie:
    
    ```python
    import math
    x = 0
    s = math.sin(x)
    
    import math.sin
    s = math.sin(x)  # importa solo il modulo 'sin'
    
    from math import sin
    s = sin(x)       # può essere usato senza specificare la libreria
    
    import math as m
    s = m.sin(x)     # usa un alias per la libreria
    
    ```
    
- Installazione Librerie
    
    Le librerie esterne possono essere installate tramite i packet manager di Python.
    
    I più utilizzati sono **conda** e **pip**.
    
    ```bash
    conda install pip
    pip install numpy
    
    ```
    

---

# **`ESERCIZI`**

- **Parte 1:** Esercizi sulle Funzioni, Liste e Dizionari
    - `Esercizio 1` :Scrivi una funzione che, presa una lista, stampi il tipo di ogni elemento.
        
        ```python
        def print_types(lst):
            for element in lst:
                print(f"L'elemento {element} è di tipo {type(element)}")
        
        # Esempio d'uso:
        print_types([1, "ciao", 3.14, True])
        
        ```
        
        **Spiegazione:**
        
        La funzione `print_types` riceve una lista, scorre ogni elemento e usa la funzione built-in `type()` per determinare e stampare il tipo dell'elemento insieme al suo valore.
        
    - `Esercizio 2` : Scrivi una funzione che crei un dizionario, dato una lista di chiavi e una lista di valori.
        
        ```python
        def create_dict(keys, values):
            if len(keys) != len(values):
                raise ValueError("Le liste di chiavi e valori devono avere la stessa lunghezza!")
            return dict(zip(keys, values))
        
        # Esempio d'uso:
        chiavi = ["nome", "età", "città"]
        valori = ["Alice", 30, "Roma"]
        dizionario = create_dict(chiavi, valori)
        print(dizionario)
        
        ```
        
        **Spiegazione:**
        
        La funzione `create_dict` verifica che le due liste abbiano la stessa lunghezza (altrimenti solleva un errore) e utilizza `zip()` per accoppiare le chiavi ai valori, restituendo infine il dizionario creato.
        
    - `Esercizio 3`:Scrivi una funzione che trovi il valore minimo di ogni lista contenuta in un dizionario. Risolvila in due modi:
        - *Scrivi una funzione che trovi il valore minimo di ogni lista contenuta in un dizionario. Risolvila in due modi:
        1. Usando la funzione `min`.
        2. Senza usare la funzione `min`.**
        
        *Soluzione con `min`:*
        
        ```python
        def min_values_with_min(d):
            result = {}
            for key, lst in d.items():
                result[key] = min(lst)
            return result
        
        # Esempio d'uso:
        dati = {"A": [3, 1, 4], "B": [10, 5, 8]}
        print("Con min:", min_values_with_min(dati))
        
        ```
        
        *Soluzione senza `min`:*
        
        ```python
        def min_values_without_min(d):
            result = {}
            for key, lst in d.items():
                # Presupponiamo che la lista non sia vuota
                min_val = lst[0]
                for num in lst:
                    if num < min_val:
                        min_val = num
                result[key] = min_val
            return result
        
        # Esempio d'uso:
        print("Senza min:", min_values_without_min(dati))
        
        ```
        
        **Spiegazione:**
        
        Nella prima soluzione, per ogni chiave del dizionario si usa `min(lst)` per trovare il minimo nella lista. Nella seconda soluzione si inizializza il minimo al primo elemento della lista e si scorre la lista aggiornando il minimo ogni volta che si trova un valore inferiore.
        
    - `Esercizio 4` : Scrivi la funzione `guess_number` che richiede un input all’utente e fornisce suggerimenti ("troppo basso" o "troppo alto") fino a quando il numero segreto viene indovinato.
        
        ```python
        def guess_number():
            secret = 7  # numero segreto fissato; può essere modificato o generato casualmente
            while True:
                try:
                    guess = int(input("Indovina il numero segreto: "))
                except ValueError:
                    print("Errore: inserisci un numero valido!")
                    continue  # ripete il ciclo se l'input non è un intero
        
                if guess < secret:
                    print("Troppo basso!")
                elif guess > secret:
                    print("Troppo alto!")
                else:
                    print("Bravo! Hai indovinato!")
                    break
        
        # Per eseguire la funzione, decommenta la riga seguente:
        # guess_number()
        
        ```
        
        **Spiegazione:**
        
        La funzione utilizza un ciclo `while True` per chiedere ripetutamente all’utente un numero. Con `try/except` si gestiscono errori nel caso in cui l’input non sia convertibile in intero. In base al confronto tra il numero inserito e il numero segreto, il programma fornisce un suggerimento o esce dal ciclo se il numero è indovinato.
        
    
- **Parte 2:** Esercizi sulle Classi in Python
    - `Esercizio 1`
        
        **Scrivi una classe `Vehicle` con attributi d'istanza `max_speed` e `current_speed`. Il valore di default per `max_speed` deve essere 200.
        Implementa inseoltre il metodo `set_speed` che, dato un target di velocità, controlla se questo supera `max_speed` e, in tal caso, imposta `current_speed` a `max_speed` (stampando un messaggio).**
        
        ```python
        class Vehicle:
            def __init__(self, current_speed, max_speed=200):
                self.max_speed = max_speed
                self.current_speed = current_speed
        
            def set_speed(self, speed):
                if speed > self.max_speed:
                    print(f"La velocità desiderata ({speed}) supera la velocità massima. Imposto {self.max_speed} come velocità.")
                    self.current_speed = self.max_speed
                else:
                    self.current_speed = speed
        
        # Esempio d'uso:
        v = Vehicle(current_speed=50)
        v.set_speed(250)  # Dovrebbe impostare current_speed a 200 e stampare un messaggio.
        print("Velocità corrente:", v.current_speed)
        
        ```
        
        **Spiegazione:**
        
        La classe `Vehicle` viene inizializzata con la velocità corrente e (opzionalmente) con una velocità massima, di default 200. Il metodo `set_speed` confronta la velocità richiesta con `max_speed` e, se la supera, imposta `current_speed` a `max_speed` mostrando un messaggio.
        
    - `Esercizio 2`
        
        **Crea una classe `Bus` che eredita da `Vehicle` e aggiunge gli attributi `max_capacity` e `occupied_seats`.
        Aggiungi un metodo `board` per aggiungere passeggeri, controllando che il numero totale di passeggeri non superi la capacità massima.**
        
        ```python
        class Bus(Vehicle):
            def __init__(self, current_speed, max_speed=200, max_capacity=50, occupied_seats=0):
                super().__init__(current_speed, max_speed)
                self.max_capacity = max_capacity
                self.occupied_seats = occupied_seats
        
            def board(self, num):
                if self.occupied_seats + num > self.max_capacity:
                    print("Capacità massima superata!")
                else:
                    self.occupied_seats += num
                    print(f"{num} passeggeri saliti. Totale a bordo: {self.occupied_seats}")
        
        # Esempio d'uso:
        bus = Bus(current_speed=0)
        bus.board(20)
        bus.board(35)  # Dovrebbe stampare un messaggio di errore per superamento capacità.
        
        ```
        
        **Spiegazione:**
        
        La classe `Bus` eredita dalla classe `Vehicle` e aggiunge due nuovi attributi relativi alla capacità: `max_capacity` e `occupied_seats`. Il metodo `board` controlla se aggiungere il numero di passeggeri richiesto supererebbe la capacità massima e, in tal caso, segnala l’errore, altrimenti incrementa il numero di posti occupati.
        
    - `Esercizio 3`
        
        Questa parte utilizza il modulo `turtle` per disegnare poligoni e per creare una classe personalizzata.
        
        ### Esercizio 3a
        
        **Implementa una funzione `draw_polygon` che, dato un'istanza di turtle, il numero di lati e la lunghezza del lato, disegni un poligono regolare. Se il numero di lati è minore di 3, solleva un errore.**
        
        ```python
        import turtle
        
        def draw_polygon(t, sides=3, side_length=100):
            if sides < 3:
                raise ValueError("Non si può disegnare un poligono con meno di tre lati!")
            # Calcola l'angolo esterno: 180 - (angolo interno)
            # Gli angoli interni di un poligono regolare: (180*(sides - 2)) / sides
            angle = 180 - ((180 * (sides - 2)) / sides)
            for _ in range(sides):
                t.forward(side_length)
                t.right(angle)
        
        # Esempio d'uso (scommenta per eseguire):
        # wn = turtle.Screen()
        # t = turtle.Turtle()
        # draw_polygon(t, sides=5)
        # wn.exitonclick()
        
        ```
        
        **Spiegazione:**
        
        La funzione `draw_polygon` prima verifica che il numero di lati sia almeno 3, altrimenti solleva un `ValueError`. Poi calcola l'angolo necessario per disegnare il poligono e usa un ciclo `for` per far avanzare la turtle e ruotarla di conseguenza.
        
        - spiegazione migliore
            
            Il codice nel file `test.py` utilizza la libreria `turtle` per disegnare un poligono. Ecco una spiegazione passo-passo:
            
            1. Importa la libreria `turtle` che permette di disegnare graficamente.
            2. Definisce una funzione `draw_polygon` che accetta tre parametri:
                - `t`: l'oggetto turtle che disegna.
                - `sides`: il numero di lati del poligono (default è 3).
                - `side_length`: la lunghezza di ciascun lato (default è 100).
            3. Controlla se il numero di lati è inferiore a 3 e, in tal caso, solleva un'eccezione (`ValueError`).
            4. Calcola l'angolo esterno del poligono usando la formula: `180 - ((180 * (sides - 2)) / sides)`.
            5. Utilizza un ciclo `for` per disegnare ogni lato del poligono:
                - Muove la turtle in avanti di `side_length`.
                - Ruota la turtle a destra di `angle`.
            6. Crea una finestra `turtle.Screen()` e un oggetto turtle `turtle.Turtle()`.
            7. Chiama la funzione `draw_polygon` per disegnare un poligono con 5 lati.
            8. La finestra si chiude quando si clicca su di essa (`wn.exitonclick()`).
            
            Ecco il codice con i commenti in italiano per maggiore chiarezza:
            
            ```python
            import turtle
            
            def draw_polygon(t, sides=3, side_length=100):
                if sides < 3:
                    raise ValueError("Non si può disegnare un poligono con meno di tre lati!")
                # Calcola l'angolo esterno: 180 - (angolo interno)
                # Gli angoli interni di un poligono regolare: (180*(sides - 2)) / sides
                angle = 180 - ((180 * (sides - 2)) / sides)
                for _ in range(sides):
                    t.forward(side_length)
                    t.right(angle)
            
            # Esempio d'uso (scommenta per eseguire):
            wn = turtle.Screen()
            t = turtle.Turtle()
            draw_polygon(t, sides=5)
            wn.exitonclick()
            
            ```
            
            Questo codice disegnerà un pentagono (poligono con 5 lati) quando eseguito.
            
            Le righe selezionate creano una finestra grafica e un oggetto tartaruga utilizzando il modulo `turtle` di Python. Ecco una spiegazione dettagliata:
            
            ```python
            wn = turtle.Screen()
            t = turtle.Turtle()
            
            ```
            
            1. `wn = turtle.Screen()`: Questa riga crea una nuova finestra grafica (screen) dove verranno disegnate le forme. La variabile `wn` rappresenta questa finestra.
            2. `t = turtle.Turtle()`: Questa riga crea un nuovo oggetto tartaruga (turtle) che può essere utilizzato per disegnare all'interno della finestra grafica. La variabile `t` rappresenta questa tartaruga.
            
            In sintesi, queste righe inizializzano l'ambiente di disegno con una finestra e una tartaruga per tracciare le forme.
            
        
        ---
        
        ### Esercizio 3b
        
        **Implementa una classe `MyTurtle` che erediti dalla classe `turtle.Turtle` e, all'inizializzazione, imposti la forma a "turtle" e il colore a rosso. Verifica poi che funzioni con la funzione `draw_polygon`.**
        
        ```python
        import turtle
        
        class MyTurtle(turtle.Turtle):
            def __init__(self):
                super().__init__()
                self.shape("turtle")
                self.color("red")
        
        # Esempio d'uso (scommenta per eseguire):
        # wn = turtle.Screen()
        # t = MyTurtle()
        # draw_polygon(t, sides=6)
        # wn.exitonclick()
        
        ```
        
        **Spiegazione:**
        
        La classe `MyTurtle` eredita da `turtle.Turtle`. Nel metodo `__init__`, dopo aver chiamato l’inizializzazione della classe base, si impostano forma e colore in modo personalizzato (rosso). La classe eredita tutte le funzionalità della turtle originale, per cui può essere utilizzata con la funzione `draw_polygon`.
        
    
- **Parte 3:** Gestione degli Errori e Costrutti Try-Except
    - `Esercizio 1`
        
        **Modifica la funzione `draw_polygon` in modo che, se il numero di lati è minore di 3, sollevi un `ValueError` e utilizza un blocco try-except per gestire l’errore.**
        
        ```python
        def draw_polygon_safe(t, sides=3, side_length=100):
            if sides < 3:
                raise ValueError("Non si può disegnare un poligono con meno di tre lati!")
            angle = 180 - ((180 * (sides - 2)) / sides)
            for _ in range(sides):
                t.forward(side_length)
                t.right(angle)
        
        # Esempio di gestione con try-except:
        # wn = turtle.Screen()
        # t = turtle.Turtle()
        # try:
        #     draw_polygon_safe(t, sides=-1)
        # except ValueError as e:  # intercetta l'errore specifico
        #     print("Errore:", e)
        #     draw_polygon_safe(t, sides=5)
        # wn.exitonclick()
        
        ```
        
        **Spiegazione:**
        
        In questa versione della funzione, se il numero di lati è minore di 3, viene sollevato un `ValueError`. Il blocco `try-except` cattura l'errore e, in questo esempio, in caso di errore, richiama la funzione con un numero valido di lati (5).
        

---