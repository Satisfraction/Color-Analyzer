# Color-Analyzer

Dieses Programm ist ein einfaches GUI-Tool zum Analysieren der durchschnittlichen Farbe eines Bildes.

Installation:

Dieses Programm benötigt Python 3 und die folgenden Bibliotheken: tkinter, PIL (Python Imaging Library).
Die Bibliotheken können mit pip installiert werden:
pip install tkinter
pip install pillow

Verwendung:

Führen Sie das Programm aus, indem Sie "python color_analyzer.py" in der Kommandozeile eingeben.
Klicken Sie auf die Schaltfläche "Open File", um ein Bild auszuwählen.
Das ausgewählte Bild wird in der Anwendung angezeigt und die durchschnittliche Farbe des Bildes wird berechnet und in Hexadezimalform angezeigt.

Code-Erklärung:

Die Funktion analyze_color nimmt den Pfad zum Bild als Eingabe und gibt die durchschnittliche Farbe des Bildes zurück.
Die Funktion show_image nimmt den Pfad zum Bild als Eingabe und zeigt das Bild in der Anwendung an.
Die Funktion get_file wird aufgerufen, wenn die Schaltfläche "Open File" geklickt wird. Es öffnet ein Dateiauswahldialogfeld, um ein Bild auszuwählen.
Die Funktion get_color wird aufgerufen, wenn die Schaltfläche "Analyze color" geklickt wird. Es ruft die Funktion analyze_color auf, um die durchschnittliche Farbe des ausgewählten Bildes zu berechnen, und zeigt das Bild und die durchschnittliche Farbe in der Anwendung an.

!!Hinweis:

Das Programm zeigt das ausgewählte Bild in einem Label-Widget an. Wenn das Bild zu groß ist, wird es automatisch auf eine Größe von 300 x 300 Pixeln skaliert, um das Label-Widget nicht zu überladen.
