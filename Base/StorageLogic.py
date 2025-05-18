import sqlite3
from pathlib import Path

# Initialisierung der Datenbank
DB_PATH = Path("report.db")

# Erstellung der Tabelle
def init_db():
    try:
        connection = sqlite3.connect(DB_PATH)
        cursor = connection.cursor()
        cursor.execute("""
            CREATE TABLE IF NOT EXISTS WSFEITS (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                titlederst0rung TEXT,
                beschreibung TEXT,
                namedasmeldenden TEXT,
                kategorie TEXT
            )
        """)
        connection.commit()
        print("DB initialisiert.")
    except Exception as e:
        print("Fehler beim Erstellen der DB:", e)
    finally:
        if connection:
            connection.close()

# Einfügen von Daten in die Tabelle
def insert_report(data):
    try:
        connection = sqlite3.connect(DB_PATH)
        cursor = connection.cursor()
        cursor.execute("""
            INSERT INTO WSFEITS (titlederst0rung, beschreibung, namedasmeldenden, kategorie)
            VALUES (?, ?, ?, ?)
        """, (
            data.titlederst0rung,
            data.beschreibung,
            data.namedasmeldenden,
            data.kategorie
        ))
        connection.commit()
        print("Bericht hinzugefügt.")
    except Exception as e:
        print("Fehler beim Einfügen:", e)
        raise
    finally:
        if connection:
            connection.close()

# Abrufen von Daten aus der Tabelle zur Anzeige in HTML oder via JavaScript
def get_all_reports():
    connection = None
    try:
        connection = sqlite3.connect(DB_PATH)
        connection.row_factory = sqlite3.Row  # для словникового доступу
        cursor = connection.cursor()
        cursor.execute("SELECT id, titlederst0rung, beschreibung, namedasmeldenden, kategorie FROM WSFEITS")
        rows = cursor.fetchall()
        return [dict(row) for row in rows]
    except Exception as e:
        print("Fehler beim Abrufen:", e)
        return []
    finally:
     if connection:
         connection.close()

# Löschen eines Eintrags (einer Zeile) aus der Tabelle per Befehl
def delete_report_by_id(id_to_delete: int):
    try:
        connection = sqlite3.connect(DB_PATH)
        cursor = connection.cursor()
        cursor.execute("DELETE FROM WSFEITS WHERE id = ?", (id_to_delete,))
        connection.commit()
        print(f"Eintrag mit ID {id_to_delete} gelöscht.")
    except Exception as e:
        print("Fehler beim Löschen:", e)
    finally:
        if connection:
            connection.close()

# deleteEntryById() wird per JavaScript verwendet
# delete_report_by_id() wird per Python verwendet. Bei Löschung wird empfohlen, die Seite neu zu laden.
# loadReports() zeigt die gesamte Tabelle per JavaScript an
# from pprint import pprint; pprint(get_all_reports()) zeigt die Tabelle per Python an


