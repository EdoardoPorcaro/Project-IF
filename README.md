# Progetto IF
Progetto di intelligenza artificiale applicata ai mercati finanziari.

## Problemi noti
Di seguito sono elencati alcuni problemi noti che impediscono la corretta esecuzione del programma.
### `import` non funziona
- L'importazione di librerie come `from tensorflow.keras.layers import LSTM`, `from tensorflow.keras.callbacks import ModelCheckpoint, TensorBoard`, `from tensorflow.keras.models import Sequential`, `from tensorflow.keras.layers import LSTM, Dense, Dropout, Bidirectional` e altre con sintassi simile non sembrano funzionare.
- L'errore restituito è `Pylance(reportMissingImports)`, come se nell'installare TensorFlow non avessi installato tutti i moduli.
- Per l'installazione di TensorFlow ho eseguito il comando `pip install tensorflow`; **avrei dovuto fare qualcos'altro?**
- **Secondo te, è un problema di installazione delle librerie o è effettivamente un errore di sintassi?**
- Onestamente, non penso sia un errore di sintassi, siccome `import matplotlib.pyplot as plt`, ad esempio, funziona senza problemi.

## Ulteriori discussioni
Presentati di seguito alcune discussioni correlate allo sviluppo del software

### Possibili implementazioni
Seguono alcune possibili implementazioni sulla base del codice caricato.

*Da finire*

## Impatto sull'economia
Qualora il progetto venisse applicato effettivamente sui mercati finanziari, dopo aver implementato ulteriormente l'algoritmo di intelligena artificiale
