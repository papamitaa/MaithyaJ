# Simplified Airline Booking System

## Overview
This is a Django API-based application for a simplified airline booking system.

## Features
- CRUD operations for flights and passengers.
- Relationships: A flight can have multiple passengers; a passenger belongs to one flight.
- Endpoints:
  - `/api/flights/`
  - `/api/passengers/`

## Setup Instructions
1. Clone the repository:
git clone <https://github.com/papamitaa/airline-booking-164014> cd airline_booking
2. Install dependencies:
pip install -r requirements.txt
3. Run migrations:
python manage.py migrate
4. Start the development server:
python manage.py runserver

## API Endpoints
- Flights: `/api/flights/`
- Passengers: `/api/passengers/`

## Author
Brian Mitaa
