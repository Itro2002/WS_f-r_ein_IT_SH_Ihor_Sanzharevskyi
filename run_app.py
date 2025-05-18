import uvicorn
import webbrowser
import threading
import time
import code
import socket

def get_local_ip():
    # Ruft die IP des lokalen Hosts ab (z. B. 192.168.x.x)
    s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    try:
        # Verbindung zu einer nicht vorhandenen Adresse herstellen, um eine lokale IP zu erhalten
        s.connect(("10.255.255.255", 1))
        IP = s.getsockname()[0]
    except Exception:
        IP = "127.0.0.1"
    finally:
        s.close()
    return IP

def start_server():
    uvicorn.run("Base.main:app", host="0.0.0.0", port=8000)

if __name__ == "__main__":
    local_ip = get_local_ip()
    server_url = f"http://{local_ip}:8000"

    # Starten des Servers in einem Hintergrundthread
    threading.Thread(target=start_server, daemon=True).start()

    # Wir warten darauf, dass der Server hochfährt.
    time.sleep(2)

    # Öffnen Sie einen Browser mit einer lokalen IP
    webbrowser.open(server_url)

    # Ausgabe von Meldungen an die Konsole
    print("\n=== FastAPI-Server gestartet ===")
    print(f"Weboberfläche geöffnet: {server_url}")
    print("Geben Sie die folgenden Python-Befehle ein (z. B. get all reports()):\n")

    from Base.StorageLogic import get_all_reports, delete_report_by_id, insert_report
    code.interact(local=locals())