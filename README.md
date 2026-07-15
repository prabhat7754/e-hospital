# 🏥 Smart eHospital Management System

A comprehensive Hospital Management System developed using **Django** that provides an efficient platform for managing patients, doctors, appointments, and real-time health monitoring. The project also integrates **IoT (NodeMCU)** for transmitting patient IDs and supports email notifications for password reset and doctor approval workflows.

---

# 📌 Features

## 👨‍⚕️ Doctor Module

- Doctor Registration
- Doctor Login & Logout
- Doctor Dashboard
- Update Doctor Profile
- Manage Assigned Patients
- Review Patient Health Data
- Submit Medical Reviews
- Receive New Registration Notifications

---

## 🧑‍🤝‍🧑 Patient Module

- Patient Registration
- Patient Login & Logout
- Patient Dashboard
- Update Patient Profile
- Book Available Doctors
- View Health Records
- Real-Time Health Monitoring

---

## 🔐 Authentication

- User Registration
- Secure Login
- Logout
- Forgot Password
- Password Reset via Email
- Doctor Approval System

---

## 📊 Health Monitoring

- Heart Rate Monitoring
- SpO₂ Monitoring
- Temperature Monitoring
- Health Data History
- Review Status Tracking

---

## 📧 Email Services

- Password Reset Email
- Doctor Registration Approval Email
- Consultation Notifications

---

## 🌐 IoT Integration

- Send Logged-in User ID to NodeMCU
- REST API Communication
- JSON Data Exchange

---

# 🛠 Tech Stack

### Backend

- Python
- Django
- SQLite

### Frontend

- HTML5
- CSS3
- Bootstrap 5
- JavaScript

### Database

- SQLite

### Libraries

- Django Crispy Forms
- Crispy Bootstrap 5
- Requests

### Other

- SMTP Email
- NodeMCU
- Git
- GitHub

---

# 📂 Project Structure

```
eHOSPITAL/
│
├── eHospital/
├── registration/
├── templates/
├── static/
├── media/
├── manage.py
├── requirements.txt
└── README.md
```

---

# 🚀 Installation

## Clone Repository

```bash
git clone https://github.com/yourusername/eHospital.git
```

---

## Move to Project

```bash
cd eHospital
```

---

## Create Virtual Environment

### Windows

```bash
python -m venv env
```

Activate

```bash
env\Scripts\activate
```

---

## Install Dependencies

```bash
pip install -r requirements.txt
```

---

## Run Migrations

```bash
python manage.py makemigrations

python manage.py migrate
```

---

## Create Superuser

```bash
python manage.py createsuperuser
```

---

## Run Server

```bash
python manage.py runserver
```

Open

```
http://127.0.0.1:8000/
```

---

# 📸 Screenshots

You can add screenshots here.

Example

- Home Page
- Login Page
- Registration
- Patient Dashboard
- Doctor Dashboard
- Health Monitoring
- Admin Panel

---

# Future Improvements

- AI Health Prediction
- Chatbot Integration
- Video Consultation
- Electronic Medical Records
- Payment Gateway
- Mobile Application
- QR Code Patient ID
- Cloud Deployment
- Docker Support

---

# Learning Outcomes

This project helped in learning:

- Django Class-Based Views
- Authentication System
- CRUD Operations
- Email Integration
- REST Communication
- IoT Integration
- Database Design
- Bootstrap UI
- Django Forms
- Git & GitHub

---

# Author

**Prabhat Singh**

B.Tech Computer Science

Interested in:

- Generative AI
- Computer Vision
- Django Development
- Machine Learning
- AI-powered Healthcare

GitHub:
https://github.com/prabhat7754

LinkedIn:
(Add your LinkedIn URL)

---

# License

This project is developed for learning and educational purposes.
