# AstroMetor

## DEUTSCH (English version available below)

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
Wenn sie das .deb-Paket benutzen, befindet sich die Konfigurationsdatei im Verzeichnis ~/.config/astrometor/config.json. Dabei handelt es sich um ein verstecktes Verzeichnis. Wenn sie es im Dateimanager nicht sehen, aktivieren sie die Option "versteckte Dateien anzeigen" (meist STRG+H).
Das Programm wird mit json konfiguriert. Achten sie auf korrekte json-Syntax beim bearbeiten der Datei (https://jsonchecker.com/). Die Konfigurationsdatei kann bei Problemen jederzeit zurückgesetzt werden, indem man sie löscht und die App nocheinmal startet.
#### Label
Hiermit kann definiert werden, wie die Knöpfe fürs Umschalten der Modi heißen,
```
"labels": {
    "Bahndings": "Bahnelemente",
    "Knotendings": "Fruehlingspunkt"
}
```
und in welcher Reihenfolge sie angezeigt werden.
```
"labels": {
    "Frühlingspunkt": "Fruehlingspunkt",
    "Bahnelemente": "Bahnelemente"
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
Die App wird nicht aktiv maintained. Aber aufgrund der wenigen Abhängigkeiten sollte sie gut funktionieren. Im Falle von Problemen treten sie bitte mit mir in Kontakt.
