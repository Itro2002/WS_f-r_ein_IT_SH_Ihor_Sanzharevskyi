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

Technologies used: Python (FastAPI), SQLite, HTML/CSS, JavaScript, Bootstrap

Die größten Herausforderungen lagen eher beim Erstellen der Installationsdatei bzw. beim Erstellen der Tabelle selbst und beim Aktivieren aller Szenarien wie z. B. das Aktivieren des Datenübertragungsprogramms

usw. Dies nahm am meisten Zeit in Anspruch.

<img width="610" height="362" alt="image" src="https://github.com/user-attachments/assets/e07739d3-4b37-4345-8b4a-f58534140c72" />

<img width="1898" height="741" alt="image" src="https://github.com/user-attachments/assets/2d4e5cb3-9116-4516-b408-e3cdc4023abc" />

<img width="1897" height="871" alt="image" src="https://github.com/user-attachments/assets/b65e64a1-62f4-4a87-ad40-672a4ce90ac4" />

<img width="1096" height="626" alt="image" src="https://github.com/user-attachments/assets/c427ef08-3ad3-4400-b8e9-e6900595eaa9" />

<img width="1245" height="452" alt="image" src="https://github.com/user-attachments/assets/beceaf5e-8988-401a-8e6f-c71f78631cd5" />





