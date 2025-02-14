# QRcodeticketsApp

**QRcodeticketsApp** Jest to aplikacja internetowa oparta na Django, zaprojektowana w celu ułatwienia rezerwacji biletów na filmy, z wbudowaną generacją kodów QR do potwierdzenia biletów. Aplikacja pozwala użytkownikom przeglądać dostępne filmy, rezerwować bilety i otrzymywać kod QR do potwierdzonych biletów. Kod QR może zostać zeskanowany w celu walidacji w kinie lub na wydarzeniu. Projekt ten został podjęty w celu zbadania integracji Django z generowaniem kodów QR i systemami biletowymi.

---

## Table of Contents
- [Informacje ogólne](#general-information)
- [Użyte technologie](#technologies-used)
- [Funkcje](#features)
- [Zrzuty ekranu](#screenshots)
- [Konfiguracja](#setup)
- [Kroki instalacji](#installation-setup)
- [Użycie](#usage)
- [Status projektu](#project-status)
- [Możliwości rozwoju](#room-for-improvement)
- [Kontakt](#contact)
  
---

## Informacje ogólne

**QRcodeticketsApp** Jest to prosty i wydajny system biletowy, który integruje funkcjonalność kodów QR do szybkiej i bezpiecznej weryfikacji biletów. Aplikacja umożliwia użytkownikom przeglądanie i filtrowanie filmów, rezerwowanie biletów oraz otrzymywanie unikalnego kodu QR dla każdej rezerwacji. Aplikacja stanowi wprowadzenie do budowania systemu biletowego na filmy z wykorzystaniem Django.

- **Jaki problem rozwiązuje ta aplikacja?**  
  Celem jest zaoferowanie cyfrowego rozwiązania do rezerwacji biletów, poprawa doświadczeń użytkowników poprzez automatyczne generowanie biletów oraz zbadanie integracji kodów QR w aplikacji realnego świata.

- **Jaki jest cel Twojego projektu?**  
  Celem jest zaoferowanie cyfrowego rozwiązania do rezerwacji biletów, poprawa doświadczeń użytkowników poprzez automatyczne generowanie biletów oraz zbadanie integracji kodów QR w aplikacji realnego świata.

- **Dlaczego podjąłeś się tego projektu?**  
  Podjąłem się tego projektu, aby nauczyć się pracy z Django przy tworzeniu systemów biletowych oraz zrozumieć, jak kody QR mogą być użyte do zwiększenia bezpieczeństwa i wygody systemów rezerwacyjnych.

---

## Użyte technologie

- **Django** - Version 5.1.5  
  Framework webowy w języku Python używany do tworzenia logiki backendowej aplikacji.
  
- **qrcode** - Version 7.3.1  
  Biblioteka Pythona używana do generowania kodów QR dla każdej rezerwacji biletu.

- **SQLite** - Version 3.36.0  
  Lekka baza danych używana do przechowywania danych o biletach i filmach.

- **Bootstrap** - Version 5.3.0  
  Framework frontendowy używany do stylizacji aplikacji i zapewnienia responsywnego projektu.

---

## Funkcje

- **Movie Listing**: Przeglądaj dostępne filmy wraz z ich szczegółami.
- **Booking Tickets**: Rezerwuj bilety na wybrany film i otrzymuj potwierdzenie.
- **QR Code Generation**: Każda rezerwacja generuje unikalny kod QR do weryfikacji biletu.
- **Filter Movies**: Użyj opcji filtrowania, aby przeglądać filmy według gatunku lub roku.

---

## Zrzuty ekranu

![Movie Booking Page](https://github.com/user-attachments/assets/153512f8-3044-4632-aed7-4da5e9354b19)

![Book ticket](https://github.com/user-attachments/assets/6944a088-a4e4-43d7-ab76-98b6ecebdc78)

![Ticket comfirmation](https://github.com/user-attachments/assets/c0df675a-4719-47f8-a38d-372eb9af1844)

---

## Konfiguracja

Przed uruchomieniem projektu, należy zainstalować następujące zależności:

- **Python** - Version 3.x  
- **Django** - Version 5.1.5
- **qrcode** - Version 7.3.1
- **django-filters** - Version 2.4.0

---

## Kroki instalacji

Sklonuj repozytorium:

git clone https://github.com/yourusername/QRcodeticketsApp.git

---

## Użycie

1. **Dostęp do strony głównej**: Po uruchomieniu serwera, odwiedź http://127.0.0.1:8000/movies/, aby zobaczyć listę dostępnych filmów.

2. **Rezerwacja biletu**: Wybierz film i przejdź do rezerwacji biletu, wypełniając wymagane dane.

3. **Generowanie kodu QR**: Po dokonaniu rezerwacji, na stronie potwierdzenia pojawi się kod QR dla biletu.

4. **Weryfikacja biletu**: Pokaż wygenerowany kod QR na wydarzeniu lub w kinie w celu weryfikacji.

---

## Status projektu

Projekt jest zakończony, ale może być dalej rozwijany.

**Zakończone**: Wszystkie kluczowe funkcje, w tym lista filmów, rezerwacja biletów oraz generowanie kodów QR, są w pełni funkcjonalne.

---

## Możliwości rozwoju

**Ulepszenie 1**: Zintegrowanie bramki płatności do przetwarzania płatności przy rezerwacji biletów.  
**Ulepszenie 2**: Dodanie możliwości przeglądania historii rezerwacji biletów przez użytkowników.

## To Do:

**Funkcja 1**: Implementacja systemu powiadomień e-mail dla potwierdzeń biletów.  
**Funkcja 2**: Dodanie recenzji i ocen filmów.

---

## Kontakt

Created by @Sofia - feel free to contact me!

---
   
