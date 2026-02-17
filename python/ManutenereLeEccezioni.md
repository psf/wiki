# ManutenereLeEccezioni

::::::::::::::: {#content dir="ltr" lang="en"}
# Manutenere le Eccezioni {#Manutenere_le_Eccezioni}

Un semplice modo per manutenere le eccezioni è usare il blocco \"try-except\" \--\> \"prova all\'innfuoridi\"

:::: {.highlight .python}
::: {.codearea dir="ltr" lang="en"}
``` {#CA-1596d58e70594684e4effd17128db7685b65dbbc dir="ltr" lang="en"}
   1 (x,y) = (5,0)
   2 try:
   3   z = x/y
   4 except ZeroDivisionError:
   5   print "divide by zero"
```
:::
::::

Se volete esaminare l\'eccezione dal codice,guardate qua:

:::: {.highlight .python}
::: {.codearea dir="ltr" lang="en"}
``` {#CA-d06dbe18428d3041fb4df2335c6ebcb61b1ce89a dir="ltr" lang="en"}
   1 (x,y) = (5,0)
   2 try:
   3   z = x/y
   4 except ZeroDivisionError, e:
   5   z = e # representation: "<exceptions.ZeroDivisionError instance at 0x817426c>"
   6 print z # output: "integer division or modulo by zero"
```
:::
::::

## Prendiamo il controllo generale del codice {#Prendiamo_il_controllo_generale_del_codice}

Talvolta,potete prendere \"all\" tutti gli errori che è possibile generare, ma di solito non è possibile.Nella mag- gior parte dei casi,quanto specificate tanto è possibile ([CatchWhatYouCanHandle](http://c2.com/cgi/wiki?CatchWhatYouCanHandle "Wiki"){.interwiki}). Nel primo caso, se stavate usando una clausola eccezione incontrata e l\'utente ha premuto Ctrl-C,generando una [KeyboardInterrupt](./KeyboardInterrupt.html){.nonexistent} (interruzione da tastiera),non desiderate che il programma emetta il messaggio \"divide by zero\"\--\> (divisione per zero.)

Tuttavia,ci sono alcune situazioni in cui è meglio prendere *all* tutti gli errori

Per esempio, supponiamo che scriviate un modulo per un servizio web. Vorrete che le informazioni inerenti gli errori sia riportate in una pagina web, e il server continui a girare,se tutto ciò è possibile.Ma voi non avete idea che tipo di errori dovete mettere nbel vs codice.

In una situazio9ne di questo tipo,il codice potrebbe essere simile a questo:

:::: {.highlight .python}
::: {.codearea dir="ltr" lang="en"}
``` {#CA-ce44db9036689574085d27d4562078eaa39e3d34 dir="ltr" lang="en"}
   1 import sys
   2 try:
   3   untrusted.execute()
   4 except: # catch *all* exceptions
   5   e = sys.exc_info()[1]
   6   write_to_page( "<p>Error: %s</p>" % e )
```
:::
::::

[MoinMoin](MoinMoin) software è un buon esempio su dove in generale catturare gli errori. Se scrivte MoinMoin macro estensione,e diamo avvio ad un errore,Moin*Moin prepareà un dettagliato rapporto circa l\'errore e la catena di eventi che conduce a lui. Il software Python deve essere abilitato a catturare tutti gli errori, e li spedisce poi alla pagina web.*

## Ricerca di Nomi Specifici di Eccezioni {#Ricerca_di_Nomi_Specifici_di_Eccezioni}

Eccezioni Standard che possono essere emesse sono dettaglaite in questo sito:

- [http://python.org/doc/lib/module-exceptions.html](http://python.org/doc/lib/module-exceptions.html){.http}

Osservate la Classe documentazione per trovare che eccezioni una data classe può emeyttere.

# Vedi Anche {#Vedi_Anche}

Su questa [WritingExceptionClasses](WritingExceptionClasses), [TracebackModule](./TracebackModule.html){.nonexistent}.

Per idde generali(non specificate in Python) circa le eccezioni,consulatre [ExceptionPatterns](http://c2.com/cgi/wiki?ExceptionPatterns "Wiki"){.interwiki}.

# Per scrivere sull\'argomento\...\.... {#Per_scrivere_sull.27argomento.......}

- Dammi un esempio di IOError, e interpretiamo il codice di errore
- Dammi un esempio di eccezioni multiple. Manteniamo le eccezioni multiple in linea
- Mostra come usare \"else\" e \"finalità\"
- Mostra come continuare con un \"rialzo\"

# Domande {#Domande}

## Manutenzione generale degli errori {#Manutenzione_generale_degli_errori}

Nella sezione \"manutenzione generale degli errori\", si è detto che per la cattura degli errori userete questo codice:

:::: {.highlight .python}
::: {.codearea dir="ltr" lang="en"}
``` {#CA-ce44db9036689574085d27d4562078eaa39e3d34-1 dir="ltr" lang="en"}
   1 import sys
   2 try:
   3   untrusted.execute()
   4 except: # catch *all* exceptions
   5   e = sys.exc_info()[1]
   6   write_to_page( "<p>Error: %s</p>" % e )
```
:::
::::

Tuttavia in origine era:

:::: {.highlight .python}
::: {.codearea dir="ltr" lang="en"}
``` {#CA-197e2604e6df3cf91b01bf6e0394a25e12c44269 dir="ltr" lang="en"}
   1 try:
   2   untrusted.execute()
   3 except Exception, e:
   4   write_to_page( "<p>Error: %s</p>" % str(e) )
```
:::
::::

Alcune indicano che \"except\" catturano piu di un semplice \"except Exception, e.\"

Perchè è questo il caso??.Qual è la differenza? *\--[LionKimbro](LionKimbro).*

Per ora ( nella ver. 2.3) l\'eccezionempm ha ereditato da Exception. Allora pianifichiamo \'except:\' catturiamo tutte le eccezioni,non solo quelle di sistema. \-- [MikeRovner](MikeRovner) 2004-01-19 05:49:19

## Prendiamo utili Informazioni da una eccezione {#Prendiamo_utili_Informazioni_da_una_eccezione}

Cosi si pò avere qualcosa di simile:

:::: {.highlight .python}
::: {.codearea dir="ltr" lang="en"}
``` {#CA-b98ff467fe070fff76c1e8cef151779fb2ff69f7 dir="ltr" lang="en"}
   1 (a,b,c) = d
```
:::
::::

\... e Python soffia indietro

    ValueError: unpack list of wrong size

\.... e cosi,naturalmente chiederete, \"bene che, cosa \'era\' in `d`?\"
:::::::::::::::
