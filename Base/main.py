from fastapi import FastAPI, Request
from fastapi.responses import HTMLResponse
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel
# Verbindung zur Logik der Datenbank
from Base.StorageLogic import  insert_report, init_db, get_all_reports, delete_report_by_id
# Aktivierung der Webanwendung
app = FastAPI()
# Einbindung des Frontends (JavaScript, CSS, HTML)
app.mount("/static", StaticFiles(directory="Base/Frontend/Static"), name="static")
templates = Jinja2Templates(directory="Base/Frontend/Templates")
# Aktivierung und Überprüfung der Datenbank and Erstellung der Tabelle
init_db()
# Aktivierung der CORS-Sicherheitsrichtlinien für die Datenübertragung
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_methods=["*"],
    allow_headers=["*"],
)
# Definition einer Klasse zum Empfangen und Übermitteln von Daten an die Datenbanktabelle
class ReportData(BaseModel):
    titlederst0rung: str
    beschreibung: str
    namedasmeldenden: str
    kategorie: str
# Einbindung der HTML-Datei und des gesamten Frontends
@app.get("/", response_class=HTMLResponse)
async def read_root(request: Request):
    return templates.TemplateResponse("index_Report.html", {"request": request})
# Empfangen von Daten und Speichern in der Datenbanktabelle
@app.post("/submit")
async def submit_report(data: ReportData):
    insert_report(data)
    return {"message": "Daten erfolgreich empfangen"}
# Abrufen aller Datenbankeinträge und Rückgabe als JSON (z.B. für die Anzeige in HTML-Tabellen)
@app.get("/get_reports")
async def fetch_reports():
    return get_all_reports()
# Löschen eines Eintrags aus der Tabelle, nur per API-Befehl möglich
@app.delete("/delete/{id}")
async def api_delete_report(id: int):
    success = delete_report_by_id(id)
    if success:
        return {"message": f"Eintrag mit ID {id} wurde gelöscht."}
    else:
        return {"error": f"Löschen des Eintrags mit ID {id} fehlgeschlagen."}

