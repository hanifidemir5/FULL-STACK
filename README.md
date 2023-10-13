# FULL-STACK Restaurant Project

![GitHub last commit](https://img.shields.io/github/last-commit/hanifidemir5/FULL-STACK)
![License](https://img.shields.io/badge/license-MIT-blue)

This repository houses a full-stack restaurant project, employing Django, HTML, CSS, JavaScript, and MySQL as the database. Customers can make reservations, view available days and hours, and receive real-time updates to ensure a seamless booking experience.

## Table of Contents

- [Features](#features)
- [Prerequisites](#prerequisites)
- [Installation](#installation)
- [Usage](#usage)
- [License](#license)

## Features

- **Reservation System**: Customers can easily book reservations for their desired date and time.

- **Real-Time Updates**: The project provides real-time feedback, preventing customers from selecting already booked dates and hours.

- **Availability Check**: Customers can check if a specific day and hour are available by selecting their preferred date.

## Prerequisites

Before you begin, ensure you have met the following requirements:

- **Pipenv**: Ensure that `pipenv` is installed and available on your system.

- **Python**: Install Python (>= 3.7) on your system.

## Installation

1. **Clone this repository:**

   ```bash
   git clone https://github.com/hanifidemir5/FULL-STACK.git
   ```

2. **Navigate to the project directory:**

   ```bash
   cd FULL-STACK
   ```

3. **Activate the Pipenv Virtual Environment:**

   ```bash
   pipenv shell
   ```

4. **Install Dependencies:**

   - Install Django and `mysqlclient`:

     ```bash
     pipenv install django
     pipenv install mysqlclient
     ```
5. **Start The Server**
6. 
     ```bash
     cd FullStack
     python manage.py runserver
     ```
## Usage

Once you have the project set up, you can:

- Browse available dates and hours for booking reservations.

- Select a date and time for your reservation.

- Receive real-time feedback on the availability of dates and hours.

## License

This project is licensed under the [MIT License](LICENSE).

Happy dining!
