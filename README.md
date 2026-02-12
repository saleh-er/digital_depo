# 🛒 DigitalDepot | Modular Marketplace

A robust, modular Django marketplace application designed for high scalability and clean architecture. This project features a multi-app structure, custom user authentication, and a dynamic product catalog.

## 🌟 Key Features
- **Modular Architecture:** Apps are organized within a dedicated `apps/` directory for better maintainability.
- **Product Management:** Full CRUD (Create, Read, Update, Delete) functionality for digital and physical products.
- **Search & Discovery:** Real-time filtering system for products by name or category.
- **Custom User Profiles:** Extended authentication system to manage buyers and sellers separately.
- **Responsive UI:** Modern frontend built with Bootstrap 5 and Django Template Inheritance.

## 🛠️ Tech Stack
- **Backend:** Python 3.11, Django 5.x
- **Database:** SQLite (Development) / PostgreSQL ready
- **Frontend:** Bootstrap 5, HTML5, CSS3
- **Architecture:** MVT (Model-View-Template) with nested app discovery

## 📂 Project Structure
```text
digital_depot/
├── apps/               # Custom modular applications
│   ├── products/       # Inventory and catalog logic
│   ├── users/          # Authentication and profile logic
│   └── orders/          # Transaction and cart logic
├── core/               # Project configuration (settings, urls, wsgi)
├── media/              # User-uploaded product images
├── static/             # Global CSS, JS, and Assets
└── templates/          # Global HTML base layouts