# AstroMetor

## DEUTSCH ([English version available below](#english))

AstroMetor ist eine kleine Python-App zur Visualisierung der Bahnelemente und des aufsteigenden/absteigenden Knotens (Frühlingspunkt). Sie wurde mithilfe von matplotlib als Schulprojekt erstellt. Es gibt einen deutschen Zweig, der Hauptzweig ist aber auf Englisch.
### Installieren
Es gibt zwei Möglichkeiten zur Installation des Programmes:
#### Verwendung der Python3-Laufzeit
* Laden Sie den Quellcode herunter, indem sie folgendes im Terminal ausführen
```
git clone https://github.com/koslowto/astrometor
cd astrometor/
```
* Wenn Sie die deutsche Version benutzen möchten, wechseln Sie auf den deutschen Entwicklungszweig
```
git fetch
git checkout deutsch
```
* Installieren Sie die Abhängigkeiten
```
pip install matplotlib numpy
```
* Starten Sie die Anwendung (dies können Sie auch in ihrer Entwicklungsumgebung (VSCode, Thonny, ...) tun, wenn dort die Abhängigkeiten installiert sind)
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
#### Verwendung des .deb-Pakets (funktioniert nur auf Debian-basierten Linux Distributionen, z.B. Ubuntu, Linux Mint...)
* Laden Sie die neueste Version aus den Releases herunter
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
Wenn Sie das .deb-Paket benutzen, befindet sich die Konfigurationsdatei im Verzeichnis ~/.config/astrometor/config.json. Dabei handelt es sich um ein verstecktes Verzeichnis. Falls es im Dateimanager nicht erscheint, aktivieren Sie die Option "versteckte Dateien anzeigen" (meist STRG+H).
Das Programm wird mit json konfiguriert. Achten Sie auf korrekte json-Syntax beim bearbeiten der Datei (https://jsonchecker.com/). Die Konfigurationsdatei kann bei Problemen jederzeit zurückgesetzt werden, indem man sie löscht und die App nocheinmal startet.
#### Label
Hiermit kann definiert werden, wie die Knöpfe fürs Umschalten der Modi heißen,
```
"labels": {
    "Bahndings": "Orbital Elements",
    "Knotendings": "Orbital Nodes"
}
```
und in welcher Reihenfolge sie angezeigt werden.
```
"labels": {
    "Orbital Nodes": "Orbital Nodes",
    "Orbital Elements": "Orbital Elements"
}
```
#### Preview Interval
Diese Variable gibt an, um wie viel Grad man einen Slider verändern muss, damit eine neue Preview gerendert wird. Werte über 360° sorgen dafür, dass gar keine Previews mehr gezeigt werden.
```
"preview_interval": 361
```
#### Slider
Hiermit können die Werte der Slider zum Aufruf des Programms festgelegt werden.
```
"sliders": {
    "e": 0.9,
    "i": 90,
    "o": 90,
    "w": 90,
    "v": 90
}
```
### Maintenance
Die App wird nicht aktiv maintained. Aber aufgrund der wenigen Abhängigkeiten sollte sie gut funktionieren. Im Falle von Problemen treten Sie bitte mit mir in Kontakt.

## ENGLISH

A simple python app to visualise the orbital elements and the ascending/descending node. Built with matplotlib for a German student project. Development on the main branch is however done in English.
### Install
There are two ways of installing the program:
#### Using the python3 runtime
* Get the source code by running these commands inn a terminal
```
git clone https://github.com/koslowto/astrometor
cd astrometor/
```
* Install the dependencies
```
pip install matplotlib numpy
```
* Run the app (you can also do this in your favourite IDE (VSCode, Thonny...) if all the dependencies are installed)
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
If you are using the .deb package, the configuration file is located in the directory ~/.config/astrometor/config.json. This is a hidden directory. If you do not see it in the file manager, activate the option “Show hidden files” (usually CTRL+H).
The program is configured with json. Pay attention to correct json syntax when editing the file (https://jsonchecker.com/). If problems occur, the configuration file can be reset at any time by deleting it and restarting the app.
#### Label
This can be used to define the names of the buttons for switching modes,
```
"labels": {
    "Place your": "Orbital Elements",
    "text here": "Orbital Nodes"
}
```
and in which order they are displayed.
```
"labels": {
    "Orbital Nodes": "Orbital Nodes",
    "Orbital Elements": "Orbital Elements"
}
```
#### Preview Interval
This variable specifies by how many degrees a slider must be changed for a new preview to be rendered. Values above 360° ensure that no more previews are shown.
```
"preview_interval": 361
```
#### Slider
The initial values of the sliders when launching the program can be defined here.
```
"sliders": {
    "e": 0.9,
    "i": 90,
    "o": 90,
    "w": 90,
    "v": 90
}
```
### Maintenance
The app is not actively maintained. But due to its few dependencies it should work fine. In case of any issues please reach out to me.
