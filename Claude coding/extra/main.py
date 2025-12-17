"""
Restaurant & Café Management System
Main Application Entry Point
"""

import tkinter as tk
from tkinter import ttk, messagebox
import sys
import os

# Add project root to path
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))

from backend.database import Database
from ui.dashboard_ui import DashboardUI
from ui.menu_ui import MenuUI
from ui.order_ui import OrderUI
from ui.billing_ui import BillingUI
from ui.inventory_ui import InventoryUI
from ui.tables_ui import TablesUI


class RestaurantApp:
    """Main Application Class"""
    
    def __init__(self, root):
        self.root = root
        self.root.title("Restaurant & Café Management System")
        self.root.geometry("1200x700")
        self.root.minsize(1000, 600)
        
        # Initialize database
        self.db = Database()
        
        # Configure style
        self.setup_styles()
        
        # Create main container
        self.create_main_layout()
        
        # Show dashboard by default
        self.show_dashboard()
        
    def setup_styles(self):
        """Configure application styles"""
        style = ttk.Style()
        style.theme_use('clam')
        
        # Configure colors
        bg_color = "#f0f0f0"
        sidebar_color = "#2c3e50"
        accent_color = "#3498db"
        
        style.configure("Sidebar.TFrame", background=sidebar_color)
        style.configure("Main.TFrame", background=bg_color)
        style.configure("SidebarButton.TButton", 
                       background=sidebar_color,
                       foreground="white",
                       borderwidth=0,
                       focuscolor="none",
                       font=("Arial", 11))
        style.map("SidebarButton.TButton",
                 background=[("active", accent_color)])
        
    def create_main_layout(self):
        """Create main application layout"""
        # Sidebar
        self.sidebar = ttk.Frame(self.root, style="Sidebar.TFrame", width=200)
        self.sidebar.pack(side=tk.LEFT, fill=tk.Y)
        self.sidebar.pack_propagate(False)
        
        # Header
        header = tk.Label(self.sidebar, text="Restaurant\nManagement",
                         bg="#2c3e50", fg="white", font=("Arial", 14, "bold"),
                         pady=20)
        header.pack(fill=tk.X)
        
        # Navigation buttons
        self.nav_buttons = {
            "Dashboard": self.show_dashboard,
            "Menu": self.show_menu,
            "Orders": self.show_orders,
            "Billing": self.show_billing,
            "Tables": self.show_tables,
            "Inventory": self.show_inventory,
        }
        
        for btn_text, command in self.nav_buttons.items():
            btn = tk.Button(self.sidebar, text=btn_text, command=command,
                          bg="#2c3e50", fg="white", font=("Arial", 11),
                          borderwidth=0, pady=15, cursor="hand2",
                          activebackground="#3498db", activeforeground="white")
            btn.pack(fill=tk.X, padx=10, pady=5)
        
        # Exit button
        exit_btn = tk.Button(self.sidebar, text="Exit", command=self.exit_app,
                           bg="#e74c3c", fg="white", font=("Arial", 11, "bold"),
                           borderwidth=0, pady=15, cursor="hand2")
        exit_btn.pack(fill=tk.X, padx=10, pady=5, side=tk.BOTTOM)
        
        # Main content area
        self.main_frame = ttk.Frame(self.root, style="Main.TFrame")
        self.main_frame.pack(side=tk.RIGHT, fill=tk.BOTH, expand=True)
        
    def clear_main_frame(self):
        """Clear the main content area"""
        for widget in self.main_frame.winfo_children():
            widget.destroy()
            
    def show_dashboard(self):
        """Show dashboard view"""
        self.clear_main_frame()
        DashboardUI(self.main_frame, self.db)
        
    def show_menu(self):
        """Show menu management view"""
        self.clear_main_frame()
        MenuUI(self.main_frame, self.db)
        
    def show_orders(self):
        """Show order management view"""
        self.clear_main_frame()
        OrderUI(self.main_frame, self.db)
        
    def show_billing(self):
        """Show billing view"""
        self.clear_main_frame()
        BillingUI(self.main_frame, self.db)
        
    def show_tables(self):
        """Show table reservation view"""
        self.clear_main_frame()
        TablesUI(self.main_frame, self.db)
        
    def show_inventory(self):
        """Show inventory management view"""
        self.clear_main_frame()
        InventoryUI(self.main_frame, self.db)
        
    def exit_app(self):
        """Exit application"""
        if messagebox.askyesno("Exit", "Are you sure you want to exit?"):
            self.db.close()
            self.root.destroy()


def main():
    """Main entry point"""
    root = tk.Tk()
    app = RestaurantApp(root)
    root.mainloop()


if __name__ == "__main__":
    main()