# WS_f-r_ein_IT_SH_Ihor_Sanzharevskyi
Meine Project für Test Arbeit. Aufgabe "Webbasierter Störungserfasser für ein IT-Systemhaus"

Szenario:

Ein interner Mitarbeiter bei ccnet möchte eine einfache Webanwendung, um kleinere IT-Störungen im Unternehmen zu melden – z. B. „Drucker geht nicht“, „Outlook startet nicht“, „VPN bricht ab“. Diese Informationen 

sollen gesammelt und angezeigt werden.

Aufgabenstellung:

Erstelle eine einfache Webanwendung zur Störungserfassung mit folgenden Funktionen:
 
  Frontend:
  
    Formular zur Eingabe einer neuen Störung mit folgenden Feldern:
    
      Titel der Störung
      
      Beschreibung
      
      Name des Meldenden
      
      Kategorie (Drucker, Software, Netzwerk, Sonstiges)
    
    Übersicht der bisher gemeldeten Störungen als Liste/Tabelle
  
  Backend (z. B. in PHP oder Python/Flask):
    
    Verarbeitung der Formulardaten (Speicherung lokal in einer Datei oder in einer SQLite/MySQL-Datenbank)
    
    Abrufen und Anzeigen aller gemeldeten Störungen
    
    (Optional) Möglichkeit zum „Löschen“ einzelner Einträge
  Anforderungen:
    
    Klar strukturierter und kommentierter Code
    
    Responsive Gestaltung (z. B. mit Bootstrap)
    
    Einfache Fehlerbehandlung (z. B. „Feld darf nicht leer sein“)
    
    (Optional) Eingabefeld für Priorität (hoch/mittel/niedrig)
 

Entpacken Sie die Datei

Setup_WS_for_an_IT_SH_Ihor_Sanzharevskyi.zip. Führen Sie anschließend

die Datei Installer.exe aus, um die Anwendung zu installieren. Nach der

Installation finden Sie die ausführbare Datei WS_für_ein_IT_SH_Ihor_Sanzharevskyi.exe im

Installationsverzeichnis oder, falls Sie „Verknüpfung auf dem Desktop

erstellen“ ausgewählt haben. Führen Sie diese Datei aus, um den FastAPIServer zu aktivieren. Ein Browserfenster mit der Webanwendung öffnet sich

automatisch, und in der Konsole wird folgender Text angezeigt:

=== FastAPI-Server gestartet ===

Die Weboberfläche ist geöffnet: http://{local_ip}:8000

Geben Sie die folgenden Python-Befehle ein (z. B. get_all_reports()):

In der F12-Konsole des Browsers können Sie JavaScript-Befehle wie

deleteEntryById() verwenden, um Einträge zu löschen, oder loadReports(), um

alle Einträge anzuzeigen. In der Python-Konsole der Anwendung können Sie

unter anderem mit delete_report_by_id(ID) einen bestimmten Eintrag löschen

oder from pprint import pprint; Verwenden Sie pprint(get_all_reports()), um die

Datenbankeinträge tabellarisch anzuzeigen. Die Webanwendung ist jederzeit

über http://{local_ip}:8000 erreichbar, wobei {local_ip}} Ihre lokale IPAdresse ist, z. B. 127.0.0.1 oder 192.168.X.X. Zum Beenden schließen Sie

einfach das Konsolenfenster oder beenden die Anwendung direkt.
