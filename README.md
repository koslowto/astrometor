# AstroMetor

## DEUTSCH (English version available below)

AstroMetor ist eine kleine Python-App zur Visualisierung der Bahnelemente und des aufsteigenden/absteigenden Knotens (Frühlingspunkt). Sie wurde mithilfe von matplotlib als Schulprojekt erstellt. Es gibt zwar einen Deutschen Zweig, der Hauptzweig ist aber auf Englisch - passen Sie also auf. Weiterhin wichtig: Die Anwendung wurde auf Linux für Linux entwickelt. Daher könnte es auf Windows bei der Konfiguration zu Problemen kommen. Mehr dazu finden sie im Konfigurationsabschnitt des readmes.
### Installieren
Es gibt zwei Möglichkeiten zur Installation des Programmes:
#### Verwendung der Python3-Laufzeit
* Laden Sie den Quellcode herunter, indem sie folgendes im Terminal ausführen
```
git clone https://github.com/koslowto/astrometor
cd astrometor/
```
* Installieren Sie die Abhängigkeiten
```
pip install matplotlib numpy
```
* Starten Sie die Anwendung
```
python3 main.py
```
##### Mögliche Probleme
Möglicherweise müssen Sie eine virtuelle Umgebung verwenden, um die Abhängigkeiten zu installieren und das Programm zu starten.
```
python3 -m venv venv
source venv/bin/activate
```
Es kann auch sein, dass Sie PyQt5 als Grafik-Backend installieren müssen, wenn Sie auf Probleme stoßen.

```
pip install pyqt5
``` 
#### Verwendung des .deb-Pakets (funktioniert nur auf Debian-basierten Distributionen, z.B. Ubuntu, Linux Mint...)
* Laden Sie die neueste Version herunter
* Wechseln Sie im Terminal zu Ihrem Download-Verzeichnis
```
cd <Ihr Download-Verzeichnis>
```
* Installieren Sie das Paket
```
dpkg -i astrometor.deb
```
* Die App kann jetzt über das Systemmenü gestartet werden
### Konfiguration
Die Konfigurationsdatei befindet sich in ~/.config/astrometor/astrometor.conf (verstecktes Verzeichnis). Wenn sie Windows benutzen müssen sie also 
Sie können darin das Aktualisierungsintervall für die Vorschau beim Ziehen der Schieberegler ändern. 
```
prev_interval=[1-361]
```
Der Wert legt fest, um wie viel Grad Sie den Schieberegler verändern müssen, damit eine neue Vorschau gerendert wird. Niedrige Werte können die Leistung stark beeinträchtigen. Um die Vorschauen zu stoppen, setzen Sie den Wert auf mehr als 360°. Weiterhin können Sie den Modus konfigurieren, in dem die Anwendung gestartet wird. Gültige Werte sind:
```
default-mode=Orbital Elements
default-mode=Orbital Nodes
```
### Maintenance
Die App wird nicht aktiv maintained. Aber aufgrund der wenigen Abhängigkeiten sollte sie gut funktionieren. Im Falle von Problemen treten sie bitte mit mir in Kontakt.

## ENGLISH

A simple python app to visualize the orbital elements and the ascending/descending node. Built with matplotlib for a German student project. Development on the main branch is however done in English.
### Install
There are two ways of installing the program:
#### Using the python3 runtime
* Get the source code by running these comands inn a terminal
```
git clone https://github.com/koslowto/astrometor
cd astrometor/
```
* Install the dependencies
```
pip install matplotlib numpy
```
* Run the app
```
python3 main.py
```
##### Troubleshooting
You may need to use a virtual environment to install the dependencies and run the program.
```
python3 -m venv venv
source venv/bin/activate
```
You might also need to install PyQt5 as a graphics backend if you're encountering problems.

```
pip install pyqt5
``` 
#### Using the .deb package (only works on Debian-based distributions, e.g. Ubuntu, Linux Mint...)
* Download the latest release
* Go to your download location in a terminal
```
cd <your download location>
```
* Install the package
```
dpkg -i astrometor.deb
```
* The app can now be run from your system menu
### Configuration
The configuration file is located in ~/.config/astrometor/astrometor.conf (hidden directory). You can change the update interval for the preview, when dragging sliders.
```
prev_interval=[1-361]
```
The value configures the degrees by which you need to change the slider for a new preview to be rendered. Low values might seriously impact performance. To stop previews set the value to be larger than 360.
Secondly, you can configure the mode in which the app launches. Valid values are:
```
default-mode=Orbital Elements
default-mode=Orbital Nodes
```
### Maintenance
The app is not actively maintained. But due to its few dependencies it should work fine. In case of any issues please reach out to me.
