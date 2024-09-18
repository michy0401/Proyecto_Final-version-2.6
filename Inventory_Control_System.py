import tkinter as tk
from tkinter import ttk, messagebox, Menu
from Product_Management import Product_Management
from conexion import Registro_datos
from Product import Product
from datetime import datetime

class Inventory_Control_System:
    def __init__(self, root):
        self.root = root
        self.root.title("Sistema de Control de Inventarios Santa Fe")
        self.db_connection = Registro_datos()
        self.product_management = Product_Management(self.db_connection)
        self.job_title = None
        self.employee_name = None
        self.main_window = None
        self.entries = {}
        self.create_widgets()

    def create_widgets(self):
        self.frame = tk.Frame(self.root)
        self.frame.pack(padx=100, pady=100)
        
        self.user_label = tk.Label(self.frame, text="Usuario:")
        self.user_label.grid(row=0, column=0, padx=5, pady=5)
        self.user_entry = tk.Entry(self.frame)
        self.user_entry.grid(row=0, column=1, padx=5, pady=5)
        
        self.password_label = tk.Label(self.frame, text="Contraseña:")
        self.password_label.grid(row=1, column=0, padx=5, pady=5)
        self.password_entry = tk.Entry(self.frame, show="*")
        self.password_entry.grid(row=1, column=1, padx=5, pady=5)
        
        self.login_button = tk.Button(self.frame, text="Iniciar Sesión", command=self.log_in)
        self.login_button.grid(row=2, column=0, columnspan=2, pady=10)

    def log_in(self):
        user = self.user_entry.get()
        password = self.password_entry.get()
        user_data = self.db_connection.busca_usuario(user, password)
        if user_data:
            id_user = user_data[0]
            empleado_data = self.db_connection.busca_empleado(id_user)
            if empleado_data:
                self.root.withdraw()
                self.employee_name = empleado_data[0]
                self.job_title = empleado_data[1]
                self.show_main_window(self.employee_name, self.job_title)
            else:
                messagebox.showerror("Ingreso Fallido", "No se encontraron los datos del empleado")
        else:
            messagebox.showerror("Ingreso Fallido", "Usuario o contraseña incorrectos")
        self.user_entry.delete(0, tk.END)
        self.password_entry.delete(0, tk.END)

    def show_main_window(self, employee_name, job_title):
        if self.main_window:
            self.main_window.lift()
            return
        self.main_window = tk.Toplevel(self.root)
        self.main_window.title("Sistema de Control de Inventarios Santa Fe")
        self.main_window.state('zoomed')
        
        header_frame = tk.Frame(self.main_window)
        header_frame.pack(pady=10)
        
        name_employee_label = tk.Label(header_frame, text=f"Empleado: {employee_name}", font=("Arial", 16))
        name_employee_label.pack(side=tk.LEFT, padx=10)
        job_title_label = tk.Label(header_frame, text=f"Cargo: {job_title}", font=("Arial", 16))
        job_title_label.pack(side=tk.LEFT, padx=10)
        
        self.menu_bar = Menu(self.main_window)
        self.create_main_menu(job_title)
        self.main_window.config(menu=self.menu_bar)
        
        self.main_frame = tk.Frame(self.main_window)
        self.main_frame.pack(fill=tk.BOTH, expand=True)

    def create_main_menu(self, job_title):
        product_menu = Menu(self.menu_bar, tearoff=0)
        product_menu.add_command(label="Buscar Producto", command=self.show_search_product)
        product_menu.add_command(label="Agregar Producto", command=self.show_add_product_form)
        if job_title == "Manager":
            product_menu.add_command(label="Eliminar Producto", command=self.show_delete_product)
            product_menu.add_command(label="Modificar Producto", command=self.show_modify_product_form)
        self.menu_bar.add_cascade(label="Productos", menu=product_menu)
        
        logout_menu = Menu(self.menu_bar, tearoff=0)
        logout_menu.add_command(label="Cerrar Sesión", command=self.logout)
        self.menu_bar.add_cascade(label="Cerrar Sesión", menu=logout_menu)

    def logout(self):
        if self.main_window:
            self.main_window.destroy()
        self.root.deiconify()

    def show_search_product(self):
        self.clear_frame()

        search_frame = ttk.Frame(self.main_frame)
        search_frame.grid(row=0, column=0, padx=10, pady=10, sticky="nsew")

        self.tree_frame = ttk.Frame(self.main_frame)
        self.tree_frame.grid(row=0, column=1, padx=10, pady=10, sticky="nsew")

        self.main_frame.grid_columnconfigure(0, weight=1)
        self.main_frame.grid_columnconfigure(1, weight=1)
        self.main_frame.grid_rowconfigure(0, weight=1)

        self.search_label = ttk.Label(search_frame, text="Buscar Producto por Nombre o ID:")
        self.search_label.grid(row=0, column=0, padx=5, pady=5, sticky="w")

        self.search_entry = ttk.Entry(search_frame)
        self.search_entry.grid(row=0, column=1, padx=5, pady=5, sticky="ew")

        self.search_button = ttk.Button(search_frame, text="Buscar", command=self.perform_search)
        self.search_button.grid(row=1, column=0, columnspan=2, padx=5, pady=5, sticky="ew")

        search_frame.grid_columnconfigure(0, weight=0)
        search_frame.grid_columnconfigure(1, weight=1)

        columns = ("ID", "Nombre", "Precio", "Presentación")
        self.results_tree = ttk.Treeview(self.tree_frame, columns=columns, show='headings')
        self.results_tree.heading("ID", text="ID")
        self.results_tree.heading("Nombre", text="Nombre")
        self.results_tree.heading("Precio", text="Precio")
        self.results_tree.heading("Presentación", text="Presentación")
        self.results_tree.column("ID", width=50)
        self.results_tree.column("Nombre", width=200)
        self.results_tree.column("Precio", width=100)
        self.results_tree.column("Presentación", width=150)

        self.vsb = ttk.Scrollbar(self.tree_frame, orient="vertical", command=self.results_tree.yview)
        self.hsb = ttk.Scrollbar(self.tree_frame, orient="horizontal", command=self.results_tree.xview)

        self.results_tree.configure(yscrollcommand=self.vsb.set, xscrollcommand=self.hsb.set)
        self.results_tree.grid(row=0, column=0, sticky='nsew')
        self.vsb.grid(row=0, column=1, sticky='ns')
        self.hsb.grid(row=1, column=0, sticky='ew')

        self.tree_frame.grid_rowconfigure(0, weight=1)
        self.tree_frame.grid_columnconfigure(0, weight=1)

        self.load_all_products()

    def show_add_product_form(self):
        self.clear_frame()

        form_frame = ttk.Frame(self.main_frame)
        form_frame.grid(row=0, column=0, padx=10, pady=10, sticky="nsew")

        self.entries = {
            "Tipo de Presentación:": tk.Entry(form_frame),
            "Categoría:": tk.Entry(form_frame),
            "Proveedor:": tk.Entry(form_frame),
            "Producto:": tk.Entry(form_frame),
            "Cantidad:": tk.Entry(form_frame),
            "Costo unitario:": tk.Entry(form_frame),
            "Precio de Venta:": tk.Entry(form_frame),
            "Fecha de Expiración:": tk.Entry(form_frame),
            "Marca:": tk.Entry(form_frame),
            "Sabor:": tk.Entry(form_frame),
            "Necesita Prescripción:": tk.Entry(form_frame),
            "Edad Recomendada:": tk.Entry(form_frame),
            "Instrucciones:": tk.Entry(form_frame),
            "Garantía:": tk.Entry(form_frame)
        }

        row = 0
        for label, entry in self.entries.items():
            tk.Label(form_frame, text=label).grid(row=row, column=0, padx=5, pady=5, sticky="w")
            entry.grid(row=row, column=1, padx=5, pady=5, sticky="ew")
            row += 1

        self.add_product_button = ttk.Button(form_frame, text="Agregar Producto", command=self.add_product)
        self.add_product_button.grid(row=row, column=0, columnspan=2, pady=10)

        self.tree_frame = ttk.Frame(self.main_frame)
        self.tree_frame.grid(row=0, column=1, padx=10, pady=10, sticky="nsew")

        columns = ("ID", "Nombre", "Precio", "Presentación")
        self.results_tree = ttk.Treeview(self.tree_frame, columns=columns, show='headings')
        self.results_tree.heading("ID", text="ID")
        self.results_tree.heading("Nombre", text="Nombre")
        self.results_tree.heading("Precio", text="Precio")
        self.results_tree.heading("Presentación", text="Presentación")
        self.results_tree.column("ID", width=50)
        self.results_tree.column("Nombre", width=200)
        self.results_tree.column("Precio", width=100)
        self.results_tree.column("Presentación", width=150)

        self.vsb = ttk.Scrollbar(self.tree_frame, orient="vertical", command=self.results_tree.yview)
        self.hsb = ttk.Scrollbar(self.tree_frame, orient="horizontal", command=self.results_tree.xview)

        self.results_tree.configure(yscrollcommand=self.vsb.set, xscrollcommand=self.hsb.set)
        self.results_tree.grid(row=0, column=0, sticky='nsew')
        self.vsb.grid(row=0, column=1, sticky='ns')
        self.hsb.grid(row=1, column=0, sticky='ew')

        self.tree_frame.grid_rowconfigure(0, weight=1)
        self.tree_frame.grid_columnconfigure(0, weight=1)

        self.load_all_products()

    def add_product(self):
        data = {}
        for label, entry in self.entries.items():
            data[label[:-1]] = entry.get()

        new_product = Product(
            id_presentation_type=data["Tipo de Presentación"],
            id_category_product=data["Categoría"],
            id_supplier=data["Proveedor"],
            name_product=data["Producto"],
            quantity=int(data["Cantidad"]),
            unit_cost=float(data["Costo unitario"]),
            product_price=float(data["Precio de Venta"]),
            expiration_date=datetime.strptime(data["Fecha de Expiración"], "%Y-%m-%d").date(),
            id_brand_product=data["Marca"],
            id_flavor_product=data["Sabor"],
            required_prescription=data["Necesita Prescripción"],
            recommended_age=data["Edad Recomendada"],
            instruction=data["Instrucciones"],
            guarantee=data["Garantía"]
        )

        try:
            self.product_management.add_product(new_product)
            messagebox.showinfo("Éxito", "Producto agregado correctamente")
            self.load_all_products()
        except Exception as e:
            messagebox.showerror("Error", f"Error al agregar el producto: {e}")

    def show_delete_product(self):
        self.clear_frame()

        search_frame = ttk.Frame(self.main_frame)
        search_frame.grid(row=0, column=0, padx=10, pady=10, sticky="nsew")

        self.tree_frame = ttk.Frame(self.main_frame)
        self.tree_frame.grid(row=0, column=1, padx=10, pady=10, sticky="nsew")

        self.main_frame.grid_columnconfigure(0, weight=1)
        self.main_frame.grid_columnconfigure(1, weight=1)
        self.main_frame.grid_rowconfigure(0, weight=1)

        self.search_label = ttk.Label(search_frame, text="Buscar Producto por Nombre o ID:")
        self.search_label.grid(row=0, column=0, padx=5, pady=5, sticky="w")

        self.search_entry = ttk.Entry(search_frame)
        self.search_entry.grid(row=0, column=1, padx=5, pady=5, sticky="ew")

        self.search_button = ttk.Button(search_frame, text="Buscar", command=self.perform_search_for_deletion)
        self.search_button.grid(row=1, column=0, columnspan=2, padx=5, pady=5, sticky="ew")

        search_frame.grid_columnconfigure(0, weight=0)
        search_frame.grid_columnconfigure(1, weight=1)

        columns = ("ID", "Nombre", "Precio", "Presentación")
        self.results_tree = ttk.Treeview(self.tree_frame, columns=columns, show='headings')
        self.results_tree.heading("ID", text="ID")
        self.results_tree.heading("Nombre", text="Nombre")
        self.results_tree.heading("Precio", text="Precio")
        self.results_tree.heading("Presentación", text="Presentación")
        self.results_tree.column("ID", width=50)
        self.results_tree.column("Nombre", width=200)
        self.results_tree.column("Precio", width=100)
        self.results_tree.column("Presentación", width=150)

        self.vsb = ttk.Scrollbar(self.tree_frame, orient="vertical", command=self.results_tree.yview)
        self.hsb = ttk.Scrollbar(self.tree_frame, orient="horizontal", command=self.results_tree.xview)

        self.results_tree.configure(yscrollcommand=self.vsb.set, xscrollcommand=self.hsb.set)
        self.results_tree.grid(row=0, column=0, sticky='nsew')
        self.vsb.grid(row=0, column=1, sticky='ns')
        self.hsb.grid(row=1, column=0, sticky='ew')

        self.tree_frame.grid_rowconfigure(0, weight=1)
        self.tree_frame.grid_columnconfigure(0, weight=1)

        self.delete_button = ttk.Button(self.tree_frame, text="Eliminar Producto Seleccionado", command=self.confirm_delete_product)
        self.delete_button.grid(row=2, column=0, columnspan=2, pady=10)

        self.load_all_products()

    def perform_search_for_deletion(self):
        search_term = self.search_entry.get()
        results = self.product_management.search_product(search_term)
        self.populate_tree(results)

    def confirm_delete_product(self):
        selected_item = self.results_tree.selection()
        if not selected_item:
            messagebox.showerror("Error", "Seleccione un producto para eliminar")
            return
        product_id = self.results_tree.item(selected_item, "values")[0]
        confirm = messagebox.askyesno("Confirmar Eliminación", f"¿Está seguro de que desea eliminar el producto con ID {product_id}?")
        if confirm:
            self.product_management.delete_product(product_id)
            messagebox.showinfo("Éxito", "Producto eliminado correctamente")
            self.load_all_products()

    def show_modify_product_form(self):
        self.clear_frame()

        # Frame para el formulario
        form_frame = ttk.Frame(self.main_frame)
        form_frame.grid(row=0, column=0, padx=10, pady=10, sticky="nsew")

        # Definición de campos del formulario
        self.entries = {
            "ID Presentación:": tk.Entry(form_frame),
            "ID Categoría:": tk.Entry(form_frame),
            "ID Proveedor:": tk.Entry(form_frame),
            "Nombre Producto:": tk.Entry(form_frame),
            "Cantidad:": tk.Entry(form_frame),
            "Costo Unitario:": tk.Entry(form_frame),
            "Precio Producto:": tk.Entry(form_frame),
            "Fecha de Expiración:": tk.Entry(form_frame),
            "ID Marca:": tk.Entry(form_frame),
            "ID Sabor:": tk.Entry(form_frame),
            "Requiere Prescripción:": tk.Entry(form_frame),
            "Edad Recomendada:": tk.Entry(form_frame),
            "Instrucción:": tk.Entry(form_frame),
            "Garantía:": tk.Entry(form_frame)
        }

        # Añadir campos al formulario
        row = 0
        for label, entry in self.entries.items():
            tk.Label(form_frame, text=label).grid(row=row, column=0, padx=5, pady=5, sticky="w")
            entry.grid(row=row, column=1, padx=5, pady=5, sticky="ew")
            row += 1

        # Botón para modificar producto
        self.modify_product_button = ttk.Button(form_frame, text="Modificar Producto", command=self.modify_product)
        self.modify_product_button.grid(row=row, column=0, columnspan=2, pady=10)

        # Frame para la tabla
        self.tree_frame = ttk.Frame(self.main_frame)
        self.tree_frame.grid(row=0, column=1, padx=10, pady=10, sticky="nsew")

        # Configurar el Treeview
        columns = ("ID", "Nombre", "Precio", "Presentación")
        self.results_tree = ttk.Treeview(self.tree_frame, columns=columns, show='headings')
        self.results_tree.heading("ID", text="ID")
        self.results_tree.heading("Nombre", text="Nombre")
        self.results_tree.heading("Precio", text="Precio")
        self.results_tree.heading("Presentación", text="Presentación")
        self.results_tree.column("ID", width=50)
        self.results_tree.column("Nombre", width=200)
        self.results_tree.column("Precio", width=100)
        self.results_tree.column("Presentación", width=150)

        # Scrollbars
        self.vsb = ttk.Scrollbar(self.tree_frame, orient="vertical", command=self.results_tree.yview)
        self.hsb = ttk.Scrollbar(self.tree_frame, orient="horizontal", command=self.results_tree.xview)
        self.results_tree.configure(yscrollcommand=self.vsb.set, xscrollcommand=self.hsb.set)

        self.results_tree.grid(row=0, column=0, sticky='nsew')
        self.vsb.grid(row=0, column=1, sticky='ns')
        self.hsb.grid(row=1, column=0, sticky='ew')

        self.tree_frame.grid_rowconfigure(0, weight=1)
        self.tree_frame.grid_columnconfigure(0, weight=1)

        # Ajuste de columnas y filas
        self.main_frame.grid_columnconfigure(0, weight=1)
        self.main_frame.grid_columnconfigure(1, weight=1)
        self.main_frame.grid_rowconfigure(0, weight=1)

        self.results_tree.bind("<<TreeviewSelect>>", self.on_product_select)

        self.load_all_products()

    def perform_search(self):
        search_term = self.search_entry.get()
        results = self.product_management.search_product(search_term)
        self.populate_tree(results)

    def populate_tree(self, products):
        self.results_tree.delete(*self.results_tree.get_children())
        for product in products:
            self.results_tree.insert("", "end", values=(product.id_product, product.name_product, product.product_price, product.id_presentation_type))

    def load_all_products(self):
        try:
            results = self.product_management.search_all_products()
            for item in self.results_tree.get_children():
                self.results_tree.delete(item)
            for row in results:
                self.results_tree.insert('', 'end', values=row)
        except Exception as e:
            messagebox.showerror("Error", f"Error al cargar los productos: {e}")


    def clear_frame(self):
        for widget in self.main_frame.winfo_children():
            widget.destroy()

    def on_product_select(self, event):
        selected_item = self.results_tree.selection()
        if selected_item:
            product_id = self.results_tree.item(selected_item, "values")[0]
            product = self.product_management.get_product_by_id(product_id)
            if product:
                self.entries["ID Presentación:"].delete(0, tk.END)
                self.entries["ID Presentación:"].insert(0, product.id_presentation_type)
                self.entries["ID Categoría:"].delete(0, tk.END)
                self.entries["ID Categoría:"].insert(0, product.id_category_product)
                self.entries["ID Proveedor:"].delete(0, tk.END)
                self.entries["ID Proveedor:"].insert(0, product.id_supplier)
                self.entries["Nombre Producto:"].delete(0, tk.END)
                self.entries["Nombre Producto:"].insert(0, product.name_product)
                self.entries["Cantidad:"].delete(0, tk.END)
                self.entries["Cantidad:"].insert(0, product.quantity)
                self.entries["Costo Unitario:"].delete(0, tk.END)
                self.entries["Costo Unitario:"].insert(0, product.unit_cost)
                self.entries["Precio Producto:"].delete(0, tk.END)
                self.entries["Precio Producto:"].insert(0, product.product_price)
                self.entries["Fecha de Expiración:"].delete(0, tk.END)
                self.entries["Fecha de Expiración:"].insert(0, product.expiration_date)
                self.entries["ID Marca:"].delete(0, tk.END)
                self.entries["ID Marca:"].insert(0, product.id_brand_product)
                self.entries["ID Sabor:"].delete(0, tk.END)
                self.entries["ID Sabor:"].insert(0, product.id_flavor_product)
                self.entries["Requiere Prescripción:"].delete(0, tk.END)
                self.entries["Requiere Prescripción:"].insert(0, product.required_prescription)
                self.entries["Edad Recomendada:"].delete(0, tk.END)
                self.entries["Edad Recomendada:"].insert(0, product.recommended_age)
                self.entries["Instrucción:"].delete(0, tk.END)
                self.entries["Instrucción:"].insert(0, product.instruction)
                self.entries["Garantía:"].delete(0, tk.END)
                self.entries["Garantía:"].insert(0, product.guarantee)

    def modify_product(self):
        selected_item = self.results_tree.selection()
        if not selected_item:
            messagebox.showerror("Error", "Seleccione un producto para modificar")
            return
        product_id = self.results_tree.item(selected_item, "values")[0]
        data = {}
        for label, entry in self.entries.items():
            data[label[:-1]] = entry.get()

        modified_product = Product(
            id_product=product_id,
            id_presentation_type=data["ID Presentación"],
            id_category_product=data["ID Categoría"],
            id_supplier=data["ID Proveedor"],
            name_product=data["Nombre Producto"],
            quantity=int(data["Cantidad"]),
            unit_cost=float(data["Costo Unitario"]),
            product_price=float(data["Precio Producto"]),
            expiration_date=datetime.strptime(data["Fecha de Expiración"], "%Y-%m-%d").date(),
            id_brand_product=data["ID Marca"],
            id_flavor_product=data["ID Sabor"],
            required_prescription=data["Requiere Prescripción"],
            recommended_age=data["Edad Recomendada"],
            instruction=data["Instrucción"],
            guarantee=data["Garantía"]
        )

        try:
            self.product_management.modify_product(modified_product)
            messagebox.showinfo("Éxito", "Producto modificado correctamente")
            self.load_all_products()
        except Exception as e:
            messagebox.showerror("Error", f"Error al modificar el producto: {e}")
# main
if __name__ == "__main__":
    root = tk.Tk()
    app = Inventory_Control_System(root)
    root.mainloop()