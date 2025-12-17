# 🍽️ Complete Setup Guide - Restaurant Management System

## 📁 Step 1: Create Project Structure

Create the following folder structure on your computer:

```
restaurant_app/
│
├── main.py
├── README.md
├── requirements.txt
├── SETUP_GUIDE.md
│
├── ui/
│   ├── __init__.py
│   ├── dashboard_ui.py
│   ├── menu_ui.py
│   ├── order_ui.py
│   ├── billing_ui.py
│   ├── inventory_ui.py
│   └── tables_ui.py
│
├── backend/
│   ├── __init__.py
│   └── database.py
│
└── data/
    (This folder will be auto-created)
```

### Creating the Folders

**Windows:**
```cmd
mkdir restaurant_app
cd restaurant_app
mkdir ui backend data
```

**Mac/Linux:**
```bash
mkdir -p restaurant_app/ui restaurant_app/backend restaurant_app/data
cd restaurant_app
```

## 📝 Step 2: Create Files

### Create Empty `__init__.py` Files

These files tell Python that the folders are packages:

**ui/__init__.py** (empty file)
**backend/__init__.py** (empty file)

**Windows:**
```cmd
type nul > ui\__init__.py
type nul > backend\__init__.py
```

**Mac/Linux:**
```bash
touch ui/__init__.py
touch backend/__init__.py
```

### Copy All Code Files

Copy the provided code into these files:

1. **main.py** - Main application entry point
2. **backend/database.py** - Database manager
3. **ui/dashboard_ui.py** - Dashboard interface
4. **ui/menu_ui.py** - Menu management
5. **ui/order_ui.py** - Order management
6. **ui/billing_ui.py** - Billing & invoices
7. **ui/tables_ui.py** - Table reservations
8. **ui/inventory_ui.py** - Inventory management
9. **README.md** - Documentation
10. **requirements.txt** - Dependencies

## 🔧 Step 3: Install Python

### Check if Python is Installed

```bash
python --version
```

Or:

```bash
python3 --version
```

You need **Python 3.10 or higher**.

### Install Python (if needed)

