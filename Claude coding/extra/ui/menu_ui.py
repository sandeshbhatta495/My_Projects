"""
Menu Management UI
Add, edit, delete menu items
"""

import tkinter as tk
from tkinter import ttk, messagebox


class MenuUI:
    """Menu management interface"""
    
    def __init__(self, parent, db):
        self.parent = parent
        self.db = db
        self.selected_item = None
        self.create_widgets()
        self.load_menu_items()
        
    def create_widgets(self):
        """Create menu management widgets"""
        # Header
        header = tk.Label(self.parent, text="Menu Management",
                         font=("Arial", 20, "bold"), bg="#f0f0f0")
        header.pack(pady=20)
        
        # Main container
        container = tk.Frame(self.parent, bg="#f0f0f0")
        container.pack(fill=tk.BOTH, expand=True, padx=20)
        
        # Left side - Menu list
        left_frame = tk.Frame(container, bg="#f0f0f0")
        left_frame.pack(side=tk.LEFT, fill=tk.BOTH, expand=True, padx=(0, 10))
        
        # Category filter
        filter_frame = tk.Frame(left_frame, bg="#f0f0f0")
        filter_frame.pack(fill=tk.X, pady=(0, 10))
        
        tk.Label(filter_frame, text="Filter by Category:", font=("Arial", 10),
                bg="#f0f0f0").pack(side=tk.LEFT, padx=(0, 10))
        
        self.category_var = tk.StringVar(value="All")
        categories = ["All", "Drinks", "Meals", "Snacks", "Desserts"]
        self.category_combo = ttk.Combobox(filter_frame, textvariable=self.category_var,
                                          values=categories, state="readonly", width=15)
        self.category_combo.pack(side=tk.LEFT)
        self.category_combo.bind("<<ComboboxSelected>>", lambda e: self.load_menu_items())
        
        # Search
        tk.Label(filter_frame, text="Search:", font=("Arial", 10),
                bg="#f0f0f0").pack(side=tk.LEFT, padx=(20, 10))
        self.search_var = tk.StringVar()
        self.search_var.trace("w", lambda *args: self.load_menu_items())
        search_entry = tk.Entry(filter_frame, textvariable=self.search_var, width=20)
        search_entry.pack(side=tk.LEFT)
        
        # Menu table
        columns = ("ID", "Name", "Category", "Price", "Status")
        self.menu_tree = ttk.Treeview(left_frame, columns=columns, show="headings", height=15)
        
        widths = [50, 200, 100, 80, 80]
        for col, width in zip(columns, widths):
            self.menu_tree.heading(col, text=col)
            self.menu_tree.column(col, width=width)
            
        self.menu_tree.pack(side=tk.LEFT, fill=tk.BOTH, expand=True)
        
        scrollbar = ttk.Scrollbar(left_frame, orient=tk.VERTICAL, command=self.menu_tree.yview)
        self.menu_tree.configure(yscroll=scrollbar.set)
        scrollbar.pack(side=tk.RIGHT, fill=tk.Y)
        
        self.menu_tree.bind("<<TreeviewSelect>>", self.on_item_select)
        
        # Right side - Item details form
        right_frame = tk.LabelFrame(container, text="Item Details", font=("Arial", 12, "bold"),
                                   bg="#f0f0f0", padx=20, pady=20)
        right_frame.pack(side=tk.RIGHT, fill=tk.BOTH, padx=(10, 0))
        
        # Form fields
        tk.Label(right_frame, text="Item Name:", font=("Arial", 10),
                bg="#f0f0f0").grid(row=0, column=0, sticky=tk.W, pady=5)
        self.name_entry = tk.Entry(right_frame, font=("Arial", 10), width=25)
        self.name_entry.grid(row=0, column=1, pady=5)
        
        tk.Label(right_frame, text="Category:", font=("Arial", 10),
                bg="#f0f0f0").grid(row=1, column=0, sticky=tk.W, pady=5)
        self.cat_var = tk.StringVar()
        self.cat_combo = ttk.Combobox(right_frame, textvariable=self.cat_var,
                                     values=["Drinks", "Meals", "Snacks", "Desserts"],
                                     state="readonly", width=23)
        self.cat_combo.grid(row=1, column=1, pady=5)
        
        tk.Label(right_frame, text="Price ($):", font=("Arial", 10),
                bg="#f0f0f0").grid(row=2, column=0, sticky=tk.W, pady=5)
        self.price_entry = tk.Entry(right_frame, font=("Arial", 10), width=25)
        self.price_entry.grid(row=2, column=1, pady=5)
        
        tk.Label(right_frame, text="Description:", font=("Arial", 10),
                bg="#f0f0f0").grid(row=3, column=0, sticky=tk.NW, pady=5)
        self.desc_text = tk.Text(right_frame, font=("Arial", 10), width=25, height=4)
        self.desc_text.grid(row=3, column=1, pady=5)
        
        tk.Label(right_frame, text="Available:", font=("Arial", 10),
                bg="#f0f0f0").grid(row=4, column=0, sticky=tk.W, pady=5)
        self.available_var = tk.IntVar(value=1)
        available_check = tk.Checkbutton(right_frame, variable=self.available_var,
                                        bg="#f0f0f0")
        available_check.grid(row=4, column=1, sticky=tk.W, pady=5)
        
        # Buttons
        btn_frame = tk.Frame(right_frame, bg="#f0f0f0")
        btn_frame.grid(row=5, column=0, columnspan=2, pady=20)
        
        tk.Button(btn_frame, text="Add New", command=self.add_item,
                 bg="#2ecc71", fg="white", font=("Arial", 10, "bold"),
                 padx=15, pady=8, cursor="hand2").pack(side=tk.LEFT, padx=5)
        
        tk.Button(btn_frame, text="Update", command=self.update_item,
                 bg="#3498db", fg="white", font=("Arial", 10, "bold"),
                 padx=15, pady=8, cursor="hand2").pack(side=tk.LEFT, padx=5)
        
        tk.Button(btn_frame, text="Delete", command=self.delete_item,
                 bg="#e74c3c", fg="white", font=("Arial", 10, "bold"),
                 padx=15, pady=8, cursor="hand2").pack(side=tk.LEFT, padx=5)
        
        tk.Button(btn_frame, text="Clear", command=self.clear_form,
                 bg="#95a5a6", fg="white", font=("Arial", 10, "bold"),
                 padx=15, pady=8, cursor="hand2").pack(side=tk.LEFT, padx=5)
        
    def load_menu_items(self):
        """Load menu items from database"""
        # Clear existing
        for item in self.menu_tree.get_children():
            self.menu_tree.delete(item)
            
        category = self.category_var.get()
        search = self.search_var.get()
        
        query = "SELECT id, name, category, price, available FROM menu_items WHERE 1=1"
        params = []
        
        if category != "All":
            query += " AND category = ?"
            params.append(category)
            
        if search:
            query += " AND name LIKE ?"
            params.append(f"%{search}%")
            
        query += " ORDER BY category, name"
        
        items = self.db.execute_query(query, params) if params else self.db.execute_query(query)
        
        if items:
            for item in items:
                item_id, name, cat, price, available = item
                status = "Available" if available else "Unavailable"
                self.menu_tree.insert("", tk.END, values=(item_id, name, cat, f"${price:.2f}", status))
                
    def on_item_select(self, event):
        """Handle item selection"""
        selection = self.menu_tree.selection()
        if selection:
            item = self.menu_tree.item(selection[0])
            values = item['values']
            item_id = values[0]
            
            # Load full details
            query = "SELECT name, category, price, description, available FROM menu_items WHERE id = ?"
            result = self.db.execute_query(query, (item_id,))
            
            if result:
                self.selected_item = item_id
                name, cat, price, desc, available = result[0]
                
                self.name_entry.delete(0, tk.END)
                self.name_entry.insert(0, name)
                self.cat_var.set(cat)
                self.price_entry.delete(0, tk.END)
                self.price_entry.insert(0, str(price))
                self.desc_text.delete("1.0", tk.END)
                self.desc_text.insert("1.0", desc if desc else "")
                self.available_var.set(available)
                
    def add_item(self):
        """Add new menu item"""
        if not self.validate_form():
            return
            
        name = self.name_entry.get()
        category = self.cat_var.get()
        price = float(self.price_entry.get())
        desc = self.desc_text.get("1.0", tk.END).strip()
        available = self.available_var.get()
        
        query = """INSERT INTO menu_items (name, category, price, description, available)
                   VALUES (?, ?, ?, ?, ?)"""
        result = self.db.insert(query, (name, category, price, desc, available))
        
        if result:
            messagebox.showinfo("Success", "Menu item added successfully!")
            self.clear_form()
            self.load_menu_items()
        else:
            messagebox.showerror("Error", "Failed to add menu item!")
            
    def update_item(self):
        """Update selected menu item"""
        if not self.selected_item:
            messagebox.showwarning("Warning", "Please select an item to update!")
            return
            
        if not self.validate_form():
            return
            
        name = self.name_entry.get()
        category = self.cat_var.get()
        price = float(self.price_entry.get())
        desc = self.desc_text.get("1.0", tk.END).strip()
        available = self.available_var.get()
        
        query = """UPDATE menu_items SET name=?, category=?, price=?, 
                   description=?, available=? WHERE id=?"""
        self.db.execute_query(query, (name, category, price, desc, available, self.selected_item))
        
        messagebox.showinfo("Success", "Menu item updated successfully!")
        self.clear_form()
        self.load_menu_items()
        
    def delete_item(self):
        """Delete selected menu item"""
        if not self.selected_item:
            messagebox.showwarning("Warning", "Please select an item to delete!")
            return
            
        if messagebox.askyesno("Confirm", "Are you sure you want to delete this item?"):
            query = "DELETE FROM menu_items WHERE id = ?"
            self.db.execute_query(query, (self.selected_item,))
            messagebox.showinfo("Success", "Menu item deleted successfully!")
            self.clear_form()
            self.load_menu_items()
            
    def clear_form(self):
        """Clear form fields"""
        self.selected_item = None
        self.name_entry.delete(0, tk.END)
        self.cat_var.set("")
        self.price_entry.delete(0, tk.END)
        self.desc_text.delete("1.0", tk.END)
        self.available_var.set(1)
        
    def validate_form(self):
        """Validate form data"""
        if not self.name_entry.get():
            messagebox.showwarning("Validation", "Please enter item name!")
            return False
            
        if not self.cat_var.get():
            messagebox.showwarning("Validation", "Please select category!")
            return False
            
        try:
            price = float(self.price_entry.get())
            if price <= 0:
                raise ValueError
        except:
            messagebox.showwarning("Validation", "Please enter valid price!")
            return False
            
        return True