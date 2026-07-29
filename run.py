import datetime
import os
import urllib.request

SERVICE_NAME = "${{ values.name }}"


def log(msg):
    print(f"[{datetime.datetime.utcnow().isoformat()}] {SERVICE_NAME} - {msg}", flush=True)


def check_backend():
    # S79 (ADR S0-083, service-ref Phase C -- pod-to-pod) -- BACKEND_URL
    # est vide tant qu'aucune dependance n'est declaree (D5, non-bloquant),
    # ou tant que la resolution nature=pod n'est pas encore implementee.
    # Best-effort, ne fait jamais echouer le job.
    backend_url = os.environ.get("BACKEND_URL", "")
    if not backend_url:
        log("aucun backend reference (BACKEND_URL vide)")
        return
    try:
        with urllib.request.urlopen(backend_url, timeout=5) as resp:
            log(f"backend {backend_url} -> HTTP {resp.status}")
    except Exception as e:
        log(f"backend {backend_url} -> erreur: {e}")


def main():
    log("batch run start")
    check_backend()
    # TODO: remplacer par la logique batch reelle
    log("batch run done")


if __name__ == "__main__":
    main()
