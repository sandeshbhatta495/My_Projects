"""
Order Management UI
Create and manage customer orders
"""

import tkinter as tk
from tkinter import ttk, messagebox
from datetime import datetime
import json


class OrderUI:
    """Order management interface"""
    
    def __init__(self, parent, db):
        self.parent = parent
        self.db = db
        self.cart = []  # List of (item_id, name, price, quantity)
        self.create_widgets()
        self.load_menu_items()
        
    def create_widgets(self):
        """Create order management widgets"""
        # Header
        header = tk.Label(self.parent, text="Order Management",
                         font=("Arial", 20, "bold"), bg="#f0f0f0")
        header.pack(pady=20)
        
        # Main container
        container = tk.Frame(self.parent, bg="#f0f0f0")
        container.pack(fill=tk.BOTH, expand=True, padx=20)
        
        # Left side - Menu items
        left_frame = tk.LabelFrame(container, text="Menu Items",
                                   font=("Arial", 12, "bold"), bg="#f0f0f0",
                                   padx=10, pady=10)
        left_frame.pack(side=tk.LEFT, fill=tk.BOTH, expand=True, padx=(0, 10))
        
        # Category filter
        filter_frame = tk.Frame(left_frame, bg="#f0f0f0")
        filter_frame.pack(fill=tk.X, pady=(0, 10))
        
        tk.Label(filter_frame, text="Category:", font=("Arial", 10),
                bg="#f0f0f0").pack(side=tk.LEFT, padx=(0, 10))
        
        self.category_var = tk.StringVar(value="All")
        categories = ["All", "Drinks", "Meals", "Snacks", "Desserts"]
        category_combo = ttk.Combobox(filter_frame, textvariable=self.category_var,
                                     values=categories, state="readonly", width=15)
        category_combo.pack(side=tk.LEFT)
        category_combo.bind("<<ComboboxSelected>>", lambda e: self.load_menu_items())
        
        # Menu items list
        columns = ("ID", "Name", "Price")
        self.menu_tree = ttk.Treeview(left_frame, columns=columns, show="headings", height=12)
        
        widths = [50, 200, 80]
        for col, width in zip(columns, widths):
            self.menu_tree.heading(col, text=col)
            self.menu_tree.column(col, width=width)
            
        self.menu_tree.pack(side=tk.LEFT, fill=tk.BOTH, expand=True)
        
        scrollbar = ttk.Scrollbar(left_frame, orient=tk.VERTICAL, command=self.menu_tree.yview)
        self.menu_tree.configure(yscroll=scrollbar.set)
        scrollbar.pack(side=tk.RIGHT, fill=tk.Y)
        
        # Add to cart section
        add_frame = tk.Frame(left_frame, bg="#f0f0f0")
        add_frame.pack(fill=tk.X, pady=10)
        
        tk.Label(add_frame, text="Quantity:", font=("Arial", 10),
                bg="#f0f0f0").pack(side=tk.LEFT, padx=(0, 10))
        
        self.quantity_var = tk.IntVar(value=1)
        quantity_spin = tk.Spinbox(add_frame, from_=1, to=99, textvariable=self.quantity_var,
                                  width=10, font=("Arial", 10))
        quantity_spin.pack(side=tk.LEFT, padx=(0, 10))
        
        tk.Button(add_frame, text="Add to Cart", command=self.add_to_cart,
                 bg="#2ecc71", fg="white", font=("Arial", 10, "bold"),
                 padx=15, pady=5, cursor="hand2").pack(side=tk.LEFT)
        
        # Right side - Cart and order details
        right_frame = tk.Frame(container, bg="#f0f0f0")
        right_frame.pack(side=tk.RIGHT, fill=tk.BOTH)
        
        # Customer info
        info_frame = tk.LabelFrame(right_frame, text="Order Information",
                                   font=("Arial", 11, "bold"), bg="#f0f0f0",
                                   padx=10, pady=10)
        info_frame.pack(fill=tk.X, pady=(0, 10))
        
        tk.Label(info_frame, text="Table #:", font=("Arial", 10),
                bg="#f0f0f0").grid(row=0, column=0, sticky=tk.W, pady=5)
        self.table_entry = tk.Entry(info_frame, font=("Arial", 10), width=20)
        self.table_entry.grid(row=0, column=1, pady=5, padx=(0, 10))
        
        tk.Label(info_frame, text="Customer:", font=("Arial", 10),
                bg="#f0f0f0").grid(row=1, column=0, sticky=tk.W, pady=5)
        self.customer_entry = tk.Entry(info_frame, font=("Arial", 10), width=20)
        self.customer_entry.grid(row=1, column=1, pady=5)
        
        # Cart
        cart_frame = tk.LabelFrame(right_frame, text="Shopping Cart",
                                   font=("Arial", 11, "bold"), bg="#f0f0f0",
                                   padx=10, pady=10)
        cart_frame.pack(fill=tk.BOTH, expand=True, pady=(0, 10))
        
        columns = ("Item", "Price", "Qty", "Total")
        self.cart_tree = ttk.Treeview(cart_frame, columns=columns, show="headings", height=8)
        
        widths = [150, 60, 40, 70]
        for col, width in zip(columns, widths):
            self.cart_tree.heading(col, text=col)
            self.cart_tree.column(col, width=width)
            
        self.cart_tree.pack(side=tk.LEFT, fill=tk.BOTH, expand=True)
        
        cart_scroll = ttk.Scrollbar(cart_frame, orient=tk.VERTICAL, command=self.cart_tree.yview)
        self.cart_tree.configure(yscroll=cart_scroll.set)
        cart_scroll.pack(side=tk.RIGHT, fill=tk.Y)
        
        # Cart buttons
        cart_btn_frame = tk.Frame(cart_frame, bg="#f0f0f0")
        cart_btn_frame.pack(fill=tk.X, pady=(5, 0))
        
        tk.Button(cart_btn_frame, text="Remove Item", command=self.remove_from_cart,
                 bg="#e74c3c", fg="white", font=("Arial", 9),
                 padx=10, pady=3, cursor="hand2").pack(side=tk.LEFT, padx=5)
        
        tk.Button(cart_btn_frame, text="Clear Cart", command=self.clear_cart,
                 bg="#95a5a6", fg="white", font=("Arial", 9),
                 padx=10, pady=3, cursor="hand2").pack(side=tk.LEFT)
        
        # Order summary
        summary_frame = tk.LabelFrame(right_frame, text="Order Summary",
                                     font=("Arial", 11, "bold"), bg="#f0f0f0",
                                     padx=10, pady=10)
        summary_frame.pack(fill=tk.X, pady=(0, 10))
        
        tk.Label(summary_frame, text="Subtotal:", font=("Arial", 10),
                bg="#f0f0f0").grid(row=0, column=0, sticky=tk.W, pady=3)
        self.subtotal_label = tk.Label(summary_frame, text="$0.00",
                                      font=("Arial", 10, "bold"), bg="#f0f0f0")
        self.subtotal_label.grid(row=0, column=1, sticky=tk.E, pady=3)
        
        tk.Label(summary_frame, text="Tax (10%):", font=("Arial", 10),
                bg="#f0f0f0").grid(row=1, column=0, sticky=tk.W, pady=3)
        self.tax_label = tk.Label(summary_frame, text="$0.00",
                                 font=("Arial", 10), bg="#f0f0f0")
        self.tax_label.grid(row=1, column=1, sticky=tk.E, pady=3)
        
        tk.Label(summary_frame, text="Service (5%):", font=("Arial", 10),
                bg="#f0f0f0").grid(row=2, column=0, sticky=tk.W, pady=3)
        self.service_label = tk.Label(summary_frame, text="$0.00",
                                      font=("Arial", 10), bg="#f0f0f0")
        self.service_label.grid(row=2, column=1, sticky=tk.E, pady=3)
        
        tk.Label(summary_frame, text="Discount (%):", font=("Arial", 10),
                bg="#f0f0f0").grid(row=3, column=0, sticky=tk.W, pady=3)
        self.discount_entry = tk.Entry(summary_frame, font=("Arial", 10), width=10)
        self.discount_entry.insert(0, "0")
        self.discount_entry.bind("<KeyRelease>", lambda e: self.update_summary())
        self.discount_entry.grid(row=3, column=1, sticky=tk.E, pady=3)
        
        ttk.Separator(summary_frame, orient='horizontal').grid(row=4, column=0,
                                                               columnspan=2, sticky="ew