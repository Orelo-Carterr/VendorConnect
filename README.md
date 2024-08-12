# VendorConnect

## Overview

**VendorConnect** is a Django-based platform designed to enhance the campus dining experience. It connects students and staff with a variety of food vendors, offering a seamless way to explore menus, place orders, and enjoy exclusive deals. The platform is built to provide convenience, variety, and quality, all in one place.

## Features

- **Vendor Management**: Vendors can easily register, manage their menus, and process orders.
- **Menu Exploration**: Users can browse through various categories and menu items from different vendors.
- **Order Placement**: Secure and efficient order processing, with options for pickup or delivery.
- **User Reviews**: Customers can leave reviews and ratings for vendors, helping others make informed choices.
- **Responsive Design**: Optimized for both desktop and mobile devices.
- **Admin Dashboard**: Full control over user management, orders, and vendor operations.

## Installation

### Prerequisites

- Python 3.12+
- Virtualenv
- asgiref==3.8.1
- Django==5.1
- sqlparse==0.5.1
- tzdata==2024.1

### Setup Instructions

1. **Clone the repository:**

   ```bash
   git clone https://github.com/Orelo/VendorConnect.git
   cd VendorConnect
   ```
2. **Create a virtual environment**
   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows use `venv\Scripts\activate`
   ```
3. **Install dependencies**
   ```bash
   pip install -r requirements.txt
   ```
4. **Set up the database**
   ```bash
   python manage.py migrate
   ```
5. **Create a superuser:**
   ```bash
   python manage.py createsuperuser
   ```
6. **Run the development server**
   ```bash
   python manage.py runserver
   ```
7. **Access the application**
    Open your browser and go to http://127.0.0.1:8000/ to see VendorConnect in action.

## Project Structure

- `VendorConnect/` - Main Django project folder.
- `mainapp/` - Contains the core application code, including models, views, and templates.
- `static/` - Static files like CSS, JavaScript, and images.
- `templates/` - HTML templates for the frontend.
- `requirements.txt` - Python dependencies for the project.

## Contributing

We welcome contributions! Please follow these steps:

1. Fork the repository.
2. Create a new branch (`git checkout -b feature-branch`).
3. Make your changes.
4. Commit your changes (`git commit -am 'Add some feature'`).
5. Push to the branch (`git push origin feature-branch`).
6. Create a new Pull Request.

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## Contact

For any inquiries or support, please contact the project maintainer at [`aikulolaoreoluwa222@gmail.com`](mailto:aikulolaoreoluwa222@gmail.com).




