# Kyzyl-Suu Tourism Platform 🇰🇬

A Django web application for hiking and tourism tours in Kyzyl-Suu, Kyrgyzstan.

## Features
- Tour listing and detail pages
- Tour booking system
- Admin-only tour management (edit/delete)
- Clean UI with Tailwind CSS
- Secure order creation

## Tech Stack
- Python 3.10
- Django 5.2
- SQLite (development)
- Tailwind CSS

## Project Structure


config/        - Project settings and global URLs  
core/          - Static pages (home, layout logic)  
tour/          - Tours (models, views, CRUD)  
order/         - Orders and booking logic  
templates/     - Base layout  
static/        - CSS, images, JS  


## Architecture
This project follows Django's MTV pattern:

- Models: Business data (Tour, Order)
- Views: Request handling and permissions
- Templates: UI rendering

Apps are organized by responsibility (feature-based architecture).
