# 🛍️ Online Shop API

A feature-rich Django backend for an online store, supporting Persian translation, advanced product management, cart and order systems, and full Docker deployment. Built with scalability, clean architecture, and internationalization in mind.

---

## 🚀 Features

✅ **User Authentication**
Django Allauth integration for registration, login, logout, and password management.

✅ **Product Management**
Products, categories, media uploads (with Pillow), and CKEditor integration for rich text descriptions.

✅ **Shopping Cart & Orders**
Add-to-cart, quantity updates, order placement, and tracking.

✅ **Internationalization (i18n)**
Persian translation, Jalali date support, and Persian number formatting.

✅ **Admin Interface**
Django admin for managing products, users, orders, and content.

✅ **Pages & Templates**
Dynamic pages, homepage, about page, and template-based views.

✅ **Static & Media Handling**
Proper separation of static files, media uploads, and product covers.

✅ **Dockerized Setup**
Ready-to-use `Dockerfile` and `docker-compose.yml` for container deployment.

---

## ⚙️ Tech Stack

* **Backend:** Django, Django REST Framework
* **Auth:** Django Allauth
* **Database:** PostgreSQL / SQLite (development)
* **Rich Text:** CKEditor
* **Image Processing:** Pillow
* **Containerization:** Docker, docker-compose

---

## 📦 Installation

```bash
git clone https://github.com/hatef97/online_shop.git
cd online_shop
```

### Setup virtual environment

```bash
python -m venv venv
source venv/bin/activate  # Windows: venv\Scripts\activate
pip install -r requirements.txt
```

### Configure .env

```
DEBUG=True
SECRET_KEY=your-secret-key
DATABASE_URL=postgres://user:password@localhost:5432/online_shop
```

### Run migrations & create superuser

```bash
python manage.py migrate
python manage.py createsuperuser
```

### Start development server

```bash
python manage.py runserver
```

### Using Docker

```bash
docker-compose up --build
```

---

## 🗂 Project Structure

```
accounts/         # Django Allauth setup
cart/            # Cart app
config/          # Project settings
media/           # Product images
orders/          # Order processing
pages/          # Static and dynamic pages
persian_translate/ # Jalali date and Persian numbers
products/        # Product models and APIs
static/         # Static assets
staticfiles/    # CKEditor and external static files
templates/      # Django templates
```

---

---

## 🤝 Contributing

We welcome contributions! Please open an issue or submit a pull request.

---
