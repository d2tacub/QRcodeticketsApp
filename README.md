# QRcodeticketsApp

**QRcodeticketsApp** is a Django-based web application designed to facilitate movie ticket booking, with integrated QR code generation for ticket confirmation. The app allows users to view available movies, book tickets, and receive a QR code for their confirmed tickets. The QR code can be scanned for validation at the cinema or event. This project was undertaken to explore the integration of Django with QR code generation and ticketing systems.

Live demo: [Insert live demo link here]

---

## Table of Contents

- [General Info](#general-information)
- [Technologies Used](#technologies-used)
- [Features](#features)
- [Screenshots](#screenshots)
- [Setup](#setup)
- [Usage](#usage)
- [Project Status](#project-status)
- [Room for Improvement](#room-for-improvement)
- [Acknowledgements](#acknowledgements)
- [Contact](#contact)

---

## General Information

**QRcodeticketsApp** is a simple and efficient ticketing system that integrates QR code functionality for quick and secure ticket verification. The app allows users to view and filter movies, book tickets, and receive a unique QR code for each booking. The application serves as an introduction to building a movie ticketing system using Django.

- **What problem does it solve?**  
  The app solves the problem of manual ticket verification by providing a secure and digital solution for confirming movie bookings using QR codes.

- **What is the purpose of your project?**  
  The purpose is to offer a digital solution for ticket bookings, enhance user experience by automating ticket generation, and explore QR code integration in a real-world application.

- **Why did you undertake it?**  
  I undertook this project to learn how to work with Django for creating ticketing systems, and to understand how QR codes can be used to enhance the security and convenience of booking systems.

---

## Technologies Used

- **Django** - Version 5.1.5  
  A Python web framework used for building the backend logic of the app.
  
- **qrcode** - Version 7.3.1  
  A Python library used to generate QR codes for each ticket booking.

- **SQLite** - Version 3.36.0  
  A lightweight database used for storing ticket and movie data.

- **Bootstrap** - Version 5.3.0  
  A front-end framework used for styling the application and ensuring a responsive design.

---

## Features

- **Movie Listing**: View available movies with their details.
- **Booking Tickets**: Book tickets for a selected movie and receive a confirmation.
- **QR Code Generation**: Each booking generates a unique QR code for ticket validation.
- **Filter Movies**: Use filtering options to view movies based on genre or year.

---

## Screenshots

**Example screenshot of the movie booking page:**

![Movie Booking Page](example_screenshot.png)

---

## Setup

### Requirements

Before running the project, you need to have the following dependencies installed:

- **Python** - Version 3.x  
- **Django** - Version 5.1.5
- **qrcode** - Version 7.3.1
- **django-filters** - Version 2.4.0

---

### Installation Steps

1. Clone the repository:
   ```bash
   git clone https://github.com/yourusername/QRcodeticketsApp.git

2. Navigate to the project directory

cd QRcodeticketsApp

3. Create the Django app (if not already created)

python manage.py startapp movies

4. Install required dependencies
Install the required dependencies listed in the requirements.txt file:

pip install -r requirements.txt

5. Apply migrations to set up the database
Run the migrations to set up the initial database:

python manage.py migrate

6. Create a superuser to access the admin panel
Create a superuser so that you can access the Django admin panel:

python manage.py createsuperuser

You will be prompted to enter the username, email, and password for the superuser.

Example:

Username (leave blank to use 'yourusername'): admin
Email address: admin@example.com
Password: ********

7. Run the development server
Start the Django development server

python manage.py runserver

8. Visit the app
Once the server is running, visit http://127.0.0.1:8000/ to use the application.

To access the Django admin panel, visit http://127.0.0.1:8000/admin/ and log in with the superuser credentials you created earlier.

---

## Usage

1. Access the Home Page: Once the server is running, visit http://127.0.0.1:8000/ to see the list of available movies.

2. Book a Ticket: Select a movie and proceed to book a ticket by filling in the required details.

3. Generate QR Code: After booking, a confirmation page will display a QR code for the ticket.

4. Validate the Ticket: Show the generated QR code at the event or cinema for verification.

---

## Project Status

The project is complete but can be enhanced further.

Completed: All core features, including movie listing, ticket booking, and QR code generation, are fully functional.

---

## Room for Improvement

Improvement 1: Integrate payment gateway for processing payments when booking tickets.
Improvement 2: Add the ability to view ticket booking history for users.

## To Do:

Feature 1: Implement an email notification system for ticket confirmations.
Feature 2: Add movie reviews and ratings.

---

## Acknowledgements:

Inspiration: This project was inspired by several Django tutorials on building web applications.
Tutorials: Many thanks to Django Documentation for providing excellent resources on building Django apps.
Libraries: Special thanks to qrcode for offering an easy way to integrate QR code generation into the project.

---

## Contacts

Created by @sofia - feel free to contact me!


   
