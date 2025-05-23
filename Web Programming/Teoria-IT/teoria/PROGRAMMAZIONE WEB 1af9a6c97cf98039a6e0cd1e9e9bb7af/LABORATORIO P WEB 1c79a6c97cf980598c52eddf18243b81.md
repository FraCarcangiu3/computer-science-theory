# LABORATORIO P.WEB

---

**`LAB 1 - INTRODUZIONE`**

- Introduzione a FastAPI
    
    **Cos’è FastAPI:**
    
    FastAPI è una libreria scritta in Python che, pur mantenendo una sintassi semplice, risulta estremamente efficiente. Offre numerosi meccanismi integrati (gli “irti”, ovvero strumenti e controlli) che riducono il rischio di errori e bug durante lo sviluppo dell’applicazione. Questi controlli, insieme all’utilizzo delle type hints, permettono di avere un controllo stretto sugli input e rendono il codice più sicuro e robusto.
    
    - **Cos’è FastAPI:**
    FastAPI è una libreria scritta in Python che, pur essendo molto semplice da usare, risulta estremamente efficiente.
        - È progettata per ridurre errori e bug comuni nello sviluppo, grazie a meccanismi integrati che validano gli input e rendono il codice più sicuro.
        - È già utilizzata in numerose applicazioni reali.
        - Per ulteriori dettagli e una guida introduttiva, si può consultare la documentazione ufficiale:[https://fastapi.tiangolo.com/tutorial/](https://fastapi.tiangolo.com/tutorial/)
- Creazione dell’Environment
    
    **Utilizzo di Conda:**
    
    - Per creare o attivare un environment specifico tramite Conda, si utilizza il comando:
    Questo comando permette di passare all’ambiente in cui saranno installate le librerie necessarie (come FastAPI).
        
        ```
        conda activate "nome dell’environment"
        ```
        
    
    **Utilizzo di PyCharm:**
    
    - In PyCharm, è possibile creare un nuovo progetto e, durante la creazione, scegliere di creare un ambiente virtuale personalizzato (custom environment).
    - Nella configurazione, si specifica la versione di Python desiderata (per esempio, Python 3.10) tramite un menu a tendina.
    - Questo passaggio è fondamentale per garantire che il progetto utilizzi la versione corretta di Python e che tutte le librerie siano installate nel contesto isolato dell’environment.
    - **`Creazione del progetto`**
        - **IDE e Scelta dell’Editor:**
            
            Puoi utilizzare qualsiasi IDE o editor di testo (ad esempio PyCharm, VS Code o anche un editor semplice).
            
            - Crea una cartella o un nuovo progetto per organizzare il tuo codice.
        - **Creazione dell’Environment:**
            
            È importante creare un ambiente virtuale Python (usando Conda o virtualenv) per assicurarti di utilizzare la versione corretta di Python (consigliata la versione ≥ 3.8, meglio ≥ 3.10) e per isolare le dipendenze del progetto.
            
            **Esempio con Conda o virtualenv:**
            
            - Con Conda, attiva l’environment con:
                
                ```
                conda activate "nome_dell_environment"
                
                ```
                
            - Con virtualenv, crea e attiva l’ambiente virtuale:
                
                ```
                python -m venv .venv
                source .venv/bin/activate  # su macOS/Linux
                .venv\\Scripts\\activate     # su Windows
                
                ```
                
        - **Installazione delle Librerie:**
            
            Una volta attivato l’environment, installa FastAPI e altre librerie utili (ad esempio requests) tramite pip:
            
            ```
            pip install fastapi[standard] requests
            
            ```
            
        - **Creazione del File Principale:**
            
            Nella cartella del progetto, crea un file chiamato `main.py` che conterrà il codice della tua applicazione FastAPI.
            
    - **`Creazione dell’enviroment`**
        
        ---
        
        ## 🐍 1. **ENVIRONMENT VIRTUALE (virtualenv)**
        
        ### ▶️ **Su PyCharm**
        
        ### ✅ Come fare:
        
        1. **Apri PyCharm** e crea un nuovo progetto.
        2. Nella schermata iniziale scegli:
            - ✅ **"New environment using: Virtualenv"**
            - ✅ Specifica il percorso del nuovo ambiente (`.venv`).
            - ✅ Scegli l'interprete Python da usare.
        3. Clicca su **"Create"**.
        
        📌 Dopo la creazione, PyCharm userà **automaticamente** quell’environment per il progetto.
        
        ---
        
        ### ▶️ **Su Visual Studio (con Python workload installato)**
        
        ### ✅ Come fare:
        
        1. **Apri Visual Studio** e crea un nuovo progetto Python.
        2. Vai su **Solution Explorer** > clic destro su progetto > **Python Environment**.
        3. Clic su **"Add Environment"**.
        4. Seleziona:
            - ✅ **Virtual Environment**
            - ✅ Scegli il base interpreter (Python)
        5. Dai un nome e clicca **Create**.
        
        📌 L’ambiente sarà visibile e gestibile nel pannello "Python Environments".
        
        ---
        
        ## 🐳 2. **ENVIRONMENT CONTAINER (Docker)**
        
        ### ▶️ **Su PyCharm Professional (non disponibile in Community)**
        
        ### ✅ Come fare:
        
        1. Apri il progetto.
        2. Vai su **Settings > Project > Python Interpreter**.
        3. Clic sull’⚙️ e scegli **"Add..."** > **"Docker"**.
        4. Scegli:
            - Docker Engine (local o remoto)
            - Immagine base (es. `python:3.10`)
        5. PyCharm userà Docker come interprete.
        
        📦 Puoi anche creare un `Dockerfile`:
        
        ```
        FROM python:3.10
        WORKDIR /app
        COPY . .
        RUN pip install -r requirements.txt
        CMD ["python", "main.py"]
        
        ```
        
        ---
        
        ### ▶️ **Su Visual Studio (con Docker Tools)**
        
        ### ✅ Come fare:
        
        1. Crea o apri un progetto.
        2. Clic destro sul progetto > **Add > Docker Support**.
        3. Scegli Python e genera automaticamente il `Dockerfile`.
        
        Visual Studio creerà:
        
        - `Dockerfile`
        - `docker-compose.yml`
        
        Per eseguire: premi **F5** e gira tutto nel container!
        
        ---
        
        ## ✅ Conclusione
        
        | IDE | Virtualenv | Docker |
        | --- | --- | --- |
        | **PyCharm** | Impostato al progetto | Solo con versione Pro |
        | **Visual Studio** | Da Python Environments | Con Docker Tools installati |
        
        ---
        
        Vuoi un esempio pratico completo (tipo con `requirements.txt`, `Dockerfile`, ecc.)?
        
- Installazione di Fast API
    
    **Comando di Installazione:**
    
    - Una volta attivato l’environment, per installare FastAPI si esegue il seguente comando:
        
        ```
        pip install 'fastapi[standard]'
        
        ```
        
    - La sintassi con le parentesi quadre (`[standard]`) serve a installare non solo FastAPI ma anche tutte le dipendenze consigliate (le “estensioni standard”) che garantiscono un funzionamento ottimale e una maggiore copertura delle funzionalità.
- **Prima Applicazione Web con FastAPI**
    - Configurazione Base
        
        Nel file `main.py`, scrivi il seguente codice per creare la tua prima applicazione web:
        
        ```python
        from fastapi import FastAPI
        
        # Creazione dell'istanza dell'applicazione FastAPI
        app = FastAPI()
        
        # Definizione di un endpoint per il metodo GET all'indirizzo "/"
        @app.get("/")
        def hello_world():
            return "Hello World!"
        
        ```
        
        - **Spiegazione:**
            - **Istanza dell'Applicazione:**`app = FastAPI()` crea l'oggetto principale che rappresenta la tua applicazione.
            - **Decoratore @app.get("/")**
            Indica che la funzione seguente verrà eseguita quando viene effettuata una richiesta HTTP GET all'URL radice (`/`).
                
                Definire un endpoint per il metodo GET all'indirizzo "/" significa che stai creando un punto finale nel tuo server web che risponde alle richieste HTTP GET inviate al percorso radice del sito. 
                In altre parole:
                Quando un client (ad esempio un browser) invia una richiesta GET a "http://tuo_server/" (senza percorsi aggiuntivi dopo il dominio), il server esegue la funzione che hai definito per quel percorso.
                
            - In FastAPI, questo viene fatto utilizzando il decoratore `@app.get("/")` che associa la funzione successiva all'URL "/" per il metodo GET.
            La funzione, chiamata anche "endpoint function", gestisce la richiesta e restituisce una risposta (ad esempio, una stringa o un oggetto JSON).
            Quindi, con l'istruzione "# Definizione di un endpoint per il metodo GET all'indirizzo '/'" **si intende che stai impostando il comportamento del tuo server per rispondere correttamente alle richieste GET dirette alla root dell'applicazione.**
            - **Funzione hello_world:**
            La funzione viene chiamata "path function" o "endpoint function". Essa restituisce la stringa `"Hello World!"` che, in automatico, viene convertita in formato JSON nella risposta HTTP.
    - Esecuzione dell’Applicazione
        
        **Avvio con Uvicorn:**
        
        Per eseguire l'applicazione, posizionati nella cartella contenente `main.py` e lancia il comando:
        
        ```
        uvicorn main:app
        
        ```
        
        - Qui, `main` è il nome del file (senza `.py`) e `app` è l'istanza dell'applicazione.
        - Una volta avviato, l’app verrà eseguita sul localhost (generalmente all’indirizzo `http://127.0.0.1:8000`).
    - Verifica
        
        ---
        
        ### ✅ COSA TI SERVE
        
        - Avere il server FastAPI già **in esecuzione** (con `uvicorn main:app --reload`)
        - Avere installata la libreria `requests` (puoi installarla con `pip install requests`)
        - Avere un file `.py` dove scrivere il codice
        
        ---
        
        ### ✅ PASSAGGI DA FARE
        
        ### 🟢 1. Crea un nuovo file Python
        
        - Se sei in **VS Code** o **PyCharm**, fai clic con il tasto destro sulla cartella del progetto e scegli **"New File"**.
        - Chiamalo per esempio: `test_request.py`
        
        ### 🟢 2. Scrivi dentro questo file il codice:
        
        ```python
        import requests  # importa la libreria requests
        
        # fai una richiesta GET al server FastAPI
        response = requests.get("<http://127.0.0.1:8000>")
        
        # stampa il contenuto della risposta del server
        print(response.text)
        
        ```
        
        > Nota: se il tuo server FastAPI risponde su una porta diversa dalla 8000, cambia l’URL di conseguenza.
        > 
        
        ### 🟢 3. Esegui lo script
        
        - Apri il **terminale** nella stessa cartella dove hai salvato `test_request.py`
        - Esegui il file con questo comando:
            
            ```
            python test_request.py
            ```
            
        - Se tutto funziona, vedrai stampato nel terminale:
            
            ```
            "Hello World!"
            ```
            
        
        ---
        
        ### 📌 Importante
        
        Assicurati che **FastAPI sia già avviato** prima di eseguire lo script, altrimenti otterrai un errore di connessione.
        
        Esempio di comando per avviare FastAPI:
        
        ```
        uvicorn main:app --reload
        
        ```
        
        ---
        
    - Ricaricamento Automatico!
        - **Comando con Ricaricamento:**
            
            Durante lo sviluppo, è comodo non dover riavviare manualmente l'app ogni volta che apporti modifiche. Usa:
            
            ```
            uvicorn main:app --reload
            
            ```
            
            Il flag `--reload` fa sì che il server si riavvii automaticamente ad ogni modifica del codice.
            
        - **Nuovo Comando in FastAPI:**
            
            Le ultime versioni di FastAPI introducono anche il comando:
            
            ```
            fastapi dev main.py
            
            ```
            
            che attiva il reload di default e non richiede di specificare l’app da eseguire, a meno che non ci siano più istanze nel file.
            
- Gestione dei Percorsi URL e Parametri
    - Modifica dell’Endpoint
        - **Modifica del Percorso:**
        Puoi cambiare il percorso a cui l'app risponde modificando il decoratore. Ad esempio:
        Ora l'endpoint risponderà alle richieste all'indirizzo `http://127.0.0.1:8000/hello`.
            
            ```python
            @app.get("/hello")
            def hello_world():
                return "Hello World!"
            ```
            
    - Struttura dell’URL
        
        Un URL completo ha la forma:
        
        ```
        http://<host>[:<port>][/<path>][?<query>]
        
        ```
        
        - La **query string** inizia dopo il simbolo `?` e contiene coppie `chiave=value` separate dal simbolo `&`.
    - Gestione dei **`parametri`** in FastAPI
        
        Puoi definire una funzione che accetta parametri come argomenti:
        
        ```python
        @app.get("/")
        def hello_world(param1, param2):
            return f"Hello World! param1={param1} param2={param2}"
        ```
        
        Se visiti, per esempio, `http://127.0.0.1:8000/?param1=1&param2=2`, la funzione riceverà i valori e restituirà la stringa con i parametri incorporati.
        
    - Parametri Opzionali
        
        Se vuoi che un parametro sia opzionale, puoi definirne un valore di default:
        
        ```python
        @app.get("/")
        def hello_world(param1, param2=2):
            return f"Hello World! param1={param1} param2={param2}"
        
        ```
        
        In questo modo, se il parametro `param2` non viene passato, assume il valore di default `2`.
        
- Parametri di Percorso
    - Definizione di Parametri di Percorso
        
        Puoi definire un endpoint che accetta un parametro direttamente dal percorso:
        
        ```python
        @app.get("/items/{item_id}")
        def get_item(item_id):
            return f"Hello World! item_id={item_id}"
        
        ```
        
        - Quando fai una richiesta a `http://127.0.0.1:8000/items/qualcosa`, il valore al posto di `{item_id}` viene passato alla funzione.
    - Uso Combinato di Parametri di Percorso e Query String:
        
        È possibile definire un endpoint che accetta sia parametri di percorso che query string, applicando type hints per la validazione:
        
        ```python
        @app.get("/items/{item_id}")
        def get_item(item_id: int, param1: int, param2: int = 2):
            return f"Hello World! item_id={item_id}, param1={param1}, param2={param2}"
        
        ```
        
        - In questo esempio, se `item_id` non è un intero o se i parametri passati non rispettano il tipo, FastAPI genererà un errore.
        - esempio per testare:
        
        [http://127.0.0.1:8000/items/5?param1=10](http://127.0.0.1:8000/items/5?param1=10)
        
    - Ordine degli Endpoint
        
        Se hai un endpoint con un valore fisso e uno parametrico, devi dichiarare prima l’endpoint a valore fisso. Ad esempio:
        
        ```python
        @app.get("/items/pippo")
        def fixed_item():
            return "Hello World! - ENDPOINT PIPPO"
        
        @app.get("/items/{item_id}")
        def get_item(item_id: str):
            return f"Hello World! item_id={item_id}"
        
        ```
        
        Questo garantisce che una richiesta a `/items/pippo` venga gestita dalla funzione fissa e non catturata dall’endpoint parametrico.
        
- Introduzione ai Type Hints
    - Perchè i Type Hints
        
        Python è un linguaggio dinamico, il che significa che una variabile può assumere qualsiasi tipo di dato. Questo offre flessibilità ma può portare a bug e vulnerabilità.
        
        - I type hints, introdotti a partire da Python 3.5, permettono di esplicitare il tipo di dato che una variabile o parametro deve avere.
        - Anche se a runtime Python non obbliga il rispetto dei type hints, gli IDE (come PyCharm o VS Code) mostrano alert utili per lo sviluppo.
        - FastAPI, tramite Pydantic, usa questi type hints per validare gli input e garantire che vengano rispettati i tipi previsti.
    - **`ESEMPI`** di type Hints
        - **Per Variabili:**
            
            ```python
            name: str = "name"
            number: int = 0
            values: list[str] = ["a", "b"]
            dictionary: dict[str, int] = {"a": 0}
            
            ```
            
        - **Per le Funzioni:**
            
            ```python
            def somma(x: int, y: int) -> int:
                return x + y
            
            def stampa(testo: str) -> None:
                print(testo)
            
            ```
            
        - **Utilizzo nei Parametri degli Endpoint:**
            
            ```python
            @app.get("/")
            def hello_world(param1: int, param2: int = 2):
                return f"Hello World! param1={param1} param2={param2}"
            
            ```
            
            Se si prova a passare un valore non intero (ad esempio, `pippo`), FastAPI restituirà un errore, garantendo così la corretta tipizzazione degli input.
            

---

 Documentazione completa Pydantic: [https://docs.pydantic.dev/latest/concepts/fields/](https://docs.pydantic.dev/latest/concepts/fields/)

**`LAB 2 - GITHUB - PARTE BACKEND`**

- Creazione e Configurazione del Repository GitHub
    - Accedete all’interfaccia web di GitHub e cliccate su “Create Repository”.
    - Impostate:
        - Nome del repository
        - Descrizione
        - Visibilità (pubblico o privato)
        - Eventuali file iniziali (README, .gitignore – consigliato il template per Python –, licenza)
    - Concludete cliccando su "Create Repository".
- Clonazione del Repository
    - **Recupero del link:**
        
        Dal repository creato, cliccate su “Code” per visualizzare e copiare il link.
        
    - **Clonazione tramite terminale:**
        - Aprite un terminale nella cartella scelta e lanciate il comando:
            
            ```
            git clone <link del repository>
            
            ```
            
        - Dopo la clonazione, la cartella locale avrà lo stesso nome del repository e risulterà collegata a quello remoto.
    - **Controlli utili:**
        - `git status` per verificare lo stato dei file
        - `git branch` per consultare i branch disponibili
            
            
- Configurazione del Repository e Gestione dei File
    - **Utilizzo dell’IDE:**
        - Aprite il progetto in un IDE come PyCharm per agevolare la gestione dei file.
    - **Creazione di un file per le librerie (requirements.txt):**
        - Creare un file denominato `requirements.txt` in cui inserire:
            - `fastapi[standard]`
            - `requests`
    - **Aggiunta dei file al controllo versione:**
        - Se non viene chiesto automaticamente dall’IDE, utilizzare il comando da terminale:
            
            ```
            git add <nome_file>
            ```
            
            o, per aggiungere tutti i file, usare:
            
            ```
            git add .
            ```
            
        
- Creazione dell’Ambiente Python
    - **Creazione dell’environment:**
        - Utilizzando strumenti come `virtualenv` o `conda`, create un nuovo ambiente Python. Ad esempio, con Conda:
            
            ```
            conda create -n <nome_env> python=3.10
            conda activate <nome_env>
            ```
            
    - **Installazione delle dipendenze:**
        
        Una volta attivato l’environment, installate i requisiti tramite:
        
        ```
        pip install -r requirements.txt
        ```
        
    - **Aggiornamento del repository remoto:**
        
        Dopo aver apportato delle modifiche, ricordate di salvare i cambiamenti con:
        
        ```
        git commit -m "<commit_message>"
        git push
        ```
        
- *altri comandi utili* GITHUB
    - **m in git commit:**
    
    L'opzione “-m” sta per “message” e ti permette di specificare direttamente il messaggio del commit, senza aprire l’editor predefinito.
    
    Esempio:
    
    ```
    git commit -m "Aggiunta nuova funzionalità"
    
    ```
    
    ---
    
    Di seguito, una lista di “sotto-comandi” e opzioni utili per utilizzare GitHub da terminale:
    
    - **git log:**
    
    Mostra la cronologia dei commit.
    
    - Puoi usare opzioni come `-oneline` per una vista compatta o `-graph` per visualizzare la struttura dei branch.
    - **git diff:**
    
    Mostra le differenze tra lo stato attuale dei file e l’ultimo commit (o tra commit differenti).
    
    - Puoi specificare file o branch per vedere differenze più specifiche.
    - **git reset:**
    
    Permette di annullare commit o rimuovere file dall'area di staging.
    
    - `git reset HEAD <file>`: Rimuove il file dall'area di staging.
    - `git reset --hard`: Ripristina completamente lo stato del repository allo stato dell'ultimo commit (attenzione, i cambiamenti non committati vengono persi).
    - **git stash:**
    
    Salva temporaneamente le modifiche non ancora committate e ripristina lo stato pulito del repository.
    
    - `git stash pop`: Ripristina le modifiche salvate e le rimuove dallo stash.
    - **git branch:**
    
    Oltre ad elencare i branch, puoi creare e cancellarli:
    
    - `git branch nuovo-branch`: Crea un nuovo branch.
    - `git checkout -b nuovo-branch`: Crea e sposta contemporaneamente al nuovo branch.
    - `git branch -d nome-branch`: Elimina un branch locale (se non contenente commit non uniti).
    - **git checkout:**
    
    Oltre a spostarti tra branch, ti permette di ripristinare file specifici:
    
    - `git checkout <nome_branch>`: Passa a un branch esistente.
    - `git checkout -- <nome_file>`: Ripristina un file allo stato dell’ultimo commit.
    - **git merge:**
    
    Unisce le modifiche di un branch in quello corrente.
    
    - Ad esempio:
        
        ```
        git merge nome-branch
        
        ```
        
    - **git rebase:**
    
    Unisce le modifiche mantenendo una cronologia più lineare (più avanzato rispetto a merge).
    
    - Ad esempio:
        
        ```
        git rebase main
        
        ```
        
    - **git remote:**
    
    Gestisce i repository remoti.
    
    - `git remote -v`: Mostra gli URL dei repository remoti.
    - `git remote add origin <url>`: Aggiunge un nuovo remoto chiamato “origin”.
    - **git pull:**
    
    Combina `git fetch` e `git merge`, aggiornando il branch corrente con i cambiamenti remoti.
    
- Struttura del Progetto e Organizzazione del Codice
    - **Obiettivo della struttura modulare:**
        
        Separare le responsabilità del codice per rendere il progetto più semplice da comprendere, mantenere, testare e riutilizzare.
        
    - **Struttura consigliata (ispirata a FastAPI):**
        
        ```
        ├── **app**
        │   ├── __init__.py
        │   ├── main.py           # File principale dell'applicazione
        │   ├── **routers**           # Cartella contenente tutti gli endpoint
        │   │   ├── __init__.py
        │   │   └── books.py       # Endpoint per l'API /books
        │   └── **model**             # Cartella contenente le definizioni dei modelli da
        │       ├── __init__.py
        │       └── book.py        # Definizione del modello "Book"
        |
        ```
        
    - **Importante:**
        
        Organizzare il codice in moduli aiuta anche nella separazione dei file per la gestione dei dati e degli endpoint.
        
    - **Creazione della classe `Book`:**
        - Utilizzare la libreria Pydantic per definire il modello dati, ereditando da `BaseModel`.
        - Specificare gli attributi principali per ogni libro:
            - `id`: intero
            - `title`: stringa
            - `author`: stringa
            - `review`: (utilizzato inizialmente come stringa o intero, ma con validazione che ne impone valori compresi)
    - **Aggiunta di vincoli e validazioni:**
        - Per applicare restrizioni (ad esempio, recensione compresa tra 1 e 5), si utilizza il tipo `Annotated` dalla libreria `typing` insieme a `Field` di Pydantic.
        - Esempio:
            
            ```python
            from pydantic import BaseModel, Field
            from typing import Annotated
            
            class Book(BaseModel):
                id: int
                title: str
                author: str
                review: Annotated[int, Field(ge=1, le=5)]
            ```
            
    - **Documentazione tramite Schema OpenAPI:**
        
        In questo modo, nella documentazione automatica dell’API (es. raggiungibile via [http://127.0.0.1:8000/docs](http://127.0.0.1:8000/docs)) saranno visualizzati anche esempi e restrizioni sui dati. 
        
- Creazione di Dati Fittizi (Simulazione di Database)
    - **Simulazione di un database:**
        - Creare un package denominato `data` con un file `books.py` in cui si definisce un dizionario che contiene alcuni oggetti `Book`.
        - Esempio:
            
            ```python
            from models.book import Book
            
            books = {
                0: Book(id=0, title="libro zero", author="autore zero", review=3),
                1: Book(id=1, title="libro uno", author="autore uno", review=5),
                2: Book(id=2, title="libro due", author="autore due", review=1),
            }
            ```
            
    - **Nota sulla configurazione del PYTHONPATH:**
        
        Se gli import non funzionano, impostate il path corretto impostando come "Sources root" la cartella `app` oppure, da terminale:
        
        ```
        export PYTHONPATH=$PYTHONPATH:<path_cartella_app>
        ```
        
- Pydantic libreria
    
    **Pydantic** è una libreria Python che utilizza i type hints per definire modelli di dati e validare automaticamente le informazioni in ingresso. Con Pydantic, è possibile:
    
    - Definire strutture dati in maniera semplice e leggibile usando classi che ereditano da BaseModel.
    - Applicare validazioni e restrizioni sui campi (ad esempio, valori minimi, massimi, lunghezza minima) tramite la funzione Field insieme a Annotated per associare metadati ai tipi.
    - Serializzare e deserializzare dati, trasformandoli in oggetti Python e viceversa, con garanzia di coerenza e correttezza.
    - Gestire errori di validazione in modo esplicito, facilitando il debug e migliorando l’affidabilità dell’applicazione.
    
    Pydantic è particolarmente utile in applicazioni web (ad esempio con FastAPI) dove la validazione e la gestione dei dati in entrata sono fondamentali per garantire la sicurezza e il corretto funzionamento delle API.
    
- **Implementazione delle API**
    - API per Ottenere Libri
        - **Endpoint GET /books:**
            - Definito in `routers/books.py` per restituire la lista di libri disponibili:
                
                ```python
                @router.get("/")
                def get_all_books() -> list[Book]:
                    """Returns the list of available books."""
                    return list(books.values())
                ```
                
        - **Endpoint GET /books/{id}:**
            - Permette di ottenere il dettaglio di un singolo libro, includendo anche la gestione di errori (se l’ID non viene trovato, viene lanciata una `HTTPException` con status 404):
                
                ```python
                @router.get("/{id}")
                def get_book_by_id(id: Annotated[int, Path(description="The ID of the book to get")]) -> Book:
                    try:
                        return books[id]
                    except KeyError:
                        raise HTTPException(status_code=404, detail="Book not found")
                ```
                
        - **Endpoint per riordinare le recensioni in base al valore delle recensioni**
        
        La riga di codice selezionata:
        
        ```python
        return sorted(books.values(), key=lambda book: book.review)
        
        ```
        
        fa quanto segue:
        
        1. **`books.values()`**: Ottiene tutti i valori del dizionario `books`, che sono oggetti della classe `Book`.
        2. **`sorted()`**: Ordina questi valori in base a un criterio specificato.
        3. **`key=lambda book: book.review`**: Specifica il criterio di ordinamento. Qui viene utilizzata una funzione lambda che prende un oggetto `book` e restituisce il valore del suo attributo `review`. Questo significa che i libri saranno ordinati in base al valore della loro recensione (`review`).
        4. **`return`**: Restituisce la lista ordinata dei libri.
        
        In sintesi, questa riga restituisce una lista di libri ordinati in base al valore della loro recensione (`review`) in ordine crescente.
        
    - API per Gestire Recensioni
        - **Definizione del modello per la recensione:**
            - Creare un nuovo file in `models` (ad es. `review.py`) definendo il modello `Review`:
                
                ```python
                from pydantic import BaseModel, Field
                from typing import Annotated
                
                class Review(BaseModel):
                    review: Annotated[int, Field(ge=1, le=5)]
                
                ```
                
        - **Endpoint POST per Aggiungere una Recensione:**
            - Definito su `/books/{id}` per aggiungere la recensione a un libro già esistente. Il codice gestisce eccezioni sia per libri inesistenti (KeyError) sia per richieste non valide (ValidationError):
                
                ```python
                @router.post("/{id}")
                def add_review(
                    id: Annotated[int, Path(description="The ID of the book to which add the review")],
                    review: Review
                ):
                    try:
                        books[id].review = review.review
                        return "Review successfully added"
                    except KeyError:
                        raise HTTPException(status_code=404, detail="Book not found")
                    except ValidationError:
                        raise HTTPException(status_code=400, detail="Not a valid request"
                ```
                
                - spiegazione
                    
                    ---
                    
                    ## ✅ Cosa sta succedendo?
                    
                    - `review` è il **nome del parametro** della funzione.
                    - `Review` è il **modello Pydantic** che hai definito, ad esempio così:
                    
                    ```python
                    class Review(BaseModel):
                        review: Annotated[int | None, Field(ge=1, le=5)] = None
                    
                    ```
                    
                    👉 Quindi il parametro `review` è un **oggetto Review**
                    
                    che ha un **attributo chiamato anch’esso `review`** (che contiene il numero da 1 a 5).
                    
                    ---
                    
                    ## 🧠 Quindi `review.review` significa:
                    
                    - Il **primo `review`** è il **nome dell’oggetto** passato alla funzione (tipo `Review`)
                    - Il **secondo `review`** è il **campo dentro l’oggetto**
                    
                    ### 🧾 Esempio pratico:
                    
                    Immagina che il corpo della richiesta sia:
                    
                    ```json
                    {
                      "review": 4
                    }
                    
                    ```
                    
                    FastAPI lo trasforma automaticamente in:
                    
                    ```python
                    review = Review(review=4)
                    
                    ```
                    
                    Quindi:
                    
                    ```python
                    review.review  # = 4
                    
                    ```
                    
                    ---
                    
                    ## ✅ E cosa fa `books[id].review = review.review`?
                    
                    - `books[id]` → è il libro con quell’ID
                    - `.review` → è il campo del libro (classe `Book`)
                    - `= review.review` → stai **assegnando al libro** la **nuova recensione** ricevuta
                    
                    ---
                    
                    ## 💡 In sintesi da ricordare:
                    
                    | Parte | Significato |
                    | --- | --- |
                    | `review` (1°) | L'oggetto ricevuto dalla richiesta (tipo Review) |
                    | `.review` (2°) | Il campo interno che contiene il numero da 1 a 5 |
                    | `books[id].review` | Aggiorna il campo review del libro con quel valore |
                    
                    📌 È normale vedere nomi duplicati così se campo e oggetto hanno lo stesso nome.
                    
                    Se ti confonde, puoi rinominare il parametro della funzione, ad esempio:
                    
                    ```python
                    def add_review(id: int, review_data: Review):
                        books[id].review = review_data.review
                    
                    ```
                    
                    Vuoi che te lo riscriva anche con un mini esempio da testare passo-passo?
                    
    - API per Inserimento e Aggiornamento di Libri
        - **Endpoint POST /books:**
            - Consente di inserire un nuovo libro, controllando che l’ID non sia già presente (in caso affermativo, viene restituito il codice di errore 403):
                
                ```python
                @router.post("/")
                def add_book(book: Book):
                    if book.id in books:
                        raise HTTPException(status_code=403, detail="Book ID already exists")
                    books[book.id] = book
                    return "Book successfully added"
                ```
                
        - **Endpoint PUT /books/{id}:**
            - Utilizzato per aggiornare completamente un libro esistente. Se il libro non esiste, viene lanciata una `HTTPException` con status 404:
                
                ```python
                @router.put("/{id}")
                def update_book(
                    id: Annotated[int, Path(description="The ID of the book to update")],
                    book: Book
                ):
                    if book.id not in books:
                        raise HTTPException(status_code=404, detail="Book not found")
                    books[id] = book
                    return "Book successfully updated"
                ```
                
            
    - API per Eliminare Libri
        - **Endpoint DELETE per cancellazioni:**
            - Eliminazione di tutti i libri:
                
                ```python
                @router.delete("/")
                def delete_all_books():
                    books.clear()
                    return "All books successfully deleted"
                ```
                
            - Eliminazione di un libro specifico, con gestione dell’errore se l’ID non esiste:
                
                ```python
                @router.delete("/{id}")
                def delete_book(id: Annotated[int, Path(description="The ID of the book to delete")]):
                    try:
                        del books[id]
                        return "Book successfully deleted"
                    except KeyError:
                        raise HTTPException(status_code=404, detail="Book not found")
                ```
                
    - Gestione dei Metodi HTTP e Parametri
        - **Differenza dei Metodi:**
            - **GET:** per recuperare dati (inserisce parametri via URL o header)
            - **POST:** per inviare dati più consistenti nel body della richiesta
            - **PUT/PATCH:** per aggiornare una risorsa esistente (PUT sostituisce interamente la risorsa, PATCH solo parzialmente)
            - **DELETE:** per eliminare risorse
        - **Parametri di Query:**
            - I parametri query possono essere utilizzati per ordinamenti, filtraggi o altre opzioni sulla risposta, come ad esempio ordinare i libri in base al valore della recensione.
                
                
- Integrazione e Documentazione dell'Applicazione
    - **File Principale dell’Applicazione (`main.py`):**
        - Viene creato un file `main.py` dove si inizializza l’applicazione FastAPI, si includono i router (es. il router dei libri) e si definisce l’accesso alla documentazione automatica tramite il parametro `tags`:
            
            ```python
            from fastapi import FastAPI
            from routers import books
            
            app = FastAPI()
            app.include_router(books.router, tags=["books"])
            ```
            
    - **Accesso alla Documentazione:**
        - Dopo l’avvio del server, è possibile visionare la documentazione interattiva all’indirizzo `http://127.0.0.1:8000/docs`.
    - **Gestione degli Errori:**
        - Per ogni errore non gestito, il server risponde in maniera standard con uno status 500 e il messaggio "Internal Server Error".
- **RIEPILOGO STEP PROGETTAZIONE APP**
    
    ---
    
    - 1. Organizzazione di base del progetto
        
        Una struttura tipica del progetto FastAPI potrebbe essere:
        
        ```
        my_project/
        │
        ├─ main.py              # Punto d’ingresso: dove avvii l’app FastAPI
        ├─ requirements.txt
        ├─ routes/
        │   ├─ __init__.py
        │   ├─ books.py         # Qui definiamo le API relative ai “books”
        │   └─ users.py         # Esempio di un altro modulo di rotte
        ├─ models/
        │   └─ book.py          # Definizione del modello Book (Pydantic o ORM)
        ├─ database/
        │   └─ db.py            # Connessione e setup database (se usi un DB)
        └─ ...
        
        ```
        
        ### Perché organizzare le rotte in un package (cartella `routes`)?
        
        - Mantieni il codice suddiviso per funzionalità (es.: `books.py` si occupa dei libri, `users.py` degli utenti, ecc.).
        - Puoi facilmente importare e “montare” queste rotte nel file `main.py`.
    - 2. Creare le rotte in FastAPI (esempio `books.py`)
        
        In FastAPI, per definire le rotte, si usa tipicamente un **`APIRouter`**. Ecco i passaggi:
        
        1. **Importare `APIRouter` da `fastapi`:**
            
            ```python
            from fastapi import APIRouter, HTTPException, status
            
            ```
            
        2. **Creare il router**:
            
            ```python
            router = APIRouter(
                prefix="/books",        # prefisso URL (es. /books)
                tags=["books"]          # tag usato nella documentazione OpenAPI
            )
            
            ```
            
        3. **Definire le rotte** usando i decorator corrispondenti ai metodi HTTP:
            
            ```python
            @router.get("/", response_description="Lista di tutti i libri")
            def get_books():
                # logica per recuperare tutti i libri
                # ad es.: books = db.get_all_books()
                return {"data": "lista di libri"}
            
            @router.get("/{book_id}", response_description="Ottieni un libro specifico")
            def get_book(book_id: int):
                # logica per recuperare un libro
                # ad es. book = db.get_book_by_id(book_id)
                # se non trovato -> raise HTTPException(status_code=404, detail="Libro non trovato")
                return {"data": f"informazioni sul libro {book_id}"}
            
            @router.post("/", status_code=status.HTTP_201_CREATED)
            def create_book(book_data: dict):
                # logica per creare un libro
                # es.: new_book = db.create_book(book_data)
                return {"data": "nuovo libro creato"}
            
            @router.put("/{book_id}")
            def update_book(book_id: int, book_data: dict):
                # logica per aggiornare un libro
                # se il libro non esiste -> HTTPException(404, "Libro non trovato")
                return {"data": f"libro {book_id} aggiornato"}
            
            @router.delete("/{book_id}", status_code=status.HTTP_200_OK)
            def delete_book(book_id: int):
                # logica per eliminare un libro
                return {"data": f"libro {book_id} eliminato"}
            
            ```
            
            **Note**:
            
            - `prefix="/books"` fa sì che tutte le rotte diventino: `GET /books/`, `GET /books/{book_id}`, ecc.
            - `tags=["books"]` serve per classificare queste rotte nella documentazione di FastAPI (Swagger UI).
            - Puoi usare `status_code=...` per impostare il codice di stato di default in caso di successo.
            - Per segnalare errori o mancanze di risorse, si usano eccezioni come `HTTPException`.
        4. **(Facoltativo) Validazione dei dati in ingresso**:
            - Spesso, al posto di `dict`, si utilizzano **modelli Pydantic** per validare le request.
            - Esempio:
                
                ```python
                from pydantic import BaseModel
                
                class BookModel(BaseModel):
                    title: str
                    author: str
                    pages: int
                
                ```
                
            - Poi, nella rotta:
                
                ```python
                @router.post("/", status_code=status.HTTP_201_CREATED)
                def create_book(book_data: BookModel):
                    # adesso "book_data" è già validato da Pydantic
                    # book_data.title, book_data.author, ...
                    return {"data": "nuovo libro creato"}
                
                ```
                
    - 3. Includere (montare) le rotte in `main.py`
        
        Una volta definito il router `router` nel file `books.py`, lo importi in `main.py` e lo includi nella tua app FastAPI.
        
        1. **Creare l’app principale** in `main.py`:
            
            ```python
            from fastapi import FastAPI
            from routes import books  # oppure from routes.books import router as books_router
            
            app = FastAPI(title="La mia API di libri")
            
            # Includi il router di "books"
            app.include_router(books.router)
            
            ```
            
        2. **Avviare l’app** (in locale) usando Uvicorn (o un server compatibile ASGI):
            
            ```bash
            uvicorn main:app --reload
            
            ```
            
            - `main` è il nome del file, `app` è l’oggetto FastAPI.
            - `-reload` riavvia il server automaticamente ad ogni modifica del codice (utile in sviluppo).
        3. **Verificare la documentazione**:
            - Avviato il server, puoi andare su `http://127.0.0.1:8000/docs` e vedere lo **Swagger UI** che FastAPI genera automaticamente.
            - Oppure su `http://127.0.0.1:8000/redoc` per la **Redoc documentation**.
    - 4. Gestione del Database (opzionale, ma molto comune)
        
        Se devi interfacciarti con un database:
        
        1. **Scegli e configura un ORM** (ad es. SQLAlchemy).
        2. **Crea i tuoi modelli** (tabelle) in `models/` e la **connessione al DB** in `database/db.py`.
        3. **Scrivi funzioni** per CRUD in un modulo (repository/servizio) e usale nelle tue rotte.
            - Esempio:
                
                ```python
                from sqlalchemy.orm import Session
                from models.book import Book
                
                def get_book_by_id(db: Session, book_id: int):
                    return db.query(Book).filter(Book.id == book_id).first()
                
                ```
                
        4. **Recupera la sessione** nelle rotte (o crea dei *dependency injection* in FastAPI):
            
            ```python
            from fastapi import Depends
            from .db import get_db
            
            @router.get("/{book_id}")
            def get_book(book_id: int, db: Session = Depends(get_db)):
                book = get_book_by_id(db, book_id)
                if not book:
                    raise HTTPException(status_code=404, detail="Libro non trovato")
                return book
            
            ```
            
    - 5. Struttura consigliata dei file `books.py` (rotte) e `main.py`
        
        ```python
        # routes/books.py
        from fastapi import APIRouter, HTTPException, status
        from pydantic import BaseModel
        
        router = APIRouter(
            prefix="/books",
            tags=["books"]
        )
        
        # Esempio di modello Pydantic per la validazione
        class BookIn(BaseModel):
            title: str
            author: str
            pages: int
        
        # Rotta per ottenere tutti i libri
        @router.get("/", response_description="Lista di tutti i libri")
        def get_books():
            # logica per recuperare i libri, ad es. books = ...
            return {"data": "lista di libri"}
        
        # Rotta per ottenere un libro specifico
        @router.get("/{book_id}", response_description="Dati di un libro specifico")
        def get_book(book_id: int):
            # logica per recuperare un libro
            # se non trovato -> raise HTTPException(404, ...)
            return {"data": f"informazioni libro {book_id}"}
        
        # Rotta per creare un nuovo libro
        @router.post("/", status_code=status.HTTP_201_CREATED)
        def create_book(book_data: BookIn):
            # logica per creare il libro usando i dati validati
            return {"data": "nuovo libro creato"}
        
        # Rotta per aggiornare un libro
        @router.put("/{book_id}")
        def update_book(book_id: int, book_data: BookIn):
            # logica per aggiornare
            # se il libro non esiste -> raise HTTPException(404, ...)
            return {"data": f"libro {book_id} aggiornato"}
        
        # Rotta per eliminare un libro
        @router.delete("/{book_id}", status_code=status.HTTP_200_OK)
        def delete_book(book_id: int):
            # logica per eliminare
            return {"data": f"libro {book_id} eliminato"}
        
        ```
        
        ### `main.py`
        
        ```python
        # main.py
        from fastapi import FastAPI
        from routes import books  # Import del package "routes" e dentro c'è books
        
        app = FastAPI(
            title="API dei Libri",
            description="Un semplice esempio di API con FastAPI",
            version="1.0.0"
        )
        
        # Include il router definito in books.py
        app.include_router(books.router)
        
        # Se vuoi un semplice endpoint di test
        @app.get("/")
        def root():
            return {"message": "Benvenuto nella mia API di libri"}
        
        # Per avviare il server: uvicorn main:app --reload
        
        ```
        
    - 6. Ulteriori best practice / suggerimenti
        1. **Use Dependencies**: se hai bisogno di passare la sessione del DB o controllare l’autenticazione, puoi definire funzioni `Depends(...)` che riducono il boilerplate di codice nelle rotte.
        2. **Eccezioni personalizzate**: crea delle eccezioni o funzioni di risposta custom per gestire meglio gli errori.
        3. **Organizzazione**:
            - Mantieni la logica di business (lettura/scrittura DB) separata dalla definizione delle rotte, magari in un modulo `services` o `repositories`.
            - Le rotte dovrebbero solo “chiamare” tali servizi.
        4. **Documentazione**:
            - Grazie a FastAPI e ai modelli Pydantic, la documentazione Swagger si crea automaticamente.
            - Usa parametri come `response_model`, `response_description`, `summary`, `description` nei decorator per arricchire la doc.
        5. **Test**:
            - Scrivi test (ad esempio, usando `pytest`) per verificare che le rotte restituiscano il risultato atteso.
        6. **File `.env`**: se devi gestire credenziali o variabili sensibili (DB, token, ecc.), usa un file `.env` e `python-dotenv` (o simili) per caricarle.
    - Riepilogo finale step-by-step
        1. **Crea la cartella `routes/`** con un file per ogni gruppo di rotte (es. `books.py`).
        2. **In `books.py`** (o in un altro file simile):
            - Importa `APIRouter` e crea `router = APIRouter(...)`.
            - Definisci le rotte (`@router.get(...)`, `@router.post(...)`, ecc.).
            - (Opzionale) Usa modelli Pydantic per la validazione dei dati.
        3. **In `main.py`**:
            - Crea l’oggetto `app = FastAPI(...)`.
            - Includi i router con `app.include_router(...)`.
            - Avvia con: `uvicorn main:app --reload`.
        4. **Testa** le rotte su `http://127.0.0.1:8000/docs` o con strumenti come Postman/Insomnia.
        5. **(Se serve un DB)** Integra un ORM e configuralo in un file dedicato, importalo nelle rotte o usando `Depends(...)`.
    
    ---
    
- **CREAZIONE DEL FILE MAIN**
    
    ---
    
    - 1. Cosa fa `main.py`?
        
        In un progetto FastAPI (o in generale in un’applicazione web), il file `main.py` è il **punto di ingresso** dell’applicazione.
        
        - È dove **creiamo** l’istanza di `FastAPI()`.
        - È dove **colleghiamo** le rotte (endpoints) principali o i router esterni.
        - È dove eventualmente **configuriamo** parametri come title, descrizione, version, e altri metadati dell’API.
        - È il file che lanciamo con `uvicorn` per far partire il server web.
        
        ### Schema riassuntivo
        
        1. Import delle librerie (FastAPI, eventuali router, config, ecc.).
        2. Creazione dell’oggetto `app = FastAPI(...)`.
        3. (Opzionale) Eventuali funzioni di avvio/chiusura (startup/shutdown).
        4. Registrazione delle rotte “globali” (se servono) o inclusione di router provenienti da altri file.
        5. Funzione principale (endpoints di base o di test).
        6. Avvio dell’app (tramite `uvicorn main:app --reload`).
    - 2. Creazione dell’ambiente e installazione delle dipendenze
        
        Prima di scrivere `main.py`, è buona norma:
        
        1. **Creare un ambiente virtuale** (consigliato) con `python -m venv venv` e poi attivarlo.
        2. Installare FastAPI e un server ASGI (es. `uvicorn`) nel tuo ambiente:
            
            ```bash
            pip install fastapi uvicorn
            
            ```
            
        3. Se prevedi l’uso di un database o di un ORM, installa i pacchetti necessari (ad es. `sqlalchemy`, `databases`, ecc.).
    - 3. Struttura minima di `main.py`
        
        Ecco un **esempio minimale** di come potrebbe apparire:
        
        ```python
        # main.py
        from fastapi import FastAPI
        
        app = FastAPI(
            title="Titolo della mia API",
            description="Breve descrizione del mio progetto",
            version="0.1.0"
        )
        
        @app.get("/")
        def root():
            return {"message": "Benvenuto nella mia prima API FastAPI"}
        
        # Per avviare l'applicazione da terminale:
        # uvicorn main:app --reload
        
        ```
        
        ### Spiegazione
        
        - **`from fastapi import FastAPI`**: importiamo la libreria.
        - **`app = FastAPI(...)`**: creiamo l’istanza dell’app, definendo i metadati (title, description, version).
        - **`@app.get("/")`**: definisce una rotta GET sull’endpoint `/`. È come la homepage della tua API.
        - **`uvicorn main:app --reload`**: avvia il server su `localhost:8000`; `-reload` fa riavviare automaticamente il server se cambi il codice.
    - 4. Organizzare le rotte (router) in altri file e includerle in `main.py`
        
        Quando il tuo progetto cresce, è meglio **separare** le rotte in file diversi (ad es. in una cartella `routes/`) e poi “includerle” in `main.py`. Questo rende il codice più organizzato e manutenibile.
        
        ### Esempio di router in `routes/books.py`
        
        ```python
        # routes/books.py
        from fastapi import APIRouter, HTTPException
        
        router = APIRouter(
            prefix="/books",
            tags=["Books"]
        )
        
        @router.get("/")
        def get_books():
            return {"data": "lista di libri"}
        
        @router.get("/{book_id}")
        def get_book(book_id: int):
            if book_id < 1:
                raise HTTPException(status_code=400, detail="ID non valido")
            return {"data": f"informazioni sul libro {book_id}"}
        
        ```
        
        **Note**:
        
        - Creiamo un `APIRouter`.
        - Usiamo `prefix="/books"` per avere gli endpoint `/books/` e `/books/{book_id}`.
        - Usiamo `tags=["Books"]` per raggrupparli nella documentazione Swagger.
        
        ### Includerlo in `main.py`
        
        ```python
        # main.py
        from fastapi import FastAPI
        from routes import books  # Importo il file / package delle mie rotte
        
        app = FastAPI(
            title="La mia API",
            description="Progetto di esempio con FastAPI",
            version="1.0.0"
        )
        
        # Inclusione del router definito in books.py
        app.include_router(books.router)
        
        @app.get("/")
        def root():
            return {"message": "Benvenuto nella mia API FastAPI"}
        
        ```
        
        1. **`from routes import books`**: importiamo il file (o package) dove abbiamo definito il router.
        2. **`app.include_router(books.router)`**: aggiungiamo tutte le rotte del router “books” all’app principale.
        3. Qualsiasi endpoint definito in `books.router` sarà automaticamente disponibile.
    - 5. Gestione dell’avvio e della chiusura dell’app (startup/shutdown events)
        
        Se il tuo progetto richiede l’esecuzione di codice all’avvio (per esempio inizializzare un database) o prima dello spegnimento del server, puoi usare gli “eventi” di FastAPI:
        
        ```python
        # main.py
        from fastapi import FastAPI
        from routes import books
        
        app = FastAPI()
        
        @app.on_event("startup")
        async def startup_event():
            # Eseguito 1 volta all'avvio
            print("Sto avviando il server...")
        
        @app.on_event("shutdown")
        async def shutdown_event():
            # Eseguito 1 volta prima dello spegnimento
            print("Sto spegnendo il server...")
        
        app.include_router(books.router)
        ```
        
    - 6. Configurazioni avanzate: middleware, CORS, eccezioni
        
        Man mano che il progetto diventa più complesso, nel file `main.py` (o in un file dedicato) potresti configurare:
        
        1. **Middleware** (ad es. logging, controllo performance, manipolazione di richieste/risposte).
        2. **CORS (Cross-Origin Resource Sharing)** per permettere a client su domini diversi di accedere alle tue API:
            
            ```python
            from fastapi.middleware.cors import CORSMiddleware
            
            app.add_middleware(
                CORSMiddleware,
                allow_origins=["*"],
                allow_credentials=True,
                allow_methods=["*"],
                allow_headers=["*"],
            )
            
            ```
            
        3. **Gestione delle eccezioni personalizzate** per rispondere con formati JSON specifici.
    - 7. Esecuzione e test
        
        Una volta che hai scritto `main.py`, puoi avviare il server con:
        
        ```bash
        uvicorn main:app --reload
        
        ```
        
        - Di default, il server gira su `http://127.0.0.1:8000`.
        - La **documentazione interattiva** è su `http://127.0.0.1:8000/docs`.
        - La doc in formato Redoc è su `http://127.0.0.1:8000/redoc`.
        
        Prova le tue rotte (ad es. `/`, `/books/`, ecc.) da un **browser**, da **Postman** o da strumenti analoghi.
        
    - 8. Consigli di base per progetti futuri
        1. **Separazione del codice**: mantieni i file `main.py` leggeri, spostando la logica pesante (query, calcoli, ecc.) in altri moduli (services, database, repository).
        2. **Versionamento delle API**: se hai versioni diverse (`v1`, `v2`), puoi usare prefissi diversi o più file `main_v1.py`, `main_v2.py`, ecc.
        3. **Configurazione tramite file `.env`**: se devi gestire credenziali o variabili d’ambiente (DB_URL, SECRET_KEY, ecc.), utilizza `.env` e librerie come `python-dotenv`.
        4. **Test**: scrivi test automatici (ad es. con `pytest`) per verificare che `main.py` e gli endpoint funzionino come previsto.
        5. **Deployment**: quando sposti il tuo progetto in produzione, potresti usare server come **Gunicorn** con **UvicornWorker** o container Docker (dipende dall’infrastruttura).
    - 9. Conclusione
        
        Il **file `main.py`** è il fulcro da cui parte tutto:
        
        - Crea l’app FastAPI.
        - Configura metadati, middleware, eventi di avvio/chiusura.
        - Include i router separati (se hai rotte organizzate in più file).
        - Fornisce un endpoint di test (ad esempio `/`) per verificare velocemente che il server sia up & running.
        
        Se segui questi **step** e ti abitui a una struttura pulita, potrai facilmente **scalare** il tuo progetto, aggiungere nuove rotte, integrare database, autenticazione e molto altro. Buon sviluppo con FastAPI!
        
    
    ---
    

---

**`SIMULAZIONE ESAME`**

- TESTO
    
    Ci è stato chiesto di progettare un sistema per la gestione di eventi. Il sistema deve
    prevedere:
    
    - Una API per creare un nuovo evento (con ID evento, titolo, descrizione, data,
    luogo);
    - Una API per visualizzare lʼelenco di eventi nel sistema;
    - Una API per registrarsi a un evento come partecipante, indicando nome e
    cognome dellʼutente.
    Si osservi che lʼevento deve essere identificato in modo univoco dal suo ID, mentre può
    avere gli altri campi non univoci. Si può assumere che ci sia solo un evento al giorno,
    per cui una stringa con la data può essere usata come ID, e viene creata
    automaticamente dal sistema (non passata dallʼutente in fase di creazione). La risorsa
    evento può essere usata in diverse API. Si può assumere un sistema semplificato per cui
    agli utenti non è richiesta autenticazione.
- Domanda 1: Definizione delle API (15 punti)
    - Definire gli endpoint API (strutture URL e metodi HTTP); (2.5 punti per ogni API)
    - Specificare i parametri di richiesta e le possibili risposte, possibilmente con un
    esempio di richiesta andata a buon fine; (1.5 punti per ogni API)
    - Dettagliare i modelli di dati previsti per le richieste e le risposte. (3 punti in
    totale)
- Domanda 2: Gestione degli Errori API (5 punti)
    
    Una buona API deve gestire efficacemente gli errori.
    
    - Descrivere le risposte di errore comuni (es. 400, 404, 500) e quando dovrebbero
    essere utilizzate nel contesto delle API appena progettate. (3 punti)
    - Fornire esempi di risposta per almeno due casi di errore. (1 punto per ogni
    esempio)

---

**`LAB 3 - PARTE FRONTEND`**

- Introduzione
    
    Finora abbiamo lavorato solo sul **backend**, cioè sulle API della nostra app (es. ottenere lista libri). Ma per rendere il progetto accessibile anche a chi non sa usare API, dobbiamo costruire una **pagina web**, cioè il **frontend**. In questa lezione impareremo a creare pagine HTML, integrarle con FastAPI, mostrare contenuti dinamici e gestire form, immagini e stile (CSS).
    
- Iniziare con una pagina HTML base
    
    Per prima cosa, creiamo un endpoint `@app.get("/")` che restituisce una semplice pagina HTML. FastAPI però, per impostazione predefinita, restituisce le risposte in JSON. Questo significa che anche se nel codice scriviamo HTML, il browser lo interpreta male. Per risolvere il problema, dobbiamo dire esplicitamente che vogliamo restituire una **risposta HTML**, usando `HTMLResponse`.
    
    ```python
    from fastapi import FastAPI
    from fastapi.responses import HTMLResponse
    
    app = FastAPI()
    
    @app.get("/", response_class=HTMLResponse)
    def home():
        return """
        <!DOCTYPE html>
        <html>
          <body>
            <h1>Hello world!</h1>
            <p>Hellooo!</p>
          </body>
        </html>
        """
    ```
    
- Separare l’HTML in file esterni con i **template**
    - Introduzione **Template** di Jinja2
        
        Scrivere HTML come stringa dentro Python è scomodo. La soluzione è usare un **motore di template**, che ci permette di separare il codice HTML in file `.html` esterni. FastAPI supporta **Jinja2**, un motore di templating molto usato.
        
        Creiamo la cartella `app/templates/` e dentro un file `home.html` con il nostro codice HTML. Poi, modifichiamo il codice Python per caricare quel file usando `Jinja2Templates`.
        
        ```python
        from fastapi import FastAPI, Request
        from fastapi.responses import HTMLResponse
        from fastapi.templating import Jinja2Templates
        
        app = FastAPI()
        templates = Jinja2Templates(directory="app/templates")
        
        @app.get("/", response_class=HTMLResponse)
        def home(request: Request):
            return templates.TemplateResponse("home.html", {"request": request})
        ```
        
    - 📦 Organizzare il progetto
        
        È buona pratica spostare il codice che gestisce la parte "visiva" (frontend) in un file dedicato. Quindi creiamo `routers/frontend.py`, dove sposteremo l’endpoint sopra, usando un `router` (come già facciamo per i libri). Ricorda: nel nuovo file si usa `@router.get("/")` al posto di `@app.get`.
        
        Nel `main.py` aggiungiamo:
        
        ```python
        from routers import frontend
        app.include_router(frontend.router)
        
        ```
        
    - 🧱 Estendere i template: base comune
        
        Spesso più pagine hanno parti comuni (es. header, menu, footer). Jinja2 ci permette di creare un file `base.html` con la struttura comune e poi "estenderlo" nei singoli file.
        
        ```html
        <!-- base.html -->
        <!DOCTYPE html>
        <html>
          <head>
            <title>Library</title>
          </head>
          <body>
            <header><h1>Library</h1></header>
            <nav>
              <a href="/">Home</a>
              <a href="#">Book List</a>
              <a href="#">Add Book</a>
            </nav>
        
            <div class="container">
              {% block content %}{% endblock %}
            </div>
        
            <footer>
              <p>&copy; 2025 Programmazione Web UNICA </p>
            </footer>
          </body>
        </html>
        
        ```
        
        Nel file `home.html`, estendiamo `base.html` e inseriamo il contenuto dentro il blocco `content`.
        
        ```html
        {% extends "base.html" %}
        {% block content %}
          <h3 style="text-align: center">Welcome to the library</h3>
        {% endblock %}
        ```
        
        Il nostro file `FRONTEND` ora includerà questo:
        
        ```python
        ***...import di varie librerie....***
        
        templates = Jinja2Templates(directory="app/templates")
        # Configurazione per servire i file statici (CSS, JavaScript)
        # Questo permette di accedere ai file nella directory "app/static" attraverso l'URL "/static"
        router = APIRouter()
        router.mount("/static", StaticFiles(directory="app/static"), name="static")
        
        @router.get("/", response_class=HTMLResponse)
        def home(request: Request):
            # Renderizza il template home.html, passando l'oggetto request come parametro
            # (necessario per Jinja2 per generare correttamente i link e i form)
        
            text = {
                "title": "Welcome to the Library Online",
                "content": "This is the home page of the Library Online application."
            }
            return templates.TemplateResponse(
                request=request, name="home.html",
                context={"text": text} # Passa il testo come variabile al template,
                # è un dizionario che ci aiuta anche per la sicurezza # (per evitare attacchi XSS, Cross-Site Scripting)
            )
        ```
        
    
- Inserire dati dinamici
    
    Possiamo mostrare dati dal backend usando variabili. In `home.html`, scriviamo:
    
    ```html
    <h3>{{ text }}</h3>
    
    ```
    
    Nel Python:
    
    ```python
    @app.get("/", response_class=HTMLResponse)
    def home(request: Request):
        return templates.TemplateResponse("home.html", {
            "request": request,
            "text": "Benvenuto nella nostra biblioteca"
        })
    
    ```
    
    Le `{{ }}` indicano una variabile che sarà sostituita dal suo valore.
    
    🔐 **Sicurezza**: se il valore di `text` contiene HTML, potrebbe essere pericoloso. Per evitare esecuzioni di codice non volute (XSS), usiamo il filtro `|e`:
    
    ```html
    <p>{{ text|e }}</p>
    ```
    
- 🔄 Cicli e dizionari nei template
    
    Jinja2 permette di fare cicli (es. per stampare una lista) e usare dizionari:
    
    ```html
    {% for book in books %}
      <p>{{ book.title }}</p>
    {% endfor %}
    
    ```
    
    Nel backend:
    
    ```python
    context = {"books": [{"title": "Libro A"}, {"title": "Libro B"}]}
    
    ```
    
    Per dizionari:
    
    ```html
    {% for key, value in dati.items() %}
      <p>{{ key }}: {{ value }}</p>
    {% endfor %}
    ```
    
- 📷 Inserire immagini e file statici
    
    Per usare immagini o CSS, creiamo la cartella `app/static/` e ci mettiamo i file (es. `biblio.avif`, `styles.css`).
    
    Nel `main.py` montiamo la cartella:
    
    ```python
    from fastapi.staticfiles import StaticFiles
    app.mount("/static", StaticFiles(directory="app/static"), name="static")
    ```
    
    Nel file HTML:
    
    ```html
    <img src="{{ url_for('static', path='biblio.avif') }}" alt="library">
    ```
    
- 🎨 Aggiungere stile con CSS
    
    Nel file `styles.css` dentro `app/static/`:
    
    ```css
    body {
        background-color: #f2f2f2;
        color: #333;
        font-family: Arial, sans-serif;
    }
    nav {
        background: #005599;
        padding: 10px;
    }
    nav a {
        color: white;
        margin: 0 15px;
    }
    ...
    ```
    
    Nel `base.html`, aggiungiamo il collegamento:
    
    ```html
    <link rel="stylesheet" href="{{ url_for('static', path='styles.css') }}">
    
    ```
    
- 📚 Lista dei libri (pagina dinamica)
    
    Creiamo il file `list.html`:
    
    ```html
    {% extends "base.html" %}
    {% block content %}
    <table>
      <tr><th>ID</th><th>Title</th><th>Author</th><th>Review</th></tr>
      {% for book in books %}
        <tr>
          <td>{{ book.id }}</td>
          <td>{{ book.title }}</td>
          <td>{{ book.author }}</td>
          <td>{{ book.review }}</td>
        </tr>
      {% endfor %}
    </table>
    {% endblock %}
    
    ```
    
    E la funzione:
    
    ```python
    @router.get("/book_list", response_class=HTMLResponse)
    def show_books(request: Request):
        context = {"request": request, "books": list(books.values())}
        return templates.TemplateResponse("list.html", context)
    ```
    
- spiegazione file frontend
    
    ---
    
    ## ✅ COSA STIAMO FACENDO
    
    Stiamo creando un **frontend** per una semplice applicazione web chiamata “Library Online”. Usiamo **FastAPI** per gestire le richieste web e **Jinja2** per generare pagine HTML dinamiche (cioè pagine web che cambiano in base ai dati).
    
    ---
    
    - 📥 1. IMPORTAZIONI
        
        ```python
        from fastapi import Request, APIRouter
        from fastapi.responses import HTMLResponse
        from fastapi.templating import Jinja2Templates
        from fastapi.staticfiles import StaticFiles
        from data.books import books
        
        ```
        
        ### Spiegazione:
        
        - `APIRouter`: serve per organizzare le funzioni che gestiscono le pagine (è come un “contenitore” per i percorsi).
        - `HTMLResponse`: dice a FastAPI di rispondere con una **pagina web (HTML)** e non con JSON.
        - `Jinja2Templates`: permette di **collegare file HTML esterni** al codice Python (sistema di “template”).
        - `Request`: rappresenta la richiesta del browser (serve per generare URL nei template).
        - `StaticFiles`: serve per caricare **file statici** come immagini e CSS.
        - `books`: è una lista (o dizionario) di libri caricata da un altro file. La usiamo per stampare la lista dei libri.
    
    ---
    
    - 🛠️ 2. CONFIGURAZIONE TEMPLATE E FILE STATICI
        
        ```python
        templates = Jinja2Templates(directory="app/templates")
        router = APIRouter()
        router.mount("/static", StaticFiles(directory="app/static"), name="static")
        
        ```
        
        ### Spiegazione:
        
        - `templates`: dice a FastAPI dove sono salvati i file HTML. In questo caso, nella cartella `app/templates`.
        - `router = APIRouter()`: inizializza un router, cioè un insieme di percorsi della web app.
        - `router.mount(...)`: permette di accedere ai file statici. Se hai un’immagine in `app/static/logo.png`, puoi vederla su `localhost:8000/static/logo.png`.
    
    ---
    
    - 🏠 3. HOME PAGE ("/")
        
        ```python
        @router.get("/", response_class=HTMLResponse)
        def home(request: Request):
            text = {
                "title": "Welcome to the Library Online",
                "content": "This is the home page of the Library Online application."
            }
            return templates.TemplateResponse(
                request=request, name="home.html",
                context={"text": text}
            )
        
        ```
        
        ### Spiegazione:
        
        - `@router.get("/")`: dice che questa funzione risponde quando qualcuno visita la **pagina principale ("/")** del sito.
        - `request: Request`: è necessario per far funzionare correttamente i link nel template.
        - `text = {...}`: crea un dizionario (cioè una variabile con più campi), con il titolo e contenuto da mostrare nella pagina.
        - `TemplateResponse(...)`:
            - `name="home.html"`: carica il file HTML chiamato `home.html`.
            - `context={"text": text}`: invia la variabile `text` al file HTML, così il contenuto può essere inserito nella pagina.
        
        ### Esempio nel file HTML:
        
        Nel file `home.html` puoi scrivere:
        
        ```html
        <h1>{{ text.title }}</h1>
        <p>{{ text.content }}</p>
        
        ```
        
        E FastAPI sostituirà questi `{{ }}` con i dati passati nel context.
        
        ---
        
    
    ---
    
    - 📚 4. LISTA LIBRI ("/book_list")
        
        ```python
        @router.get("/book_list", response_class=HTMLResponse)
        def show_book_list(request: Request):
            context = {"books": list(books.values())}
            return templates.TemplateResponse(
                request=request, name="list.html",
                context=context
            )
        ```
        
        La funzione `show_book_list` è una route definita con FastAPI che serve per gestire una pagina web che mostra una lista di libri. Ecco una spiegazione dettagliata passo per passo:
        
        - 1. **Definizione della route**
            
            ```python
            @router.get("/book_list", response_class=HTMLResponse)
            ```
            
            - `@router.get("/book_list")`: Questo è un **decoratore** che dice a FastAPI di associare questa funzione all'URL `/book_list` e al metodo HTTP `GET`. Quando un utente visita questa URL, FastAPI eseguirà questa funzione.
            - `response_class=HTMLResponse`: Specifica che la risposta sarà in formato HTML (una pagina web).
        - 2. **Definizione della funzione**
            
            ```python
            def show_book_list(request: Request):
            ```
            
            - `def show_book_list`: È il nome della funzione. Puoi chiamarla come preferisci, ma è utile darle un nome descrittivo.
            - `request: Request`: Questo parametro rappresenta la richiesta HTTP inviata dal client (ad esempio, il browser). Contiene informazioni come i dati della richiesta, gli header, ecc.
        - 3. **Creazione del contesto**
            
            ```python
            context = {"books": list(books.values())}
            ```
            
            - `context`: È un dizionario che contiene i dati che vogliamo passare al template HTML.
            - `books`: È una variabile importata da un altro file (`data.books`) che probabilmente contiene un elenco di libri. Ogni libro è probabilmente rappresentato come un oggetto o un dizionario.
            - `list(books.values())`: Converte i valori del dizionario `books` in una lista. Questo è utile perché i template HTML lavorano meglio con liste quando si tratta di iterare sui dati.
        - 4. **Renderizzazione del template**
            
            ```python
            return templates.TemplateResponse(
                request=request, name="list.html",
                context=context
            )
            ```
            
            - `templates.TemplateResponse`: È un metodo che utilizza il motore di template Jinja2 per generare una pagina HTML dinamica.
            - `request=request`: Passa l'oggetto `request` al template. Questo è necessario per alcune funzionalità di Jinja2, come la generazione di URL.
            - `name="list.html"`: Specifica il file del template HTML che deve essere usato. In questo caso, il file si chiama `list.html` e si trova nella directory `app/templates`.
            - `context=context`: Passa il dizionario `context` al template. Questo permette al template di accedere ai dati (in questo caso, la lista dei libri).
        
        5. **Cosa fa questa funzione?**
        
        Quando un utente visita l'URL `/book_list`:
        
        1. La funzione raccoglie i dati dei libri dalla variabile `books`.
        2. Prepara un dizionario (`context`) con i dati da passare al template.
        3. Usa il file `list.html` per generare una pagina HTML dinamica.
        4. Restituisce la pagina HTML al browser dell'utente.
        
        In pratica, questa funzione serve per mostrare una lista di libri in una pagina web.
        
        ### Esempio nel file `list.html`:
        
        ```html
        <table>
          <tr>
            <th>ID</th><th>Title</th><th>Author</th><th>Review</th>
          </tr>
          {% for book in books %}
            <tr>
              <td>{{ book.id }}</td>
              <td>{{ book.title }}</td>
              <td>{{ book.author }}</td>
              <td>{{ book.review }}</td>
            </tr>
          {% endfor %}
        </table>
        
        ```
        
        Il ciclo `for` in Jinja2 stampa una riga per ogni libro.
        
        ---
        
    
    ---
    
    - ✚📚5. AGGIUNGI LIBRO (”/add_book”)
        
        🎯 Obiettivo
        
        Creare una pagina web con un **form HTML** dove l’utente può inserire un nuovo libro, e fare in modo che, cliccando su “Add”, i dati vengano inviati a FastAPI che li **salva (simulando un database)**.
        
        - 🔧 1. Parte Frontend – il form HTML (`add.html`)
            
            Questo è il codice HTML che l’utente vedrà nel browser:
            
            ```html
            {% extends "base.html" %}
            {% block content %}
            <form action="{{ url_for('add_book_from_form')}}" method="post">
              <label for="id">ID:</label><br>
              <input type="number" name="id" id="id" min="0" required><br>
            
              <label for="title">Title:</label><br>
              <input type="text" name="title" id="title" required><br>
            
              <label for="author">Author:</label><br>
              <input type="text" name="author" id="author" required><br>
            
              <label for="review">Review:</label><br>
              <input type="number" name="review" id="review" min="1" max="5"><br><br>
            
              <input type="submit" value="Add">
              <input type="reset" value="Reset">
            </form>
            {% endblock %}
            
            ```
            
            ### Cosa succede qui?
            
            - Il form ha 4 **campi di input**: `id`, `title`, `author`, `review`.
            - Quando l’utente clicca **Add**, i dati vengono **inviati** a un indirizzo (endpoint) usando il metodo `POST`.
            - `action="{{ url_for('add_book_from_form') }}"`: questa riga dice **dove inviare i dati**. Si collega a una funzione Python chiamata `add_book_from_form`.
        - 🌐 2. Endpoint GET – Mostrare il form nel browser
            
            
            Questa funzione serve solo per **mostrare** il form:
            
            ```python
            @router.get("/add_book", response_class=HTMLResponse)
            def add_book_form(request: Request):
                return templates.TemplateResponse(
                    request=request, name="add.html"
                )
            
            ```
            
            - Quando visiti `/add_book`, FastAPI carica il file `add.html`.
            - Il form è vuoto, pronto per essere compilato.
        - ❗ Problema da risolvere
            
            Se non specifichiamo bene `action` e `method="post"` nel form, il comportamento predefinito del browser è:
            
            - Inviare i dati **allo stesso URL** da cui è stato caricato (`/add_book`)
            - Inviarli come **query string** (`?id=1&title=Libro...`)
            - Ma le nostre API vogliono i dati in **formato JSON**, non in query string
            
            ## 🧠 Soluzione: Creare un endpoint POST che riceva i dati da form
            
            Nel file `routers/books.py` aggiungiamo:
            
            ```python
            from fastapi import Form, HTTPException
            
            @router.post("/books_form")
            def add_book_from_form(
                id: int = Form(...),
                title: str = Form(...),
                author: str = Form(...),
                review: int = Form(...)
            ):
                if id in books:
                    raise HTTPException(status_code=403, detail="Book ID already exists")
                books[id] = Book(id=id, title=title, author=author, review=review)
                return "Book successfully added"
            
            ```
            
            ### Spiegazione:
            
            - Ogni campo del form (id, title, etc.) è ricevuto come parametro usando `Form(...)`.
            - FastAPI li raccoglie dal form **automaticamente**.
            - Se l’ID del libro esiste già → errore 403.
            - Altrimenti, aggiunge il libro a `books` (che simula un database).
            - Ritorna una stringa di conferma.
        - 🔗 4. Aggiungere il link al form nella navbar
            
            Nel file `base.html`, dentro il menu:
            
            ```html
            <a href="{{ url_for('add_book_form') }}">Add Book</a>
            
            ```
            
            Questo crea il link “Add Book” nella barra in alto, che porta alla pagina `/add_book`.
            
        - **`add.html`**
            
            ### Contesto generale
            
            Il codice rappresenta un template HTML per una pagina web che consente agli utenti di aggiungere un nuovo libro a una collezione. Questo template utilizza **Jinja2**, un motore di template per Python, ed estende un file base chiamato `base.html`. La pagina include un modulo HTML (`<form>`) per raccogliere i dati del libro da aggiungere.
            
            ---
            
            ### Linea per linea
            
            ### **Linee 1-2**
            
            ```html
            {% extends "base.html" %}
            {% block content %}
            
            ```
            
            - **`{% extends "base.html" %}`**: Indica che questo template eredita la struttura di base dal file `base.html`. Tutti gli elementi comuni (come header, footer, ecc.) sono definiti in `base.html`.
            - **`{% block content %}`**: Definisce un blocco di contenuto che sovrascrive il blocco `content` definito in `base.html`. Tutto il contenuto specifico di questa pagina sarà inserito qui.
            
            ---
            
            ### **Linee 4-20**
            
            ```html
            <form action="{{ url_for('add_book_from_form')}}" method="post">
            
            ```
            
            - **`<form>`**: Crea un modulo HTML per raccogliere i dati.
                - **`action="{{ url_for('add_book_from_form') }}"`**: Specifica l'URL a cui inviare i dati del modulo. La funzione `url_for` genera dinamicamente l'URL per la funzione `add_book_from_form` definita nel backend (in `app/routers/books.py`).
                - **`method="post"`**: Indica che i dati del modulo saranno inviati tramite il metodo HTTP POST.
            
            ---
            
            ### **Linee 6-7**
            
            ```html
            <label for="id">ID:</label><br>
            <input type="number" name="id" id="id" min="0" required><br>
            
            ```
            
            - **`<label>`**: Etichetta per il campo di input. L'attributo `for="id"` collega l'etichetta al campo con `id="id"`.
            - **`<input>`**: Campo di input per l'ID del libro.
                - **`type="number"`**: Accetta solo numeri.
                - **`name="id"`**: Nome del campo, usato per inviare i dati al backend.
                - **`id="id"`**: Identificatore univoco del campo.
                - **`min="0"`**: Valore minimo accettato.
                - **`required`**: Campo obbligatorio.
            
            ---
            
            ### **Linee 9-10**
            
            ```html
            <label for="title">Title:</label><br>
            <input type="text" name="title" id="title" required><br>
            
            ```
            
            - Campo per il titolo del libro.
                - **`type="text"`**: Accetta testo.
                - **`name="title"`**: Nome del campo.
                - **`required`**: Campo obbligatorio.
            
            ---
            
            ### **Linee 12-13**
            
            ```html
            <label for="author">Author:</label><br>
            <input type="text" name="author" id="author" required><br>
            
            ```
            
            - Campo per l'autore del libro.
                - **`type="text"`**: Accetta testo.
                - **`name="author"`**: Nome del campo.
                - **`required`**: Campo obbligatorio.
            
            ---
            
            ### **Linee 15-16**
            
            ```html
            <label for="review">Review:</label><br>
            <input type="number" name="review" id="review" min="1" max="5"><br><br>
            
            ```
            
            - Campo per la recensione del libro.
                - **`type="number"`**: Accetta solo numeri.
                - **`name="review"`**: Nome del campo.
                - **`min="1"` e `max="5"`**: Limita i valori accettati tra 1 e 5.
                - **Non obbligatorio**: Non ha l'attributo `required`.
            
            ---
            
            ### **Linee 18-19**
            
            ```html
            <input type="submit" value="Add">
            <input type="reset" value="Reset">
            
            ```
            
            - **`<input type="submit">`**: Pulsante per inviare i dati del modulo.
                - **`value="Add"`**: Testo visualizzato sul pulsante.
            - **`<input type="reset">`**: Pulsante per resettare i campi del modulo.
                - **`value="Reset"`**: Testo visualizzato sul pulsante.
            
            ---
            
            ### **Linee 22**
            
            ```html
            {% endblock %}
            
            ```
            
            - Chiude il blocco `content` iniziato alla linea 2.
            
            ---
            
            ### Funzionamento complessivo
            
            1. L'utente compila il modulo con i dati del libro (ID, titolo, autore, recensione).
            2. Quando preme il pulsante "Add", i dati vengono inviati al backend tramite una richiesta POST all'endpoint `add_book_from_form`.
            3. Il backend elabora i dati e aggiunge il libro alla collezione.
            
            Questo template è parte di un'applicazione web basata su **FastAPI** e utilizza **Jinja2** per generare pagine HTML dinamiche.
            
        - ***add_book_from_form** API BACKEND*
            
            Il codice selezionato definisce un endpoint FastAPI per aggiungere un nuovo libro alla collezione utilizzando i dati inviati tramite un form HTML. Ecco una spiegazione dettagliata:
            
            ### Funzione `add_book_from_form`
            
            - **Decoratore `@router.post("books_form/")`**:
                - Registra un endpoint HTTP POST con il percorso `/books_form/`.
                - Questo endpoint è utilizzato per ricevere i dati di un libro da un form HTML.
            - **Parametro `book: Annotated[Book, Form()]`**:
                - Il parametro `book` è un'istanza del modello `Book` (definito altrove nel progetto).
                - `Form()` indica che i dati del libro saranno estratti dai campi di un form HTML inviato con il metodo POST.
            - **Logica della funzione**:
                1. **Controllo duplicati**:
                    - Verifica se esiste già un libro con lo stesso `id` nel dizionario `books`.
                    - Se sì, restituisce un errore HTTP 403 con il messaggio "Esiste già un libro con questo ID".
                2. **Aggiunta del libro**:
                    - Se l'`id` non è già presente, aggiunge il libro al dizionario `books` utilizzando l'`id` come chiave.
                3. **Risposta**:
                    - Restituisce un messaggio di successo: "Libro aggiunto con successo".
            
            ### Utilizzo
            
            Questo endpoint è pensato per essere utilizzato con un form HTML come quello definito nel file `add.html`. I dati del form (come `id`, `title`, `author`, e `review`) vengono inviati al server, che li processa e aggiunge il libro alla collezione.
            
            ### Nota
            
            Il codice utilizza il dizionario `books` come "database" per memorizzare i libri. Questo approccio è adatto per applicazioni semplici o di esempio, ma non è scalabile per applicazioni reali.
            
    
    ## ✅ Riepilogo completo
    
    | Parte | Cosa fa |
    | --- | --- |
    | `add.html` | Mostra il form da compilare |
    | `@router.get("/add_book")` | Mostra il template HTML del form |
    | `@router.post("/books_form")` | Riceve i dati inviati dal form e li salva |
    | `Form(...)` | Indica a FastAPI che il dato arriva da un campo HTML |
    | `url_for(...)` | Costruisce automaticamente l’URL corretto per il form |
    | CSS | Serve a rendere visivamente migliori i pulsanti |
    
    ---
    
    Se vuoi, posso anche costruirti un esempio intero da copiare/incollare o farti provare tutto in un mini progetto. Vuoi che ti prepari anche la parte server avviabile o un test interattivo?
    
    ## 📌 RIEPILOGO
    
    | Cosa | Spiegazione |
    | --- | --- |
    | `HTMLResponse` | Serve per inviare pagine HTML al browser |
    | `Jinja2Templates` | Collega Python ai file HTML (con variabili dinamiche) |
    | `request: Request` | Obbligatorio per usare template, genera URL corretti |
    | `context={}` | Dati che mandiamo al file HTML da usare con `{{ variabile }}` |
    | `router.get(...)` | Funzione che gestisce una pagina (es. home, book_list) |
    | `books` | Dati finti (mock) da visualizzare, come se fossero presi da un database |
    
    ---
    
    Se vuoi, posso anche prepararti **uno schema visuale** del flusso o aiutarti a scrivere un mini progetto a partire da questo codice. Vuoi procedere in quella direzione?
    
- adsadas

- spiegazione differenza file [frontend.py](http://frontend.py) e altrifile.py
    
    ---
    
    ## 📂 1. Struttura generale del progetto
    
    ```
    app/
    ├── main.py                ← punto d’ingresso che include tutti i router
    ├── routers/
    │   ├── frontend.py        ← **frontend**: rotte che restituiscono pagine HTML
    │   └── books.py           ← **backend**: rotte CRUD per i dati dei libri (API)
    ├── templates/             ← Jinja2 templates (file `.html`)
    │   ├── base.html          ← layout comune :contentReference[oaicite:0]{index=0}:contentReference[oaicite:1]{index=1}
    │   ├── home.html          ← homepage :contentReference[oaicite:2]{index=2}:contentReference[oaicite:3]{index=3}
    │   ├── list.html          ← lista libri :contentReference[oaicite:4]{index=4}:contentReference[oaicite:5]{index=5}
    │   └── add.html           ← form aggiunta libro :contentReference[oaicite:6]{index=6}:contentReference[oaicite:7]{index=7}
    ├── static/                ← CSS, immagini, JS
    │   └── styles.css
    ├── models/                ← definizioni Pydantic (Book, Review)
    └── data/
        └── books.py           ← “database” in memoria (dizionario)
    
    ```
    
    ---
    
    ## 📋 2. Ruolo di ciascun file
    
    | File | Frontend / Backend | Responsabilità principale |
    | --- | --- | --- |
    | **frontend.py** | Frontend | Definire rotte `GET` che rendono template HTML |
    | **books.py** | Backend (API) | Definire rotte CRUD (`GET`, `POST`, `PUT`, `DELETE`) sui libri |
    | **templates/*.html** | Frontend | Struttura delle pagine, con variabili Jinja2 (`{{ }}`) |
    | **static/** | Frontend | Stili e risorse statiche |
    | **data/books.py** | Backend | Dizionario Python che simula il database |
    | **models/** | Backend | Classi Pydantic per validazione dei dati |
    | **main.py** | Core | Crea `FastAPI()`, include i router |
    
    ---
    
    ## 🔄 3. Comunicazione Frontend ↔ Backend
    
    1. **Browser → Frontend**
        - L’utente visita un URL (es. `/book_list` o `/add_book`).
        - FastAPI cerca nel router di `frontend.py` una rotta `@router.get(...)` corrispondente.
    2. **Frontend.py → Jinja2 Template**
        - La funzione in `frontend.py` chiama:
            
            ```python
            return templates.TemplateResponse(
              request=request,
              name="list.html",
              context={"books": list(books.values())}
            )
            
            ```
            
        - Jinja2 unisce `list.html` con i dati in `context`, sostituendo `{{ book.title }}` ecc. .
    3. **Template → Browser**
        - Il browser riceve l’HTML “completo” e lo rende visivamente.
    4. **Form HTML → Backend API**
        - In `add.html` il form ha:
            
            ```html
            <form action="{{ url_for('add_book_from_form') }}" method="post">
            
            ```
            
            Quando l’utente invia, il browser fa una **POST** a `/books_form/`.
            
    5. **Backend (books.py) elabora i dati**
        - In `books.py` c’è:
            
            ```python
            @router.post("books_form/")
            def add_book_from_form(
              id: int = Form(...),
              title: str = Form(...),
              …
            ):
              books[id] = Book(id, title, …)
              return "Libro aggiunto con successo"
            
            ```
            
        - FastAPI estrae i campi del form con `Form(...)`, aggiorna il “database” e restituisce conferma.
    6. **Risposta al Browser**
        - Puoi restituire testo, JSON o fare un redirect a una pagina HTML.
    
    ---
    
    ## 🎯 4. Differenza tra `frontend.py` e `books.py`
    
    | Aspetto | frontend.py | books.py |
    | --- | --- | --- |
    | Scopo | **Mostrare** pagine HTML | **Gestire** dati/API |
    | Response | `HTMLResponse` + `templates.TemplateResponse` | JSON o stringa (es. conferma) |
    | Import principali | `Jinja2Templates`, `StaticFiles` | `APIRouter(prefix="/books")`, `HTTPException`, `Form`, modelli Pydantic |
    | Quando aggiungere qui rotta? | Se serve una pagina, un form, un report HTML | Se serve un endpoint CRUD, logica di validazione, mutazione dei dati |
    
    **Regola pratica**:
    
    - Se la rotta **restituisce HTML**, va in **frontend.py**.
    - Se la rotta **gestisce dati** (riceve JSON o form, modifica il dizionario), va in **books.py**.
    
    ---
    
    ## 🛠️ 5. Quando creare un nuovo file in `routers/`
    
    - **Nuova area funzionale**: es. utenti → `users.py`
    - **Separazione di responsabilità**: es. libri (`books.py`), ordini (`orders.py`), autenticazione (`auth.py`)
    - **Dimensione e chiarezza**: se un file supera ~200 righe, valuta di suddividerlo per appartenenza logica.
    
    ---
    
    ## ⚙️ 6. Criteri di progettazione modulare
    
    1. **Separation of Concerns**
        - Frontend (render HTML) vs Backend (logica, dati).
    2. **Single Responsibility**
        - Ogni router gestisce un dominio (es. libri, utenti).
    3. **Coesione**
        - Funzioni correlate nello stesso file; codice riutilizzabile in moduli separati.
    4. **Bassa dipendenza**
        - Router indipendenti, comunicano solo via import dei dati o servizi.
    
    ---
    
    ## 🔄 7. Flusso dei dati (esempio “Aggiungi libro”)
    
    ```
    [1] Browser mostra form → (GET /add_book)   ← frontend.py → add.html
    [2] Utente compila → click “Add” → POST /books_form/
    [3] books.py riceve Form(...), aggiorna books[id]
    [4] books.py risponde “successo”
    [5] (Opzionale) redirect → GET /book_list → mostra lista aggiornata
    
    ```
    
    ---
    
    ## 📝 Schema di flusso (ASCII)
    
    ```
    +--------+        GET /add_book         +---------------+
    |Browser | ───────────────────────────> | frontend.py   |
    |        |                              | (add_book_form)|
    +--------+                              +---------------+
                                                  |
                                                  | render add.html
                                                  v
                                             +-----------+
                                             | add.html  |
                                             +-----------+
                                                  |
                fill & submit form              |
                                                  v
    +--------+       POST /books_form         +-----------+
    |Browser | ───────────────────────────>   | books.py  |
    +--------+                                | (add_book)|
                                              +-----------+
                                                  |
                                                  | update data
                                                  v
                                              +-----------+
                                              | data/books|
                                              +-----------+
                                                  |
                                              return success
                                                  |
                                                  v
                                             +-------------+
                                             |Browser shows|
                                             | confirmation|
                                             +-------------+
    
    ```
    
    ---
    
    ### ✔️ Ripasso dopo un mese
    
    - **frontend.py** = rotte che **renderizzano** template
    - **books.py** = rotte che **manipolano** dati
    - **templates/** = HTML con `{{ }}` e `{% %}`
    - **static/** = CSS/immagini
    - **Form(...)** in backend **estrae** dati dai form
    - **context** passa variabili Python ai template
    
    Con questi criteri potrai **progettare da zero** qualsiasi web‑app: crea router per dominio, separa rendering da logica, usa template per l’HTML e API per i dati.
    
- altra spiegazione
    
    Ottima osservazione! 💡
    
    Ti stai chiedendo:
    
    > “Se l’aggiunta del libro la fa books.py, perché devo anche creare un endpoint /add_book nel file frontend.py?”
    > 
    
    La risposta è: **perché una cosa è *mostrare il modulo HTML*, un’altra è *ricevere e gestire i dati inviati dal modulo***.
    
    ---
    
    ## 🎯 Differenza tra i due endpoint `/add_book` e `/books_form`
    
    | Endpoint | File | Metodo | Cosa fa | Chi lo chiama? |
    | --- | --- | --- | --- | --- |
    | `/add_book` | `frontend.py` | `GET` | Mostra la **pagina HTML** con il **form vuoto** | Il **browser** quando clicchi "Add Book" |
    | `/books_form` | `books.py` | `POST` | Riceve i dati del form, **salva il libro** | Il **form HTML** quando premi “Invia” |
    
    ---
    
    ### 📌 Esempio pratico
    
    **Nel browser:**
    
    1. L’utente clicca su **"Add Book"**
    2. Vai su `/add_book` → questa pagina HTML è servita da `frontend.py`:
        
        ```python
        @router.get("/add_book", response_class=HTMLResponse)
        def add_book_form(request: Request):
            return templates.TemplateResponse("add.html", {"request": request})
        
        ```
        
        ⤷ Mostra la pagina con il **form HTML** (vuoto) .
        
    
    ---
    
    **Nel form HTML (`add.html`):**
    
    ```html
    <form action="{{ url_for('add_book_from_form') }}" method="post">
    
    ```
    
    ⤷ Quando clicchi "Add", il browser **invia una richiesta POST a `/books_form`**.
    
    ---
    
    **In `books.py`:**
    
    ```python
    @router.post("/books_form")
    def add_book_from_form(...):
        # Elabora i dati del form e salva il libro
    
    ```
    
    ⤷ Riceve i dati del form e aggiorna la lista dei libri.
    
    ---
    
    ## 🧠 Confronto visivo: mostrare vs. elaborare
    
    ```
              (clic da menu)
    Browser ───── GET /add_book ───▶ frontend.py
                              ▼
                        mostra add.html
                              ▼
                      Utente compila form
                              ▼
                   POST /books_form (dati)
                              ▼
                       backend: books.py
                              ▼
                      Salva il nuovo libro
    
    ```
    
    ---
    
    ## ✅ Riepilogo semplice per i tuoi appunti
    
    | Azione | Dove scrivere |
    | --- | --- |
    | Voglio **mostrare** il form di aggiunta libro | `frontend.py` con rotta GET `/add_book` |
    | Voglio **ricevere** i dati del form e **salvare** il libro | `books.py` con rotta POST `/books_form` |
    
    Questa separazione ti aiuta a:
    
    - **organizzare il codice meglio**
    - **capire chi fa cosa**
    - e **riusare** lo stesso backend anche se domani userai React o un’altra interfaccia.
    
    ---
    
    Se vuoi, posso anche costruirti un esempio minimo (con due file `.py` e due `.html`) che puoi incollare e provare. Ti servirebbe?
    
- file routers/…
    
    ---
    
    ## 📁 **Cosa sono i file nella directory `routers/`**
    
    La cartella `routers/` contiene i **moduli che gestiscono le rotte** (cioè gli URL) del tuo sito web o API.
    
    Ogni file `.py` dentro `routers/`:
    
    - definisce un **insieme di percorsi (endpoint)** che il server deve gestire
    - usa `@router.get(...)`, `@router.post(...)` ecc.
    - viene poi **incluso** nel `main.py` con `app.include_router(...)`
    
    ---
    
    ## 🧱 **Differenza tra i vari file in `routers/`**
    
    | File | Cosa fa | Tipo | Quando lo usi |
    | --- | --- | --- | --- |
    | `frontend.py` | Mostra pagine HTML all’utente | Frontend | Quando l’utente visita pagine nel browser |
    | `books.py` | Gestisce dati (aggiungi, salva...) | Backend/API | Quando ricevi dati da un form o una chiamata API |
    
    ---
    
    ## 🔤 **Come vengono chiamati questi file nei progetti reali**
    
    | Nome nel tuo progetto | Nome “comune” nei progetti reali | Significato |
    | --- | --- | --- |
    | `frontend.py` | `views.py`, `pages.py`, `web.py` | Mostra **viste HTML** (pagine visibili nel browser) |
    | `books.py` | `api_books.py`, `books_routes.py` | Espone **API** (per lavorare con i dati) |
    | `auth.py` (esempi futuri) | `api_auth.py`, `auth_routes.py` | API per login/registrazione |
    | `users.py` | `api_users.py` | API per utenti |
    
    ---
    
    ## ✅ Esempio semplice
    
    Hai un sito tipo “Libreria online”.
    
    ### `frontend.py`
    
    Contiene:
    
    ```python
    @router.get("/book_list")
    def mostra_pagina_html():
        # Mostra list.html con l’elenco dei libri
    
    ```
    
    Serve a **mostrare una pagina HTML al visitatore**.
    
    ---
    
    ### `books.py`
    
    Contiene:
    
    ```python
    @router.post("/books_form")
    def ricevi_dati():
        # Riceve i dati del form e salva il libro
    
    ```
    
    Serve a **gestire i dati del form**, non a mostrare una pagina.
    
    ---
    
    ## 🎯 Riassunto finale da scrivere nei tuoi appunti:
    
    > I file in routers/ servono a dividere il codice per tipo di funzionalità:
    > 
    > - `frontend.py`: mostra le **pagine HTML** – è il **frontend**
    > - `books.py`: gestisce i **dati e le operazioni (API)** – è il **backend**
    > 
    > In progetti veri si chiamano anche `views.py`, `api_books.py`, `routes.py` a seconda del tipo.
    > 
    > Questa divisione aiuta a **tenere ordinato il codice** e **capire cosa fa ogni file**.
    > 
    
    ---
    
    Vuoi che ti prepari anche uno **schema visivo a colori** per questo concetto?
    

---

**`LAB 4 - DATABASE`**

- Cos’è un database relazionale e perché usarlo
    
    Le applicazioni web moderne non possono più “affidarsi” a semplici liste o dizionari Python: i dati devono **perdurare** tra un riavvio e l’altro, essere **condivisi** tra più utenti/istanze e mantenere **coerenza** e **integrità**. Un **database relazionale** risponde a queste esigenze organizzando le informazioni in tabelle collegate tramite chiavi e vincoli.
    
    In questo corso scegliamo **SQLite** (database leggero, file unico) e **SQLModel**, la libreria che fonde Pydantic (validazione degli schemi) con SQLAlchemy (ORM), per integrarsi agevolmente in FastAPI .
    
- Configurazione e inizializzazione del database
    1. **Installazione**
        
        ```bash
        pip install sqlmodel
        
        ```
        
        Aggiungi poi `sqlmodel` a `requirements.txt` .
        
    2. **Engine di connessione** (`data/db.py`)
        
        ```python
        from sqlmodel import create_engine, SQLModel
        
        sqlite_file_name = "app/data/database.db"
        sqlite_url = f"sqlite:///{sqlite_file_name}"
        connect_args = {"check_same_thread": False}
        
        engine = create_engine(sqlite_url, connect_args=connect_args, echo=True)
        
        ```
        
        - `check_same_thread=False`: abilita connessioni multithread indispensabili per FastAPI.
        - `echo=True`: logga in console ogni query SQL per il debug .
    3. **Inizializzazione automatica delle tabelle**
        
        ```python
        def init_database() -> None:
            SQLModel.metadata.create_all(engine)
        
        ```
        
        - Chiama sempre `init_database()` all’avvio dell’app, altrimenti le tabelle non verranno mai create .
    4. **Eventi di “lifespan” in FastAPI**
        
        ```python
        from contextlib import asynccontextmanager
        from fastapi import FastAPI
        from data.db import init_database
        
        @asynccontextmanager
        async def lifespan(app: FastAPI):
            init_database()   # on start
            yield
            # on shutdown: eventuali cleanup
        
        app = FastAPI(lifespan=lifespan)
        
        ```
        
        Così l’inizializzazione scatta automaticamente prima di servire richieste .
        
- Object-Relational Mapping con SQLModel
    
    L’**ORM** traduce classi e oggetti Python in tabelle e righe SQL, evitando di scrivere manualmente query complesse. Con SQLModel:
    
    ```python
    from sqlmodel import SQLModel, Field
    from typing import Annotated
    
    class BookBase(SQLModel):
        title: str
        author: str
        review: Annotated[int | None, Field(ge=1, le=5)] = None
    
    class Book(BookBase, table=True):
        id: int = Field(default=None, primary_key=True)
    
    class BookCreate(BookBase):
        pass
    
    class BookPublic(BookBase):
        id: int
    
    ```
    
    - **BookBase**: campi comuni e validazione Pydantic.
    - **Book**: aggiunge `table=True` e `id` per definire la tabella.
    - **BookCreate/BookPublic**: schemi separati per input (senza `id`) e output (con `id`).
    - Conversione: `Book.model_validate(book_create)` genera un’istanza valida da salvare .
- spiegazione classi
    
    ### 1. BookBase
    
    - **Cos'è:** Una classe base astratta che definisce i campi comuni a tutti i modelli di libro.
    - **Campi:** `title`, `author`, `review`.
    - **Uso:** Non viene mai usata direttamente per creare oggetti o tabelle, ma serve come base per le altre classi. Permette di evitare ripetizioni di codice.
    
    ### 2. Book
    
    - **Cos'è:** Il modello principale che rappresenta la tabella `book` nel database.
    - **Campi:** Tutti quelli di `BookBase` più `id` (chiave primaria).
    - **Uso:** Usata da SQLModel per creare la tabella nel database e per rappresentare i record completi dei libri (incluso l’ID).
    
    ### 3. BookCreate
    
    - **Cos'è:** Un modello per la creazione di nuovi libri.
    - **Campi:** Solo quelli di `BookBase` (senza `id`).
    - **Uso:** Usata come schema di input nelle API quando l’utente vuole aggiungere un nuovo libro. L’ID non serve perché viene generato dal database.
    
    ### 4. BookPublic
    
    - **Cos'è:** Un modello per l’output pubblico dei dati dei libri.
    - **Campi:** Tutti quelli di `BookBase` più `id`.
    - **Uso:** Usata per restituire i dati dei libri nelle risposte API, senza essere mappata a una tabella del database.
    
    ---
    
    ## Come usarle
    
    - **BookCreate:** Quando ricevi dati dall’utente per creare un libro (input).
    - **Book:** Quando lavori con i dati interni del database (lettura/scrittura).
    - **BookPublic:** Quando restituisci dati all’utente tramite API (output).
    - **BookBase:** Non la usi direttamente, ma serve per evitare duplicazione di codice tra le altre classi.
    
    Se hai bisogno di esempi pratici di utilizzo, chiedi pure!
    
- Dipendenze, sessioni e operazioni CRUD
    
    ### Dipendenze e sessioni
    
    Per gestire correttamente le transazioni:
    
    ```python
    from sqlmodel import Session
    from fastapi import Depends
    from typing import Annotated
    
    def get_session():
        with Session(engine) as session:
            yield session
    
    SessionDep = Annotated[Session, Depends(get_session)]
    
    ```
    
    Inserendo `session: SessionDep` negli endpoint, FastAPI apre e chiude automaticamente la sessione .
    
    ### Operazioni CRUD
    
    - **Create**:
        
        ```python
        @router.post("/")
        def add_book(session: SessionDep, book: BookCreate):
            db_book = Book.model_validate(book)
            session.add(db_book)
            session.commit()
            return {"message": "Book added"}
        
        ```
        
    - **Read (tutti)**:
        
        ```python
        @router.get("/", response_model=list[BookPublic])
        def get_all_books(session: SessionDep, sort: bool = False):
            books = session.exec(select(Book)).all()
            return sorted(books, key=lambda b: b.review or 0) if sort else books
        
        ```
        
    - **Read (per ID)**:
        
        ```python
        @router.get("/{id}", response_model=BookPublic)
        def get_book_by_id(session: SessionDep, id: int):
            book = session.get(Book, id)
            if not book:
                raise HTTPException(404, "Not found")
            return book
        
        ```
        
    - **Update/Delete**: simili: `session.get` → modifica o `session.delete` → `session.commit()` .
- Popolamento automatico con dati fittizi
    
    Per test rapidi in fase di sviluppo, usiamo **Faker**:
    
    ```bash
    pip install Faker
    
    ```
    
    E in `data/db.py`:
    
    ```python
    import os
    from faker import Faker
    
    def init_dataset() -> None:
        ds_exists = os.path.isfile("app/data/database.db")
        SQLModel.metadata.create_all(engine)
        if not ds_exists:
            f = Faker("it_IT")
            with Session(engine) as session:
                for _ in range(10):
                    session.add(Book(
                        title=f.sentence(nb_words=5),
                        author=f.name(),
                        review=f.pyint(1, 5)
                    ))
                session.commit()
    
    ```
    
    Così, solo alla prima creazione del file `.db`, verranno inseriti dieci libri casuali, risparmiandoti l’inserimento manuale durante i test .
    

- spiegazione generalizzata

---

gitignore è ….

routers = funzioni endpoint

models = definizione strutture dati

annotated, funzione field di pydentic 

mark directory as → sources root  per far si che …

export PYTHONPATH="app"