# PROGRAMMAZIONE WEB

**`2 - Strumenti e consigli`**

- comandi shell, base git e github + comandi
    - comandi shell
        
        **`ls` :** fare la lista dei file in una directory
        
        **`cd` :** change directory
        
        **`cd .` :** torna alla cartella corrente 
        
        **`cd ..` :** torna alla cartella che c’è prima 
        
        **`PERMESSI`** : 
        
        - permesso di lettura (r)
        - permesso di scrittura (w)
        - permesso di esecuzione (x)
        
        Esempio di output di `ls -l`:
        
        ```
        -rw-r--r--  1 user group  1234 Mar  7 12:00 file.txt
        
        ```
        
        Analizziamo il primo carattere:
        
        - Il primo carattere può essere:
            - → file normale
            - **`d`** → directory
            - **`l`** → link simbolico
            - **`c`** → file a caratteri (dispositivi speciali, come `/dev/tty`)
            - **`b`** → file a blocchi (dispositivi come dischi)
        
        Nel caso dell’esempio `-rw-r--r--`, il primo carattere è **"-"**, quindi significa che **"file.txt" è un file normale** (non una cartella, un link o un dispositivo).
        
        ### Spiegazione dei permessi seguenti:
        
        I restanti 9 caratteri rappresentano i permessi del file in tre gruppi:
        
        1. **`rw-`** (per l'utente proprietario)
        2. **`r--`** (per il gruppo)
        3. **`r--`** (per gli altri utenti)
        
        Nei sistemi Unix/Linux, i concetti di **user** e **group** sono fondamentali per la gestione dei permessi e della sicurezza. Vediamo cosa significano:
        
        ### **User (Utente)**
        
        L'**utente** (user) rappresenta il proprietario del file o della directory. Ogni file ha un utente associato, che di solito è colui che lo ha creato.
        
        - Puoi vedere l'utente proprietario di un file con il comando:
            
            ```bash
            ls -l
            
            ```
            
            Esempio di output:
            
            ```
            -rw-r--r--  1 mario developers  1234 Mar  7 12:00 file.txt
            
            ```
            
            Qui **"mario"** è l'utente proprietario del file.
            
        - Puoi cambiare il proprietario di un file con:
            
            ```bash
            sudo chown nuovo_utente file.txt
            
            ```
            
        
        ---
        
        ### **Group (Gruppo)**
        
        Il **gruppo** è un insieme di utenti che condividono certi privilegi sui file e directory. Ogni file ha un gruppo associato, e tutti gli utenti membri di quel gruppo ereditano i permessi specificati per il gruppo.
        
        - Nell'esempio sopra:
            
            ```
            -rw-r--r--  1 mario developers  1234 Mar  7 12:00 file.txt
            
            ```
            
            **"developers"** è il gruppo associato al file.
            
        - Per vedere i gruppi a cui un utente appartiene:
            
            ```bash
            groups
            
            ```
            
        - Per cambiare il gruppo di un file:
            
            ```bash
            sudo chown :nuovo_gruppo file.txt
            
            ```
            
        - Per aggiungere un utente a un gruppo:
            
            ```bash
            sudo usermod -aG nome_gruppo nome_utente
            
            ```
            
        
        ---
        
        ### **Relazione con i Permessi**
        
        I permessi dei file sono suddivisi in tre sezioni:
        
        ```
        -rw-r--r--  1 mario developers  1234 Mar  7 12:00 file.txt
        
        ```
        
        - **`rw-`** (utente proprietario, `mario`)
        - **`r--`** (gruppo, `developers`)
        - **`r--`** (tutti gli altri utenti)
        
        Quindi, in questo caso:
        
        - L'utente **mario** può **leggere e scrivere** il file.
        - Gli utenti nel gruppo **developers** possono solo **leggere**.
        - Tutti gli altri utenti possono solo **leggere**.
        
        ![image.png](PROGRAMMAZIONE%20WEB%201af9a6c97cf98039a6e0cd1e9e9bb7af/image.png)
        
    - base git e github
        
        ---
        
        # **Gestione del Codice e Versionamento**
        
        ## **1. Importanza del Versionamento**
        
        Il versionamento del codice è essenziale per una gestione efficiente dei progetti software, specialmente in ambienti di sviluppo collaborativo. I principali benefici sono:
        
        - **Tracciabilità e cronologia delle modifiche** → Permette di monitorare ogni cambiamento nel codice e, se necessario, ripristinare versioni precedenti.
        - **Collaborazione tra sviluppatori** → Facilita il lavoro in team distribuiti, assicurando che tutti abbiano accesso alla versione più aggiornata del progetto.
        - **Riproducibilità dei risultati** → Aiuta a diagnosticare e correggere bug, mantenendo una registrazione di tutte le modifiche apportate.
        
        ---
        
        ## **2. Strumenti per il Versionamento: Git**
        
        **Git** è il sistema di controllo versione più utilizzato per gestire progetti software.
        
        - **Installazione e configurazione di Git**: [Scarica Git](https://git-scm.com/downloads)
        - **Disponibilità di strumenti grafici (GUI)** oltre alla riga di comando:
            - Client GUI
            - Integrazione con gli IDE (es. PyCharm, VS Code)
        
        ---
        
        ## **3. Concetti Fondamentali di Git**
        
        ### **Repository**
        
        Un repository Git è un ambiente di lavoro che contiene tutti i file del progetto e la cronologia delle modifiche, sia a livello locale che remoto.
        
        ### **Commit**
        
        Ogni commit rappresenta uno snapshot del progetto, consentendo di ripristinare versioni precedenti.
        
        - Git salva solo le differenze rispetto alla versione precedente (diff), ottimizzando lo spazio e la gestione delle modifiche.
        
        ### **Branching e Merging**
        
        - **Branching** → Creazione di rami indipendenti per sviluppare nuove funzionalità senza interferire con il codice principale.
        - **Merging** → Unione delle modifiche da un branch al branch principale, mantenendo la cronologia.
        - **Gestione dei conflitti** → Quando più persone modificano lo stesso file, Git richiede una risoluzione manuale dei conflitti.
        
        ---
        
        ## **4. Comandi Iniziali di Git**
        
        | **Comando** | **Descrizione** |
        | --- | --- |
        | `git init` | Inizializza un nuovo repository Git locale. |
        | `git clone <URL>` | Copia un repository remoto sul computer locale. |
        | `git add <file>` | Aggiunge file all'area di staging per il commit. |
        | `git commit -m "messaggio"` | Registra le modifiche nell'area di staging, creando una nuova versione. |
        
        ---
        
        ## **5. Gestione dei Branch**
        
        - Il **branch principale** (`main` o `master`) contiene la versione stabile del codice.
        - Si possono creare **branch indipendenti** per sviluppare nuove funzionalità.
        - Il comando `git checkout` permette di passare da un branch all'altro.
        - La fusione dei branch nel principale avviene tramite `git merge`.
        
        ---
        
        ## **6. Condivisione del Codice e Repository Online: GitHub**
        
        ### **Cos’è GitHub?**
        
        GitHub è una piattaforma che fornisce hosting per repository Git e strumenti per la collaborazione tra sviluppatori.
        
        - Git è il sistema di controllo versione, GitHub è una piattaforma per ospitare repository remoti.
        - **Strumenti di GitHub**:
            - Revisione del codice
            - Gestione delle **issue** (bug, miglioramenti, funzionalità richieste)
            - Integrazione con **CI/CD** per automazione
        
        ### **Comandi per la gestione remota**
        
        | **Comando** | **Descrizione** |
        | --- | --- |
        | `git remote add origin <URL>` | Collega il repository locale a uno remoto su GitHub. |
        | `git push origin <branch>` | Invia le modifiche locali al repository remoto. |
        | `git pull origin <branch>` | Recupera le modifiche da GitHub per aggiornare il codice locale. |
        
        ---
        
        ## **7. Collaborazione su GitHub**
        
        ### **Forking e Pull Requests**
        
        - **Forking** → Creazione di una copia indipendente di un repository, utile per contribuire a progetti open-source.
        - **Pull Requests (PR)** → Proposta di modifica al repository originale, che deve essere approvata prima di essere integrata.
        
        ---
        
        ## **8. Continuous Integration (CI) e Continuous Deployment (CD)**
        
        - **Continuous Integration (CI)** → Automatizza test e verifica del codice a ogni modifica.
        - **Continuous Deployment (CD)** → Automatizza il rilascio del codice in produzione.
        - **Strumenti comuni**: **GitHub Actions, Jenkins, GitLab CI/CD**.
        - **Processo tipico**:
            1. **Commit & Push** → Il codice viene inviato al repository.
            2. **Build** → Il sistema compila e prepara il codice.
            3. **Test** → Esecuzione di test automatici.
            4. **Deploy** → Il codice viene distribuito in staging o produzione.
        
        ---
        
        ## **9. Best Practices per Git e GitHub**
        
        ### **Scrivere buoni commit**
        
        - **Commit frequenti** → Evitare commit troppo grandi, suddividendo il lavoro in piccoli step.
        - **Messaggi chiari** → Usare descrizioni concise e significative per i commit.
        
        ### **Documentare il codice**
        
        - Mantenere README aggiornati.
        - Scrivere commenti chiari nel codice.
        - Usare GitHub Wiki o documentazione interna per i progetti complessi.
        
        ---
        
        [documentazione ufficiale di Git](https://git-scm.com/doc). 🚀
        
    - comandi github vscode
        1. vai su github e crea la **repository** e copia il link in **code→** **https** 
        2. su VSCODE in esplora risorse apri la cartella dove vuoi salvare il tutto 
        3. vai il terminale ed esegui il primo comando:
        
        ```python
        git clone link-https
        ```
        
        1. ora isola il progetto per cui vuoi lavorare andando su **file→apri cartella→seleziona la cartella del progetto su cui vuoi lavorare**
        2. ora dopo che ho effettuato delle modifiche devo salvare i cambiamenti e e pushare. Vado nel controllo del codice sorgente per effettuare tutte le modifiche 
        
        ### …or create a new repository on the command line
        
        ```
        echo "# nuovo-test-pycharm" >> README.md
        git init
        git add README.md
        git commit -m "first commit"
        git branch -M main
        git remote add origin https://github.com/FraCarcangiu3/nuovo-test-pycharm.gitgit push -u origin main
        ```
        
        ### …or push an existing repository from the command line
        
        ```
        git remote add origin https://github.com/FraCarcangiu3/nuovo-test-pycharm.gitgit branch -M main
        git push -u origin main
        ```
        


---

**`3 - Il World Wide Web (WWW)`**

- spiegazione
    - Panoramica sul Web e come funziona
        
        ### **Il World Wide Web (WWW)**
        
        Il **World Wide Web** è una rete di documenti ipertestuali interconnessi accessibili tramite Internet. Fu proposto nel 1989 da **Tim Berners-Lee** al CERN di Ginevra e successivamente sviluppato con **Robert Cailliau**. Il primo sito web venne creato nel 1991, inizialmente destinato alla comunità scientifica.
        
        ---
        
        ### **Ipertesti e il Web**
        
        Un **ipertesto** è un insieme di documenti collegati tramite link. 
        
        I documenti sono localizzati tramite **identificatori virtuali.**  
        
        Sul Web, questi documenti sono generalmente scritti in **HTML (HyperText Markup Language)**. A differenza di un testo lineare, un ipertesto permette la navigazione tra diversi contenuti tramite collegamenti ipertestuali, includendo immagini, video e audio.
        
        ---
        
        ### **Componenti del WWW: Client e Server**
        
        - Un **client** è un programma (come un browser) che invia richieste a un server.
        - Un **server web** è un'applicazione che risponde a queste richieste, fornendo le risorse richieste.
    - Anatomia di un server Web
        
        ### **`Identificatori Virtuali: URI, URL e URN`**
        
        Tutte le risorse del Web sono identificate da **URI (Uniform Resource Identifier)**, che possono essere:
        
        - **URN (Uniform Resource Name)**: identifica una risorsa tramite un nome unico, indipendentemente dalla sua posizione.
        - **URL (Uniform Resource Locator)**: identifica una risorsa indicando anche il percorso per raggiungerla, ad esempio:
            
            ```
            <https://www.esempio.com/pagina.html>
            ```
            
            ![Screenshot 2025-03-13 alle 17.57.39.png](PROGRAMMAZIONE%20WEB%201af9a6c97cf98039a6e0cd1e9e9bb7af/Screenshot_2025-03-13_alle_17.57.39.png)
            
    - Dialogo tra client e server e RESTful API
        
        ---
        
        **`Le API (Application Programming Interfaces)`**
        
        Le **API** sono un insieme di regole e protocolli che permettono la comunicazione tra applicazioni software diverse. Grazie alle API, programmi e servizi indipendenti possono interagire tra loro senza essere direttamente integrati.
        
        ### **Ruolo delle API nel Web**
        
        Le API sono fondamentali per lo sviluppo moderno perché:
        
        - **Permettono l'integrazione tra servizi diversi** (es. una app che usa un'API meteo per ottenere dati in tempo reale).
        - **Automatizzano processi** tra client e server.
        - **Migliorano la scalabilità** e l’efficienza di un sistema software.
        
        ---
        
        **`Il Protocollo HTTP (HyperText Transfer Protocol)`**
        
        - L’**HTTP** è il protocollo usato per la trasmissione di dati tra client (browser) e server nel Web, è il protocollo di **livello applicativo dello stack TCP/IP**.
        - Si basa sul modello **stateless**, il che significa che ogni richiesta è indipendente dalle altre.
        
        I messaggi HTTP sono sequenze di byte composte da due parti:
        
        **Struttura di un messaggio HTTP**
        
        Un messaggio HTTP è composto da:
        
        1. **Header**: contiene informazioni sul messaggio, come il tipo di contenuto e le impostazioni di connessione.
        2. **Body** (opzionale): contiene i dati della richiesta o della risposta.
        
        **Gestione delle richieste:**
        
        - Il **client** (es. un browser) invia una richiesta HTTP al server.
        - Il **server** riceve la richiesta, la elabora e risponde con i dati richiesti.
        - A livello di trasporto sono gestiti con TCP (udp non è adatto perhche non garantisce la consegna) tcp tramite le ACK informa se il pacchetto è arrivato o no.
        - Dopo che il client manda la richiesta il server accetta la connessione, manda la risposta (ACK), e chiude la connessione.
        - La porta 80 è la porta dove comunicano i browser.
        
        ![image.png](PROGRAMMAZIONE%20WEB%201af9a6c97cf98039a6e0cd1e9e9bb7af/image%201.png)
        
        ---
        
        - La connessione può chiudersi subito (HTTP/1.0) o restare aperta per più richieste (HTTP/1.1 e HTTP/2).
        
        # **`Versioni di HTTP`**
        
        ### **HTTP/1.0**
        
        - Ogni richiesta apre e chiude una connessione.
        - Le pagine vengono caricate più lentamente.
        
        ### **HTTP/1.1**
        
        - Introduce le **connessioni persistenti**: più richieste possono essere gestite con una sola connessione (ovvero la connessione non viene chiusa).
        - Supporta il **pipelining**: il client può inviare più richieste senza attendere le risposte.
        
        ### **HTTP/2**
        
        - **Multiplexing**: più richieste vengono gestite simultaneamente in una singola connessione.
        - **Compressione degli header**: riduce la dimensione dei dati trasmessi.
        - **Push lato server**: il server può inviare dati al client prima che vengano richiesti.
        
        ![Screenshot 2025-03-16 alle 12.09.48.png](PROGRAMMAZIONE%20WEB%201af9a6c97cf98039a6e0cd1e9e9bb7af/Screenshot_2025-03-16_alle_12.09.48.png)
        
    - Sessioni Web
        
        # **`Metodi HTTP`**
        
        I metodi HTTP definiscono il tipo di operazione richiesta al server:
        
        - **`GET`**: Richiede una risorsa senza modificarla. Usata per prendere informazioni.
        
        ![image.png](PROGRAMMAZIONE%20WEB%201af9a6c97cf98039a6e0cd1e9e9bb7af/image%202.png)
        
        - **`POST`**: Invia dati al server (es. compilazione di un modulo). Usata per inviare inforrmazioni. 
        I dettagli della risorsa sono contenuti nel body del messaggio. Non ha limiti di lunghezza per i parametri e il message body può essere cifrato
        - **PUT**: Carica o aggiorna una risorsa.
        - **DELETE**: Cancella una risorsa.
        - **HEAD**: Simile a GET, ma restituisce solo gli header.
        - **OPTIONS**: Mostra i metodi disponibili per una risorsa.
        - **TRACE**: Serve per testare le richieste HTTP.
        
        **Esempio di richiesta GET:**
        
        ```
        GET /index.html HTTP/1.1
        Host: www.sito.com
        
        ```
        
        ---
        
        # **`Risposte HTTP e Codici di Stato`**
        
        Il server risponde alle richieste con un codice di stato che indica l’esito dell’operazione.
        
        ### **Classi di codici di stato**
        
        - **1xx – Informativi** (es. 100 Continue), non importante
        - **2xx – Successo** (es. 200 OK), la richiesta è stata processata con successo
        - **3xx – Reindirizzamenti** (es. 301 Moved Permanently), Il server ha ricevuto risposta ma il client deve eseguire altre azioni per portarle a termine.
        - **4xx – Errori del client** (es. 404 Not Found)
        - **5xx – Errori del server** (es. 500 Internal Server Error)
        
        Esempio di risposta HTTP:
        
        ```
        HTTP/1.1 200 OK
        Content-Type: text/html
        Content-Length: 1234
        
        ```
        
        ---
        
        # **`Cookie e Sessioni Web`**
        
        Poiché HTTP è **stateless**, per mantenere lo stato di un utente si usano i **cookie** e le **sessioni**.
        
        ### **Cookie**
        
        - Sono file di testo salvati nel browser per memorizzare dati come login o preferenze dell'utente.
        - Ogni volta che un utente visita il sito, il browser invia automaticamente i cookie al server.
        - Servono a far diventare una communicazione da statelss a statefull.
        
        ### **Sessioni**
        
        - Salvano informazioni temporanee su un utente (es. un carrello in un e-commerce).
        - Gestite lato server e collegate al client tramite un identificatore unico.
        
        ---
        
        # **`Autenticazione e Sicurezza nel Web`**
        
        ### **Metodi di autenticazione**
        
        1. **Basic Authentication** – Invia username e password in chiaro (poco sicuro).
        2. **Form con login e password** – Più sicuro, trasmesso con metodo **`POST`**.
        3. **Token di autenticazione** – Un metodo moderno usato per API e sessioni sicure.
        
        ### **HTTPS e TLS**
        
        Per proteggere i dati trasmessi tra client e server si usa **HTTPS**, che combina HTTP con **TLS (Transport Layer Security)** per garantire:
        
        - **Crittografia** dei dati trasmessi.
        - **Autenticazione** del server tramite certificati digitali.
        - **Integrità** dei dati, impedendo alterazioni.

---

**`4 - HTML e CSS`**

- Introduzione al Web e ai linguaggi di Markup
    - **Origini del Web e degli ipertesti:**
        - Il Web è nato per condividere documenti ipertestuali, inizialmente statici e preparati in anticipo, visualizzati tramite browser (Chrome, Firefox, Safari, ecc.).
        - Successivamente sono stati introdotti strumenti per generare pagine dinamiche con contenuti personalizzati.
    - **`Linguaggi di Markup:`**
        - **Definizione:** Utilizzano 
        - **tag** (istruzioni) che rappresentano le caratteristiche del formato per il documento
        - una grammatica 
        - una semantica per descrivere la struttura e il contenuto.
        
        `<p>Testo di contenuto </p>`
        
        I tag introducono dei caratteri speciali che li delimitano e permettono al browser di distinguere il testo del contenuto dal testo che contiene i tag.
        
        - **Tipologie:**
            - *Procedurali:* Indicano esplicitamente le procedure per trattare il testo (es. troff, TEX).
            - *Descrittivi:* Si concentrano sulla struttura e la leggibilità, lasciando al browser/scaricatore la scelta della presentazione (es. SGML, HTML, XML).
        - **Focus nel corso:** Si utilizzano prevalentemente linguaggi descrittivi, in particolare l’HTML.
    - **HTML come Linguaggio di Markup:**
        - È usato per descrivere documenti ipertestuali e non è un linguaggio di programmazione.
        - HTML5, definito come “living standard”, viene aggiornato periodicamente mantenendo la retrocompatibilità. La prima versione è stata pubblicata nel 2012 dal WHATWG.
- Struttura e Sintassi di **`HTML`**
    - Elementi di base - **TAG**
        - **Tag:**
            - Delimitati da “<” e “>”, normalmente appaiono in coppia (apertura e chiusura), ad esempio:
                
                ```html
                <p>Testo di contenuto</p>
                start_tag            end_tag
                ```
                
            - **ECCEZIONI**: Alcuni tag non hanno chiusura (es. `<br>` NEW LINE) e possono essere annidati (es. `<p><b>Testo</b></p>`).
        
    - Elementi di base - **Eccezioni** ⚠️
        
        ![image.png](PROGRAMMAZIONE%20WEB%201af9a6c97cf98039a6e0cd1e9e9bb7af/image%203.png)
        
    - Elementi di base - **Attributi**
        - Forniscono informazioni aggiuntive sugli elementi HTML tramite coppie chiave-valore, con il valore racchiuso tra apici (singoli o doppi).
        Esempio:
            
            ```html
            <a href="<https://www.google.com>">Visit Google</a>
            
            ```
            
    - Struttura di un documento `HTML`
        - **Elementi essenziali**
            - `<!DOCTYPE>`: Specifica il tipo di documento e il DTD (Document Type Definition) per le regole di interpretazione.
                
                ![image.png](PROGRAMMAZIONE%20WEB%201af9a6c97cf98039a6e0cd1e9e9bb7af/image%204.png)
                
            - `<html>`: Elemento radice che specifica al browser che la pagina sarà formattata in HTML,  può includere l’attributo `lang` per indicare la lingua.
                
                ![image.png](PROGRAMMAZIONE%20WEB%201af9a6c97cf98039a6e0cd1e9e9bb7af/image%205.png)
                
            - `<head>`: L’header (delimitato dal tag <head>) contiene i metadati per il documento, che non sono visualizzati all’interno del documento (ma alcuni impostano visualizzazioni particolari nel browser)
            - Il tag `<title>` è un esempio di questi metadati, e specifica il titolo della pagina che sarà mostrato nella testata della finestra o tab del browser
            - Il tag `<meta>` contiene metadati (dati sui dati) e informazioni utili ad applicazioni esterne, come per esempio i motori di ricerca
            Gli elementi esterni vengono inclusi nell’HTML dentro l’header, tramite i campi:
                - `<link>` collegamenti verso file esterni
                - `<script>` codice eseguibile utilizzato dal documento (solitamente JavaScript)
                - `<style>` informazioni di stile (CSS locali)
            
            ![image.png](PROGRAMMAZIONE%20WEB%201af9a6c97cf98039a6e0cd1e9e9bb7af/image%206.png)
            
            - `<body>`: Contiene il contenuto visibile (intestazioni, paragrafi, liste, tabelle, moduli, link, immagini, etc.).
                
                Questa è la parte che viene visualizzata dal browser, e costituisce l’elemento radice in cui possono essere messi altri elementi anche in modo annidato:
                
                - intestazioni (titoli)
                - strutture di testo come paragrafi
                - elenchi e liste
                - tabelle
                - moduli elettronici (form)
                - collegamenti ipertestuali
                - immagini e contenuti multimediali
                - contenuti interattivi
        - **Contenitori** e Elementi Specifici
            - **`<div>`**
                - Elemento “a blocchi” **usato per raggruppare altri element**i e strutturare il layout.
                - elementi per dare una struttura in righe e colonne alla pagina NEW LINE
                - Può essere reso visibile o stilizzato tramite CSS.
                Se non viene associato uno stile (per esempio un background) è invisibile
                    
                    ![image.png](PROGRAMMAZIONE%20WEB%201af9a6c97cf98039a6e0cd1e9e9bb7af/image%207.png)
                    
            - **`<span>`**
                - Contenitore generico che può essere annidato.
                - **inline usato per raggruppare parti di testo** senza introdurre interruzioni di linea .
                - La differenza col <div> è che questo è inline e quindi non mette una nuova riga tra un elemento e l’altro
                
            - **`<a>` (Anchor)**
                - viene usato per collegare un documento HTML a un altro o a un altro punto
                dello stesso documento
                - Il link è **composto** da **due estremi detti ”anchors”**
                - **Source anchor** (ancora sorgente) **→ destination anchor** (ancora destinazione)
                - Il **source anchor è contenuto nella pagina di partenza**, mentre **il destination anchor è un’altra risorsa web**
                
                ![image.png](PROGRAMMAZIONE%20WEB%201af9a6c97cf98039a6e0cd1e9e9bb7af/image%208.png)
                
            - `URL` Relativi e Assoluti
                - Gli **URL assoluti** contengono direttamente il link completo per la nuova risorsa
                *– es. [https://it.wikipedia.org/wiki/World_Wide_Web](https://it.wikipedia.org/wiki/World_Wide_Web)*
                - Gli **URL relativi** sono risolti utilizzando come base quella del documento corrente
                *– es. se sono già su Wikipedia, le altre risorse possono essere definite in modo relativo alla pagina corrente*
            
        
    - **`ESEMPIO`** di `HTML`
        - *Scopo e Obiettivi*
            
            Iniziamo a costruire un HTML e indicare degli elementi
            
            - titoli e paragrafi
            - una lista puntata
            - una tabella
            - un menu a tendina
            - dei link
        - **Header** e inizio
            
            ```html
            <!DOCTYPE html> <!-- dichiara il tipo di documento -->
            <html lang="it"> <!-- dichiara la lingua del documento -->
            <head>
                <meta charset="UTF-8"> <!-- per supportare tutti i caratteri -->
                <meta name="viewport" content="width=device-width, initial-scale=1.0"> <!-- per adattare la pagina a tutti i dispositivi -->
                <title>Il mio titolo</title>
            </head>
            ```
            
        - Contenuti dell’HTML: **header, paragrafi, liste puntate**
            
            ![image.png](PROGRAMMAZIONE%20WEB%201af9a6c97cf98039a6e0cd1e9e9bb7af/image%209.png)
            
            ```html
            <body>
                <div>
                    <h1>Esempio di HTML</h1>
                    <p>Pagina di test</p>
                    <p>Esempio semplice di HTML per il corso di Web Programming.</p>
                    <h3>Lista puntata:</h3>
                    <ul>
                        <li>Primo elemento</li>
                        <li>Secondo elemento</li>
                        <li>Terzo elemento</li>
                    </ul>
            
            </body>
            ```
            
        - Contenuti dell’HTML:  **Tabelle**
            
            ```html
                <div>
                    <h3>Tabella:</h3>
                    <table>
                        <tr> <!--riga-->
                            <th>Anno</th> <!--intestazione-->
                            <th>Evento</th>
                            <th>Descrizione</th>
                        </tr>
                        <tr>
                            <td>1 Febbraio 2025</td> <!--cella-->
                            <td>Corso di Web Programming</td>
                            <td>CLezione 1</td>
                        </tr>
                        <tr>
                            <td>2 Febbraio 2025</td>
                            <td>Corso di Web Programming</td>
                            <td>Lezione 2</td>
                    </table>
                </div>
            ```
            
            ![image.png](PROGRAMMAZIONE%20WEB%201af9a6c97cf98039a6e0cd1e9e9bb7af/image%2010.png)
            
        - Contenuti dell’HTML: **menu a tendina e link**
            
            ```html
                <div>
                    <h3>Seleziona un progetto</h3>
                    <select>
                    <option value="">Scegli un progetto</option>
                    <option value="1">Opzione 1</option>
                    <option value="1">Opzione 2</option>
                    <option value="1">Opzione 3</option>
                </select>
                </div>
            <div>
                <a href="https://github.com/unica-web" target="_blank">GitHub</a> <!-- link esterno, il target blank apre il link in una nuova scheda -->
            </div>
            </body>
            </html>
            ```
            
            ![image.png](PROGRAMMAZIONE%20WEB%201af9a6c97cf98039a6e0cd1e9e9bb7af/image%2011.png)
            
        - CODICE TOTALE
            
            ```html
            <!DOCTYPE html> <!-- dichiara il tipo di documento -->
            <html lang="it"> <!-- dichiara la lingua del documento -->
            <head>
                <meta charset="UTF-8"> <!-- per supportare tutti i caratteri -->
                <meta name="viewport" content="width=device-width, initial-scale=1.0"> <!-- per adattare la pagina a tutti i dispositivi -->
                <title>Il mio titolo</title>
            </head>
            <body>
                <div>
                    <h1>Esempio di HTML</h1>
                    <p>Pagina di test</p>
                    <p>Esempio semplice di HTML per il corso di Web Programming.</p>
                    <h3>Lista puntata:</h3>
                    <ul>
                        <li>Primo elemento</li>
                        <li>Secondo elemento</li>
                        <li>Terzo elemento</li>
                    </ul>
                </div>
                <div>
                    <h3>Tabella:</h3>
                    <table>
                        <tr> <!--riga-->
                            <th>Anno</th> <!--intestazione-->
                            <th>Evento</th>
                            <th>Descrizione</th>
                        </tr>
                        <tr>
                            <td>1 Febbraio 2025</td> <!--cella-->
                            <td>Corso di Web Programming</td>
                            <td>CLezione 1</td>
                        </tr>
                        <tr>
                            <td>2 Febbraio 2025</td>
                            <td>Corso di Web Programming</td>
                            <td>Lezione 2</td>
                    </table>
                </div>
                <div>
                    <h3>Seleziona un progetto</h3>
                    <select>
                    <option value="">Scegli un progetto</option>
                    <option value="1">Opzione 1</option>
                    <option value="1">Opzione 2</option>
                    <option value="1">Opzione 3</option>
                </select>
                </div>
            <div>
                <a href="https://github.com/unica-web" target="_blank">GitHub</a> <!-- link esterno, il target blank apre il link in una nuova scheda -->
            </div>
            </body>
            </html>
            ```
            
    - Document Object Model (**DOM**)
        - La pagina HTML viene interpretata come una struttura ad albero (DOM), in cui l’elemento `<html>` è la radice.
        - Il DOM permette la manipolazione dinamica degli elementi tramite script.
            
            ![image.png](PROGRAMMAZIONE%20WEB%201af9a6c97cf98039a6e0cd1e9e9bb7af/image%2012.png)
            
- Introduzione e Uso dei **`CSS`**
    - Cos’è il CSS (Cascading Style Sheets)
        - È il sistema per separare il contenuto dalla presentazione.
        - Permette di definire come gli elementi HTML debbano essere visualizzati, facilitando la manutenzione e il riutilizzo degli stili.
        
    - Vantaggi dell’uso dei CSS
        - **Separazione Contenuto/Stile:** Riutilizzo degli stessi stili in pagine differenti.
        - **Adattabilità:** Possibilità di creare stili diversi in base al contesto o al dispositivo (responsive design).
        - **Prestazioni:** File CSS possono essere memorizzati nella cache, riducendo i tempi di caricamento.
    - **Metodi per includere i CSS in HTML**
        - **Inline:** Stili applicati direttamente agli elementi (meno consigliato per progetti complessi).
        - **Interno:** Uso del tag `<style>` all’interno della sezione `<head>`.
        - **Esterno:** Collegamento di un file CSS tramite il tag
        
        `<link rel="stylesheet" type="text/css" href="styles.css">`
        
        - **Esempio di Inclusione di CSS Esterno:**
            
            ```html
            <!DOCTYPE html>
            <html>
            <head>
              <link rel="stylesheet" href="styles.css">
            </head>
            <body>
              <h1>Titolo pagina</h1>
              <p>Paragrafo di testo.</p>
            </body>
            </html>
            ```
            
            - Poi creiamo un altro file, chiamato “**styles.css”**, e lo mettiamo nella stessa cartella
            - Questo definisce gli stili per gli elementi dell’HTML
        
        ![image.png](PROGRAMMAZIONE%20WEB%201af9a6c97cf98039a6e0cd1e9e9bb7af/446901f5-1114-4b5f-befd-a36cbf4fee04.png)
        
- Sintassi, Regole e Specificità dei **`CSS`**
    - Struttura di una Regola CSS
        - **Selettore:** Identifica l’elemento o il gruppo di elementi (es. `p`, `.classe`, `#id`).
        - **Dichiarazioni:** Coppie proprietà-valore racchiuse tra parentesi graffe.
            
            – Proprietà: cosa si vuole cambiare
            – Valore: come si vuole cambiare
            
        
        ```css
        p {
          color: red;
          text-align: center;
        }
        
        ```
        
        ![image.png](PROGRAMMAZIONE%20WEB%201af9a6c97cf98039a6e0cd1e9e9bb7af/image%2013.png)
        
    - Selettori Avanzati:
        
        Esistono anche dei modi avanzati per definire specifici elementi o gruppi di elementi, denominati **classi**
        
        - Specifici elementi si identificano nell’HTML tramite l’attributo **`id=“nome_id”`**
            
            ![image.png](PROGRAMMAZIONE%20WEB%201af9a6c97cf98039a6e0cd1e9e9bb7af/image%2014.png)
            
        - Si identificano nell’HTML tramite l’attributo **`class=“nome_classe”`**
            
            ![image.png](PROGRAMMAZIONE%20WEB%201af9a6c97cf98039a6e0cd1e9e9bb7af/image%2015.png)
            
        - Ci sono poi ulteriori costrutti come le pseudoclassi (es. link visitati o hover) e pseudo elementi (es. la prima linea o la prima lettera di un paragrafo)
    - Unità di Misura:
        
        **Unità di misura relative**
        – em: relativo al font size dell’elemento (2em = 2 volte il font)
        – %: relativo all’elemento genitore
        – px: relativi al dispositivo di visualizzazione
        
        **Unità di misura assolute**
        – in: pollici (inches)
        – cm: centimetri
        – mm: millimetri
        – pt: points (1pt = 0.35 mm)
        – pc: picas (1pc = 12 pt)
        
    - Specificità e Ordine di Applicazione
        - La priorità degli stili viene determinata dalla specificità:
            - **Stili inline** hanno la **massima specificità**
            - **Seguiti** **dagli ID,** **poi dalle classi** **e dai selettori di tipo**.
        - Se due regole hanno la stessa specificità, viene applicata quella dichiarata per ultima.
        - Esempio illustrativo:
            
            ```html
            <html>
            <head>
              <style>
              .test { color: green; }
              p { color: red; }
              </style>
            </head>
            <body>
              <p class="test">Hello!</p>
            </body>
            </html>
            
            ```
            
- Riassunto -parte finale
    - Tipi di stili in HTML e CSS
        
        ### **1. Stili Inline**
        
        Si scrivono direttamente all’interno del tag HTML usando l’attributo `style`.
        
        **Esempio:**
        
        ```html
        <p style="color: red;">Testo rosso</p>
        
        ```
        
        **Caratteristica:** Hanno la priorità più alta tra gli stili normali (escluso l'uso di `!important`).
        
        ---
        
        ### **2. Stili di ID**
        
        Si applicano a elementi che hanno un attributo `id`. Nel CSS, si usa il simbolo `#`.
        
        **Esempio:**
        
        ```html
        <p id="paragrafo">Paragrafo</p>
        
        <style>
          #paragrafo {
            color: blue;
          }
        </style>
        
        ```
        
        ---
        
        ### **3. Stili di Classe**
        
        Si applicano a elementi con una certa classe. Nel CSS si usa il `.`.
        
        **Esempio:**
        
        ```html
        <p class="importante">Paragrafo importante</p>
        
        <style>
          .importante {
            color: green;
          }
        </style>
        
        ```
        
        ---
        
        ### **4. Selettori di Tipo (o di elemento)**
        
        Si riferiscono direttamente al tipo di elemento HTML.
        
        **Esempio:**
        
        ```html
        <p>Paragrafo normale</p>
        
        <style>
          p {
            color: black;
          }
        </style>
        
        ```
        
    - 📊 Tabella della Specificità
        
        
        | Tipo di Stile | Sintassi CSS | Specificità (valori) | Priorità |
        | --- | --- | --- | --- |
        | **Inline** | `<p style="...">` | (1,0,0,0) | ★★★★ |
        | **ID Selector** | `#id` | (0,1,0,0) | ★★★ |
        | **Classe, Attributo, Pseudo-classe** | `.classe`, `[attr]`, `:hover` | (0,0,1,0) | ★★ |
        | **Selettore di Tipo (elemento)** | `p`, `h1`, `div` | (0,0,0,1) | ★ |
        | **Universale o combinatori** | `*`, `+`, `>` | (0,0,0,0) | Nessuna |
    - Ordine di priorità (dal più forte al più debole):
        1. **Inline styles** (scritti nel tag stesso).
        2. **ID selectors** (`#id`).
        3. **Class selectors**, attributi e pseudo-classi (`.classe`, `[attr]`, `:hover`).
        4. **Element selectors** (`p`, `div`, `h1`).
        5. **Selettore universale** (), combinatori e ereditati.
        6. In caso di conflitto tra regole con stessa specificità, vince quella **scritta dopo**.
        7. A parte, **`!important`** sovrascrive tutto, ma va usato con attenzione.
    - Esempi Avanzati di CSS Integrato in HTML
        - **Stilizzazione con Flexbox e Componenti (es. Card):**
        Esempio di CSS per centrare il contenuto, stilizzare una “card” e definire stili per immagini, titoli, paragrafi e link:
        Questi esempi mostrano come integrare CSS per ottenere layout centrati, stilizzare componenti come tabelle, liste, menu a tendina e link interattivi.
            
            ```html
            <style>
              body {
                display: flex;
                justify-content: center;
                align-items: center;
                min-height: 100vh;
                margin: 0;
                background-color: #f0f2f5;
                font-family: Arial, sans-serif;
              }
              .card {
                background-color: white;
                border-radius: 10px;
                padding: 20px;
                text-align: center;
                width: 400px;
                box-shadow: 0 2px 5px rgba(0, 0, 0, 0.1);
              }
              img {
                width: 150px;
                height: 150px;
                border-radius: 50%;
                margin-bottom: 15px;
              }
              h1 {
                color: #1a1a1a;
                margin: 10px 0;
                font-size: 24px;
              }
              .titolo {
                color: #4a90e2;
                font-weight: bold;
                margin: 5px 0;
              }
              .descrizione {
                color: #666;
                font-size: 14px;
                line-height: 1.5;
                margin: 15px 0;
              }
              .contatti {
                display: flex;
                justify-content: center;
                gap: 15px;
                margin-top: 20px;
              }
              .contatti a {
                color: #4a90e2;
                text-decoration: none;
                padding: 8px 15px;
                border: 1px solid #4a90e2;
                border-radius: 20px;
                transition: all 0.3s ease;
              }
              .contatti a:hover {
                background-color: #4a90e2;
                color: white;
              }
              ul {
                text-align: left;
                margin: 20px 0;
                padding-left: 30px;
              }
              li {
                margin: 10px 0;
                color: #444;
              }
              table {
                width: 100%;
                margin: 20px 0;
                border-collapse: collapse;
              }
              th, td {
                padding: 10px;
                border: 1px solid #ddd;
              }
              th {
                background-color: #f5f5f5;
              }
              select {
                padding: 8px;
                margin: 10px 0;
                border-radius: 5px;
                border: 1px solid #ddd;
              }
            </style>
            
            ```
            
    - Conclusioni
        - **Sintesi:**
            - **HTML** definisce la struttura e il contenuto della pagina, mentre **CSS** gestisce la presentazione e lo stile.
            - La separazione dei contenuti dalla presentazione permette un design più flessibile e un riutilizzo efficiente degli stili.
            - È importante comprendere la sintassi dei tag, il funzionamento degli attributi, la struttura del documento e le regole CSS, inclusa la specificità, per realizzare pagine web ben strutturate e coerenti.
        - **Approccio Pratico:**
            - “Learn by doing” è il metodo consigliato: sperimentare con esempi pratici (es. esercizi di HTML e CSS) è il modo migliore per apprendere e consolidare le competenze.
- Riassunto Completo
    - `Introduzione al Web e ai Linguaggi di Markup`
        - **Origini del Web e degli ipertesti**
            - Il Web è nato per condividere documenti ipertestuali (pagine contenenti link ad altre pagine), inizialmente statici.
            - I browser (Chrome, Firefox, Safari, ecc.) servono per visualizzare queste pagine.
            - In seguito si sono sviluppati strumenti in grado di generare pagine dinamiche con contenuti personalizzati.
        - **Cosa sono i Linguaggi di Markup**
            - Sono linguaggi che usano **tag** (istruzioni speciali) per descrivere come deve essere formattato o strutturato un contenuto.
            - Si basano su:
                - **Struttura (tag)**: per indicare semantica e disposizione degli elementi.
                - **Grammatica**: regole su come scrivere correttamente i tag.
                - **Semantica**: significato del contenuto (ad esempio, cosa è un paragrafo, cosa è un titolo, ecc.).
            - **Tipologie di linguaggi di markup**:
                - Procedurali (es. troff, TEX): spiegano come il testo viene “trattato” passo passo.
                - Descrittivi (es. SGML, HTML, XML): si concentrano sulla struttura logica e lasciano al programma (browser) il compito di decidere come renderizzare graficamente il contenuto.
            - **HTML** fa parte dei linguaggi descrittivi. Non è un linguaggio di programmazione, ma serve a descrivere la struttura di una pagina web.
        - **HTML e la sua evoluzione**
            - Attualmente si usa **HTML5**, considerato uno “standard vivente”. È retro-compatibile con le versioni precedenti e viene aggiornato gradualmente.
    - Struttura e Sintassi di `HTML`
        - Elementi di base: Tag e Attributi
            - **Tag**
                - Sono racchiusi tra i simboli `< >` e spesso si usano in coppia: `<tag>…</tag>`.
                    - Esempio: `<p>Testo di contenuto</p>`
                - Alcuni tag **non** hanno un tag di chiusura (es. `<br>` per andare a capo).
                - Si possono **annidare** (ad esempio `<p><b>Testo in grassetto</b></p>`).
            - **Attributi**
                - Aggiungono informazioni o proprietà ai tag.
                - Si scrivono dentro il tag di apertura, come `chiave="valore"`.
                    - Esempio: `<a href="<https://www.google.com>">Visita Google</a>`
                - L’attributo `href` indica il link di destinazione.
        - Struttura di un documento HTML
            
            Un documento HTML standard include:
            
            1. `<!DOCTYPE html>`
                - Indica il tipo di documento. Serve al browser per capire che è una pagina HTML5.
            2. `<html lang="it"> … </html>`
                - È l’elemento radice (tutto il codice sta qui dentro).
                - L’attributo `lang` dichiara la lingua.
            3. `<head> … </head>`
                - Contiene **metadati** e informazioni non mostrate direttamente nella pagina:
                    - `<title>` per il titolo della finestra o della scheda del browser.
                    - `<meta>` per specificare il set di caratteri (`charset="UTF-8"`) o informazioni per i motori di ricerca.
                    - `<link>` per collegare file esterni (es. fogli di stile CSS).
                    - `<script>` per includere codice JavaScript.
            4. `<body> … </body>`
                - Qui va il **contenuto visibile** della pagina (testi, immagini, link, tabelle, form, ecc.).
            
            Esempio minimale:
            
            ```html
            <!DOCTYPE html>
            <html lang="it">
            <head>
              <meta charset="UTF-8">
              <title>Il mio titolo</title>
            </head>
            <body>
              <!-- Contenuto visibile -->
            </body>
            </html>
            
            ```
            
            ### 2.3 Altri elementi fondamentali
            
            - **`<div>`**
                - Contenitore “a blocchi” usato per raggruppare altri elementi e organizzare il layout (righe, colonne, sezioni).
                - Di norma è invisibile a meno che non si applichino stili (per esempio un colore di sfondo).
            - **`<span>`**
                - Contenitore **inline** usato per “raggruppare” parti di testo o elementi senza andare a capo automaticamente.
                - Utile per applicare stili a singole parole o piccole porzioni di testo.
            - **`<a>` (Anchor)**
                - Crea un collegamento ipertestuale.
                - L’attributo più importante è `href`, che indica la destinazione (URL).
                - Due tipi di URL:
                    - **Assoluto**: es. `https://www.esempio.it`.
                    - **Relativo**: es. `pagina.html` (funziona rispetto alla posizione del file corrente).
        - Esempio completo di HTML
            
            Esempio di pagina con:
            
            - Titolo
            - Paragrafi
            - Lista puntata (`<ul><li>…</li></ul>`)
            - Tabella (`<table>`)
            - Menu a tendina (`<select>`)
            - Link (`<a>`)
            
            ```html
            <!DOCTYPE html>
            <html lang="it">
            <head>
              <meta charset="UTF-8">
              <title>Il mio titolo</title>
            </head>
            <body>
              <div>
                <h1>Esempio di HTML</h1>
                <p>Pagina di test</p>
                <p>Un semplice esempio per il corso di Web Programming.</p>
                <h3>Lista puntata:</h3>
                <ul>
                  <li>Primo elemento</li>
                  <li>Secondo elemento</li>
                  <li>Terzo elemento</li>
                </ul>
              </div>
            
              <div>
                <h3>Tabella:</h3>
                <table>
                  <tr>
                    <th>Anno</th>
                    <th>Evento</th>
                    <th>Descrizione</th>
                  </tr>
                  <tr>
                    <td>1 Febbraio 2025</td>
                    <td>Corso di Web Programming</td>
                    <td>Lezione 1</td>
                  </tr>
                  <tr>
                    <td>2 Febbraio 2025</td>
                    <td>Corso di Web Programming</td>
                    <td>Lezione 2</td>
                  </tr>
                </table>
              </div>
            
              <div>
                <h3>Seleziona un progetto</h3>
                <select>
                  <option value="">Scegli un progetto</option>
                  <option value="1">Opzione 1</option>
                  <option value="2">Opzione 2</option>
                  <option value="3">Opzione 3</option>
                </select>
              </div>
            
              <div>
                <a href="<https://github.com/unica-web>" target="_blank">GitHub</a>
              </div>
            </body>
            </html>
            
            ```
            
            ### 2.5 Document Object Model (DOM)
            
            - Una pagina HTML viene rappresentata internamente come un albero di oggetti (nodi) dove `<html>` è la radice.
            - Si può manipolare la pagina dinamicamente (ad esempio con JavaScript) usando questa struttura ad albero.
    - Introduzione e uso dei `CSS`
        - Introduzione
            - **Cosa sono i CSS**
                - Cascading Style Sheets: servono a **separare** il contenuto (HTML) dalla **presentazione** (aspetto grafico).
                - Rendono più facile cambiare l’aspetto di un sito e mantenere i fogli di stile in modo centralizzato.
            - **Vantaggi**
                1. **Separazione contenuto/stile**: puoi riutilizzare lo stesso file CSS su più pagine.
                2. **Adattabilità**: puoi definire stili diversi in base al tipo di dispositivo (responsive design).
                3. **Prestazioni**: un file CSS esterno viene scaricato una sola volta e può essere messo in cache.
            - **Come includere i CSS in un documento HTML**
                1. **Inline**: scrivi lo stile dentro il singolo tag, con l’attributo `style="…"`. (Sconsigliato per progetti complessi.)
                2. **Interno**: usi il tag `<style>` nell’`<head>` dell’HTML.
                3. **Esterno**: crei un file `.css` separato e lo colleghi con
                (metodo più ordinato e professionale).
                    
                    ```html
                    <link rel="stylesheet" type="text/css" href="styles.css">
                    
                    ```
                    
        - Sintassi, Regole e Specificità dei CSS
            - **Struttura di una Regola CSS**
                
                ```css
                selettore {
                  proprietà: valore;
                  proprietà: valore;
                }
                
                ```
                
                - **Selettore**: indica a quali elementi HTML applicare la regola (es. `p` per tutti i paragrafi, `.nomeClasse` per gli elementi con quella classe, `#idUnico` per un elemento con quell’ID).
                - **Dichiarazioni**: coppie proprietà–valore (ad esempio `color: red;`, `font-size: 16px;`).
            - **Selettori Avanzati**
                - **Classi**: `class="nome_classe"`. Nel CSS si usano con il punto: `.nome_classe { … }`.
                - **ID**: `id="nome_id"`. Nel CSS si usano con il cancelletto: `#nome_id { … }`.
                - Esistono anche **pseudoclassi** (per es. `:hover`, `:visited`) e **pseudo-elementi** (per es. `::first-line`).
            - **Unità di Misura**
                - **Relative**: `em`, `%`, `px` (dipendono dal contesto, dal font o dalla risoluzione).
                - **Assolute**: `cm`, `mm`, `in`, `pt`. Più tipiche per la stampa, meno per il web.
            - **Specificità e Ordine di Applicazione**
                - L’ordine con cui vengono applicate le regole:
                    1. Stili **inline** (dentro i tag) → massima priorità
                    2. Stili con **ID**
                    3. Stili con **classi**
                    4. Stili con **selettori di tipo** (es. `p`, `h1`, ecc.)
                - Se due regole hanno la stessa specificità, vale quella scritta più in basso (ultima in ordine di codice).
            
            Esempio veloce:
            
            ```html
            <p class="test">Ciao!</p>
            
            ```
            
            ```css
            /* CSS interno o esterno */
            p { color: red; }       /* tutti i paragrafi rossi */
            .test { color: green; } /* tutti gli elementi con classe test verdi */
            
            ```
            
            Il paragrafo con classe `test` sarà verde, perché la regola `.test` è più specifica del semplice `p`.
            
    - TABELLE RIASSUNTIVE
        
        ---
        
        ### Tabella `HTML`
        
        | **Argomento** | **Dettagli** |
        | --- | --- |
        | **Origini e Concetto** | Il Web nasce per condividere documenti ipertestuali statici; in seguito si è evoluto in pagine dinamiche. I linguaggi di markup, come HTML, servono a descrivere la struttura e il contenuto delle pagine. |
        | **Linguaggio di Markup** | Utilizza **tag** (istruzioni racchiuse tra `<` e `>`) per definire struttura, semantica e formattazione. Distinto dai linguaggi di programmazione. |
        | **Struttura Base di un Documento** | Comprende: 
        • `<!DOCTYPE html>` per dichiarare il tipo di documento. 
        • `<html lang="it">` come radice. 
        • `<head>` per metadati, titoli, collegamenti a file esterni e script.  • `<body>` per il contenuto visibile. |
        | **Tag e Sintassi** | I tag si usano in coppia (apertura e chiusura) ad eccezione di alcuni (es. `<br>`). Possibile annidamento dei tag (es. `<p><b>Testo</b></p>`). |
        | **Attributi** | Forniscono informazioni aggiuntive ai tag tramite coppie chiave-valore (es. `href="<https://www.google.com>"`). I valori sono racchiusi in apici. |
        | **Elementi di Contenimento** | • `<div>`: Contenitore a blocchi per raggruppare e strutturare il layout. 
        • `<span>`: Contenitore inline per parti di testo. 
        • `<a>`: Per creare collegamenti ipertestuali (URL assoluti o relativi). |
        | **Esempi Pratici** | Struttura di una pagina completa, uso di liste, tabelle, form e menu a tendina. |
        | **Document Object Model (DOM)** | Rappresentazione della pagina come struttura ad albero, che permette di manipolare dinamicamente gli elementi tramite script (es. JavaScript). |
        
        ---
        
        ### Tabella `CSS`
        
        | **Argomento** | **Dettagli** |
        | --- | --- |
        | **Cos'è il CSS** | CSS (Cascading Style Sheets) è un linguaggio per definire la presentazione (stili, layout e formattazione) degli elementi HTML, separando il contenuto dalla forma. |
        | **Vantaggi** | • Separazione contenuto/stile: Consente il riutilizzo degli stessi stili in pagine diverse. 
        • Adattabilità: Possibilità di creare design responsive per diversi dispositivi. 
        • Migliore performance grazie alla cache. |
        | **Metodi di Inclusione** | • **Inline:** Uso dell’attributo `style` direttamente nell'HTML. 
        • **Interno:** Tag `<style>` nel `<head>`. 
        • **Esterno:** File CSS collegato tramite `<link rel="stylesheet" href="styles.css">`. |
        | **Struttura di una Regola CSS** | Ogni regola è composta da: 
        • **Selettore:** Identifica gli elementi a cui applicare lo stile (es. `p`, `.classe`, `#id`). 
        • **Dichiarazioni:** Coppie proprietà-valore racchiuse tra `{}`. |
        | **Selettori** | • Selettori di tipo (es. `h1`, `p`). 
        • Classi (es. `.nomeClasse`) definite in HTML con `class="nomeClasse"`. 
        • ID (es. `#nomeID`) definiti con `id="nomeID"`. <br> • Pseudoclassi e pseudo-elementi per stili particolari. |
        | **Unità di Misura** | • **Relative:** `em`, `%`, `px` (dipendono da fattori come il font o il contenitore). 
        • **Assolute:** `cm`, `mm`, `in`, `pt` (meno usate per il web). |
        | **Specificità e Ordine di Applicazione** | La priorità degli stili si determina in questo modo: 
        1. Stili inline 
        2. Selettori con ID 
        3. Selettori con classi 
        4. Selettori di tipo 
        Se regole con la stessa specificità, vince quella scritta per ultima. |
        
        ---
        
    - info utili lezione
        - **DROPDOWN HTML:** Per trovare tutti i tag HTML https://www.w3schools.com/tags/tag_select.asp
        - **DOM:** pagine HTML come strutture ad albero
        - hover → CSS cambia dinamicamente con lo spostamento del mouse

---

**`5 - JSON e XML`**

- Introduzione generale
    - **Obiettivo:**
        
        Dopo aver visto come visualizzare documenti e applicare stili, ci si concentra sul contenuto, ossia su come passare dei dati al documento HTML affinché questi vengano visualizzati al suo interno.
        
    - **I due formati di scambio dati trattati:**
        - EXtensible Markup Language (XML)
        - JavaScript Object Notation (JSON)
- **`XML`**: Struttura, Caratteristiche e Validazione
    - Introduzione e Caratteristiche di `XML`
        - **Cos’è XML:**
            - È un formato che consente la rappresentazione di dati strutturati (ad esempio, dati da inserire in tabelle).
            - Nasce come sottoinsieme semplificato di SGML (lo stesso insieme a cui appartiene anche l’HTML).
            - È un linguaggio a marcatori: usa tag per identificare ogni elemento.
        - **Leggibilità e Portabilità:**
            - I documenti XML sono leggibili sia da computer sia da umani, soprattutto se formattati con indentazione corretta.
            - XML è indipendente dalla piattaforma e dall’applicazione in cui viene usato, può essere archiviato su qualsiasi supporto e aperto con qualsiasi editor di testo.
            - È facilmente trasmesso via Internet e sono disponibili numerose librerie per manipolarlo (ad es. per formattarlo dopo averlo estratto da un database).
        - ESEMPIO di `XML`
            - **Esempio Base:**
            Il seguente esempio mostra un semplice documento XML con una dichiarazione e alcuni elementi:
                
                ```xml
                <?xml version="1.0" encoding="UTF-8"?>
                <note>
                  <to>Tove</to>
                  <from>Jani</from>
                  <subject>Greetings</subject>
                  <message>Hello!</message>
                </note>
                
                ```
                
    - `XML`  come Metalinguaggio
        - **Definizione di Metalinguaggio:**
            - XML è un metalinguaggio, ossia un “linguaggio per descrivere linguaggi”.
            - Ciò significa che definisce regole metasintattiche (la sintassi per scrivere sintassi) per descrivere un linguaggio.
        - **Regole e Grammatica:**
            - L’autore deve definire i tag e la struttura del documento seguendo regole che indicano quali elementi possono essere usati e in che forma (i tag devono essere aperti e chiusi, e sono delimitati da caratteri speciali).
    - Struttura e Gerarchia dei Documenti `XML`
        - **Composizione del Documento:**
            - I documenti XML sono composti da elementi che rappresentano componenti logici del documento.
            - Ogni elemento può avere sotto-elementi, formando una struttura ad albero:
                - Il documento parte da un nodo radice, da cui si diramano “child” e “siblings”.
                - I rapporti tra i nodi sono descritti con termini come “parent”, “child” e “siblings”.
        - **Esempio di Documento XML con Struttura Gerarchica:**
            
            ```xml
            <?xml version="1.0" encoding="UTF-8"?>
            <bookstore>
              <book category="cooking">
                <title lang="en">Everyday Italian</title>
                <author>Giada De Laurentiis</author>
                <year>2005</year>
                <price>30.00</price>
              </book>
              <book category="children">
                <title lang="en">Harry Potter</title>
                <author>J K. Rowling</author>
                <year>2005</year>
                <price>29.99</price>
              </book>
            </bookstore>
            
            ```
            
    - Regole di Grammatica e Sintassi di `XML`
        - **Tipi di Contenuto:**
            - Il documento XML è una stringa di caratteri ASCII o Unicode e può contenere elementi utili alla visualizzazione come spazi, a capo e commenti.
        - **Case Sensitivity:**
            - I nomi di elementi, attributi ed entità sono *case sensitive* (ad esempio, `<tag>` e `<Tag>` sono elementi differenti).
        - **Caratteri Speciali e Sostituzioni:**
            - I tag sono delimitati dai caratteri “<” e “>”, mentre l’ampersand (&) viene usato per entità.
            - Questi caratteri non possono comparire come contenuto diretto, ma devono essere sostituiti con le relative entità:
                - `<` diventa `&lt;`
                - `>` diventa `&gt;`
                - `&` diventa `&amp;`
            - I commenti sono scritti così:
                
                ```xml
                <!-- Commento -->
                
                ```
                
    - Struttura dei Documenti `XML`: Prologo e Corpo
        - **Il Documento si Divide in Due Parti:**
            - **Prologo:**
                - Contiene la dichiarazione XML (es. `<?xml version="1.0" encoding="UTF-8"?>`) e, eventualmente, riferimenti a documenti esterni come fogli di stile o regole di validazione (es. `<?xml-stylesheet type="text/css" href="style.css"?>`).
            - **Corpo:**
                - Contiene i dati e i contenuti veri e propri del documento.
    - Elementi, Tag e Attributi
        - **Tag di Apertura e Chiusura:**
            - Come in HTML, un elemento XML è delimitato da uno start tag e da un end tag.
            Esempio:
                
                ```xml
                <NomeTag lista-attributi>contenuto</NomeTag>
                
                ```
                
            - Per elementi vuoti si usa la sintassi autonoma:
                
                ```xml
                <NomeTag/>
                
                ```
                
        - **Attributi negli Elementi:**
            - Ogni elemento può avere attributi (coppie nome-valore).
            - Gli attributi si scrivono all’interno dello start tag e i valori devono essere racchiusi tra singoli o doppi apici.
            Esempio:
                
                ```xml
                <immagine file="immagine1.jpg"></immagine>
                
                ```
                
            - Gli attributi non si annidano e si riferiscono esclusivamente all’elemento in cui sono dichiarati.
    - Validità e Formattazione di un Documento `XML`
        - **Documenti Ben Formati:**
            
            Per essere considerato ben formato, un XML deve:
            
            - Avere una dichiarazione corretta nel prologo.
            - Assicurarsi che ogni elemento abbia un tag di apertura e uno di chiusura.
            - Rispettare l’annidamento corretto (i tag aperti devono essere chiusi in ordine).
            - Avere i valori degli attributi racchiusi tra apici.
        - **Validazione tramite DTD e XSD:**
            - **DTD (Document Type Definition):**
                - Elenca le dichiarazioni che descrivono la struttura del documento, definendo quali elementi e attributi possono essere usati.
            - **XML Schema Definition (XSD):**
                - È una definizione dello schema in formato XML.
                - Può includere:
                    - Dichiarazioni di elementi (nome, tipo, vincoli).
                    - Dichiarazioni di attributi (nome, tipo, valori predefiniti).
                    - Tipi di dato semplici (interi, stringhe, ecc.) e complessi (ad esempio, una durata composta da due date).
                    - Definizioni di gruppi di modelli e attributi, oltre ad altri componenti specializzati.
                - Queste regole permettono di verificare, mediante validazione, se un documento XML rispetta la struttura prevista.
    - Document Object Model (DOM) per `XML`
        - **Cos’è il DOM:**
            - Un modello che rappresenta il contenuto XML come un albero in memoria.
        - **Interfacce Fondamentali del DOM:**
            - **Node:** L’elemento base.
            - **NodeList:** Una collezione ordinata di nodi.
            - **NamedNodeMap:** Una collezione di attributi.
        - **Uso del Parser DOM:**
            - Si utilizza per trasformare un documento XML in una struttura ad albero (DOM) e viceversa, permettendo la manipolazione dinamica dei dati.
- **`JSON`**: Struttura, Sintassi e Confronto con `XML`
    - Introduzione al `JSON`
        - **Cos’è JSON:**
            - JSON (JavaScript Object Notation) è un formato di testo per la conservazione e il trasporto dei dati.
            - È stato creato per essere facilmente caricato e usato in JavaScript.
        - **Confronto con XML:**
            - XML è un formato più “stringente” e richiede una struttura completa con tag di chiusura;
            - JSON non richiede lo schema, è più rapido da realizzare e leggere ed è generalmente più compatto, eliminando la ripetizione dei nomi dei tag nella chiusura degli elementi.
    - Struttura e Sintassi del `JSON`
        - **Organizzazione dei Dati:**
            - I dati sono organizzati in coppie chiave-valore.
            - Sia il nome che il valore sono racchiusi tra doppi apici ("") e separati da due punti (:).
            - Le coppie sono separate da virgole.
        - **Elementi Fondamentali di JSON:**
            - **Oggetti:**
                - Racchiusi tra parentesi graffe `{ }`.
                - Esempio:
                    
                    ```json
                    {"name": "John", "age": 30, "car": null}
                    
                    ```
                    
                - Definisce un oggetto con le proprietà "name", "age" e "car".
            - **Array:**
                - Racchiusi tra parentesi quadre `[ ]`.
                - Utilizzati per raggruppare una lista ordinata di valori (che possono essere stringhe, oggetti, array, booleani o null).
                - Esempio:
                    
                    ```json
                    {
                      "name": "John",
                      "age": 30,
                      "cars": ["Ford", "BMW", "Fiat"]
                    }
                    
                    ```
                    
    - Sintassi `JSON` in Dettaglio
        - **Dettagli Sintattici:**
            - La sintassi JSON è un sottoinsieme della sintassi usata per definire oggetti in JavaScript.
            - Regole principali:
                - I dati sono formati da coppie chiave-valore, in cui la chiave è una stringa (racchiusa in doppi apici) seguita dai due punti e dal valore.
                - Le coppie sono separate da virgole.
                - Gli oggetti sono definiti tra parentesi graffe `{ }`.
                - Gli array sono definiti tra parentesi quadre `[ ]`.
        - **Esempio Sintattico:**
            
            ```json
            {"name": "John", "age": 30, "car": null}
            
            ```
            
    - Confronto: `JSON` vs `XML`
        - **Struttura degli Esempi:**
            - **JSON:**
                
                ```json
                {"employees":[
                  { "firstName":"John", "lastName":"Doe" },
                  { "firstName":"Anna", "lastName":"Smith" },
                  { "firstName":"Peter", "lastName":"Jones" }
                ]}
                
                ```
                
            - **XML:**
                
                ```xml
                <employees>
                  <employee>
                    <firstName>John</firstName>
                    <lastName>Doe</lastName>
                  </employee>
                  <employee>
                    <firstName>Anna</firstName>
                    <lastName>Smith</lastName>
                  </employee>
                  <employee>
                    <firstName>Peter</firstName>
                    <lastName>Jones</lastName>
                  </employee>
                </employees>
                
                ```
                
        - **Somiglianze:**
            - Entrambi sono formati auto-descritti e facilmente leggibili dall’uomo.
            - Entrambi sono strutturati in maniera gerarchica e possono avere valori annidati.
            - Possono essere utilizzati in molti linguaggi di programmazione e trasferiti tramite richieste HTTP GET.
        - **Differenze:**
            - JSON non utilizza tag di chiusura; invece, usa parentesi e virgolette per delimitare gli oggetti e gli array.
            - JSON è generalmente più compatto e più facile da leggere e scrivere.
            - JSON supporta nativamente gli array, rendendo più semplice la gestione di collezioni ordinate.
    - Tipi di Dato in `JSON`
        - **Tipi di Valori Ammessi in JSON:**
            
            I valori in JSON devono essere uno dei seguenti tipi:
            
            - Stringhe
            - Numeri (interi o in virgola mobile)
            - Oggetti (altri JSON)
            - Array
            - Booleani (true o false)
            - null
        - **Esempio di Oggetto JSON con Tipi Diversi:**
            
            ```json
            {
              "employee": {
                "name": "John",
                "age": 30,
                "city": "New York"
              }
            }
            
            ```
            
    - Gli Array in `JSON`
        - **Utilizzo e Vantaggi degli Array:**
            - Gli array consentono di raggruppare più valori (simili agli array in JavaScript).
            - Sono particolarmente comodi per iterare e scorrere tra gli elementi, per esempio per stampare ogni valore in una nuova riga.
        - **Esempio di Array in JSON:**
            
            ```json
            {
              "name": "John",
              "age": 30,
              "cars": ["Ford", "BMW", "Fiat"]
            }
            
            ```
            
- conclusioni e considerazioni finali
    - **XML:**
        - È un formato versatile e strutturato, ideale per rappresentare dati complessi.
        - Richiede una definizione esplicita di tag e attributi, e permette la validazione mediante DTD o XSD.
        - Il modello DOM consente di manipolare dinamicamente il contenuto XML.
    - **JSON:**
        - Offre una sintassi semplice, compatta e facilmente integrabile in ambienti JavaScript e in altri linguaggi (come Python, grazie alla sua somiglianza con i dizionari).
        - È meno stringente rispetto all’XML e più rapido da scrivere e leggere, soprattutto per lo scambio di dati in applicazioni web.
    - **Scelta del Formato:**
        
        La decisione tra XML e JSON dipende dalle esigenze specifiche dell’applicazione:
        
        - XML è preferibile quando è necessaria una forte validazione e una descrizione dettagliata della struttura.
        - JSON è la scelta ideale quando si richiede rapidità, leggerezza e facilità di integrazione, soprattutto in ambienti web.
- RIASSUNTO + TABELLE
    - Perché XML e JSON?
        
        Quando si realizzano applicazioni web o software che richiedono lo scambio di dati, è fondamentale scegliere un formato efficace per rappresentarli. XML e JSON sono tra i formati più diffusi:
        
        - **XML (Extensible Markup Language)**: linguaggio basato su tag, molto esteso e versatile, spesso impiegato quando è necessaria una rigorosa validazione dei dati e un’ampia descrittività.
        - **JSON (JavaScript Object Notation)**: formato più semplice e leggero, particolarmente adatto alle applicazioni web (soprattutto in ambito JavaScript), grazie alla sua sintassi compatta e facile da interpretare.
    - XML in breve
        - **Cos’è XML**
            
            XML è un metalinguaggio, ovvero un linguaggio che definisce altre grammatiche (dove i tag e la struttura vengono stabiliti dall’utente). Serve per rappresentare dati in modo strutturato e gerarchico.
            
        - **Caratteristiche principali**
            - Basato su tag, con elementi annidati che formano una struttura ad albero.
            - Case sensitive (i tag `<Book>` e `<book>` sono considerati diversi).
            - Richiede chiusura corretta dei tag.
            - Supporta attributi all’interno dei tag per aggiungere metadati.
            - Indipendente dalla piattaforma e leggibile sia da uomo che da macchina.
            - Può essere validato tramite **DTD** o **XSD** (XML Schema) per garantire che rispetti uno schema predefinito.
        - **Struttura tipica**
            - **Prologo**: contiene la dichiarazione XML (versione, encoding) e, facoltativamente, riferimenti a stylesheet o schemi.
            - **Corpo**: il contenuto vero e proprio, organizzato in un elemento radice che racchiude gli altri.
        - **Esempio Minimo**
            
            ```xml
            <?xml version="1.0" encoding="UTF-8"?>
            <note>
              <to>Tove</to>
              <from>Jani</from>
              <message>Hello!</message>
            </note>
            
            ```
            
        - **Validità e Ben Formazione**
            
            Un file XML è “ben formato” se rispetta la sintassi (tag aperti e chiusi correttamente, attributi tra apici, annidamenti corretti, ecc.). Può anche essere “valido” se segue le regole di uno schema (DTD o XSD).
            
        - **DOM (Document Object Model)**
            - Un documento XML può essere caricato e interpretato come un albero di oggetti (nodi), con un nodo radice e relazioni parent-child (genitore-figlio).
            - Attraverso il parser DOM, si possono leggere e modificare i dati programmaticamente.
    - JSON in breve
        - **Cos’è JSON**
            
            JSON (JavaScript Object Notation) è un formato testuale per rappresentare dati tramite coppie chiave-valore e liste (array). È stato ideato per essere semplice da gestire all’interno del linguaggio JavaScript, ma oggi è supportato dalla maggior parte dei linguaggi.
            
        - **Caratteristiche principali**
            - Estremamente leggero e facile da leggere.
            - Utilizza parentesi graffe `{}` per definire oggetti, parentesi quadre `[]` per definire array.
            - Le chiavi sono sempre stringhe in **doppi apici**, seguite dai due punti `:` e dal valore.
            - Supporta stringhe, numeri, booleani, null, oggetti annidati, array annidati.
            - Non prevede tag di apertura/chiusura: la struttura è determinata solo da parentesi e virgole.
        - **Esempio Minimo**
            
            ```json
            {
              "name": "John",
              "age": 30,
              "car": null
            }
            
            ```
            
        - **Sintassi e Validità**
            - Molto più compatta rispetto a XML: non essendoci tag, non si rischiano confusione tra maiuscole/minuscole o annidamenti errati tipici di XML.
            - Se viene rispettata la regola di chiavi in stringhe e parentesi/virgole correttamente posizionate, il JSON è valido.
        - **Vantaggi rispetto a XML**
            - Più conciso.
            - Più facile da trasmettere sulle reti (meno caratteri e ridondanza).
            - Interpretazione immediata in JavaScript (può essere convertito in oggetti JavaScript con un’unica funzione, ad es. `JSON.parse()`).
    - Confronto Finale tra XML e JSON
        - **Somiglianze**
            - Entrambi sono formati di testo e quindi facilmente leggibili e ispezionabili.
            - Entrambi possono avere struttura gerarchica (annidamento).
            - Compatibili con numerosi linguaggi di programmazione.
        - **Differenze**
            - **Validazione**: XML offre meccanismi più articolati (DTD, XSD); JSON è meno “stringente”.
            - **Sintassi**: XML fa uso di tag (apertura/chiusura), JSON di coppie chiave-valore e array.
            - **Verbosità**: XML risulta spesso più ridondante rispetto a JSON.
            - **Integrazione con JavaScript**: JSON è nativamente supportato.
        - **Quando usare XML**
            - Se serve una rigorosa validazione tramite DTD/XSD o necessiti di un formato fortemente descrittivo.
            - Se hai bisogno di trasformazioni complesse (es. XSLT) o di protocolli storicamente basati su XML.
        - **Quando usare JSON**
            - Scambio di dati veloce e leggero in applicazioni web, soprattutto con JavaScript.
            - Quando la sintassi semplice e la leggibilità sono prioritarie su una validazione formale.
    
    ---
    
    ### **XML**
    
    | **Caratteristica** | **Descrizione** |
    | --- | --- |
    | **Tipo di formato** | Linguaggio a marcatori (metalinguaggio) basato su tag (apertura e chiusura). |
    | **Struttura** | Gerarchica ad albero, con un singolo elemento radice; tag annidati e attributi. |
    | **Prologo** | Contiene dichiarazioni e/o riferimenti a DTD/XSD (es. `<?xml version="1.0" encoding="UTF-8"?>`). |
    | **Case Sensitivity** | I tag sono *case sensitive* (es. `<Title>` diverso da `<title>`). |
    | **Validazione** | Può essere “ben formato” (se rispetta la sintassi) e/o “valido” (se rispetta un DTD o un XSD). |
    | **Formattazione** | Necessita di tag di apertura/chiusura coerenti, attributi tra apici, annidamento corretto. |
    | **Vantaggi** | Alto livello di descrittività, forte standardizzazione, valido per dati complessi. |
    | **Svantaggi** | Più verboso e ridondante rispetto a JSON, richiede un parser più “pesante”. |
    | **Uso tipico** | Configurazioni, protocolli standard (SOAP, RSS), ambienti in cui serve validazione forte (ad es. documenti strutturati a livello enterprise). |
    | **Esempio Semplice** | `xml<br><?xml version="1.0"?><br><note><br>  <to>Tove</to><br>  <from>Jani</from><br>  <message>Hello!</message><br></note>` |
    
    ### `JSON`
    
    | **Caratteristica** | **Descrizione** |
    | --- | --- |
    | **Tipo di formato** | Formato di testo basato su coppie chiave-valore e array, derivato dalla sintassi di JavaScript. |
    | **Struttura** | Utilizza parentesi graffe `{}` per gli oggetti e parentesi quadre `[]` per gli array. |
    | **Chiavi e Valori** | Le chiavi sono sempre stringhe (racchiuse in doppi apici), i valori possono essere stringhe, numeri, booleani, null, array o oggetti. |
    | **Case Sensitivity** | Le chiavi (stringhe) non subiscono differenze di interpretazione per il maiuscolo/minuscolo. Il testo interno però è considerato letterale (rispettando i caratteri). |
    | **Validazione** | Non c’è un meccanismo di validazione formale paragonabile a DTD/XSD, ma esistono strumenti che eseguono un controllo di conformità sintattica (JSON Schema). |
    | **Formattazione** | Niente tag di apertura/chiusura, si usano virgole e due punti per separare elementi e chiavi-valori. |
    | **Vantaggi** | Leggero, rapido da trasferire, immediatamente interpretabile in JavaScript (uso di `JSON.parse()`). |
    | **Svantaggi** | Meno adatto a dati estremamente complessi che richiedono validazione rigorosa o definizioni formali di struttura. |
    | **Uso tipico** | Trasferimento di dati tra server e client (soprattutto in applicazioni web SPA, RESTful API, microservizi). |
    | **Esempio Semplice** | `json<br>{"name": "John", "age": 30, "car": null}<br>` |
    
    ---
    
    **Conclusione**: Con questi punti fondamentali dovresti avere un’ottima base per comprendere e utilizzare sia XML che JSON. La scelta tra i due formati dipende dal contesto: se serve un elevato controllo formale e un modello di validazione rigoroso, XML è preferibile; se occorre un formato leggero e semplice da integrare (specie con JavaScript), JSON risulta la soluzione migliore.
    

---

**`6 - Progettazione Web Dinamico`**

- Concetto di API e servizi
    
    – Inizialmente il web era solo un archivio di documenti statici.
    
    – Evoluzione verso servizi complessi caratterizzati da:
    
    • Alta **modularità** – consente la composizione di servizi e la comunicazione tramite API
    
    • **Trasparenza** – le operazioni di basso livello (recupero informazioni, logica di funzionamento) non sono visibili all’utente
    
- Progettazione e Architettura del Web Server
    
    Il server risponde alle richieste degli utenti e si articola in due livelli principali:
    
    - **Frontend:** Il layer di presentazione.
    - **Backend:** Il layer che gestisce l’accesso ai dati.
    
    ![image.png](PROGRAMMAZIONE%20WEB%201af9a6c97cf98039a6e0cd1e9e9bb7af/image%2016.png)
    
    La comunicazione tra questi layer avviene tramite API, che fungono da interfacce specifiche. Inoltre, vengono illustrati diversi approcci per iniziare la progettazione di un web server:
    
    - **Top-down:** Partendo dall’interfaccia utente e procedendo verso le operazioni sui dati.
    - **Bottom-up:** Iniziare con i dati e arrivare all’interfaccia utente.
    - **Middle-out:** Focalizzarsi sulla logica di servizio, sviluppando sia verso l’alto che verso il basso.
    
    Un punto chiave è l’importanza di pianificare accuratamente prima di iniziare a scrivere codice: così come non si costruisce una casa senza un progetto, una solida progettazione evita riscritture e perdite di tempo, soprattutto in presenza di scadenze ristrette.
    
- api
    
    **🎯 Frase da ricordare per sempre:**
    
    > “Un’API è
    > 
    > 
    > **il modo in cui due software parlano tra loro**
    > 
    
    > È come un
    > 
    > 
    > **menù**
    > 
    > **cosa puoi chiedere**
    > 
    > **cosa otterrai**
    > 
    
    ---
    
    **🤓 Trucchetto per ricordarlo**
    
    **A**pplication
    
    **P**rogramming
    
    **I**nterface
    
    ✅ Interfaccia tra **te e un software**
    
    ✅ Usi comandi (endpoint) → ricevi dati (risposta)
    
- Descrizione Dei Servizi e delle Interazioni tramite API
    
    Prima di procedere con la scrittura del codice, è fondamentale definire cosa deve fare ogni servizio e come interagirà con gli altri. 
    
    Le API non sono elementi isolati ma fanno parte di un ecosistema in cui:
    
    - Ogni API stabilisce **il protocollo** (la struttura di controllo per la comunicazione) e **il formato** (la struttura del contenuto).
    - Le evoluzioni delle API includono vari paradigmi:
        - **RPC (Remote Procedure Calls):** Chiamate di funzioni in processi remoti.
        - **Messaging:** Invio di brevi messaggi o dati in pipeline, tipicamente a seguito di eventi.
        - **Publish-Subscribe:** Un modello in cui un componente (subscriber) si iscrive per ricevere aggiornamenti da un altro (publisher).
        - **Code (queues):** Gestione di richieste che richiedono tempi di elaborazione maggiori.
    
    In questo contesto, la documentazione delle API assume un ruolo cruciale: essa permette di definire chiaramente gli input e gli output attesi e facilita sia la manutenzione che la validazione delle modifiche apportate al sistema.
    
- Standard di documentazione delle API: **OPENAPI** e **SWAGGER**
    
    Per descrivere in maniera formale le API, vediamo lo standard: **OpenAPI**, una specifica dedicata alle API basate su HTTP (tipicamente RESTful). Le principali caratteristiche sono:
    
    - **Descrizione completa:** Il file OpenAPI definisce input, output, autorizzazioni e informazioni sul fornitore del servizio.
    - **Formati utilizzabili:** Le definizioni possono essere scritte in YAML o JSON; tuttavia, il formato YAML è preferito per la sua compattezza e semplicità (non richiede virgolette per le stringhe, supporta commenti, usa l’indentazione, ed è un superset del JSON).
    - **Strumenti di supporto:**
        - **Swagger:** Un servizio (e un editor online) che permette di visualizzare e validare facilmente le definizioni OpenAPI.
        - Link utili: [GitHub OpenAPI Specification](https://github.com/OAI/OpenAPI-Specification) e [Swagger Editor](https://editor.swagger.io/).
    
    Viene anche presentato un esempio di definizione OpenAPI in YAML, dove sono inclusi dettagli come title, version, server e definizione dei percorsi (paths) con le relative risposte.
    
- Architettura REST e Best Practices per le API
    
    Approfondiamo il concetto di REST (Representational State Transfer), illustrando i principi fondamentali che caratterizzano un sistema distribuito:
    
    - **Separazione Client-Server:** Chiarezza nei ruoli e nelle responsabilità.
    - **Stateless:** Ogni richiesta è indipendente.
    - **Cacheable:** Le risposte possono essere contrassegnate come riutilizzabili.
    - **Interfaccia uniforme:** Standardizzazione dell’interazione tra componenti.
    
    Le operazioni CRUD (Create, Read, Update, Delete) vengono mappate sui metodi HTTP (GET, POST, PUT/PATCH, DELETE) e vengono fornite alcune best practices, come l’utilizzo di nomi di risorse al plurale, strutture gerarchiche negli URL e versionamento dell’API. Queste regole rendono la documentazione più chiara e agevolano lo sviluppo di SDK e test automatizzati.
    
- **`Esempi`** Pratici con Python: **GET** e **POST**
    
     Il documento include esempi di codice Python per interagire con le API:
    
    - **Richieste GET:**
        
        Viene mostrato un esempio che utilizza la libreria `requests` per inviare una richiesta GET a un URL specifico, stampando lo status code e restituendo i dati in formato JSON.
        
    - **Gestione delle eccezioni:**
        
        Un esempio esteso include un blocco try/except per gestire gli errori senza esporre messaggi di errore troppo dettagliati, evitando così di dare informazioni utili a potenziali attacchi.
        
    - **Richieste POST:**
        
        Un ulteriore esempio riguarda l’API di traduzione “funtranslations” (in “pirate”), dove si invia una richiesta POST con un payload JSON. Anche qui viene gestito il controllo degli errori tramite try/except, e viene stampata la risposta ottenuta.
        

**🔹 Strumenti utili**

•	**Swagger Editor**: editor online per scrivere e testare definizioni OpenAPI

🔗 [https://editor.swagger.io](https://editor.swagger.io/)

•	**GitHub OpenAPI Spec**: documentazione ufficiale

🔗 [https://github.com/OAI/OpenAPI-Specification](https://github.com/OAI/OpenAPI-Specification)

- **Progettazione di un Servizio di Biblioteca**
    - Obiettivo del servizio
        - Ottenere la lista dei libri.
        - Ottenere i dettagli di un singolo libro.
        - Inserire una recensione per un libro scelto.
    - Progettazione UML
        - utente → get (/libri) → server
        
                           ← [ {libro}, … ]
        
        otteniamo una lista di libri. /libri è l’endpoint ovvero un **indirizzo specifico (URL)** che il tuo server espone per **ricevere richieste** e **restituire risposte**.
        
        Ogni libro è rappresentato da:
        
        - Un identificativo numerico (id).
        - Un titolo (stringa).
        - Un autore (stringa).
        - Una recensione (numero intero, da 1 a 5).
    
    ***ESERCIZIO NEL IPAD***
    
    - info
        - **Definizione del formato dei dati (Libro):**
            
            Viene mostrato uno schema in OpenAPI (in YAML) che definisce il tipo “Libro” con esempi e vincoli sui dati.
            
        - **Specifica delle API:**
            - **Lista dei libri (/books – GET):** Restituisce un array di libri; in caso di errore, restituisce un codice 500.
            - **Dettaglio di un libro (/books/{id} – GET):** Utilizza un path parameter “id” per identificare il libro; le possibili risposte sono 200 (successo), 404 (non trovato) e 500 (errore interno).
            - **Inserimento di una recensione (/books/{id}/recensione – POST):** Accetta un body contenente la recensione (con vincoli sul valore); le risposte possibili includono 200 (successo), 400 (richiesta non valida), 404 (libro non trovato) e 500 (errore interno).
        - **Caratteristiche dei metodi HTTP:**
            
            Viene ribadito come il metodo GET utilizzi parametri via URL (con limiti di lunghezza) mentre il metodo POST permetta l’invio di dati tramite il body, senza tali restrizioni e con la possibilità di cifratura.
            
    
- Validazione, Test e Generazione della Documentazione Automatizzata
    
     Una volta definite e implementate le API, è essenziale verificarne il comportamento attraverso test che controllino:
    
    - La corretta risposta in caso di successo.
    - La gestione appropriata degli errori (input non validi, numeri fuori range, ecc.).
    
    Inoltre, viene spiegato come, utilizzando FastAPI in combinazione con Pydantic (e il suo supporto al typing esplicito in Python), sia possibile generare automaticamente la documentazione delle API a partire dal codice stesso. Questo approccio “code-first” garantisce:
    
    - Maggiore velocità di sviluppo.
    - Consistenza e modularità dell’intero servizio.
    - Un ambiente di sviluppo migliorato grazie all’autocompletamento offerto dagli IDE.
- OpenAPI
    
    **OpenAPI è una specifica formale per descrivere API basate su HTTP, usando il formato JSON o YAML**
    
    - Una descrizione formale può essere più facilmente interpretata da un software, mentre una informale no
    - Cosa significa in pratica?
        - Per esempio, si può generare del codice già “pronto” con tutte le interfacce specificate (mock server)
        - Anche scrivere i test diventa più facile perché si conosce il formato della risposta
- **Esercizi** di progettazione
    
    **Nel corso useremo FastAPI, che consente il passaggio inverso: si inizia a scrivere il codice e la documentazione sarà generata (e aggiornata) automaticamente**
    
    - Forte utilizzo del typing esplicito in Python (tramite la libreria Pydantic, [https://docs.pydantic.dev/latest/](https://docs.pydantic.dev/latest/))
    - Gestione facilitata data dall’autocompletamento dell’IDE
    - Questo non significa che le API non vadano comunque progettate!
    
    **Una volta implementate le nostre API, dovremo fare dei test per verificare che si comportino come pianificato in fase di progettazione**
    
    - risposta corretta in caso di successo
    - risposta corretta in caso di errori
    - per esempio, cosa potrebbe generare errori nella specifica appena definita?
    
    Esempi di valori da testare sul campo `recensione` (integer, min 1, max 5):
    
    - numero negativo
    - numero non intero
    - numero troppo grande
    - stringa (“Good book.”)
- Modularità dei servizi
    
    ### Componenti di un servizio web
    
    Divideremo concettualmente gli elementi che compongono un sito isolando tre strati (layers)
    
    - **Livello web**
    - **Livello della logica di servizio**
    - **Livello dei dati**
        
        E aggiungeremo i componenti aggiuntivi
        
    - Modelli e definizioni dei dati (sarà oggetto di lezioni successive)
    - Test (sarà oggetto di lezioni successive)
- Livello Web
    
    Il livello concettualmente più alto, quello del Web, fa da interfaccia tra l’utente e i livelli di servizio e di dati
    
    - Definisce cosa l’utente può fare, di solito in termini di operazioni CRUD (Create, Read, Update, Delete)
    - Spesso prevede un’interfaccia utente interattiva
    - L’utente comunica con il web layer tramite applicazioni dedicate (client) o API (nei casi di utenti più esperti)
    
    Il livello di servizio contiene quella che viene chiamata anche business logic, ovvero tutti i dettagli di ciò che il servizio web fornisce agli utenti
    
    - Controlla come gli utenti possono accedere ai dati, contenuti e gestiti nel layer sottostante
    - Comprende per esempio autenticazione (chi accede) e autorizzazione (con quali livelli di accesso)
- Livello dei dati
    
    Il livello dei dati fornisce al service layer accesso ai dati, attraverso file o funzioni di accesso e modifica di altri servizi che forniscono accesso ai dati (es. servizi di database)
    
    - Spesso i servizi web gestiscono operazioni di basso livello su database e in generale su risorse (file, hardware, …)
- Esempio di gestione di una richiesta
    1. L’utente richiede la lista di libri tramite il livello Web (browser o applicazioni specifiche)
    2. Il service layer processa i dati richiesti
    3. Il data layer recupera i dati richiesti
    4. Il service layer prepara i dati per l’utente
    5. Il web layer mostra i dati all’utente
    
    Fino al service layer in genere e python mentre il web layer è html…
    
    ![image.png](PROGRAMMAZIONE%20WEB%201af9a6c97cf98039a6e0cd1e9e9bb7af/image%2017.png)
    
    ---
    
    ### Vantaggi della struttura a strati (modularità)
    
    - ogni layer può essere progettato da specialisti diversi, Modularità significa anche dividere i compiti.
    - si possono eseguire test in isolamento
    - si possono integrare nuovi servizi e rimpiazzare servizi esistenti senza compromettere il resto dello stack, purché si rispettino le interfacce
    - la separazione va imposta all’inizio, altrimenti diventa molto difficile districare i vari aspetti dopo che il codice è stato scritto
- Architetture monolitiche vs. architetture a microservizi
    
    ### Architetture a microservizi
    
    I microservizi sono servizi indipendenti (micro perchè ognuno viene usato per una funzione specifica), autonomi e compatti, che collaborano
    
    - sono applicazioni che girano in modo indipendente
    - comunicano tramite API
    - “compatti” non significa necessariamente “piccoli”, ma applicazioni con uno scopo preciso e verticale
    - principio di Single Responsibility: un servizio fa bene un solo compito
    - esempi: invio mail, pagamenti, trasferimento file
    
    **Vantaggi:**
    
    - possono essere distribuiti su più macchine
    - isolamento per prevenire guasti all’intero sistema
    - spesso gestiti da team dedicati
    - parallelizzabili
    - test individuali facilitati
    
    **Svantaggi:**
    
    - interazione di servizi potenzialmente disomogenei
    - architettura complessa
    - approccio più costoso
    - maggior rischio di sicurezza (servizi meno protetti)
    - test di integrazione più complicati
    
    ---
    
    ### Architetture monolitiche
    
    Nelle architetture monolitiche tutte le funzionalità sono sviluppate e distribuite come un unico blocco
    
    - il controllo e la gestione sono centralizzati
    
    **Vantaggi:**
    
    - più facile coordinare gli elementi
    - più facile accesso ai dati da diverse parti dell’applicazione
    - talvolta più semplice da debuggare
    - test end-to-end più semplici
    
    **Svantaggi:**
    
    - con progetti grandi diventano difficili da gestire
    - sostituire componenti accoppiati è complesso
    - test di singoli servizi isolati sono complicati
    
    ---
    
    ### Quindi, quale scegliere?
    
    In generale la scelta dipende dal framework e dai requisiti del progetto:
    
    - molti framework (es. Django) sono pensati per applicazioni monolitiche
    - spesso si adotta un approccio ibrido: alcuni servizi come microservizi, altri integrati nel monolite
- Docker
    
    I docker oermettono di creare delle istanze isolate in cui faccio girare i miei servizi (microservizi, sistemi operativi ecc).
    
    Sono vantaggiosi perchè girando in dei cointeiner rende il tutto più sicuro perchè non c’è l’accesso diretto con il sistema operativo su cui gira la macchina. I diversi microservizi nei diversi cointeiner possono comunicare facilmente tra loro. 
    

---

**`7 - Processi Asincroni e Parallelismo`** 

- Processi Asincroni e Parallelismo
    
    Oltre all’evoluzione delle comunicazioni e dei software dei web server, c’è stato un grosso cambiamento anche nel numero di connessioni ricevute dai web server.
    
    Quando il server deve gestire connessioni multiple, due metriche fondamentali sono:
    
    - **Latenza**: tempo totale di attesa tra richiesta e risposta.
    - **Throughput**: quanti byte al secondo sono trasmessi.
    
    Per limitare ritardi dovuti a “busy waiting” (periodi in cui il server non accetta nuove richieste perché è impegnato su altre), si adottano tecniche di esecuzione non bloccante. 
    
- Gestione di utenti multipli e concorrenza
    
    ### Esecuzione sincrona vs asincrona in Python
    
    - **Sincrona**: i comandi vengono eseguiti in ordine; il comando successivo non inizia finché il precedente non è terminato. Questo è un modello **bloccante**.
    - **Asincrona**: le richieste vengono accettate immediatamente, processate con priorità minore (ad es. I/O su disco non blocca la CPU), e la risposta è inviata quando l’elaborazione è completata.
    
    ### Quando usare l’asincrono
    
    - Operazioni I/O-intensive (database, file system)
    - Chiamate a API esterne (HTTP)
    - Elaborazioni in background (report, email, immagini)
    - Streaming dati (WebSocket per aggiornamenti real-time)
- Esempi di utilizzo dei processi asincroni
    
    Per non reinventare la gestione della concorrenza da zero, si usano **framework** che offrono:
    
    - Performance ottimizzate (codice compilato)
    - Sviluppo più rapido (riuso di componenti)
    - Codice di qualità e meno bug
    - Astrazione di basso livello (es. gestione I/O asincrono)
- L’utilizzo di framework e modelli di programmazione
    
    ### Callback
    
    - Funzioni invocate al completamento di un’operazione.
    - Possono generare “callback hell” se annidate profondamente.
    
    ### Promises e Async/Await
    
    - **Promise**: rappresenta un’operazione asincrona pendente/completata/fallita.
    - **Async/Await**: sintassi che rende il codice asincrono simile al sincrono, migliorandone la leggibilità. Async: fai qualcosa, Await: finchè non fai qualcosa aspetta
    
    ### Code e task scheduling
    
    - Strumenti come Celery (Python), Sidekiq (Ruby), Bull (Node.js) gestiscono job in background.
    
    ### Event-Driven e WebSocket
    
    - WebSocket abilita comunicazione bidirezionale persistente tra client e server.
    - I modelli event-driven (es. Node.js) usano un event loop per gestire richieste asincrone.
- Interfaccia Gateway tra web server e applicazione
    
    Un’**Interfaccia Gateway** separa il web server dal framework applicativo e gestisce:
    
    - Traduzione di protocolli
    - Routing delle richieste
    - Sicurezza e autenticazione
    - Bilanciamento del carico
    
    Cambiare framework non richiede modifiche all’applicazione esposta agli utenti. 
    
- WSGI: Web Server Gateway Interface
    
    ### Caratteristiche
    
    - Standard di interfaccia tra web server e framework Python (Flask, Django).
    - Supporta modalità sincrona e, in parte, asincrona.
    
    ### Limitazioni
    
    - Gestione sequenziale delle richieste → performance ridotte sotto alto carico.
- ASGI: Asynchronous Server Gateway Interface
    
    ### Caratteristiche
    
    - Evoluzione di WSGI per applicazioni asincrone.
    - Supporto nativo a async/await.
    - Concorrenza efficiente per I/O-intensive e WebSocket.
    - Scalabilità e migliori performance in ambienti ad alto carico.
    
    ### Framework compatibili
    
    - FastAPI, Starlette
- Parallelismo, concorrenza e supporto asincrono
    - **Parallelismo**: esecuzione di sotto-task su più CPU simultaneamente.
    - **Concorrenza**: alternanza di più task su una o più CPU per minimizzare i tempi di attesa.
    - Applicazioni web beneficiano di entrambi per gestire task lunghi e numerosi utenti.
- Calcolo parallelo e distribuito
    - Task suddivisi in sotto-task su più CPU (parallelo) o su più macchine (distribuito).
    - Ottimizza tempi di elaborazione evitando colli di bottiglia.
- Processi e thread nel sistema operativo
    
    ### Processi
    
    - Istanza di un programma con memoria separata.
    - Forte isolamento, overhead di creazione elevato, IPC complessa.
    
    ### Thread
    
    - Unità di esecuzione all’interno di un processo.
    - Condividono memoria e risorse, comunicazione più rapida, creazione leggera.
- Esempio di codice asincrono in Python
    
    ```python
    import asyncio, random
    
    async def tell_joke_part(i):
        parts = ["Why","did","the","chicken","cross","the","road"]
        await asyncio.sleep(random.random())
        print(parts[i])
        return parts[i]
    
    async def main():
        jokes = [tell_joke_part(i) for i in range(7)]
        results = await asyncio.gather(*jokes)
        print("Async Joke:", ' '.join(results))
    
    await main()
    
    ```
    
    - `async def` definisce coroutine non bloccanti.
    - `await` sospende fino al completamento.
    - In un notebook Colab (ambiente async) si usa `await main()`, altrimenti `asyncio.run(main())`.
- Web server multithread vs asincrono
    - **Multithread**: ogni richiesta HTTP in un thread separato → alta concorrenza I/O, scalabilità orizzontale.
    - **WSGI**: thread sincroni sequenziali.
    - **ASGI**: thread asincroni non bloccanti.
    - Nota: async/await non rende il codice più veloce di per sé, ma evita blocchi durante l’I/O.
- AJAX (Asynchronous JavaScript And XML)
    
    ### Definizione
    
    AJAX permette di aggiornare porzioni di pagina in modo asincrono, senza ricaricare l’intera pagina.
    
    - Combina XMLHttpRequest (o Fetch) e JavaScript/HTML.
    - Non è limitato a XML: supporta JSON, testo semplice, ecc.
    
    ### Flusso di funzionamento
    
    1. Evento utente (click).
    2. JavaScript crea e invia la richiesta al server.
    3. Server risponde.
    4. JavaScript legge la risposta e aggiorna il DOM. 
- **`RIASSUNTO SPIEGAZIONE`**
    
    ---
    
    ## 1. Fondamenti di Concorrenza, Asincronia e Parallelismo
    
    Quando un web-server deve servire migliaia di client contemporaneamente, due metriche diventano critiche: **latenza** (il tempo che intercorre fra la richiesta di un client e la risposta del server) e **throughput** (la quantità di dati — byte al secondo — che il server riesce a inviare complessivamente). In un modello tradizionale sincrono, ogni operazione di I/O (lettura da file, accesso a database, comunicazione di rete) blocca il thread finché non termina: durante quell’attesa la CPU resta inutilizzata (“busy waiting”), e la latenza aumenta.
    
    Per sfruttare al meglio la CPU e ridurre i tempi morti, si impiegano tecniche di:
    
    - **I/O non-bloccante**: il thread avvia l’operazione di I/O e immediatamente torna a servire altre richieste; quando l’I/O è pronto, un meccanismo di notifica (callback o ripresa di una coroutine) completa l’elaborazione.
    - **Concorrenza cooperativa**: più task si alternano sullo stesso thread in momenti in cui ognuno è in attesa di I/O, coordinati da un event loop.
    - **Threading**: ogni richiesta gira in un thread separato; se un thread va in attesa I/O, gli altri continuano a lavorare.
    - **Parallelismo**: per compiti CPU-intensivi, si lanciano più processi (o thread in ambienti senza GIL) su core differenti, eseguendo calcoli in vero simultaneo.
    
    In pratica, le applicazioni web miste sfruttano I/O-non-bloccante per tutte le operazioni di rete e database, e ricorrono a pool di processi o micro-servizi separati per i calcoli pesanti.
    
    ---
    
    ## 2. Modelli di Programmazione Asincrona in Python
    
    Python mette a disposizione il modulo `asyncio` per scrivere codice non-bloccante basato su coroutine. Le parole chiave sono `async def` (definisce una coroutine) e `await` (sospende la coroutine finché l’operazione I/O innestata non completa, ma senza bloccare l’intero thread).
    
    ```python
    import asyncio, random
    
    async def tell_joke_part(i):
        parts = ["Why","did","the","chicken","cross","the","road?"]
        await asyncio.sleep(random.random())     # simula I/O non-bloccante
        print(parts[i])
        return parts[i]
    
    async def main():
        # lancio 7 coroutine in concorrenza
        jokes = [tell_joke_part(i) for i in range(7)]
        results = await asyncio.gather(*jokes)  # attende tutte
        print("Async Joke:", ' '.join(results))
    
    asyncio.run(main())
    
    ```
    
    Quando usare `asyncio`:
    
    - Operazioni I/O-intensive: chiamate HTTP, accesso database, lettura/scrittura file.
    - WebSocket e streaming: aggiornamenti in tempo reale.
    - Task di background leggeri (inviare email, generare report).
    
    Per operazioni compute-bound (codice che satura la CPU), invece, è preferibile il module `multiprocessing` o un cluster di worker: l’`asyncio` da solo non sfrutta più core per calcoli numerici.
    
    - ALTRO ESEMPIO
        
        ```python
        import asyncio
        
        async def say_after(delay, msg):
            await asyncio.sleep(delay)      # simula I/O: non blocca il programma
            print(msg)
        
        async def main():
            # creo due attività che possono correre insieme
            task1 = say_after(1, "Ciao")
            task2 = say_after(2, "Mondo")
            # gather aspetta che entrambe finiscano
            await asyncio.gather(task1, task2)
        
        asyncio.run(main())
        ```
        
        - `say_after` aspetta senza bloccare;
        - `gather` lancia le due coroutine insieme;
        - risultato in console dopo 1s “Ciao”, dopo 2s “Mondo”.
    
    ---
    
    ## 3. Gateway e Interfacce fra Web-Server e Applicazione
    
    Per separare la logica dell’applicazione dal web-server front-end (Nginx, Apache, Caddy), si inserisce un layer gateway che:
    
    1. Traduce il protocollo HTTP/HTTPS in chiamate interne all’app (e viceversa).
    2. Esegue il routing delle richieste verso istanze multiple dell’applicazione.
    3. Gestisce SSL/TLS termination, autenticazione, limiti di rate.
    4. Bilancia il carico e permette di cambiare framework senza toccare l’interfaccia esposta.
    
    In Python esistono due standard principali:
    
    - **WSGI** (Web Server Gateway Interface): nato per applicazioni sincrone (Django, Flask). Ogni richiesta viene mappata a una chiamata di funzione che restituisce la risposta. Semplice ma, sotto carico elevato di I/O, rischia di creare thread bloccati e colli di bottiglia.
    - **ASGI** (Asynchronous Server Gateway Interface): estende WSGI con supporto nativo a `async`/`await` e protocolli WebSocket. Un server ASGI (uvicorn, daphne) mantiene un event loop e gestisce migliaia di connessioni non-bloccanti, ideale per app real-time e API I/O-bound (FastAPI, Starlette, Django Channels).
    
    ---
    
    ## 4. Strumenti e Architetture di Concorrenza
    
    In un progetto Python multi-tenant si combinano spesso:
    
    1. **asyncio** per l’I/O non-bloccante nel singolo processo.
    2. **ThreadPoolExecutor** per operazioni di libreria bloccanti che non supportano async.
    3. **ProcessPoolExecutor** o **multiprocessing** per sfruttare più core in task CPU-intensive.
    4. **Celery** (o RQ) per distribuire job su più worker, orchestrati via broker (Redis, RabbitMQ). Utile per attività in background (invio email, elaborazioni batch).
    5. **Load-balancer** esterno (Nginx, AWS ELB) per distribuire traffico su più istanze del server ASGI/WSGI.
    
    Questa architettura ibrida copre qualsiasi tipo di carico: I/O sporco, elaborazioni lunghe, comunicazioni in tempo reale.
    
    ---
    
    ## 5. Interazione Client-Server: AJAX e WebSocket
    
    - **AJAX** (Asynchronous JavaScript and XML): tecnica lato browser per inviare richieste HTTP (Fetch API o XMLHttpRequest) e aggiornare porzioni di pagina senza reload completo. Flusso: evento utente → invio richiesta → risposta JSON/testo → modifica DOM.
    - **WebSocket**: canale TCP full-duplex mantenuto aperto tra client e server. Permette di pushare dati in tempo reale (chat, dashboard). Un server ASGI può gestire WebSocket nativamente, integrando la logica di evento nel medesimo event loop delle API HTTP.
    
    ---
    
    Con queste quattro sezioni hai un percorso narrativo completo:
    
    1. **Perché** serve l’asincronia,
    2. **Come** si programma in Python,
    3. **Dove** si colloca il gateway tra web-server e app,
    4. **Quali** strumenti usare in produzione,
    5. **Come** interagisce il browser (AJAX/WebSocket).
    
    Ogni punto include esempi concreti e consigli pratici per i tuoi appunti su Notion.
    

---

**`8 - Autenticazione e Autorizzazione`** 

- Introduzione
    
    Quando progettiamo un servizio web, uno degli obiettivi fondamentali è proteggere le informazioni e le funzionalità da accessi non desiderati. Per farlo, interveniamo su due livelli:
    
    1. **Autenticazione**: ci assicuriamo che chi si collega sia davvero chi afferma di essere.
    2. **Autorizzazione**: una volta verificata l’identità, definiamo con precisione quali azioni quell’utente può compiere e quali risorse può vedere.
    
    Solo combinando correttamente questi due meccanismi possiamo garantire che dati sensibili rimangano protetti e che ogni utente operi entro i limiti consentiti .
    
- **Autenticazione**
    
    Immagina la porta di un edificio: prima di entrare, devi mostrare un documento d’identità. Analogamente, nei sistemi web l’autenticazione è il processo che verifica la tua identità. Esistono diversi modi per farlo:
    
    - **Credenziali (username + password)**: il metodo più diffuso, ma soggetto a rischi come attacchi “brute‑force” o phishing.
    - **Multi‑Factor Authentication (MFA)**: richiede almeno due prove di identità, ad esempio la password più un codice temporaneo (OTP).
    - **Token**: dopo il login, il server ti consegna un “gettone” digitale (sessione o JWT) che mostri a ogni richiesta successiva. è una stringa molto lunga che mi permette di accedere al servizio, è diversa ad una password perchè posso revocarla quando voglio
    - **Federata (OAuth 2.0 / OpenID Connect)**: ti affidi a un provider esterno (Google, Facebook…) per autenticarti, senza creare un account dedicato sul servizio. è il servizio che garantisce che l’utente è quello lì
- Flusso tipico dell’autenticazione
    
    Il processo di base è sempre questo:
    
    1. L’utente inserisce le proprie credenziali (ad esempio username e password).
    2. Il sistema confronta queste credenziali con quelle memorizzate: se combaciano, prosegue; altrimenti rifiuta l’accesso.
    3. Quando la verifica ha successo, il server crea un **token** (o apre una **sessione**) e lo invia al client.
    4. Il client include quel token in ogni richiesta successiva: il server, vedendo un token valido, riconosce l’utente senza chiedere di rifare il login .
    
    Questo approccio rende l’esperienza più fluida: non devi reinserire username e password a ogni azione.
    
- Autenticazione basata su credenziali
    
    Nel dettaglio:
    
    - **Username e password** rimangono il metodo più comune.
    - **Rischi**: attacchi automatici che provano migliaia di combinazioni (“brute‑force”) o tentativi di inganno (“phishing”) ovvero chiedo infromazioni all’utente e riesco a capire qualche possibile risultato.
    - **Contromisure**:
        - **Hashing sicuro** delle password (con algoritmi come bcrypt o Argon2) e uso di **salt** unici per ciascun utente, in modo che anche password identiche appaiano diverse nel database.
        - **Policy di complessità**: lunghezza minima, mix di lettere, numeri e simboli obbligatori per rendere la password più difficile da indovinare .
- Multi‑Factor Authentication (MFA)
    
    Per aumentare la sicurezza, puoi combinare due (o più) dei seguenti fattori:
    
    1. **Qualcosa che sai**: password o PIN.
    2. **Qualcosa che hai**: un codice temporaneo (OTP) inviato via SMS, email, o generato da un’app (es. Google Authenticator).
    3. **Qualcosa che sei**: un elemento biometrico, come l’impronta digitale o il riconoscimento facciale.
    
    Ad esempio, nella **2‑factor authentication (2FA)** inserisci la password (fattore 1) e poi un codice OTP (fattore 2). Anche se un malintenzionato scopre la tua password, senza il secondo fattore non potrà entrare .
    
- Autenticazione basata su token
    
    Dopo aver fatto il login, il server ti affida un token che dimostra la tua identità:
    
    - **Session Token**: memorizzato dal browser in un cookie o in localStorage; il server ne conserva traccia in memoria o nel database, fino a fine della sua scadenza o fino a quando il token non viene disabilitato.
    - **JSON Web Token (JWT)**: un “gettone” autosufficiente, firmato digitalmente. Contiene un piccolo pacchetto di dati (payload) con informazioni sull’utente e sui suoi permessi. Poiché è firmato, il server non ha bisogno di mantenere uno stato: basta verificare la firma del token per accettarlo.
    
    **Pro**: grande scalabilità, perfetto per API RESTful.
    
    **Contro**: se memorizzato in modo insicuro (es. localStorage senza protezioni) può essere rubato via attacchi XSS .
    
- Autenticazione federata
    
    Invece di creare un nuovo account, puoi usare credenziali di terze parti:
    
    - **OAuth 2.0 / OpenID Connect**: ti reindirizzano a un provider (Google, Facebook, Microsoft). Se l’autenticazione ha successo, il provider restituisce al tuo servizio un “certificato” di identità. Usiamo questi provider perchè hanno un ottimo sistema di sicurezza.
    - **Single Sign‑On (SSO)**: con un unico login accedi a più applicazioni senza dover ripetere il processo.
    
    Questo rende più semplice la gestione delle password e migliora l’esperienza utente, ma svantaggi emergono se l’account esterno viene compromesso: l’attaccante avrebbe accesso a tutti i servizi collegati .
    
- **Autorizzazione**
    
    Una volta che sappiamo chi sei, dobbiamo stabilire **cosa** puoi fare. L’autorizzazione è il filtro che decide, per ciascuna risorsa (pagina, dato, funzione), se mostrartela o meno. Esistono tre modelli fondamentali:
    
    1. **Role‑Based Access Control (RBAC)**: ogni utente appartiene a uno o più ruoli (es. “amministratore”, “moderatore”, “utente standard”); i ruoli hanno permessi predefiniti.
    2. **Attribute‑Based Access Control (ABAC)**: si definiscono regole più articolate basate su attributi dell’utente (età, reparto), della risorsa (sensibilità) e del contesto (orario, dispositivo).
    3. **Access Control List (ACL)**: per ciascuna risorsa si mantiene una lista di coppie `<soggetto, permesso>`, che indica esattamente chi può fare cosa .
- Esempio di flusso di autorizzazione
    
    Il passo‑passo è:
    
    1. Un utente già autenticato invia una richiesta per una risorsa protetta.
    2. Il sistema esamina il token o la sessione, estrae ruoli o attributi.
    3. Confronta queste informazioni con le regole di autorizzazione:
        - Se c’è corrispondenza, **accesso consentito**.
        - Altrimenti, **accesso negato**.
    
    Questo controllo avviene in ogni punto in cui servono permessi speciali .
    
- Role‑Based Access Control (RBAC)
    
    In RBAC:
    
    - **Definiamo ruoli**: ad esempio “amministratore” ha tutti i permessi, “utente” ne ha di base.
    - **Assegniamo utenti ai ruoli**: Maria è “moderatore”, Luca è “utente”.
    - Quando Luca tenta un’azione, il sistema guarda i permessi del ruolo “utente” e decide.
    
    RBAC è semplice da capire e gestire centralmente, ma può risultare rigido se serve concedere permessi temporanei o molto specifici a un singolo utente .
    
- Attribute‑Based Access Control (ABAC)
    
    ABAC estende l’idea di RBAC aggiungendo:
    
    - **Attributi utente**: reparto, livello di anzianità, localizzazione geografica.
    - **Attributi risorsa**: classificazione (pubblica, confidenziale).
    - **Attributi contesto**: orario di accesso, tipo di dispositivo.
    
    Le regole possono essere formule complesse (es. “solo i manager del reparto vendite possono modificare i dati clienti tra le 9:00 e le 17:00, e solo dalla rete interna”). ABAC è molto flessibile, ma richiede un motore di policy più sofisticato e una definizione accurata degli attributi .
    
- Access Control List (ACL)
    
    Con le ACL:
    
    - Ogni risorsa porta con sé una lista di voci del tipo `<utente o gruppo, permesso>`.
    - Quando arriva una richiesta, il sistema scorre la lista per trovare il soggetto e verifica se il permesso richiesto è presente.
    
    Questo modello offre il massimo dettaglio (posso gestire caso per caso), ma se il sistema ha migliaia di risorse e utenti diventa complesso da amministrare .
    
- Sicurezza e best practice
    
    Per rendere davvero efficace il sistema di autenticazione e autorizzazione, è buona norma:
    
    - **Proteggere le credenziali**: password hashed + salted, policy di complessità.
    - **Usare HTTPS** su tutte le comunicazioni per evitare intercettazioni.
    - **Limitare la durata delle sessioni**: timeout automatico dopo inattività.
    - **Applicare il principio del minimo privilegio**: ogni utente ha solo i permessi strettamente necessari.
    - **Tenere log e audit trail**: registrare chi fa cosa e quando, per poter risalire a eventuali abusi.
    - **Revisioni periodiche**: verificare regolarmente che ex‑dipendenti o ruoli modificati non mantengano accessi non più giustificati.
    
    Così costruisci un’architettura solida, in cui ogni livello di difesa rinforza gli altri, rendendo molto più difficile un’intrusione non autorizzata .
    

---

**`9 - Database CRUD`**

- Cos’è una base di dati
    
    Una **base di dati** è una collezione strutturata di informazioni correlate, pensata per rappresentare una certa realtà (per esempio, gli acquisti degli utenti di un negozio online). La sua complessità cresce con il numero di entità (utenti, prodotti, ordini) e con la ricchezza delle relazioni fra esse.
    
- Il ruolo del DBMS
    
    Per gestire in modo affidabile grandi quantità di dati si utilizza un **DataBase Management System (DBMS)**, ovvero un insieme di programmi che:
    
    - Garantisce la **riservatezza** e l’**integrità** dei dati, anche in caso di guasti hardware o software.
    - Offre **manutenibilità**, permettendo di evolvere la struttura dati senza interrompere il servizio.
    - Gestisce la **concorrenza**, coordinando più utenti che leggono o scrivono contemporaneamente.
    
    All’interno del DBMS esiste un **catalogo** di metadati, cioè la descrizione logica di tabelle, colonne e vincoli: le applicazioni non devono sapere dove e come i dati sono fisicamente memorizzati, ma solo cosa rappresentano.
    
    In breve, **il catalogo è la memoria strutturale del database**: senza di esso, il DBMS non saprebbe né come sono fatte le tabelle né come applicare le regole per mantenerne la coerenza.
    
- Basi di dati relazionali
    
    Le basi di dati relazionali organizzano i dati in **tabelle** (o relazioni), ciascuna costituita da:
    
    - **Righe (tuple)**: un’istanza dell’entità (es. un singolo utente).
    - **Colonne (attributi)**: le proprietà di quell’entità (es. nome, email).
    - **Chiave primaria (Primary Key)**: un attributo (o un insieme) che identifica univocamente ogni riga.
    - **Chiave esterna (Foreign Key)**: un attributo che crea un legame logico con un’altra tabella.
    
    **Esempio**: una tabella `cities` con colonne `(cityname, ZIP, REGION, country)`, dove `cityname` è la primary key.
    
- Viste
    
    Una **vista** è una tabella virtuale: non contiene dati fisicamente, ma mostra un sottoinsieme (o una trasformazione) dei dati esistenti.
    
    Per esempio, la vista “studenti di matematica” elenca solo i nomi degli studenti iscritti a quel corso, senza duplicare i dati originali. Puoi avere viste diverse per utenti o applicazioni diverse.
    
- SQL: il linguaggio per interagire
    
    **SQL (Structured Query Language)** è il linguaggio standard per:
    
    - **DDL (Data Definition Language)**: definire strutture (CREATE TABLE, DROP TABLE).
    - **DML (Data Manipulation Language)**: inserire, leggere, aggiornare, cancellare dati (INSERT, SELECT, UPDATE, DELETE).
    
    È dichiarativo: dichiari **cosa** vuoi ottenere, non **come** ottenerlo.
    
- Lettura dei dati: **SELECT** e **WHERE**
    - **SELECT** recupera righe da una tabella.
        
        ```sql
        SELECT * FROM cities;
        ```
        
        L’asterisco `*` significa “tutte le colonne”.
        
    - **WHERE** filtra le righe in base a condizioni su colonne, usando operatori (`=`, `<`, `>`, `<>`, `BETWEEN`, `IN`, `LIKE`, `AND`, `OR`).
        
        ```sql
        SELECT * FROM cities WHERE country = 'Italy';
        ``` :contentReference[oaicite:14]{index=14}:contentReference[oaicite:15]{index=15}
        ```
        
- Unire tabelle: **JOIN**
    
    Una **JOIN** combina righe di due tabelle.
    
    - Senza condizioni, produce il **prodotto cartesiano**: ogni riga della tabella A accoppiata con ogni riga della tabella B.
    - Di solito si usa con **ON** per specificare il criterio di unione (es. chiave esterna = chiave primaria), e poi eventualmente un ulteriore **WHERE**.
        
        ```sql
        SELECT *
          FROM students
          JOIN grades
            ON students.id = grades.student_id;
        ``` :contentReference[oaicite:16]{index=16}:contentReference[oaicite:17]{index=17}
        ```
        
- Creare database e tabelle
    
    Per iniziare un nuovo database si usa:
    
    ```sql
    CREATE DATABASE world;
    ```
    
    Per creare una tabella occorre elencare tutte le colonne con i loro tipi e specificare la primary key:
    
    ```sql
    CREATE TABLE cities (
      cityname VARCHAR(30) NOT NULL PRIMARY KEY,
      ZIP INTEGER,
      REGION VARCHAR(30),
      country VARCHAR(30)
    );
    ```
    
- Inserire dati: **INSERT** e **REPLACE**
    - **INSERT** aggiunge una nuova riga; i valori devono seguire l’ordine delle colonne:
        
        ```python
         INSERT INTO cities VALUES ('Cagliari', 09100, 'Sardinia', 'Italy');
        ```
        
    - **REPLACE** funziona come INSERT, ma se esiste già una riga con la stessa chiave primaria la sovrascrive:
        
        ```sql
        REPLACE INTO cities VALUES ('Cagliari', 09100, 'Veneto', 'Italy');
        ```
        
- Aggiornare dati: UPDATE
    
    Per modificare valori in righe esistenti:
    
    ```sql
    UPDATE cities
    SET country = 'Switzerland'
    WHERE region = 'Sardinia';
    ```
    
    **Attenzione**: senza il `WHERE` aggiorni **tutte** le righe della tabella.
    
- Cancellare dati: DELETE
    
    Per eliminare righe:
    
    ```sql
    DELETE FROM cities
    WHERE cityname = 'Milano';
    ```
    
    Anche qui, omettere `WHERE` significa cancellare **tutte** le righe.
    
- Le operazioni CRUD
    
    Le quattro operazioni fondamentali su una tabella sono:
    
    | Operazione | SQL | Significato |
    | --- | --- | --- |
    | Create | INSERT | Creare nuove righe |
    | Read | SELECT | Leggere righe |
    | Update | UPDATE | Modificare righe |
    | Delete | DELETE | Cancellare righe |
    
    Concetti chiave:
    
    - Non puoi leggere, aggiornare o cancellare qualcosa che non esiste: prima lo **crei**, poi lo **leggi**, poi lo **modifichi** o **elimini**.
- Interazione applicativa
    
    Le applicazioni integrano query SQL tramite librerie di connessione (driver). Il flusso tipico:
    
    1. Apri connessione al DBMS.
    2. Invia query (SELECT, INSERT, …).
    3. Ricevi risultati o conferma di scrittura.
    4. Chiudi (o riutilizzi) la connessione.
- Cenni sui database NoSQL
    
    Quando i dati sono non strutturati o mutano spesso, si usano database “Not Only SQL”:
    
    1. **Document Store** (MongoDB, CouchDB): archivia documenti JSON/BSON, struttura flessibile.
    2. **Key‑Value Store** (Redis, DynamoDB): coppie chiave‑valore, massima velocità.
    3. **Column‑Family Store** (Cassandra, HBase): dati organizzati per colonne, ottimo per grandi volumi.
    4. **Graph Database** (Neo4j): nodi e relazioni, ideale per reti sociali e raccomandazioni.
    
    Caratteristiche NoSQL: schema‑less, scalabilità orizzontale, alta disponibilità, performance su accessi massivi. Si scelgono quando serve flessibilità o si gestiscono Big Data in tempo reale.
    
- Quando usare: DB Relazionali e DB NON Relazionali
    
    ![image.png](PROGRAMMAZIONE%20WEB%201af9a6c97cf98039a6e0cd1e9e9bb7af/image%2018.png)
    
- 📚 **Esercizi Base** su SQL
    
    Qualche esercizio su SQL
    
    - [https://sqlzoo.net/wiki/SELECT_basics](https://sqlzoo.net/wiki/SELECT_basics)
    - [https://sqlzoo.net/wiki/SELECT_](https://sqlzoo.net/wiki/SELECT_).._JOIN
    - [https://sqlzoo.net/wiki/CREATE_TABLE](https://sqlzoo.net/wiki/CREATE_TABLE)
    - [https://sqlzoo.net/wiki/INSERT_](https://sqlzoo.net/wiki/INSERT_).._VALUES
- 📚 **Esercizi Base** con **Redis (NoSQL)**
    - 🔴 **Cos'è Redis?**
        
        > Redis è un database NoSQL in-memory, basato su chiave-valore.
        > 
        
        📌 Significa che:
        
        - Salva i dati **in RAM** (è super veloce)
        - Funziona con strutture semplici come:
            - `SET` / `GET` (chiave → valore)
            - **liste**, **contatori**, **set**, **hash**
        - Viene usato per:
            - **caching** (memorizzazione temporanea)
            - **sessioni utente**
            - **code di lavoro**, **chat**, **ranking**, ecc.
    - 🔹 **Parte 1 – Avvio e Verifica del Server Redis**
        
        ### ▶️ Avvio del server Redis (se non è già attivo):
        
        ```bash
        redis-server
        
        ```
        
        ### ▶️ Connessione alla CLI in una nuova finestra (cmd+n):
        
        ```bash
        redis-cli
        
        ```
        
        ### ▶️ Verifica che Redis sia attivo:
        
        ```bash
        PING
        
        ```
        
        📌 Risposta attesa:
        
        ```
        PONG
        
        ```
        
    - 🔹 **Parte 2 – Comandi Base (Key-Value)**
        
        ### ▶️ Inserire e leggere un valore:
        
        ```bash
        SET nome "Alice"
        GET nome
        
        ```
        
        ### ▶️ Verificare se una chiave esiste:
        
        ```bash
        EXISTS nome
        
        ```
        
        ### ▶️ Eliminare una chiave:
        
        ```bash
        DEL nome
        
        ```
        
    - 🔹 **Parte 3 – Liste**
        
        ### ▶️ Inserire elementi in una lista (da sinistra):
        
        ```bash
        LPUSH compiti "studiare" "fare esercizio" "leggere"
        ```
        
        ### ▶️ Leggere tutti gli elementi della lista:
        
        ```bash
        LRANGE compiti 0 -1 #significa dal'elemento in posizione 0 all'elemento -1
        
        ```
        
        ### ▶️ Rimuovere l’ultimo elemento (da destra):
        
        ```bash
        RPOP compiti
        
        ```
        
    - 🔹 **Parte 4 – Operazioni Numeriche**
        
        ### ▶️ Impostare un numero:
        
        ```bash
        SET contatore 10
        
        ```
        
        ### ▶️ Aumentare / diminuire di 1:
        
        ```bash
        INCR contatore
        DECR contatore
        
        ```
        
        ### ▶️ Aumentare di un valore specifico:
        
        ```bash
        INCRBY contatore 5
        
        ```
        
    - 🔹 **Parte 5 – TTL e Scadenze (Time To Live)**
        
        ### ▶️ Impostare un valore con scadenza:
        
        ```bash
        SET codice "abc123"
        EXPIRE codice 10
        
        ```
        
        ### ▶️ Verificare il tempo rimanente:
        
        ```bash
        TTL codice
        
        ```
        
        ### ▶️ Dopo 10 secondi, il valore sarà scaduto:
        
        ```bash
        GET codice  # Risulterà (nil)
        
        ```
        
    - ✅ **Note**
        - Redis salva dati in **strutture chiave-valore** (Key-Value)
        - Ogni comando è **eseguito in tempo reale** nella CLI
        - Comandi come `EXPIRE` permettono di **gestire dati temporanei**
        - Redis è **NoSQL in-memory**, ideale per dati leggeri e veloci
    
    ---
    
    ---
    

---

**`10 - Testing`**

- Perché testare il codice
    
    Quando scrivi del codice, inevitabilmente possono nascondersi errori (bug) che emergono soltanto in particolari situazioni. Testare significa prevenire questi bug, perché mettendo sotto controllo ogni parte del programma possiamo accorgerci subito se qualcosa non funziona. Inoltre, se in futuro dovremo modificare o ristrutturare (refactoring) il codice, i test ci assicurano che le funzionalità già esistenti continuino a comportarsi correttamente. Automatizzare i test rende lo sviluppo più efficiente: ogni volta che cambiamo una riga di codice, possiamo lanciare una suite di test e ottenere subito un riscontro sullo stato di salute dell’intera applicazione .
    
- Tipologie di test
    
    Esistono diversi livelli di test, a seconda di quanto grande o complesso è l’elemento che vogliamo verificare:
    
    - **Unit Test**: controllano il comportamento di una singola funzione o metodo, isolata dal resto del sistema.
    - **Integration Test**: verificano che più componenti comunichino correttamente tra loro.
    - **End‑to‑End Test**: simulano l’esperienza dell’utente finale e testano il sistema nella sua interezza.
    - **Regression Test**: vengono rieseguiti dopo ogni modifica per garantire che le nuove modifiche non abbiano rotto funzionalità precedentemente funzionanti .
- Test‑Driven Development (TDD)
    
    Il TDD è un ciclo di sviluppo in tre fasi:
    
    1. **Scrivi un test che fallisce**: prima di implementare la funzionalità, definisci il test che la verifica.
    2. **Scrivi il codice per farlo passare**: realizza la minima quantità di codice necessaria perché il test superi il controllo.
    3. **Refactor del codice**: migliori la qualità interna del codice mantenendo tutti i test verdi.
    
    Questo approccio favorisce un design modulare e garantisce una copertura più ampia del codice .
    
- **`*Esercizi*`** di test semplici in Python
    
    Per mettere in pratica subito, proviamo a testare una funzione di somma:
    
    ```python
    def somma(a, b):
        return a + b
    
    def test_somma():
        assert somma(2, 3) == 5
    
    ```
    
    Per eseguire il test, si utilizza il comando:
    
    ```
    pytest test_math.py
    
    ```
    
    In questo modo verifichiamo che la funzione `somma` restituisca il risultato atteso quando sommiamo 2 e 3 .
    
- Code Coverage
    
    Il **code coverage** misura la percentuale di righe di codice che vengono effettivamente eseguite durante i test. Avere una copertura elevata è utile, ma non garantisce da sola l’efficacia dei test, perché potremmo eseguire le righe di codice senza verificarne davvero il comportamento corretto .
    
- Mocking e isolamento
    
    Quando una funzione dipende da componenti esterni (database, API, file system), per un unit test vogliamo isolarla: usiamo il **mocking**, cioè sostituiamo le dipendenze con oggetti “finti” che restituiscono risposte controllate. Ad esempio:
    
    ```python
    from unittest.mock import MagicMock
    
    db.get_user = MagicMock(return_value={"id": 1})
    
    ```
    
    Così possiamo testare la logica interna senza toccare il database reale .
    

- Obiettivo del test unitario
    - **Scopo**: verificare il comportamento di una singola funzione o metodo in **isolamento**, senza dipendere da componenti esterni (database, API, file system).
    - **Perché**: se il test coprisse anche le dipendenze esterne, un errore in quest’ultime farebbe fallire anche il test della logica interna, rendendo difficile capire dove sia il problema.
- Cos’è il mocking
    - Il **mocking** è una tecnica che consente di **simulare** il comportamento di una dipendenza esterna, creando un “finto” oggetto o metodo.
    - Con un mock possiamo:
        - Controllare esattamente quali valori restituisce la dipendenza.
        - Evitare operazioni lente o con effetti collaterali (scrittura su file, interrogazioni al database, chiamate HTTP).
        - Far sì che il test si concentri solo sulla logica interna della funzione sotto esame.
- Componenti da simulare
    
    Nei test unitari si possono mockare tipicamente:
    
    - **Accesso al database**: ad esempio, sostituire una chiamata a `db.get_user()` con un risultato predefinito.
    - **API esterne**: evitare di fare richieste reali a servizi online, restituendo risposte fittizie.
    - **File system**: simulare letture/scritture di file senza toccare il disco.
    
    ```python
    from unittest.mock import MagicMock
    
    # Esempio di mock di un metodo di database:
    db.get_user = MagicMock(return_value={"id": 1})
    
    ```
    
- `Esempio` pratico: una funzione dipendente dal database
    
    Immaginiamo di avere una classe che rappresenta l’accesso ai dati, ma per ora non vogliamo implementarne i dettagli:
    
    ```python
    class Database:
        def get_valori(self):
            # per ora non lo implementiamo
            raise NotImplementedError
    
    def somma(db: Database):
        a, b = db.get_valori()
        return a + b
    
    ```
    
    - `Database.get_valori()` solleva `NotImplementedError`, perché non contiene ancora alcuna logica.
    - La funzione `somma` chiama `db.get_valori()` e somma i due valori restituiti.
- Creare il mock e scrivere il test
    
    Per testare `somma` **senza** implementare davvero `get_valori`, creiamo un mock che fornisce valori fittizi:
    
    ```python
    import unittest # Importa unittest per i test
    from unittest.mock import MagicMock # Importa MagicMock per il mock che simula il database
    from somma_da_db import somma # Importa la funzione somma dal modulo somma_da_db
    
    class TestConMockDatabase(unittest.TestCase):
        def test_somma_mock_db(self):
            # Crea un mock del database
            mock_db = MagicMock()
            
            # Simula il comportamento del metodo get_valori simulando il ritorno di due valori 
            mock_db.get_valori.return_value = (3, 5)
    
            # Simula il comportamento del metodo somma che utilizza il mock del database
            # 3. Chiama la funzione da testare, passando il mock
            risultato = somma(mock_db)
    
            # Verifica che il risultato della somma sia corretto
            self.assertEqual(risultato, 8)
    
    if __name__ == "__main__": #Verifica se il file è eseguito come script principale ovvero non è importato
        unittest.main() 
     #avvia il framework unittest che rileva automaticamente i metodi di test 
     #definiti nella classe e li esegue, mostrando i risultati  (successi o fallimenti)
    
    ```
    
    ### Spiegazione passo-per-passo
    
    1. **Creazione del mock**
        
        ```python
        mock_db = MagicMock()
        
        ```
        
        Questa istruzione genera un oggetto fittizio con qualsiasi metodo “al volo”.
        
    2. **Configurazione del comportamento**
        
        ```python
        mock_db.get_valori.return_value = (3, 5)
        
        ```
        
        Indichiamo che quando `get_valori()` viene chiamato, il mock deve restituire la tupla `(3, 5)`.
        
    3. **Esecuzione del test**
        
        ```python
        risultato = somma(mock_db)
        
        ```
        
        Passiamo il mock a `somma()`. Poiché `mock_db.get_valori()` restituisce `(3, 5)`, la somma sarà `8`.
        
    4. **Asserzione**
        
        ```python
        self.assertEqual(risultato, 8)
        
        ```
        
        Verifichiamo che `somma` restituisca effettivamente `8`.
        
- Vantaggi del mocking e dell’isolamento
    - **Velocità**: i test non attendono risposte reali dal database o da servizi esterni.
    - **Determinismo**: i risultati sono sempre gli stessi, perché controlliamo noi i valori restituiti.
    - **Diagnosi semplificata**: se un test fallisce, il problema è nella logica interna, non nella dipendenza esterna.
    - **Facilità di scrittura**: non serve implementare componenti esterni per poter testare subito la logica.

---

- Test parametrici
    
    Per evitare di scrivere più volte lo stesso test con valori diversi, Pytest supporta i **parametric tests**. Ad esempio:
    
    ```python
    import pytest
    
    @pytest.mark.parametrize("a,b,expected", [
        (2, 3, 5),
        (-1, 1, 0),
        (0, 0, 0)
    ])
    def test_somma(a, b, expected):
        assert a + b == expected
    
    ```
    
    In un solo test definiamo più scenari, migliorando la copertura e riducendo il codice ripetuto .
    
- Testing per il Web Programming
    
    Testare un’applicazione web è più complesso di un semplice script, perché dobbiamo verificare:
    
    - La validazione di input e output.
    - La corretta gestione degli errori.
    - Lo stato dell’applicazione (database, autenticazione).
    - La sicurezza, per esempio che utenti non autorizzati non possano accedere a risorse protette.
    
    Non basta che “il codice giri”: deve restituire lo **status code** HTTP corretto (ad esempio 200 OK, 201 Created, 400 Bad Request, 401 Unauthorized, 404 Not Found, 422 Unprocessable Entity, 500 Internal Server Error) e il contenuto atteso .
    
- Casi di fallimento da testare
    
    Quando scriviamo i test di un’API, dobbiamo includere scenari di errore:
    
    1. Richieste con input malformati o incompleti.
    2. Accesso a risorse inesistenti (ad es. `/user/999`).
    3. Richieste non autorizzate.
    4. Timeout, errori di rete, errori interni del server (500).
    
    Per ciascun caso verifichiamo lo status code e, se previsto, il messaggio o il formato JSON di risposta .
    
- Test con FastAPI
    
    FastAPI offre un client di test che simula richieste HTTP senza avviare un server reale. Esempio:
    
    ```python
    from fastapi.testclient import TestClient
    from myapp import app
    
    client = TestClient(app)
    
    def test_read_root():
        response = client.get("/")
        assert response.status_code == 200
    
    ```
    
    Qui definiamo un endpoint `GET /` che restituisce `{"message": "Hello World"}`; il test conferma che risponda con 200 OK .
    
- Test di validazione degli input
    
    Con Pydantic definiamo modelli che includono vincoli:
    Questo assicura che nomi troppo corti o prezzi non validi generino un errore 422 Unprocessable Entity .
    
    ```python
    from pydantic import BaseModel, Field
    
    class Item(BaseModel):
        name: str = Field(min_length=3)
        price: float = Field(gt=0)
    
    def test_create_item_invalid():
        response = client.post("/items/", json={"name": "A", "price": -5})
        assert response.status_code == 422
    ```
    
    - **`Item`**: è un modello Pydantic che definisce i requisiti per i campi `name` (almeno 3 caratteri) e `price` (maggiore di 0).
    - **`test_create_item_invalid`**: è una funzione di test che invia una richiesta POST con dati non validi (`name` troppo corto e `price` negativo).
    - **`assert response.status_code == 422`**: verifica che l'API risponda con un codice 422, confermando che la validazione dei dati ha fallito come previsto.
    
    ### ✅ Perché è importante
    
    Utilizzare `assert` in questo modo nei test automatizzati è fondamentale per assicurarsi che l'applicazione gestisca correttamente i casi di input non valido, mantenendo l'integrità dei dati e fornendo feedback appropriati agli utenti.
    
    In sintesi, l'istruzione `assert` qui garantisce che l'API rifiuti correttamente i dati che non soddisfano i criteri di validazione definiti nel modello `Item`.
    
    Questo assicura che nomi troppo corti o prezzi non validi generino un errore 422 Unprocessable Entity .
    
- Best practice di testing API
    
    Per avere una suite di test robusta, copriamo sempre:
    
    - Percorsi di successo.
    - Fallimenti dovuti a input errati.
    - Fallimenti dovuti allo stato dell’applicazione (ad es. utente inesistente).
    - Verifica di status code, contenuto JSON e header (token, location).
    - Controlli di autorizzazione: utenti non autenticati non devono accedere; utenti autenticati vedono solo le proprie risorse .
    
    Con questi accorgimenti, il tuo codice web sarà ben protetto da regressioni e vulnerabilità.
    

- ESERCIZI
    - Test Somma
        - somma.py
            
            ```python
            def somma(a, b):
                return a + b
            
            def somma_pari(a, b):
                if a + b % 2 == 0:
                    return somma(a, b)
            
            ```
            
        - test_somma.py
            
            ```python
            from somma import somma
            import pytest
            
            def test_somma_2_3():
                assert somma(2, 3) == 5
            
            def test_somma_4_3():
                assert somma(4, 3) == 7
            
            def test_somma_sbagliata():
                assert somma(4, 2) != 7
            
            @pytest.mark.parametrize("a, b, expected", [
                (2, 3, 5), (4, 3, 7), (4, 2, 6) #lista di elementi che vanno a sostituire i parametri da testare
                ])
            
            def test_somma_multipli(a, b, expected):
                assert somma(a, b) == expected
            ```
            
    - Test di Somma tramite simulazione di Database
        - somma_da_db.py
            
            ```python
            class Database:
                def get_valori(self):
                    # per ora non lo implementiamo
                    raise NotImplementedError
            
            def somma(db: Database):
                a, b = db.get_valori()
                return a + b
            
            ```
            
        - test_somma_da_db.py
            
            ```python
            import unittest # Importa unittest per i test
            from unittest.mock import MagicMock # Importa MagicMock per il mock che simula il database
            from somma_da_db import somma # Importa la funzione somma dal modulo somma_da_db
            
            class TestConMockDatabase(unittest.TestCase):
                def test_somma_mock_db(self):
                    # Crea un mock del database
                    mock_db = MagicMock()
                    
                    # Simula il comportamento del metodo get_valori simulando il ritorno di due valori 
                    mock_db.get_valori.return_value = (3, 5)
            
                    # Simula il comportamento del metodo somma che utilizza il mock del database
                    # 3. Chiama la funzione da testare, passando il mock
                    risultato = somma(mock_db)
            
                    # Verifica che il risultato della somma sia corretto
                    self.assertEqual(risultato, 8)
            
            if __name__ == "__main__": #Verifica se il file è eseguito come script principale ovvero non è importato
                unittest.main() #avvia il framework unittest che rileva automaticamente i metodi di test 
                                #definiti nella classe e li esegue, mostrando i risultati (successi o fallimenti)
            
            ```
            
    - Test di Web Server
        - server.py
            
            ```python
            from fastapi import FastAPI
            from pydantic import BaseModel, Field
            
            app = FastAPI() # Crea un'istanza dell'app FastAPI 
            
            @app.get("/")
            def read_root():
                return {"message": "Hello World"}
            
            class Item(BaseModel): # Definisce un modello di dati per gli oggetti 
                name: str = Field(min_length=3) # Campo di tipo stringa con lunghezza minima di 3 caratteri
                price: float = Field(gt=0) # Campo di tipo float con valore maggiore di 0
            
            @app.post("/items")
            def post_item(item: Item): # Definisce un endpoint POST per ricevere oggetti di tipo Item
                return {"item received": item}
            
            ```
            
        - test_server.py
            
            ```python
            from fastapi.testclient import TestClient #
            from server import app
            
            client = TestClient(app)
            
            def test_read_root():
                response = client.get("/") #simula una richiesta GET all'endpoint radice
                assert response.status_code == 200
            
            def test_read_not_existing() -> None:
                response = client.get("/prova")
                assert response.status_code == 404
            
            def test_create_item_valid():
                response = client.post(url = "/items/", json={"name": "Book", "price": 5})
                assert response.status_code == 200
            
            def test_create_item_invalid():
                response = client.post("/items/", json={"name": "A", "price": -5})
                assert response.status_code == 422
            
            ```
            
- Spiegazione Mocking
    
    ```
    mock_db = MagicMock()
    ```
    
    ---
    
    ## **🔍 COSA È IL MOCKING?**
    
    Il **mocking** è una tecnica usata nei test automatici per **simulare (fingere)** il comportamento di oggetti complessi (come database, API esterne, file, ecc.), senza usare davvero quelle risorse reali.
    
    Questo è utile perché:
    
    - Eviti **lentezza** e **complessità** nel test.
    - Puoi **controllare completamente il comportamento** dell’oggetto simulato.
    - Ti permette di testare solo la **logica della tua funzione**, isolandola dal resto.
    
    ---
    
    ## **🧠 COSA FA mock_db = MagicMock() ?**
    
    La riga:
    
    ```
    mock_db = MagicMock()
    ```
    
    crea un **oggetto finto** (mock) che si comporta come un qualsiasi oggetto Python, ma in modo completamente controllabile. Tu puoi decidere **quali attributi e metodi ha, e cosa devono restituire**.
    
    In pratica, mock_db è come un “finto database”, ma senza bisogno di un vero database.
    
    ---
    
    ## **✅ COME SI USA mock_db ?**
    
    Nel tuo test, mock_db viene usato così:
    
    ```
    mock_db.get_valori.return_value = (3, 5)
    ```
    
    Qui stai dicendo:
    
    > “Se qualcuno chiama mock_db.get_valori(), fai finta che ritorni (3, 5)”.
    > 
    
    Poi chiami la funzione che vuoi testare:
    
    ```
    risultato = somma(mock_db)
    ```
    
    E la tua funzione somma() chiamerà mock_db.get_valori() — e grazie al mocking, restituirà (3, 5) come deciso prima.
    
    ---
    
    ## **🎯 RIASSUNTO: TUTTO CIÒ CHE DEVI SAPERE**
    
    | **Concetto** | **Spiegazione** |
    | --- | --- |
    | **Mock** | Oggetto finto che simula un altro oggetto reale. |
    | **MagicMock()** | Crea un mock altamente configurabile. |
    | **mock.method.return_value = ...** | Imposti cosa deve restituire un metodo chiamato sul mock. |
    | **Vantaggi** | Velocità, controllo, test isolati, nessun accesso a risorse esterne. |
    
    ---
    
    ## **💡 ESEMPIO COMPLETO DI MOCKING**
    
    ```
    mock_api = MagicMock()
    mock_api.chiama_endpoint.return_value = {'status': 'ok'}
    
    def usa_api(api):
        dati = api.chiama_endpoint()
        return dati['status']
    
    assert usa_api(mock_api) == 'ok'
    ```
    
    ---
    
- Spiegazione Unit
    
    ---
    
    ## **🧪 COS’È unittest ?**
    
    unittest è un **modulo integrato di Python** che ti permette di **scrivere e lanciare test automatici** per controllare che il tuo codice funzioni come previsto.
    
    È ispirato a framework simili di altri linguaggi (come JUnit in Java) e serve per:
    
    - Automatizzare i test
    - Evitare errori imprevisti
    - Garantire che modifiche future non rompano il codice esistente
    
    ---
    
    ## **🧱 STRUTTURA BASE DI UN TEST CON unittest**
    
    Nel tuo file trovi questa struttura:
    
    ```python
    import unittest
    from unittest.mock import MagicMock
    from somma_da_db import somma
    
    class TestConMockDatabase(unittest.TestCase):
        def test_somma_mock_db(self):
            ...
    ```
    
    Vediamola **passo passo**:
    
    ---
    
    ### **✅ import unittest**
    
    Importa il modulo principale per scrivere test.
    
    ---
    
    ### **✅class NomeClasseTest(unittest.TestCase)**
    
    Tutti i test devono stare dentro una **classe** che eredita da unittest.TestCase.
    
    Questo perché:
    
    - TestCase fornisce **tanti strumenti e metodi di controllo** (come assertEqual, assertTrue, ecc.)
    - Ogni metodo della classe che inizia con test_ sarà **riconosciuto automaticamente come test**.
    
    Nel tuo caso:
    
    ```
    class TestConMockDatabase(unittest.TestCase):
    ```
    
    Questa classe è un contenitore per i tuoi test, in particolare per testare l’uso del database mockato.
    
    ---
    
    ### **✅ def test_qualcosa(self):**
    
    Ogni metodo che inizia con test_ viene eseguito **automagicamente** da unittest.
    
    Nel tuo caso:
    
    ```python
    def test_somma_mock_db(self):
    ```
    
    Significa: “voglio testare il comportamento della funzione somma() usando un mock del database”.
    
    ---
    
    ### **✅ self.assertEqual(...)**
    
    unittest ti dà molti metodi per **verificare i risultati**. I più usati sono:
    
    | **Metodo** | **Cosa fa** |
    | --- | --- |
    | assertEqual(a, b) | Verifica che a == b |
    | assertNotEqual(a, b) | Verifica che a != b |
    | assertTrue(x) | Verifica che x è True |
    | assertFalse(x) | Verifica che x è False |
    | assertIsNone(x) | Verifica che x è None |
    | assertRaises(...) | Verifica che venga sollevata un’eccezione |
    
    Nel tuo esempio:
    
    ```
    self.assertEqual(risultato, 8)
    ```
    
    Controlla che il risultato ottenuto dalla funzione somma() sia esattamente 8.
    
    ---
    
    ### **✅if __name__ == "__main__": unittest.main()**
    
    Questa parte serve a dire:
    
    > “Se eseguo questo file direttamente (non come modulo importato), allora
    > 
    > 
    > **esegui tutti i test**
    > 
    
    unittest.main() fa partire l’esecuzione automatica di tutti i metodi test_ definiti nella classe.
    
    ---
    
    ## **🚀 COME SI ESEGUE UN FILE DI TEST?**
    
    Apri il terminale nella cartella del file e lancia:
    
    ```
    python test_somma_da_db.py
    ```
    
    Output tipico:
    
    ```
    .
    ----------------------------------------------------------------------
    Ran 1 test in 0.001s
    
    OK
    ```
    
    Il punto . indica che 1 test è andato a buon fine. Se ci sono errori o fallimenti, unittest ti mostra il motivo.
    
    ---
    
    ## **🧠 RIASSUNTO PRATICO PER I TUOI APPUNTI**
    
    | **Elemento** | **Spiegazione** |
    | --- | --- |
    | unittest | Modulo per scrivere test automatici |
    | TestCase | Classe base da cui erediti per i tuoi test |
    | test_... | Ogni metodo che inizia così sarà eseguito |
    | assertEqual(a, b) | Controlla se a == b |
    | unittest.main() | Lancia tutti i test nel file |
    | Vantaggi | Controlli automatici, meno errori, test veloci e ripetibili |
    
    ---
    

---

**`11 - Deployment`**

APPUNTI DA FINIRE DOPO LA LEZIONE

- Cos’è il deployment
    
    Il **deployment** è quel processo che prende il codice sorgente di un’applicazione e lo porta in un ambiente dove gli utenti reali possono usarla. Non basta scrivere funzionante il software in locale: bisogna renderlo **disponibile online**, garantirne la **sicurezza** contro attacchi e assicurarne la **scalabilità**, cioè che regga il carico di utenti quando verrà effettivamente usato.
    
- Ambienti di esecuzione
    
    Per evitare che modifiche in fase di sviluppo causino interruzioni al servizio in uso, si usano più ambienti separati:
    
    - **Development**: dove gli sviluppatori lavorano in locale.
    - **Testing/Staging**: copia identica della produzione; qui si fanno prove con dati fittizi o replicati.
    - **Production**: l’ambiente live, con alta disponibilità e massima sicurezza, usato dagli utenti finali.
    
    Solo dopo aver verificato in staging che tutto funzioni, si aggiorna la produzione, così da minimizzare rischi di interruzioni catastrofiche .
    
- Metodi di deployment
    
    ### Manuale (FTP/SSH)
    
    Si copiano file via FTP, SFTP o SSH ed si eseguono comandi a mano (scp, rsync, systemctl…). 
    
    - **Pro**: facilissimo per prototipi locali o ambienti temporanei.
    - **Contro**: soggetto a errori umani, senza tracciabilità, non scalabile.
    
    ### Script automatizzati
    
    Si scrivono script (bash, Makefile, Ansible) che eseguono copia file, migrazioni DB, riavvio servizi.
    
    - **Pro**: ripetibile, meno errori umani.
    - **Contro**: va continuamente manutenuto e fatica ad adattarsi a scenari molto dinamici .
    
    USIAMO LE PRIME DUE SOLO SE CREIAMO UNA COSA TEMPORANEA CHE DURA MASSIMO UNA SRTTIMANA (per esempio) 
    
    ### CI/CD (Continuous Integration/Continuous Deployment)
    
    Un workflow che, a ogni push su Git, esegue automaticamente i test e poi il deploy, usando strumenti come GitHub Actions, GitLab CI o Jenkins.
    
    - **Pro**: completamente automatizzato, deployment tracciabili, test on push.
    - **Contro**: configurazione iniziale complessa .
    
    ### Docker e Docker Compose
    
    - **Docker**: crea un container con l’app (software) e tutte le sue dipendenze, garantendo che funzioni identico in ogni ambiente in modo isolato.
    - **Docker Compose**: definisce in un file YAML più container (app, database, cache) e li avvia insieme.
    - **Pro**: coerenza tra dev/prod, facile scalabilità.
    - **Contro**: richiede comunque una pipeline CI per il deploy .
    - **🚀 Cos’è una pipeline CI per il deploy?**
        
        Una **pipeline CI (Continuous Integration)** per il **deploy (rilascio)** è un processo automatico che:
        
        1. **Prende il tuo codice** (ad esempio da GitHub),
        2. **Lo testa** (con test automatici),
        3. **Costruisce l’app** (es. con Docker),
        4. **E lo pubblica** su un server o servizio (es. un cloud o un VPS), **senza interventi manuali**.
    
    ### PaaS (Platform as a Service)
    
    Servizi come Heroku, Render o Railway: tu carichi il codice (via Git o interfaccia), loro costruiscono l’app e la pubblicano.
    
    - **Pro**: partenza rapidissima.
    - **Contro**: meno controllo sulle configurazioni avanzate, si pagano e anche molto .
    
    ### IaaS (Infrastructure as a Service)
    
    Server virtuali su AWS EC2, GCP Compute, DigitalOcean: hai un “PC remoto” configurabile in tutto (OS, firewall, software).
    
    - **Pro**: massima flessibilità e scalabilità.
    - **Contro**: tutta la responsabilità di sicurezza, aggiornamenti, logging è tua; serve competenza sysadmin .
- Confronto tra metodi
    
    
    | Metodo | Pro | Contro |
    | --- | --- | --- |
    | Manuale (FTP/SSH) | Facile da iniziare, per durate di pochissimo tempo | Rischi elevati, nessuna tracciabilità |
    | Script automatizzati | Ripetibile, più sicuro | Richiede manutenzione |
    | CI/CD | Completamente automatizzato, tracciato | Setup iniziale complesso |
    | PaaS | Velocissimo per iniziare | Meno controllo |
    | IaaS | Flessibilità massima | Complessità e responsabilità elevate |
- Virtualizzazione e container
    
    Un **container** è un ambiente isolato e leggero che include solo ciò che serve per eseguire un’app.
    
    - A differenza di una macchina virtuale (VM), non simula un intero sistema operativo, ma condivide il kernel del sistema host. Per questo è molto più **veloce**, **leggero** e **portabile**.
    - Sul mio sistema operativo uso un **Container Engine** (come Docker), che gestisce i container.
    - È come una **scatola** che contiene tutto: codice, librerie, dipendenze, configurazioni — tutto il necessario per far girare l’app ovunque.
    - Funziona a **strati** (layer): ogni modifica (es. installazione di una libreria) crea un nuovo livello sopra il precedente, rendendo il sistema efficiente e riutilizzabile.
    - Un esempio di **Dockerfile** (file per configurare i Container) per un’app Node.js:
        
        ```
        FROM node:20-alpine
        WORKDIR /app
        COPY . .
        RUN npm install
        CMD ["npm", "start"]
        ```
        
        Un **Dockerfile** è un file di testo che definisce le istruzioni per creare un’immagine Docker. Questo esempio crea un’immagine per una semplice app Node.js.
        
        ```
        # Usa un'immagine ufficiale di Node.js (versione 20, leggera)
        FROM node:20-alpine
        
        # Imposta la directory di lavoro all'interno del container
        WORKDIR /app
        
        # Copia tutti i file locali nella directory di lavoro del container
        COPY . .
        
        # Installa le dipendenze definite nel package.json
        RUN npm install
        
        # Comando di default all'avvio del container
        CMD ["npm", "start"]
        ```
        
        ---
        
        ### **🔍 Spiegazione rapida:**
        
        - FROM: indica l’immagine base da cui partire (qui: Node.js su Alpine Linux, minimale e veloce).
        - WORKDIR: definisce la directory in cui verranno eseguiti i comandi successivi.
        - COPY: copia i file locali (codice sorgente, package.json, ecc.) dentro l’immagine.
        - RUN: esegue un comando durante la build (qui: installa le dipendenze).
        - CMD: indica cosa deve eseguire il container quando parte.
        
        ---
        
        Con questo Dockerfile puoi costruire un’immagine e avviare la tua app Node.js in modo isolato e portabile con pochi comandi:
        
        ```
        docker build -t mia-app-node .
        docker run -p 3000:3000 mia-app-node
        ```
        
        ### **Perché l’ordine delle istruzioni è importante**
        
        Docker costruisce l’immagine **uno strato alla volta**, partendo dall’alto verso il basso. Ogni istruzione (FROM, COPY, RUN, ecc.) crea uno **snapshot**, cioè un layer separato dell’immagine.
        
        Docker utilizza un meccanismo chiamato **caching**: se una riga non cambia, Docker riusa lo snapshot già creato anziché rieseguire tutto da zero. Questo rende la build **molto più veloce**.
        
    
- Ambienti multi‑container: docker‑compose
    
    Con Docker Compose si definiscono servizi in YAML. Ad esempio:
    
    ```yaml
    version: '3.8'
    services:
      web:
        build: .
        ports:
          - "3000:3000"
      db:
        image: postgres
        environment:
          POSTGRES_PASSWORD: example
    
    ```
    
    Così avvii insieme l’app web e il database, connettendoli automaticamente .
    
- CI/CD in pratica
    
    Una pipeline CI/CD tipica in GitHub Actions può essere:
    
    ```yaml
    on: [push]
    jobs:
      deploy:
        runs-on: ubuntu-latest
        steps:
          - uses: actions/checkout@v2
          - run: docker build -t myapp .
          - run: docker run myapp
    
    ```
    
    - **Continuous Integration**: ad ogni push, build e test vengono eseguiti automaticamente.
    - **Continuous Delivery**: il pacchetto pronto va in staging per essere approvato.
    - **Continuous Deployment**: tutto ciò che passa i test finisce direttamente in produzione .
- Gestione delle configurazioni e .env
    
    Non mettere mai credenziali o segreti nel codice. Usa file **.env** per definire variabili di ambiente (DATABASE_URL, SECRET_KEY…) che:
    
    - Restano fuori dal version control, sono file di configurazione locali nella macchina.
    - Sono caricate in fase di avvio dell’app.
    - Possono differire tra dev, staging e prod.
    
    Librerie come `python-dotenv` o `dotenv` in Node.js semplificano il caricamento di queste variabili .
    
- Sicurezza in produzione (best practices)
    
    Per un deployment sicuro:
    
    - Usa **HTTPS** (ad es. Let's Encrypt), serve a non far leggere il contenuto da persone non autorizzate.
    - Applica **rate limiting** (numero di richieste massime per un utente) e difese anti‑DoS.
    - Valida sempre input lato server.
    - Definisci chiaramente permessi e ruoli di accesso.
    - Esegui **backup** regolari del database.
    - Implementa **logging** di errori, eventi e performance per monitorare attività e tentativi di attacco.
    - Prevedi meccanismi di **rollback** in caso di deploy fallito .
- Esercitazione con Docker‑Compose
    
    Per mettere in pratica, nel repository
    
    [https://github.com/maurapintor/docker-compose-tutorial](https://github.com/maurapintor/docker-compose-tutorial)
    
    trovi un esempio completo di progetto con:
    
    - Un proxy server intermediario, è un server a cui facciamo una richiesta a un altro server che fa la risposta e la manda .al server di partenza
    - Un’app Node.js e un database PostgreSQL definiti in `docker-compose.yml`.
    
    Clona, configura il `.env` locale e lancia `docker-compose up` per sperimentare un deployment multi‑container in azione .
    
    ![IMG_0574.HEIC](PROGRAMMAZIONE%20WEB%201af9a6c97cf98039a6e0cd1e9e9bb7af/IMG_0574.heic)
    
    ![IMG_0575.HEIC](PROGRAMMAZIONE%20WEB%201af9a6c97cf98039a6e0cd1e9e9bb7af/IMG_0575.heic)
    
    - se digito [localhost:8001](http://localhost:8001) vedo la get del server1
    - se digito [localhost:800](http://localhost:8001)2 vedo la get del server3

---

[LABORATORIO P.WEB](PROGRAMMAZIONE%20WEB%201af9a6c97cf98039a6e0cd1e9e9bb7af/LABORATORIO%20P%20WEB%201c79a6c97cf980598c52eddf18243b81.md)

[PYTHON CORSO RAPIDO](PROGRAMMAZIONE%20WEB%201af9a6c97cf98039a6e0cd1e9e9bb7af/PYTHON%20CORSO%20RAPIDO%201bc9a6c97cf980e6a7e8e4a5aef5bcbd.md)