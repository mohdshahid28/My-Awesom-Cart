# 🛒 My Awesome Cart

**My Awesome Cart** is a Django-based e-commerce web application where users can browse products, search for products, add products to their cart, place orders, and make online payments using Paytm.

This project is built using **Python and Django** with **SQLite3** as the database.

---

## 🚀 Features

* 🏠 Home page with product listings
* 🔎 Product search
* 🛍️ Add products to cart
* ➕ Increase or decrease product quantity
* 💰 Cart total and price calculation
* 📦 Checkout and order placement
* 💳 Paytm payment integration
* 🔍 Order tracking using Order ID and Email
* 📝 Blog section
* 📞 Contact Us page
* ℹ️ About Us page
* 👨‍💼 Django Admin Panel for managing products and orders
* 🖼️ Product images
* 📱 Responsive interface using Bootstrap

---

## 🛠️ Technologies Used

* **Python**
* **Django**
* **HTML**
* **CSS**
* **JavaScript**
* **Bootstrap**
* **SQLite3**
* **Paytm Payment Gateway**

---

## 📂 Project Structure

```text
My-Awesome-Cart/
│
├── manage.py
├── db.sqlite3
├── README.md
├── requirements.txt
│
├── shop/
│   ├── models.py
│   ├── views.py
│   ├── urls.py
│   ├── admin.py
│   └── templates/
│
├── blog/
│   ├── models.py
│   ├── views.py
│   ├── urls.py
│   └── templates/
│
├── mysite/
│   ├── settings.py
│   ├── urls.py
│   └── wsgi.py
│
├── templates/
│
└── media/
```

---

## ⚙️ Installation

### 1. Clone the repository

```bash
git clone https://github.com/mohdshahid28/My-Awesom-Cart.git
```

Go inside the project folder:

```bash
cd My-Awesom-Cart
```

### 2. Create a virtual environment

```bash
python -m venv venv
```

Activate the virtual environment on Windows:

```bash
venv\Scripts\activate
```

### 3. Install required packages

```bash
pip install -r requirements.txt
```

If `requirements.txt` is not available, install Django manually:

```bash
pip install django
```

---

## 🗄️ Database

This project uses **SQLite3** as the database.

After installing the dependencies, run:

```bash
python manage.py migrate
```

If you want to create a new admin user:

```bash
python manage.py createsuperuser
```

---

## 💳 Paytm Payment Setup

This project includes **Paytm Payment Gateway integration**.

Before using the payment feature, you need to configure **your own Paytm credentials**.

### Important

**Do not use or share someone else's Merchant ID or Merchant Key.**

Create/configure your own Paytm merchant account and add your own credentials to the project configuration.

For example:

```python
MID = "YOUR_PAYTM_MERCHANT_ID"
MKEY = "YOUR_PAYTM_MERCHANT_KEY"
```

Replace these values with your own credentials.

> ⚠️ Never upload your real Merchant Key, API keys, passwords, or other secret credentials to GitHub.

For security, it is recommended to keep sensitive credentials in environment variables.

---

## ▶️ Run the Project

Start the Django development server:

```bash
python manage.py runserver
```

Then open the following URL in your browser:

```text
http://127.0.0.1:8000/
```

---

## 👨‍💼 Django Admin Panel

You can access the Django admin panel using:

```text
http://127.0.0.1:8000/admin/
```

From the admin panel, you can manage products, orders, and other registered data.

---

## 📸 Screenshots

Screenshots will be added soon.

Some planned screenshots:

* Home Page
* Product Page
* Shopping Cart
* Checkout Page
* Payment Page
* Order Tracking
* Admin Panel

---

## 🔐 Security Note

This project is created for learning and development purposes.

Before deploying it to production:

* Use your own Paytm credentials.
* Keep secret keys outside the source code.
* Do not upload `.env` files.
* Configure Django `SECRET_KEY` securely.
* Set `DEBUG = False`.
* Configure `ALLOWED_HOSTS`.
* Use a production-ready database and web server.

---

## 🎯 Purpose of the Project

The main purpose of this project is to understand how to build an e-commerce website using Django and implement features such as product management, shopping cart functionality, order processing, payment integration, and order tracking.

---

## 👨‍💻 Author

**Mohd Shahid Ansari**

GitHub:
https://github.com/mohdshahid28

---

## ⭐ Support

If you find this project useful or helpful for learning Django, consider giving the repository a ⭐ on GitHub.

---

## 📄 License

This project is created for educational and learning purposes.
