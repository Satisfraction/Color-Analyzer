# Color Analyzer Widget

Dies ist ein PyQt5-Widget, das es Ihnen ermöglicht, die durchschnittliche Farbe eines Bildes zu analysieren und sie als Textdatei zu speichern.

## Verwendung

Um das Color Analyzer Widget zu verwenden, befolgen Sie diese Schritte:

1. Wählen Sie ein Bild aus, indem Sie auf die Schaltfläche "Open File" klicken oder den Dateipfad manuell in das Texteingabefeld eingeben.
2. Klicken Sie auf die Schaltfläche "Analyze Color", um die durchschnittliche Farbe des ausgewählten Bildes zu analysieren.
3. Die durchschnittliche Farbe wird im hexadezimalen Format unterhalb der Schaltfläche "Farbe analysieren" angezeigt.
4. Das ausgewählte Bild wird im Widget angezeigt.
5. Klicken Sie auf die Schaltfläche "Save Color", um die durchschnittliche Farbe als Textdatei zu speichern.

## Abhängigkeiten

Stellen Sie sicher, dass Sie die folgenden Abhängigkeiten installiert haben:

- PyQt5
- Pillow

## Funktionen

- `initUI()`: Definiert die Benutzeroberfläche des Widgets.
- `get_file()`: Ruft den Dateipfad des ausgewählten Bildes ab.
- `get_color()`: Analysiert die Farbe des ausgewählten Bildes und zeigt sie an.
- `analyze_color(image_path)`: Analysiert die Farbe eines Bildes und gibt die durchschnittliche Farbe zurück.
- `show_image(image_path)`: Zeigt das ausgewählte Bild im Widget an.
- `save_color()`: Speichert die durchschnittliche Farbe als Textdatei.

## Hinweis

Dieses Widget wurde von Satisfraction erstellt und unter der MIT-Lizenz lizenziert.