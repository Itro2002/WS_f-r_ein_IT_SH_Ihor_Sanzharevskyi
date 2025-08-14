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

Projektstruktur

<img width="610" height="362" alt="image" src="https://github.com/user-attachments/assets/e07739d3-4b37-4345-8b4a-f58534140c72" />

Hauptseite

<img width="1898" height="741" alt="image" src="https://github.com/user-attachments/assets/2d4e5cb3-9116-4516-b408-e3cdc4023abc" />

<img width="1897" height="871" alt="image" src="https://github.com/user-attachments/assets/b65e64a1-62f4-4a87-ad40-672a4ce90ac4" />

Bedienung des Programms selbst nach der Installation

<img width="1096" height="626" alt="image" src="https://github.com/user-attachments/assets/c427ef08-3ad3-4400-b8e9-e6900595eaa9" />

Der Feedback-Tabelle hinzufügen, dass etwas nicht stimmt.

<img width="1245" height="452" alt="image" src="https://github.com/user-attachments/assets/beceaf5e-8988-401a-8e6f-c71f78631cd5" />

1.	Wie ist Ihre Anwendung aufgebaut?
Meine Anwendung besteht aus einem Frontend, einem Backend und einem Verbindungsteil, der mit FastAPI realisiert ist.  Frontend: HTML (Struktur), CSS (Design) und JavaScript (Interaktion mit dem Backend).  Backend: Python und SQLite übernehmen die Logik und Datenspeicherung.  FastAPI verbindet Frontend und Backend über HTTP-Schnittstellen. 
2.	Warum haben Sie sich für FastAPI entschieden?
Ich habe mich für FastAPI entschieden, weil es:
 sehr schnell und leistungsstark ist, auf Asynchronität ausgelegt ist, sehr gut mit Python kompatibel ist,  und automatische Dokumentation (Swagger UI) bietet, was die Entwicklung erleichtert. Im Vergleich zu Flask oder Django ist FastAPI moderner und performanter, besonders für APIs.
3.	Wie läuft die Kommunikation zwischen Frontend und Backend ab?
Die Kommunikation erfolgt über HTTP-Requests:
 JavaScript im Frontend sendet Anfragen (GET, POST, DELETE) an die FastAPI-Endpunkte.  FastAPI verarbeitet die Anfragen und gibt JSON-Daten zurück.
4.	Welche HTTP-Methoden verwenden Sie und warum?
Ich verwende:
 GET: um Daten vom Server abzurufen (z.B. Berichte anzeigen),
 POST: um neue Daten an den Server zu senden (z.B. neue Berichte erstellen),
 DELETE: um gezielt Einträge zu löschen (in Kombination mit POST für die Auswahl der Zeile).
5.	Wie stellen Sie sicher, dass die eingegebenen Daten valide sind?
Vor dem Speichern überprüft die Funktion `sayReport`, ob alle erforderlichen Felder ausgefüllt sind. Danach wird eine Zusammenfassung der Daten angezeigt, und der Benutzer muss bestätigen, dass alles korrekt ist.
6.	Was passiert bei doppelten Einträgen?
Aktuell gibt es keine direkte Duplikatsprüfung. Einträge können sich leicht unterscheiden (z.B. unterschiedliche Beschreibung oder Schreibweise), weshalb eine strikte Prüfung nicht sinnvoll ist. Das System zeigt jedoch eine Zusammenfassung zur Kontrolle an.
7.	Welche Datenbank verwenden Sie und warum?
Ich verwende SQLite, weil:
 sie leichtgewichtig und schnell einsetzbar ist,  keine zusätzliche Serverkonfiguration nötig ist, sie ideal für kleine bis mittelgroße lokale Anwendungen (z.B. im Büro) ist.
8.	Wie funktioniert die Initialisierung der Datenbank?
Die Funktion `init_db()` wird beim Start des Servers aufgerufen. Sie erstellt (falls nicht vorhanden) die Datenbank und initialisiert die benötigten Tabellen.
9.	Wie würden Sie die Anwendung skalieren, wenn viele Benutzer gleichzeitig Berichte einreichen?
 Ich würde SQLite beibehalten, wegen der Spezifik des Projekts. Die Anwendung ist eher für den internen Bürogebrauch gedacht und nicht für eine globale Nutzung. Deshalb ist eine Hochskalierung aktuell nicht notwendig.
10.	Wie stellen Sie eine benutzerfreundliche Oberfläche sicher?
Ich habe:
 das Layout zentriert und responsiv gestaltet (für verschiedene Geräte), 
 ein einfaches, klares Design umgesetzt,
 CSS verwendet, um die Ansicht auf allen Geräten komfortabel und übersichtlich zu halten.
11.Wie verhindern Sie ungültige Zeichen im Namensfeld?
Mit JavaScript:
Js
input.addEventListener("input", function (e) {
  this.value = this.value.replace(/[^\p{L} ]/gu, "");
});
Damit sind nur Buchstaben und Leerzeichen erlaubt.

12.Wie wird CORS konfiguriert und warum ist das notwendig?
Durch FastAPI-Middleware: 
app.add_middleware(
  CORSMiddleware,
  allow_origins=[""],
  allow_methods=[""],
  allow_headers=[""]
)
Das ist notwendig, damit das Frontend (z.B. aus einem anderen Port) mit dem Backend kommunizieren darf.

13.Gibt es Schutzmaßnahmen gegen SQL-Injection?
   Ja:
   Ich verwende parametrisierte SQL-Abfragen, z.B. mit `cursor.execute("SELECT  FROM tabelle WHERE name=?", (name,))`.
   Benutzer können keinen direkten SQL-Code eingeben, da alle Eingaben gefiltert oder als Parameter übergeben werden.
 
 14.	Wie würden Sie eine Suchfunktion umsetzen?
 Zwei Möglichkeiten:
 Client-seitig (JavaScript filtert bestehende Einträge),
 Server-seitig: über FastAPI-Endpunkt wie `/get_reports?filter=...`, der per SQL nach passenden Einträgen sucht.

15.	Was würden Sie verbessern oder refaktorisieren, wenn Sie mehr Zeit hätten?
    Vielleicht das Error-Handling, obwohl es schon teilweise durch die Konsole umgesetzt ist, wo alle Fehler ausgegeben werden. Auch eine Suchfunktion in der Tabelle könnte man einbauen, aber ich sehe darin          aktuell keinen großen Sinn, da die Anwendung für ein Büro gedacht ist, wo es nur 20–50 Einträge geben kann. Diese Anzahl lässt sich bei Bedarf manuell durchsehen.






