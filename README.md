# Progetto IF
Progetto di intelligenza artificiale applicata ai mercati finanziari.

## Problemi noti
Di seguito elenco alcuni problemi noti che impediscono la corretta esecuzione del programma.
### `import` non funziona
Importazioni di librerie come
- `from tensorflow.keras.layers import LSTM`;
- `from tensorflow.keras.callbacks import ModelCheckpoint, TensorBoard`;
- ecc...
non sembrano funzionare. L'errore restituito è `c`, come se nell'installare TensorFlow non avessi installato tutti i moduli (per l'installazione ho eseguito `pip install tensorflow`; **avrei dovuto fare qualcos'altro?**).
**Secondo te, è un problema mio o effettivamente c'è un errore di sintassi?**

## Possibili implementazioni
_Scrivere qui._
