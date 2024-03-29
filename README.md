# Progetto IF
_Project IF: where Intelligence and Finance meet_  
Progetto di intelligenza artificiale applicata ai mercati finanziari.

## Nuovo progetto
Con il nuovo progetto, non solo si dà una risposta alle criticità sollevate in merito al vecchio codice, ma si dona anche una veste grafica all'applicativo, usando soprattutto elementi light-weight che possano, conseguentemente, allegerire l'esecuzione. _Vedasi il paragrafo [Riferimenti utili](https://github.com/EdoardoPorcaro/project-if/blob/main/README.md#riferimenti-utili) per ulteriori informazioni in merito ai componenti di terza parte usati nel progetto._

### Esecuzione del codice
Facendo uso di Streamlit, il progetto non dispone di un file ```main.html``` da lanciare in un qualsiasi browser. Per poter eseguire l'applicativo, si richiede l'esecuzione del comando ```streamlit run main.py``` (o, alternativamente, ```python -m streamlit run main.py```) dalla shell di Visual Studio Code affinché Streamlit generi la pagina web, che sarà aperta in ```localhost:8501```, generalmente. Una volta faccio ciò, sarà sufficiente aggiornare la pagina per visualizzare le modifiche apportate al codice in tempo reale. Qualora ci siano problemi e/o errori, lo stesso output della shell sarà visualizzata anche nella pagina web.

### Possibili implementazioni
- [ ] Si può migliorare l'esperienza utente aggiungendo dei brevi paragrafi che spieghino cosa è possibile ottenere mediante l'applicativo.
- [ ] È possibile lasciare la scelta agli utenti su quale azione eseguire l'algoritmo di predizione dell'andamento anziché fornire una scelta tra quattro. (Si noti che l'algoritmo sviluppato non ha problemi a fornire predizioni su un altro titolo; questa è, dunque, una limitazione dell'interfaccia utente piuttosto che dell'algoritmo stesso)
- [ ] Sarebbe carino migliorare il tema, aggiungendo un logo e usando una palette di colori scuri.

## Vecchio progetto
Siccome era necessario eseguire molte modifiche al codice per implementarlo così come richiesto, ho riscritto il progetto da capo, usando il comodissimo Streamlit per implementare una GUI per l'applicativo e con Prophet come algoritmo per la predizione dell'andamento futuro dei mercati. I file del vecchio progetto sono stati, quindi, rimossi dal repository.

## Riferimenti utili
Seguono alcuni riferimenti utili relativi ai componenti di terza parte usati nel progetto.
- Streamlit: [sito ufficiale](https://streamlit.io/), [video di presentazione](https://www.youtube.com/watch?v=R2nr1uZ8ffc&ab_channel=Streamlit).
- Prophet: [sito ufficiale](https://facebook.github.io/prophet/), [articolo di Medium](https://towardsdatascience.com/facebook-prophet-for-time-series-forecasting-in-python-part1-d9739cc79b1d).

## Aggiornamento del 26 ottobre 2022
Il presente repository è stato archiviato in quanto lo sviluppo del progetto è stato ultimato da tempo. Su questo codice non è previsto alcun futuro aggiornamento, sebbene rimangano concettualmente valide le impementazioni [sopracitate](https://github.com/EdoardoPorcaro/project-if/blob/main/README.md#possibili-implementazioni). Il codice **integrale** di _Project IF_ è e rimane proprietà intellettuale di [Edoardo Porcaro Holding](https://epholding.biz) e dunque non sarà reso pubblico in alcun modo.
