// Überprüfung und Aktivierung des Ladens der Datenbank-Tabelle in die HTML-Tabelle beim Laden der Seite
document.addEventListener("DOMContentLoaded", () => {
    loadReports();
});
// Skript, das verhindert, dass andere Zeichen als Buchstaben und Leerzeichen eingegeben werden
const input = document.getElementById('namedasmeldendenInput');
  input.addEventListener('input', function () {
    this.value = this.value.replace(/[^\p{L} ]/gu, '');
  });
// Funktion, die für das Senden der Daten in die Datenbanktabelle zuständig ist und überprüft, ob alle Felder ausgefüllt sind
    function sayReport() {
    // Daten aus allen Eingabefeldern
     const fields = {
     titlederst0rung: document.getElementById('titlederstörungInput').value,
     beschreibung: document.getElementById('beschreibungInput').value,
     namedasmeldenden: document.getElementById('namedasmeldendenInput').value,
     kategorie: document.getElementById('kategorieSelect').value
   };
// Array zur Sammlung von Fehlern
   const messages = {
     titlederst0rung: 'Bitte Titel der Störung eingeben',
     beschreibung: 'Bitte Beschreibung eingeben',
     namedasmeldenden: 'Bitte Name des Meldenden eingeben'
   };
// Überprüfung, ob alle Felder ausgefüllt sind
   const errors = [];
// Wenn Fehler vorhanden sind, zeige eine Warnung
   for (const [field, value] of Object.entries(fields)) {
     if (!value.trim()) {
       errors.push(messages[field]);
     }
   }
// Zeigt ein Bestätigungsfenster mit den eingegebenen Daten an
   if (errors.length > 0) {
     alert('Fehler:\n' + errors.join('\n'));
   } else {
   // Überprüft, ob die Antwort vom Server OK ist, andernfalls wird ein Fehler ausgelöst
     const isCorrect = confirm(`Überprüfen Sie Ihre Daten :\n Title der Störung: ${fields.titlederst0rung}\n Beschreibung: ${fields.beschreibung}\n Name das Meldenden: ${fields.namedasmeldenden}\nKategorie: ${fields.kategorie}\nIst alles richtig?`);
     if (isCorrect) {
      fetch("/submit", {
       method: "POST",
        headers: {
        "Content-Type": "application/json"
       },
       body: JSON.stringify(fields)
       })
    .then(response => {
    // Zeigt bei Erfolg eine Nachricht an und lädt die Tabelle neu mit neuen Daten
    if (!response.ok) {
    throw new Error("Serverfehler: " + response.status);
    }
     return response.json();
    })
    // Bei Fehlern wird eine Fehlermeldung angezeigt
    .then(data => {
     alert("Vielen Dank! Ihre Störung wurde gesendet.\nAntwort vom Server: " + data.message);
     loadReports();
      })
     .catch(error => {
     alert("Fehler beim Senden: " + error);
    });
   }
  }
 }
// Funktion, die die Datenbankdaten in die HTML-Tabelle lädt und in der Konsole anzeigt
function loadReports() {
    fetch("/get_reports")
        .then(response => response.json())
        .then(data => {
            const tableBody = document.querySelector(".table-wrapper table tbody");
            if (!tableBody) {
                console.error("Element tbody Keine Habe!");
                return;
            }
            tableBody.innerHTML = '';

            data.forEach(entry => {
                const row = tableBody.insertRow();


                row.insertCell().textContent = entry.titlederst0rung || '';
                row.insertCell().textContent = entry.beschreibung || '';
                row.insertCell().textContent = entry.namedasmeldenden || '';
                row.insertCell().textContent = entry.kategorie || '';
            });
             console.log("Gesamttabelle geladen:", data);
        })
        .catch(error => {
            console.error("Fehler beim Abrufen der Daten:", error);
        });
}
// Funktion zum Löschen eines Eintrags aus der DataBase Tabelle anhand der ID
window.deleteEntryById = function(id) {
  fetch(`/delete/${id}`, {
    method: "DELETE"
  })
  .then(response => response.json())
  .then(data => {
  // Zeigt Bestätigung an und lädt die Tabelle neu – bei Konsolenlöschung(Python) muss manuell aktualisiert werden
    console.log("Antwort vom Server:", data);
    loadReports();
  })
  // Gibt Fehlermeldung in der Konsole aus, falls beim Löschen ein Fehler auftritt
  .catch(error => {
    console.error("Fehler beim Löschen:", error);
  });
};