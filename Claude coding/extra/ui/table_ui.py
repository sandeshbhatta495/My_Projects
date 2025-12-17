"""
Inventory Management UI
Track and manage restaurant inventory
"""

import tkinter as tk
from tkinter import ttk, messagebox
from datetime import datetime


class InventoryUI:
    """Inventory management interface"""
    
    def __init__(self, parent, db):
        self.parent = parent
        self.db = db
        self.selected_item = None
        self.create_widgets()
        self.load_inventory()
        
    def create_widgets(self):
        """Create inventory widgets"""
        # Header
        header = tk.Label(self.parent, text="Inventory Management",
                         font=("Arial", 20, "bold"), bg="#f0f0f0")
        header.pack(pady=20)
        
        # Main container
        container = tk.Frame(self.parent, bg="#f0f0f0")
        container.pack(fill=tk.BOTH, expand=True, padx=20)
        
        # Top section - Summary cards
        summary_frame = tk.Frame(container, bg="#f0f0f0")
        summary_frame.pack(fill=tk.X, pady=(0, 15))
        
        self.create_summary_card(summary_frame, "Total Items", "0", "#3498db", 0)
        self.create_summary_card(summary_frame, "Low Stock", "0", "#e74c3c", 1)
        self.create_summary_card(summary_frame, "Total Value", "$0", "#2ecc71", 2)
        
        # Middle section - Inventory list and form
        middle_frame = tk.Frame(container, bg="#f0f0f0")
        middle_frame.pack(fill=tk.BOTH, expand=True)
        
        # Left - Inventory list
        left_frame = tk.LabelFrame(middle_frame, text="Inventory Items",
                                   font=("Arial", 12, "bold"), bg="#f0f0f0",
                                   padx=10, pady=10)
        left_frame.pack(side=tk.LEFT, fill=tk.BOTH, expand=True, padx=(0, 10))
        
        # Filter
        filter_frame = tk.Frame(left_frame, bg="#f0f0f0")
        filter_frame.pack(fill=tk.X, pady=(0, 10))
        
        tk.Label(filter_frame, text="Category:", font=("Arial", 10),
                bg="#f0f0f0").pack(side=tk.LEFT, padx=(0, 10))
        
        self.category_var = tk.StringVar(value="All")
        categories = ["All", "Beverages", "Dairy", "Meat", "Vegetables", "Grains", "Other"]
        category_combo = ttk.Combobox(filter_frame, textvariable=self.category_var,
                                     values=categories, state="readonly", width=12)
        category_combo.pack(side=tk.LEFT, padx=(0, 20))
        category_combo.bind("<<ComboboxSelected>>", lambda e: self.load_inventory())
        
        tk.Label(filter_frame, text="Search:", font=("Arial", 10),
                bg="#f0f0f0").pack(side=tk.LEFT, padx=(0, 10))
        self.search_var = tk.StringVar()
        self.search_var.trace("w", lambda *args: self.load_inventory())
        search_entry = tk.Entry(filter_frame, textvariable=self.search_var, width=15)
        search_entry.pack(side=tk.LEFT)
        
        # Show low stock only
        self.low_stock_var = tk.BooleanVar(value=False)
        low_stock_check = tk.Checkbutton(filter_frame, text="Low Stock Only",
                                        variable=self.low_stock_var,
                                        command=self.load_inventory,
                                        bg="#f0f0f0", font=("Arial", 9))
        low_stock_check.pack(side=tk.RIGHT)
        
        # Inventory table
        columns = ("ID", "Item", "Category", "Qty", "Unit", "Min", "Cost", "Status")
        self.inv_tree = ttk.Treeview(left_frame, columns=columns, show="headings", height=13)
        
        widths = [40, 120, 90, 60, 50, 50, 70, 70]
        for col, width in zip(columns, widths):
            self.inv_tree.heading(col, text=col)
            self.inv_tree.column(col, width=width)
            
        self.inv_tree.pack(side=tk.LEFT, fill=tk.BOTH, expand=True)
        
        scrollbar = ttk.Scrollbar(left_frame, orient=tk.VERTICAL, command=self.inv_tree.yview)
        self.inv_tree.configure(yscroll=scrollbar.set)
        scrollbar.pack(side=tk.RIGHT, fill=tk.Y)
        
        self.inv_tree.bind("<<TreeviewSelect>>", self.on_item_select)
        
        # Right - Item form
        right_frame = tk.LabelFrame(middle_frame, text="Item Details",
                                    font=("Arial", 12, "bold"), bg="#f0f0f0",
                                    padx=15, pady=15)
        right_frame.pack(side=tk.RIGHT, fill=tk.BOTH)
        
        # Form fields
        tk.Label(right_frame, text="Item Name:", font=("Arial", 10),
                bg="#f0f0f0").grid(row=0, column=0, sticky=tk.W, pady=8)
        self.name_entry = tk.Entry(right_frame, font=("Arial", 10), width=25)
        self.name_entry.grid(row=0, column=1, pady=8)
        
        tk.Label(right_frame, text="Category:", font=("Arial", 10),
                bg="#f0f0f0").grid(row=1, column=0, sticky=tk.W, pady=8)
        self.cat_var = tk.StringVar()
        cat_combo = ttk.Combobox(right_frame, textvariable=self.cat_var,
                                values=["Beverages", "Dairy", "Meat", "Vegetables", "Grains", "Other"],
                                state="readonly", width=23)
        cat_combo.grid(row=1, column=1, pady=8)
        
        tk.Label(right_frame, text="Quantity:", font=("Arial", 10),
                bg="#f0f0f0").grid(row=2, column=0, sticky=tk.W, pady=8)
        self.qty_entry = tk.Entry(right_frame, font=("Arial", 10), width=25)
        self.qty_entry.grid(row=2, column=1, pady=8)
        
        tk.Label(right_frame, text="Unit:", font=("Arial", 10),
                bg="#f0f0f0").grid(row=3, column=0, sticky=tk.W, pady=8)
        self.unit_var = tk.StringVar()
        unit_combo = ttk.Combobox(right_frame, textvariable=self.unit_var,
                                 values=["kg", "liters", "pieces", "boxes", "bottles"],
                                 state="readonly", width=23)
        unit_combo.grid(row=3, column=1, pady=8)
        
        tk.Label(right_frame, text="Min Quantity:", font=("Arial", 10),
                bg="#f0f0f0").grid(row=4, column=0, sticky=tk.W, pady=8)
        self.min_qty_entry = tk.Entry(right_frame, font=("Arial", 10), width=25)
        self.min_qty_entry.grid(row=4, column=1, pady=8)
        
        tk.Label(right_frame, text="Cost per Unit ($):", font=("Arial", 10),
                bg="#f0f0f0").grid(row=5, column=0, sticky=tk.W, pady=8)
        self.cost_entry = tk.Entry(right_frame, font=("Arial", 10), width=25)
        self.cost_entry.grid(row=5, column=1, pady=8)
        
        # Action buttons
        btn_frame = tk.Frame(right_frame, bg="#f0f0f0")
        btn_frame.grid(row=6, column=0, columnspan=2, pady=(15, 5))
        
        tk.Button(btn_frame, text="Add Item", command=self.add_item,
                 bg="#2ecc71", fg="white", font=("Arial", 10, "bold"),
                 padx=15, pady=8, cursor="hand2").grid(row=0, column=0, padx=5)
        
        tk.Button(btn_frame, text="Update", command=self.update_item,
                 bg="#3498db", fg="white", font=("Arial", 10, "bold"),
                 padx=15, pady=8, cursor="hand2").grid(row=0, column=1, padx=5)
        
        tk.Button(btn_frame, text="Delete", command=self.delete_item,
                 bg="#e74c3c", fg="white", font=("Arial", 10, "bold"),
                 padx=15, pady=8, cursor="hand2").grid(row=1, column=0, padx=5, pady=5)
        
        tk.Button(btn_frame, text="Clear", command=self.clear_form,
                 bg="#95a5a6", fg="white", font=("Arial", 10, "bold"),
                 padx=15, pady=8, cursor="hand2").grid(row=1, column=1, padx=5, pady=5)
        
        # Quick adjust quantity
        adjust_frame = tk.LabelFrame(right_frame, text="Quick Adjust",
                                    font=("Arial", 10, "bold"), bg="#f0f0f0",
                                    padx=10, pady=10)
        adjust_frame.grid(row=7, column=0, columnspan=2, pady=(15, 0), sticky="ew")
        
        tk.Label(adjust_frame, text="Adjust Qty:", font=("Arial", 9),
                bg="#f0f0f0").pack(side=tk.LEFT, padx=(0, 5))
        
        self.adjust_var = tk.DoubleVar(value=0)
        adjust_entry = tk.Entry(adjust_frame, textvariable=self.adjust_var,
                               font=("Arial", 9), width=10)
        adjust_entry.pack(side=tk.LEFT, padx=(0, 5))
        
        tk.Button(adjust_frame, text="+", command=lambda: self.adjust_quantity(True),
                 bg="#2ecc71", fg="white", font=("Arial", 9, "bold"),
                 width=3, cursor="hand2").pack(side=tk.LEFT, padx=2)
        
        tk.Button(adjust_frame, text="-", command=lambda: self.adjust_quantity(False),
                 bg="#e74c3c", fg="white", font=("Arial", 9, "bold"),
                 width=3, cursor="hand2").pack(side=tk.LEFT, padx=2)
        
    def create_summary_card(self, parent, title, value, color, col):
        """Create summary card"""
        card = tk.Frame(parent, bg=color, relief=tk.RAISED, borderwidth=2)
        card.grid(row=0, column=col, padx=10, sticky="ew")
        parent.grid_columnconfigure(col, weight=1)
        
        tk.Label(card, text=title, font=("Arial", 11),
                bg=color, fg="white").pack(pady=(15, 5))
        
        value_label = tk.Label(card, text=value, font=("Arial", 20, "bold"),
                              bg=color, fg="white")
        value_label.pack(pady=(5, 15))
        
        setattr(self, f"{title.replace(' ', '_').lower()}_label", value_label)
        
    def load_inventory(self):
        """Load inventory items"""
        for item in self.inv_tree.get_children():
            self.inv_tree.delete(item)
            
        category = self.category_var.get()
        search = self.search_var.get()
        low_stock_only = self.low_stock_var.get()
        
        query = """SELECT id, item_name, category, quantity, unit, min_quantity, 
                   cost_per_unit FROM inventory WHERE 1=1"""
        params = []
        
        if category != "All":
            query += " AND category = ?"
            params.append(category)
            
        if search:
            query += " AND item_name LIKE ?"
            params.append(f"%{search}%")
            
        if low_stock_only:
            query += " AND quantity <= min_quantity"
            
        query += " ORDER BY item_name"
        
        items = self.db.execute_query(query, params) if params else self.db.execute_query(query)
        
        total_items = 0
        low_stock_count = 0
        total_value = 0
        
        if items:
            for item in items:
                item_id, name, cat, qty, unit, min_qty, cost = item
                status = "⚠️ Low" if qty <= min_qty else "✓ OK"
                if qty <= min_qty:
                    low_stock_count += 1
                    
                total_items += 1
                total_value += qty * cost
                
                self.inv_tree.insert("", tk.END, values=(
                    item_id, name, cat, f"{qty:.1f}", unit, f"{min_qty:.1f}",
                    f"${cost:.2f}", status
                ))
                
        # Update summary cards
        self.total_items_label.config(text=str(total_items))
        self.low_stock_label.config(text=str(low_stock_count))
        self.total_value_label.config(text=f"${total_value:.2f}")
        
    def on_item_select(self, event):
        """Handle item selection"""
        selection = self.inv_tree.selection()
        if not selection:
            return
            
        item = self.inv_tree.item(selection[0])
        values = item['values']
        item_id = values[0]
        
        query = """SELECT item_name, category, quantity, unit, min_quantity, cost_per_unit
                   FROM inventory WHERE id = ?"""
        result = self.db.execute_query(query, (item_id,))
        
        if result:
            self.selected_item = item_id
            name, cat, qty, unit, min_qty, cost = result[0]
            
            self.name_entry.delete(0, tk.END)
            self.name_entry.insert(0, name)
            self.cat_var.set(cat)
            self.qty_entry.delete(0, tk.END)
            self.qty_entry.insert(0, str(qty))
            self.unit_var.set(unit)
            self.min_qty_entry.delete(0, tk.END)
            self.min_qty_entry.insert(0, str(min_qty))
            self.cost_entry.delete(0, tk.END)
            self.cost_entry.insert(0, str(cost))
            
    def add_item(self):
        """Add new inventory item"""
        if not self.validate_form():
            return
            
        name = self.name_entry.get()
        category = self.cat_var.get()
        qty = float(self.qty_entry.get())
        unit = self.unit_var.get()
        min_qty = float(self.min_qty_entry.get())
        cost = float(self.cost_entry.get())
        
        query = """INSERT INTO inventory (item_name, category, quantity, unit,
                   min_quantity, cost_per_unit) VALUES (?, ?, ?, ?, ?, ?)"""
        
        result = self.db.insert(query, (name, category, qty, unit, min_qty, cost))
        
        if result:
            messagebox.showinfo("Success", "Inventory item added!")
            self.clear_form()
            self.load_inventory()
        else:
            messagebox.showerror("Error", "Failed to add item! Item may already exist.")
            
    def update_item(self):
        """Update inventory item"""
        if not self.selected_item:
            messagebox.showwarning("Warning", "Please select an item to update!")
            return
            
        if not self.validate_form():
            return
            
        name = self.name_entry.get()
        category = self.cat_var.get()
        qty = float(self.qty_entry.get())
        unit = self.unit_var.get()
        min_qty = float(self.min_qty_entry.get())
        cost = float(self.cost_entry.get())
        
        query = """UPDATE inventory SET item_name=?, category=?, quantity=?,
                   unit=?, min_quantity=?, cost_per_unit=?, last_updated=CURRENT_TIMESTAMP
                   WHERE id=?"""
        
        self.db.execute_query(query, (name, category, qty, unit, min_qty, cost, self.selected_item))
        
        messagebox.showinfo("Success", "Inventory item updated!")
        self.clear_form()
        self.load_inventory()
        
    def delete_item(self):
        """Delete inventory item"""
        if not self.selected_item:
            messagebox.showwarning("Warning", "Please select an item to delete!")
            return
            
        if messagebox.askyesno("Confirm", "Delete this inventory item?"):
            query = "DELETE FROM inventory WHERE id = ?"
            self.db.execute_query(query, (self.selected_item,))
            
            messagebox.showinfo("Success", "Inventory item deleted!")
            self.clear_form()
            self.load_inventory()
            
    def adjust_quantity(self, increase):
        """Quick adjust quantity"""
        if not self.selected_item:
            messagebox.showwarning("Warning", "Please select an item first!")
            return
            
        try:
            adjust_val = self.adjust_var.get()
            if adjust_val <= 0:
                messagebox.showwarning("Warning", "Please enter a positive adjustment value!")
                return
                
            current_qty = float(self.qty_entry.get())
            new_qty = current_qty + adjust_val if increase else current_qty - adjust_val
            
            if new_qty < 0:
                messagebox.showwarning("Warning", "Quantity cannot be negative!")
                return
                
            self.qty_entry.delete(0, tk.END)
            self.qty_entry.insert(0, str(new_qty))
            
            # Auto-update
            self.update_item()
            
        except ValueError:
            messagebox.showerror("Error", "Invalid quantity values!")
            
    def clear_form(self):
        """Clear form fields"""
        self.selected_item = None
        self.name_entry.delete(0, tk.END)
        self.cat_var.set("")
        self.qty_entry.delete(0, tk.END)
        self.unit_var.set("")
        self.min_qty_entry.delete(0, tk.END)
        self.cost_entry.delete(0, tk.END)
        self.adjust_var.set(0)
        
    def validate_form(self):
        """Validate form data"""
        if not self.name_entry.get():
            messagebox.showwarning("Validation", "Please enter item name!")
            return False
            
        if not self.cat_var.get():
            messagebox.showwarning("Validation", "Please select category!")
            return False
            
        if not self.unit_var.get():
            messagebox.showwarning("Validation", "Please select unit!")
            return False
            
        try:
            qty = float(self.qty_entry.get())
            min_qty = float(self.min_qty_entry.get())
            cost = float(self.cost_entry.get())
            
            if qty < 0 or min_qty < 0 or cost < 0:
                raise ValueError
        except:
            messagebox.showwarning("Validation", "Please enter valid numeric values!")
            return False
            
        return True