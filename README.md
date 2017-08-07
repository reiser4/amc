# amc


Software utilizzato su Windows:

 Python 3.5.0
 https://www.python.org/ftp/python/3.5.0/python-3.5.0-amd64-webinstall.exe

 PyQt5 5.5
 http://sourceforge.net/projects/pyqt/files/PyQt5/PyQt-5.5/PyQt5-5.5-gpl-Py3.4-Qt5.5.0-x64.exe

 py2exe 0.9.2.0
 https://pypi.python.org/packages/any/p/py2exe/py2exe-0.9.2.0.win-amd64.exe#md5=05d90513c993b2f3ae0f7f21d69a6898


Per compilare per windows:

 python setup.py py2exe --includes sip


# funzionamento

il software AMC gira su beaglebone black. E` costituito da diversi componenti che interagiscono tra loro solamente tramite lettura e scrittura (atomica) di files in /tmp.


/tmp/band.txt
	contiene la banda in uso. puo` essere: 160, 80, 60, 40, 30, 20, 17, 15, 12, 10, 6

/tmp/relay.txt
	descrive i rele` attivi con la combinazione attuale di preset.
	esempio: 100000000000000000000000
	nella nostra implementazione usiamo i primi otto bits

/tmp/presetA.txt e /tmp/presetB.txt
	descrivono la combinazione da tastiera scelta dall'utente
	la pressione dei tasti provoca la variazione della combinazione
	esempio:
		TX: 01100000
		RX: 10010000

/tmp/presetTXTA.txt e /tmp/presetTXTB.txt
	contiene la lista testuale di preset attivi (per essere stampato sul display)
	senza spazi, separati da virgola, poi punto e virgola tra Rx e Tx
	esempio:
		Europa,Asia,America;Asia


/tmp/tx.txt
	contiene la lista di radio che stanno trasmettendo in quel momento
	esempio:
		A
		oppure
		B
		oppure 
		(file vuoto)

/root/amc/config.json
	contiene la configurazione con cui vengono determinate le varie combinazioni di relay da accendere.
	vedi file di esempio




# componenti software

MAIN:
	si occupa di prendere le decisioni riguardo i preset e relay da attivare.
	LEGGE: /root/amc/config.json /tmp/tx.txt /tmp/presetA.txt /tmp/presetB.txt /tmp/band.txt
	SCRIVE: /tmp/relay.txt /tmp/presetTXTA.txt /tmp/presetTXTB.txt

IOLOOP:
	ascolta il GPIO hardware per determinare la banda e la radio trasmittente.
	SCRIVE: /tmp/band.txt /tmp/tx.txt

DISPLAY:
	si occupa di mantenere il display aggiornato con lo stato attuale.
	LEGGE: /tmp/tx.txt /tmp/band.txt /tmp/presetTXTA.txt /tmp/presetTXTB.txt

KEYBOARD:
	rimane in ascolto di input da tastiera e fa i toggle dei bits dei preset
	LEGGE: /tmp/presetA.txt /tmp/presetB.txt
	SCRIVE: /tmp/presetA.txt /tmp/presetB.txt

SERIAL:
	svolge due funzioni: riporta periodicamente sulla seriale lo stato attuale per poter essere visualizzato sul pc,
	ed interagisce col pc per inviare e ricevere la configurazione.
	LEGGE: /tmp/presetA.txt /tmp/presetB.txt /tmp/tx.txt /tmp/band.txt /tmp/presetTXTA.txt /tmp/presetTXTB.txt /root/amc/config.json
	SCRIVE: /root/amc/config.json

RELAY:
	scrive su GPIO le uscite relay
	LEGGE: /tmp/relay.txt

CHECK:
	verifica che tutti i processi siano in esecuzione ed avvia eventuali processi fermi.

===================================

Requisiti software

# apt-get install git
# pip install Pillow