1. Go to [python.org](https://www.python.org/downloads/)
2. Download Python 3.10 or higher
3. **Important for Windows**: Check "Add Python to PATH" during installation
4. Complete installation

### Verify Installation

```bash
python --version
pip --version
```

## 📦 Step 4: Install Dependencies

### Navigate to Project Folder

```bash
cd path/to/restaurant_app
```

### Install Required Packages

```bash
pip install -r requirements.txt
```

Or install manually:

```bash
pip install reportlab
```

**Note**: `tkinter` and `sqlite3` come with Python by default.

### Verify Installation

```bash
pip list
```

You should see `reportlab` in the list.

## 🚀 Step 5: Run the Application

### Start the Application

```bash
python main.py
```

### First Run

On first run, the application will:
1. Create the `data` folder (if it doesn't exist)
2. Create `restaurant.db` database
3. Create all necessary tables
4. Add sample data automatically
5. Open the main window

### Expected Behavior

- A window titled "Restaurant & Café Management System" should appear
- You should see a sidebar with navigation options
- Dashboard shows initial statistics (all zeros or sample data)

## ✅ Step 6: Test the Application

### 1. Test Menu Management

1. Click **"Menu"** in sidebar
2. You should see 10 sample menu items
3. Try adding a new item:
   - Name: "Orange Juice"
   - Category: "Drinks"
   - Price: 3.99
   - Click "Add New"
4. Verify item appears in list

### 2. Test Order Management

1. Click **"Orders"** in sidebar
2. Select an item from menu
3. Set quantity and click "Add to Cart"
4. Enter table number: 5
5. Click "Place Order"
6. Should see success message

### 3. Test Billing

1. Click **"Billing"** in sidebar
2. You should see the order you just created
3. Select it and view details
4. Click "Generate PDF Invoice"
5. Save the invoice and verify it opens

### 4. Test Table Reservations

1. Click **"Tables"** in sidebar
2. You should see a 4x5 grid of tables (green = available)
3. Fill in reservation form:
   - Table: 1
   - Name: "John Doe"
   - Phone: "123-456-7890"
   - Date: Today's date
   - Time: 19:00
   - Party Size: 4
4. Click "Add Reservation"
5. Table 1 should turn red

### 5. Test Inventory

1. Click **"Inventory"** in sidebar
2. You should see 8 sample inventory items
3. Try adjusting quantity:
   - Select an item
   - Enter adjustment value (e.g., 10)
   - Click "+" or "-"
4. Verify quantity updates

### 6. Test Dashboard

1. Click **"Dashboard"** in sidebar
2. Verify statistics show:
   - Today's Sales (from orders)
   - Total Orders count
   - Active Tables count
3. Check recent orders list
4. Check low stock alerts

## 🐛 Troubleshooting

### Issue: "ModuleNotFoundError: No module named 'ui'"

**Solution**: Make sure you created `__init__.py` files in `ui` and `backend` folders.

```bash
# Create them manually
touch ui/__init__.py
touch backend/__init__.py
```

### Issue: "tkinter not found"

**Solution**: 

**Ubuntu/Debian:**
```bash
sudo apt-get install python3-tk
```

**Mac:**
```bash
brew install python-tk
```

**Windows**: Reinstall Python and ensure "tcl/tk and IDLE" is checked.

### Issue: "reportlab not found" when generating PDF

**Solution**: 

```bash
pip install reportlab
```

If still not working, the app will fall back to text files automatically.

### Issue: Database errors

**Solution**: 

```bash
# Delete the data folder and restart
rm -rf data  # Mac/Linux
rmdir /s data  # Windows

# Then run the app again
python main.py
```

### Issue: Window too large for screen

**Solution**: Edit `main.py`, change this line:

```python
self.root.geometry("1200x700")
# Change to smaller size, e.g.:
self.root.geometry("1000x600")
```

### Issue: Can't see all buttons/text

**Solution**: Your display scaling might be high. Lower it:
- **Windows**: Settings → Display → Scale
- **Mac**: System Preferences → Displays → Resolution

## 🎯 Quick Start Checklist

- [ ] Python 3.10+ installed
- [ ] All files created in correct folders
- [ ] `__init__.py` files in ui/ and backend/
- [ ] requirements.txt dependencies installed
- [ ] Can run `python main.py` without errors
- [ ] Application window opens
- [ ] Can navigate between sections
- [ ] Sample data visible
- [ ] Can create test order
- [ ] Can generate invoice

## 📚 File Overview

| File | Purpose | Lines |
|------|---------|-------|
| main.py | Application entry point, navigation | ~150 |
| backend/database.py | SQLite database management | ~200 |
| ui/dashboard_ui.py | Dashboard with statistics | ~200 |
| ui/menu_ui.py | Menu CRUD operations | ~350 |
| ui/order_ui.py | Order creation and cart | ~400 |
| ui/billing_ui.py | Billing and PDF invoices | ~350 |
| ui/tables_ui.py | Table reservations | ~400 |
| ui/inventory_ui.py | Inventory tracking | ~450 |

**Total**: ~2,500 lines of Python code

## 🎓 Code Structure

### Object-Oriented Design

Each UI module follows this pattern:

```python
class ModuleUI:
    def __init__(self, parent, db):
        # Initialize with parent frame and database
        self.parent = parent
        self.db = db
        self.create_widgets()  # Build UI
        self.load_data()       # Load from database
    
    def create_widgets(self):
        # Build all UI elements
        pass
    
    def load_data(self):
        # Fetch and display data
        pass
    
    def save_data(self):
        # Save to database
        pass
```

### Database Pattern

All database operations use the Database class:

```python
# Query data
result = self.db.execute_query(query, params)

# Insert data
row_id = self.db.insert(query, params)
```

## 🔐 Best Practices Implemented

✅ **Separation of Concerns**: UI separate from database logic  
✅ **DRY Principle**: Reusable database class  
✅ **Input Validation**: All forms validate before saving  
✅ **Error Handling**: Try-catch blocks for database operations  
✅ **User Feedback**: Success/error messages for all actions  
✅ **Data Integrity**: Foreign key relationships and constraints  
✅ **Modular Design**: Each feature in separate file  
✅ **Comments**: Code documented for clarity  

## 🚀 Next Steps

### After successful setup:

1. **Customize** menu items for your restaurant
2. **Add** real inventory items
3. **Set up** table numbers to match your layout
4. **Train** staff on using the system
5. **Backup** database regularly (copy `data/restaurant.db`)

### Optional Enhancements:

1. **Create executable**:
   ```bash
   pip install pyinstaller
   pyinstaller --onefile --windowed main.py
   ```

2. **Add more features**:
   - Employee management
   - Kitchen display
   - Reports with charts
   - Email invoices

3. **Deploy** on network:
   - Share database on network drive
   - Multiple POS terminals

## 📞 Support

If you encounter issues:

1. ✅ Check this guide's troubleshooting section
2. ✅ Verify all files are in correct locations
3. ✅ Ensure Python 3.10+ is installed
4. ✅ Check all dependencies are installed
5. ✅ Review error messages carefully

## 🎉 Success!

If you can:
- ✅ Open the application
- ✅ Navigate between sections
- ✅ Create an order
- ✅ Generate an invoice
- ✅ Make a reservation
- ✅ Update inventory

**Congratulations!** Your Restaurant Management System is fully operational!

---

**Happy Restaurant Managing! 🍽️**