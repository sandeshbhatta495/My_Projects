# Restaurant & Café Management System

A comprehensive Python GUI application for managing restaurant operations including menu management, orders, billing, table reservations, inventory tracking, and daily profit reporting.

## 📋 Features

### 1. **Dashboard**
- Real-time overview of daily sales, orders, and profit
- Active table reservations display
- Low stock alerts
- Recent orders tracking

### 2. **Menu Management**
- Add, edit, and delete menu items
- Categorize items (Drinks, Meals, Snacks, Desserts)
- Set prices and availability
- Search and filter functionality

### 3. **Order Management**
- Interactive order creation interface
- Shopping cart functionality
- Automatic price calculation
- Tax (10%) and service charge (5%) application
- Discount support
- Order history tracking

### 4. **Billing & Invoices**
- Comprehensive order history
- PDF invoice generation
- Filter by status and date
- Mark orders as completed/cancelled
- Detailed invoice with itemized breakdown

### 5. **Table Reservations**
- Visual table layout (20 tables)
- Real-time availability status
- Reservation management
- Customer information tracking
- Date-based reservation viewing

### 6. **Inventory Management**
- Track ingredient quantities
- Low stock alerts
- Category-based organization
- Cost tracking and total value calculation
- Quick quantity adjustment
- Minimum quantity thresholds

### 7. **Profit Tracking**
- Daily sales vs expenses
- Automatic profit calculation
- Summary statistics

## 🗂️ Project Structure

```
restaurant_app/
│
├── main.py                      # Application entry point
├── README.md                    # This file
├── requirements.txt             # Python dependencies
│
├── ui/                          # User interface modules
│   ├── dashboard_ui.py         # Dashboard interface
│   ├── menu_ui.py              # Menu management
│   ├── order_ui.py             # Order creation
│   ├── billing_ui.py           # Billing & invoices
│   ├── inventory_ui.py         # Inventory management
│   └── tables_ui.py            # Table reservations
│
├── backend/                     # Backend logic
│   └── database.py             # SQLite database manager
│
└── data/                        # Database files (auto-created)
    └── restaurant.db           # Main database
```

## 🚀 Installation & Setup

### Prerequisites
- Python 3.10 or higher
- pip (Python package manager)

### Step 1: Install Dependencies

```bash
pip install -r requirements.txt
```

### Step 2: Run the Application

```bash
python main.py
```

The application will automatically create the necessary database and folders on first run.

## 📦 Dependencies

- **tkinter**: GUI framework (included with Python)
- **sqlite3**: Database (included with Python)
- **reportlab**: PDF generation (optional, falls back to text files)

## 🎯 Usage Guide

### Getting Started

1. **Launch the application** by running `python main.py`
2. **Navigate** using the sidebar menu
3. **Start with Menu Management** to add your restaurant items
4. **Create Orders** by selecting items and adding to cart
5. **Manage Tables** for reservations
6. **Track Inventory** to monitor stock levels

### Menu Management

1. Click **"Menu"** in the sidebar
2. Fill in item details (name, category, price, description)
3. Click **"Add New"** to add items
4. Select items to **Update** or **Delete**
5. Use filters to search by category or name

### Creating Orders

1. Click **"Orders"** in the sidebar
2. Select items from the menu list
3. Set quantity and click **"Add to Cart"**
4. Enter table number and customer name
5. Apply discount if needed
6. Click **"Place Order"**

### Generating Invoices

1. Go to **"Billing"** section
2. Select an order from the list
3. Click **"Generate PDF Invoice"**
4. Choose save location
5. Invoice will be saved as PDF (or text file)

### Managing Reservations

1. Click **"Tables"** in the sidebar
2. View table availability (Green = Available, Red = Reserved)
3. Fill in reservation details
4. Click table number or enter manually
5. Click **"Add Reservation"**
6. Use date selector to view different dates

### Tracking Inventory

1. Navigate to **"Inventory"**
2. Add new items with quantities and costs
3. Set minimum quantity thresholds
4. Use **Quick Adjust** for stock updates
5. Monitor low stock alerts
6. View total inventory value

## 🎨 Features Breakdown

### Automatic Calculations
- **Tax**: 10% of subtotal
- **Service Charge**: 5% of subtotal
- **Total**: Subtotal + Tax + Service - Discount
- **Profit**: Sales - Expenses

### Data Validation
- Required field checking
- Numeric value validation
- Date format validation
- Duplicate entry prevention

### User Experience
- Clean, modern interface
- Color-coded status indicators
- Real-time updates
- Search and filter capabilities
- Responsive design

## 💾 Database Schema

### Tables

1. **menu_items**: Restaurant menu items
2. **orders**: Customer orders with details
3. **reservations**: Table reservations
4. **inventory**: Stock tracking
5. **daily_summary**: Daily sales/profit data
6. **expenses**: Business expenses

## 🔧 Customization

### Adding More Tables
Edit `tables_ui.py`, modify the grid layout in `create_table_layout()`:

```python
for i in range(5):  # Change row count
    for j in range(6):  # Change column count
```

### Changing Tax/Service Rates
Edit calculation methods in `order_ui.py` and `billing_ui.py`:

```python
tax = subtotal * 0.10  # 10% tax
service = subtotal * 0.05  # 5% service charge
```

### Adding Categories
Add to the category lists in respective UI files:

```python
categories = ["Drinks", "Meals", "Snacks", "Desserts", "Your_New_Category"]
```

## 📊 Sample Data

The application includes sample data for quick testing:
- 10 menu items across 4 categories
- 8 inventory items
- Sample categories and units

## 🐛 Troubleshooting

### PDF Generation Not Working
If `reportlab` is not installed, the app falls back to text files. Install it:

```bash
pip install reportlab
```

### Database Errors
If you encounter database issues:
1. Delete the `data` folder
2. Restart the application
3. Database will be recreated with sample data

### Display Issues
Ensure your screen resolution is at least 1000x600 pixels.

## 🚀 Building Executable (Optional)

To create a standalone executable:

```bash
pip install pyinstaller
pyinstaller --onefile --windowed --name "Restaurant_Manager" main.py
```

The executable will be in the `dist` folder.

## 📝 Future Enhancements

Potential features to add:
- User authentication and roles
- Multi-location support
- Employee management
- Kitchen display system
- Online ordering integration
- Analytics and charts
- Backup/restore functionality
- Multi-language support

## 🤝 Contributing

This is an educational project. Feel free to:
- Fork the repository
- Add new features
- Fix bugs
- Improve documentation
- Share improvements

## 📄 License

This project is provided as-is for educational purposes.

## 👥 Support

For issues or questions:
1. Check the troubleshooting section
2. Review the code comments
3. Verify all dependencies are installed
4. Ensure Python version is 3.10+

## 🎓 Learning Resources

This project demonstrates:
- **OOP Principles**: Classes, inheritance, encapsulation
- **GUI Development**: Tkinter widgets and layouts
- **Database Operations**: SQLite CRUD operations
- **File Handling**: PDF and text file generation
- **Data Validation**: Input checking and error handling
- **Modular Design**: Separate UI and backend logic

---

**Developed as a comprehensive restaurant management solution using Python, Tkinter, and SQLite.**