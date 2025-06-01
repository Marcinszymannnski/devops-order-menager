# 🧾 DevOps Order Manager

**DevOps Order Manager** to projekt mikroserwisowy oparty o konteneryzację, mający na celu symulację rzeczywistej aplikacji do zarządzania zamówieniami i płatnościami. Projekt został stworzony w celach edukacyjnych (DevOps / Backend) i umożliwia testowanie integracji wielu usług, baz danych oraz orkiestracji z Docker Compose.

---

## ✅ Aktualny stan projektu 01.06.2025

W obecnej wersji zrealizowano:

### 🔧 Mikroserwisy

- `orders` – zarządza zamówieniami klientów (POST, GET)
- `payments` – obsługuje płatności powiązane z zamówieniami (POST, GET)

### 🗃️ Bazy danych

Każdy mikroserwis posiada własną bazę PostgreSQL:

- `orders-db` dla serwisu `orders`
- `payments-db` dla serwisu `payments`

Każdy serwis korzysta z SQLAlchemy i osobnej konfiguracji środowiska (`DATABASE_URL`).

### 🐳 Docker / Docker Compose

- Każdy serwis ma osobny `Dockerfile`
- Całość zarządzana z `docker-compose.yml`
- Przy starcie uruchamiane są 4 kontenery:
  - `orders`, `orders-db`, `payments`, `payments-db`

---

## ▶️ Jak uruchomić

### 1. Wymagania

- Docker
- Docker Compose

### 2. Uruchomienie

Z poziomu głównego katalogu:


docker compose up --build

### 3.Testowanie

### Tworzenie zamówienia: 
curl -X POST http://localhost:5000/order \
     -H "Content-Type: application/json" \
     -d '{"item": "Laptop", "price": 2999}'

### Pobieranie zamówienia: 
curl http://localhost:5000/order/1


### Tworzenie płatności:
curl -X POST http://localhost:5001/payment \
     -H "Content-Type: application/json" \
     -d '{"order_id": 1, "status": "PAID"}'
     
### Pobieranie płatności:
curl http://localhost:5001/payment/1



