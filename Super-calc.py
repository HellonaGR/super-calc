import math
import tkinter as tk
from tkinter import ttk, messagebox

# --- Μαθηματικές Συναρτήσεις ---
def area_circle(radius):
    if radius <= 0:
        raise ValueError("Η ακτίνα πρέπει να είναι θετικός αριθμός!")
    return math.pi * radius ** 2


def perimeter_circle(radius):
    if radius <= 0:
        raise ValueError("Η ακτίνα πρέπει να είναι θετικός αριθμός!")
    return 2 * math.pi * radius


def area_square(side):
    if side <= 0:
        raise ValueError("Η πλευρά πρέπει να είναι θετικός αριθμός!")
    return side ** 2


def perimeter_square(side):
    if side <= 0:
        raise ValueError("Η πλευρά πρέπει να είναι θετικός αριθμός!")
    return 4 * side


def area_rectangle(length, width):
    if length <= 0 or width <= 0:
        raise ValueError("Οι διαστάσεις πρέπει να είναι θετικοί αριθμοί!")
    return length * width


def perimeter_rectangle(length, width):
    if length <= 0 or width <= 0:
        raise ValueError("Οι διαστάσεις πρέπει να είναι θετικοί αριθμοί!")
    return 2 * (length + width)


def area_triangle(base, height):
    if base <= 0 or height <= 0:
        raise ValueError("Βάση και ύψος πρέπει να είναι θετικοί αριθμοί!")
    return 0.5 * base * height


def perimeter_triangle(side1, side2, side3):
    if any(s <= 0 for s in (side1, side2, side3)):
        raise ValueError("Όλες οι πλευρές πρέπει να είναι θετικοί αριθμοί!")
    if not (side1 + side2 > side3 and side1 + side3 > side2 and side2 + side3 > side1):
        raise ValueError("Άκυρες πλευρές τριγώνου (τριγωνική ανισότητα)")
    return side1 + side2 + side3


def area_parallelogram(base, height):
    if base <= 0 or height <= 0:
        raise ValueError("Βάση και ύψος πρέπει να είναι θετικοί αριθμοί!")
    return base * height


def perimeter_parallelogram(base, side):
    if base <= 0 or side <= 0:
        raise ValueError("Βάση και πλευρά πρέπει να είναι θετικοί αριθμοί!")
    return 2 * (base + side)


def area_rhombus(diag1, diag2):
    if diag1 <= 0 or diag2 <= 0:
        raise ValueError("Οι διαγώνιοι πρέπει να είναι θετικοί αριθμοί!")
    return 0.5 * diag1 * diag2


def perimeter_rhombus(side):
    if side <= 0:
        raise ValueError("Η πλευρά πρέπει να είναι θετικός αριθμός!")
    return 4 * side


def area_trapezoid(base1, base2, height):
    if base1 <= 0 or base2 <= 0 or height <= 0:
        raise ValueError("Οι βάσεις και το ύψος πρέπει να είναι θετικοί αριθμοί!")
    return 0.5 * (base1 + base2) * height


def perimeter_trapezoid(base1, base2, side1, side2):
    if any(s <= 0 for s in (base1, base2, side1, side2)):
        raise ValueError("Όλες οι πλευρές πρέπει να είναι θετικοί αριθμοί!")
    return base1 + base2 + side1 + side2


def area_hexagon(side):
    if side <= 0:
        raise ValueError("Η πλευρά πρέπει να είναι θετικός αριθμός!")
    return (3 * math.sqrt(3) / 2) * side ** 2


def perimeter_hexagon(side):
    if side <= 0:
        raise ValueError("Η πλευρά πρέπει να είναι θετικός αριθμός!")
    return 6 * side

# --- Μετατροπή Μονάδων ---
def convert_length(value_cm, unit):
    factors = {
        'mm': 10,
        'cm': 1,
        'm': 1/100,
        'km': 1/100000,
        'in': 1/2.54,
        'ft': 1/30.48,
        'yd': 1/91.44,
        'mile': 1/160934.4
    }
    return value_cm * factors[unit]


def convert_area(value_cm2, unit):
    factors = {
        'mm': 10,
        'cm': 1,
        'm': 1/100,
        'km': 1/100000,
        'in': 1/2.54,
        'ft': 1/30.48,
        'yd': 1/91.44,
        'mile': 1/160934.4
    }
    f = factors[unit]
    return value_cm2 * (f ** 2)

class GeometryCalculator:
    def __init__(self, root):
        self.root = root
        self.root.title("Ακριβής Γεωμετρικός Υπολογιστής")
        self.root.geometry("550x600")
        self.root.resizable(False, False)
        self.style = ttk.Style()
        self.style.configure('TButton', font=('Arial', 10), padding=6)
        self.style.configure('Title.TLabel', font=('Arial', 16, 'bold'))
        self.create_widgets()

    def create_widgets(self):
        main_frame = ttk.Frame(self.root, padding=20)
        main_frame.pack(fill=tk.BOTH, expand=True)
        title = ttk.Label(main_frame, text="Επιλέξτε Γεωμετρικό Σχήμα", style='Title.TLabel')
        title.pack(pady=15)
        shapes = [
            ("Κύκλος", self.open_circle_window),
            ("Τετράγωνο", self.open_square_window),
            ("Ορθογώνιο", self.open_rectangle_window),
            ("Τρίγωνο", self.open_triangle_window),
            ("Παραλληλόγραμμο", self.open_parallelogram_window),
            ("Ρόμβος", self.open_rhombus_window),
            ("Τραπέζιο", self.open_trapezoid_window),
            ("Κανονικό Εξάγωνο", self.open_hexagon_window)
        ]
        for text, cmd in shapes:
            ttk.Button(main_frame, text=text, command=cmd, width=30).pack(pady=5)
        ttk.Button(main_frame, text="Πίνακας Μονάδων", command=self.open_units_table, width=30).pack(pady=15)

    def add_unit_selector(self, parent):
        frame = ttk.Frame(parent)
        ttk.Label(frame, text="Επιλογή Μονάδας:").pack(side=tk.LEFT, padx=(0,10))
        combo = ttk.Combobox(frame, values=['mm','cm','m','km','in','ft','yd','mile'], state='readonly', width=7)
        combo.set('cm')
        combo.pack(side=tk.LEFT)
        frame.pack(pady=10)
        return combo

    def open_circle_window(self):
        win = tk.Toplevel(self.root)
        win.title("Υπολογισμός Κύκλου")
        win.geometry("400x400")
        notebook = ttk.Notebook(win)
        notebook.pack(expand=True, fill=tk.BOTH, padx=10, pady=10)
        # Εμβαδόν
        tab1 = ttk.Frame(notebook)
        notebook.add(tab1, text="Εμβαδόν")
        mode1 = tk.StringVar(value="radius")
        frame1 = ttk.Frame(tab1)
        frame1.pack(pady=5)
        ttk.Radiobutton(frame1, text="Ακτίνα (cm)", variable=mode1, value="radius").pack(side=tk.LEFT)
        ttk.Radiobutton(frame1, text="Διάμετρος (cm)", variable=mode1, value="diameter").pack(side=tk.LEFT)
        entry1 = ttk.Entry(tab1)
        entry1.pack(pady=5)
        unit1 = self.add_unit_selector(tab1)
        def calc_area():
            try:
                val = float(entry1.get())
                if mode1.get() == "diameter":
                    r = val / 2
                else:
                    r = val
                unit = unit1.get()
                a_cm2 = area_circle(r)
                a = convert_area(a_cm2, unit)
                messagebox.showinfo("Εμβαδόν", f"Εμβαδόν: {a:.6g} {unit}²")
            except Exception as e:
                messagebox.showerror("Σφάλμα", str(e))
        ttk.Button(tab1, text="Υπολογισμός", command=calc_area).pack(pady=10)
        # Περίμετρος
        tab2 = ttk.Frame(notebook)
        notebook.add(tab2, text="Περίμετρος")
        mode2 = tk.StringVar(value="radius")
        frame2 = ttk.Frame(tab2)
        frame2.pack(pady=5)
        ttk.Radiobutton(frame2, text="Ακτίνα (cm)", variable=mode2, value="radius").pack(side=tk.LEFT)
        ttk.Radiobutton(frame2, text="Διάμετρος (cm)", variable=mode2, value="diameter").pack(side=tk.LEFT)
        entry2 = ttk.Entry(tab2)
        entry2.pack(pady=5)
        unit2 = self.add_unit_selector(tab2)
        def calc_perim():
            try:
                val = float(entry2.get())
                if mode2.get() == "diameter":
                    r = val / 2
                else:
                    r = val
                unit = unit2.get()
                p_cm = perimeter_circle(r)
                p = convert_length(p_cm, unit)
                messagebox.showinfo("Περίμετρος", f"Περίμετρος: {p:.6g} {unit}")
            except Exception as e:
                messagebox.showerror("Σφάλμα", str(e))
        ttk.Button(tab2, text="Υπολογισμός", command=calc_perim).pack(pady=10)

    def open_square_window(self):
        win = tk.Toplevel(self.root)
        win.title("Υπολογισμός Τετραγώνου")
        win.geometry("400x400")
        notebook = ttk.Notebook(win)
        notebook.pack(expand=True, fill=tk.BOTH, padx=10, pady=10)
        # Εμβαδόν
        tab1 = ttk.Frame(notebook)
        notebook.add(tab1, text="Εμβαδόν")
        ttk.Label(tab1, text="Πλευρά (cm):").pack(pady=5)
        entry1 = ttk.Entry(tab1)
        entry1.pack(pady=5)
        unit1 = self.add_unit_selector(tab1)
        def calc_area():
            try:
                side = float(entry1.get())
                unit = unit1.get()
                a_cm2 = area_square(side)
                a = convert_area(a_cm2, unit)
                messagebox.showinfo("Εμβαδόν", f"Εμβαδόν: {a:.6g} {unit}²")
            except Exception as e:
                messagebox.showerror("Σφάλμα", str(e))
        ttk.Button(tab1, text="Υπολογισμός", command=calc_area).pack(pady=10)
        # Περίμετρος
        tab2 = ttk.Frame(notebook)
        notebook.add(tab2, text="Περίμετρος")
        ttk.Label(tab2, text="Πλευρά (cm):").pack(pady=5)
        entry2 = ttk.Entry(tab2)
        entry2.pack(pady=5)
        unit2 = self.add_unit_selector(tab2)
        def calc_perim():
            try:
                side = float(entry2.get())
                unit = unit2.get()
                p_cm = perimeter_square(side)
                p = convert_length(p_cm, unit)
                messagebox.showinfo("Περίμετρος", f"Περίμετρος: {p:.6g} {unit}")
            except Exception as e:
                messagebox.showerror("Σφάλμα", str(e))
        ttk.Button(tab2, text="Υπολογισμός", command=calc_perim).pack(pady=10)

    def open_rectangle_window(self):
        win = tk.Toplevel(self.root)
        win.title("Υπολογισμός Ορθογώνιου")
        win.geometry("400x400")
        notebook = ttk.Notebook(win)
        notebook.pack(expand=True, fill=tk.BOTH, padx=10, pady=10)
        # Εμβαδόν
        tab1 = ttk.Frame(notebook)
        notebook.add(tab1, text="Εμβαδόν")
        ttk.Label(tab1, text="Μήκος (cm):").pack(pady=5)
        entry_l1 = ttk.Entry(tab1)
        entry_l1.pack(pady=5)
        ttk.Label(tab1, text="Πλάτος (cm):").pack(pady=5)
        entry_w1 = ttk.Entry(tab1)
        entry_w1.pack(pady=5)
        unit1 = self.add_unit_selector(tab1)
        def calc_area():
            try:
                l = float(entry_l1.get())
                w = float(entry_w1.get())
                unit = unit1.get()
                a_cm2 = area_rectangle(l, w)
                a = convert_area(a_cm2, unit)
                messagebox.showinfo("Εμβαδόν", f"Εμβαδόν: {a:.6g} {unit}²")
            except Exception as e:
                messagebox.showerror("Σφάλμα", str(e))
        ttk.Button(tab1, text="Υπολογισμός", command=calc_area).pack(pady=10)
        # Περίμετρος
        tab2 = ttk.Frame(notebook)
        notebook.add(tab2, text="Περίμετρος")
        ttk.Label(tab2, text="Μήκος (cm):").pack(pady=5)
        entry_l2 = ttk.Entry(tab2)
        entry_l2.pack(pady=5)
        ttk.Label(tab2, text="Πλάτος (cm):").pack(pady=5)
        entry_w2 = ttk.Entry(tab2)
        entry_w2.pack(pady=5)
        unit2 = self.add_unit_selector(tab2)
        def calc_perim():
            try:
                l = float(entry_l2.get())
                w = float(entry_w2.get())
                unit = unit2.get()
                p_cm = perimeter_rectangle(l, w)
                p = convert_length(p_cm, unit)
                messagebox.showinfo("Περίμετρος", f"Περίμετρος: {p:.6g} {unit}")
            except Exception as e:
                messagebox.showerror("Σφάλμα", str(e))
        ttk.Button(tab2, text="Υπολογισμός", command=calc_perim).pack(pady=10)

    def open_triangle_window(self):
        win = tk.Toplevel(self.root)
        win.title("Υπολογισμός Τριγώνου")
        win.geometry("420x420")
        notebook = ttk.Notebook(win)
        notebook.pack(expand=True, fill=tk.BOTH, padx=10, pady=10)
        # Εμβαδόν
        tab1 = ttk.Frame(notebook)
        notebook.add(tab1, text="Εμβαδόν")
        ttk.Label(tab1, text="Βάση (cm):").pack(pady=5)
        entry_b = ttk.Entry(tab1)
        entry_b.pack(pady=5)
        ttk.Label(tab1, text="Ύψος (cm):").pack(pady=5)
        entry_h = ttk.Entry(tab1)
        entry_h.pack(pady=5)
        unit1 = self.add_unit_selector(tab1)

        def calc_area():
            try:
                b = float(entry_b.get())
                h = float(entry_h.get())
                u = unit1.get()
                a_cm2 = area_triangle(b, h)
                a = convert_area(a_cm2, u)
                messagebox.showinfo("Εμβαδόν", f"Εμβαδόν: {a:.6g} {u}²")
            except Exception as e:
                messagebox.showerror("Σφάλμα", str(e))

        ttk.Button(tab1, text="Υπολογισμός", command=calc_area).pack(pady=10)

        # Περίμετρος
        tab2 = ttk.Frame(notebook)
        notebook.add(tab2, text="Περίμετρος")
        entries = []
        for lbl in ["Α (cm):", "Β (cm):", "Γ (cm):"]:
            ttk.Label(tab2, text=f"Πλευρά {lbl}").pack(pady=5)
            e = ttk.Entry(tab2)
            e.pack(pady=5)
            entries.append(e)
        unit2 = self.add_unit_selector(tab2)

        def calc_perim():
            try:
                s1, s2, s3 = [float(e.get()) for e in entries]
                u = unit2.get()
                p_cm = perimeter_triangle(s1, s2, s3)
                p = convert_length(p_cm, u)
                messagebox.showinfo("Περίμετρος", f"Περίμετρος: {p:.6g} {u}")
            except Exception as e:
                messagebox.showerror("Σφάλμα", str(e))

        ttk.Button(tab2, text="Υπολογισμός", command=calc_perim).pack(pady=10)

    def open_parallelogram_window(self):
        win = tk.Toplevel(self.root)
        win.title("Υπολογισμός Παραλληλογράμμου")
        win.geometry("400x400")
        notebook = ttk.Notebook(win)
        notebook.pack(expand=True, fill=tk.BOTH, padx=10, pady=10)
        # Εμβαδόν
        tab1 = ttk.Frame(notebook)
        notebook.add(tab1, text="Εμβαδόν")
        ttk.Label(tab1, text="Βάση (cm):").pack(pady=5)
        entry_b1 = ttk.Entry(tab1)
        entry_b1.pack(pady=5)
        ttk.Label(tab1, text="Ύψος (cm):").pack(pady=5)
        entry_h1 = ttk.Entry(tab1)
        entry_h1.pack(pady=5)
        unit1 = self.add_unit_selector(tab1)
        def calc_area():
            try:
                b = float(entry_b1.get())
                h = float(entry_h1.get())
                u = unit1.get()
                a_cm2 = area_parallelogram(b, h)
                a = convert_area(a_cm2, u)
                messagebox.showinfo("Εμβαδόν", f"Εμβαδόν: {a:.6g} {u}²")
            except Exception as e:
                messagebox.showerror("Σφάλμα", str(e))
        ttk.Button(tab1, text="Υπολογισμός", command=calc_area).pack(pady=10)
        # Περίμετρος
        tab2 = ttk.Frame(notebook)
        notebook.add(tab2, text="Περίμετρος")
        ttk.Label(tab2, text="Βάση (cm):").pack(pady=5)
        entry_b2 = ttk.Entry(tab2)
        entry_b2.pack(pady=5)
        ttk.Label(tab2, text="Πλευρά (cm):").pack(pady=5)
        entry_s2 = ttk.Entry(tab2)
        entry_s2.pack(pady=5)
        unit2 = self.add_unit_selector(tab2)
        def calc_perim():
            try:
                b = float(entry_b2.get())
                s = float(entry_s2.get())
                u = unit2.get()
                p_cm = perimeter_parallelogram(b, s)
                p = convert_length(p_cm, u)
                messagebox.showinfo("Περίμετρος", f"Περίμετρος: {p:.6g} {u}")
            except Exception as e:
                messagebox.showerror("Σφάλμα", str(e))
        ttk.Button(tab2, text="Υπολογισμός", command=calc_perim).pack(pady=10)

    def open_rhombus_window(self):
        win = tk.Toplevel(self.root)
        win.title("Υπολογισμός Ρόμβου")
        win.geometry("400x400")
        notebook = ttk.Notebook(win)
        notebook.pack(expand=True, fill=tk.BOTH, padx=10, pady=10)
        # Εμβαδόν
        tab1 = ttk.Frame(notebook)
        notebook.add(tab1, text="Εμβαδόν")
        ttk.Label(tab1, text="Διαγώνιος 1 (cm):").pack(pady=5)
        entry_d1 = ttk.Entry(tab1)
        entry_d1.pack(pady=5)
        ttk.Label(tab1, text="Διαγώνιος 2 (cm):").pack(pady=5)
        entry_d2 = ttk.Entry(tab1)
        entry_d2.pack(pady=5)
        unit1 = self.add_unit_selector(tab1)
        def calc_area():
            try:
                d1 = float(entry_d1.get())
                d2 = float(entry_d2.get())
                u = unit1.get()
                a_cm2 = area_rhombus(d1, d2)
                a = convert_area(a_cm2, u)
                messagebox.showinfo("Εμβαδόν", f"Εμβαδόν: {a:.6g} {u}²")
            except Exception as e:
                messagebox.showerror("Σφάλμα", str(e))
        ttk.Button(tab1, text="Υπολογισμός", command=calc_area).pack(pady=10)
        # Περίμετρος
        tab2 = ttk.Frame(notebook)
        notebook.add(tab2, text="Περίμετρος")
        ttk.Label(tab2, text="Πλευρά (cm):").pack(pady=5)
        entry_s = ttk.Entry(tab2)
        entry_s.pack(pady=5)
        unit2 = self.add_unit_selector(tab2)
        def calc_perim():
            try:
                s = float(entry_s.get())
                u = unit2.get()
                p_cm = perimeter_rhombus(s)
                p = convert_length(p_cm, u)
                messagebox.showinfo("Περίμετρος", f"Περίμετρος: {p:.6g} {u}")
            except Exception as e:
                messagebox.showerror("Σφάλμα", str(e))
        ttk.Button(tab2, text="Υπολογισμός", command=calc_perim).pack(pady=10)

    def open_trapezoid_window(self):
        win = tk.Toplevel(self.root)
        win.title("Υπολογισμός Τραπεζίου")
        win.geometry("420x420")
        notebook = ttk.Notebook(win)
        notebook.pack(expand=True, fill=tk.BOTH, padx=10, pady=10)
        # Εμβαδόν
        tab1 = ttk.Frame(notebook)
        notebook.add(tab1, text="Εμβαδόν")
        ttk.Label(tab1, text="Βάση 1 (cm):").pack(pady=5)
        entry_b1 = ttk.Entry(tab1)
        entry_b1.pack(pady=5)
        ttk.Label(tab1, text="Βάση 2 (cm):").pack(pady=5)
        entry_b2 = ttk.Entry(tab1)
        entry_b2.pack(pady=5)
        ttk.Label(tab1, text="Ύψος (cm):").pack(pady=5)
        entry_h = ttk.Entry(tab1)
        entry_h.pack(pady=5)
        unit1 = self.add_unit_selector(tab1)
        def calc_area():
            try:
                b1 = float(entry_b1.get())
                b2 = float(entry_b2.get())
                h = float(entry_h.get())
                u = unit1.get()
                a_cm2 = area_trapezoid(b1, b2, h)
                a = convert_area(a_cm2, u)
                messagebox.showinfo("Εμβαδόν", f"Εμβαδόν: {a:.6g} {u}²")
            except Exception as e:
                messagebox.showerror("Σφάλμα", str(e))
        ttk.Button(tab1, text="Υπολογισμός", command=calc_area).pack(pady=10)
        # Περίμετρος
        tab2 = ttk.Frame(notebook)
        notebook.add(tab2, text="Περίμετρος")
        ttk.Label(tab2, text="Βάση 1 (cm):").pack(pady=5)
        entry_b1p = ttk.Entry(tab2)
        entry_b1p.pack(pady=5)
        ttk.Label(tab2, text="Βάση 2 (cm):").pack(pady=5)
        entry_b2p = ttk.Entry(tab2)
        entry_b2p.pack(pady=5)
        ttk.Label(tab2, text="Πλευρά 1 (cm):").pack(pady=5)
        entry_s1 = ttk.Entry(tab2)
        entry_s1.pack(pady=5)
        ttk.Label(tab2, text="Πλευρά 2 (cm):").pack(pady=5)
        entry_s2 = ttk.Entry(tab2)
        entry_s2.pack(pady=5)
        unit2 = self.add_unit_selector(tab2)
        def calc_perim():
            try:
                b1 = float(entry_b1p.get())
                b2 = float(entry_b2p.get())
                s1 = float(entry_s1.get())
                s2 = float(entry_s2.get())
                u = unit2.get()
                p_cm = perimeter_trapezoid(b1, b2, s1, s2)
                p = convert_length(p_cm, u)
                messagebox.showinfo("Περίμετρος", f"Περίμετρος: {p:.6g} {u}")
            except Exception as e:
                messagebox.showerror("Σφάλμα", str(e))
        ttk.Button(tab2, text="Υπολογισμός", command=calc_perim).pack(pady=10)

    def open_hexagon_window(self):
        win = tk.Toplevel(self.root)
        win.title("Υπολογισμός Κανονικού Εξαγώνου")
        win.geometry("400x400")
        notebook = ttk.Notebook(win)
        notebook.pack(expand=True, fill=tk.BOTH, padx=10, pady=10)
        # Εμβαδόν
        tab1 = ttk.Frame(notebook)
        notebook.add(tab1, text="Εμβαδόν")
        ttk.Label(tab1, text="Πλευρά (cm):").pack(pady=5)
        entry1 = ttk.Entry(tab1)
        entry1.pack(pady=5)
        unit1 = self.add_unit_selector(tab1)
        def calc_area():
            try:
                s = float(entry1.get())
                u = unit1.get()
                a_cm2 = area_hexagon(s)
                a = convert_area(a_cm2, u)
                messagebox.showinfo("Εμβαδόν", f"Εμβαδόν: {a:.6g} {u}²")
            except Exception as e:
                messagebox.showerror("Σφάλμα", str(e))
        ttk.Button(tab1, text="Υπολογισμός", command=calc_area).pack(pady=10)
        # Περίμετρος
        tab2 = ttk.Frame(notebook)
        notebook.add(tab2, text="Περίμετρος")
        ttk.Label(tab2, text="Πλευρά (cm):").pack(pady=5)
        entry2 = ttk.Entry(tab2)
        entry2.pack(pady=5)
        unit2 = self.add_unit_selector(tab2)
        def calc_perim():
            try:
                s = float(entry2.get())
                u = unit2.get()
                p_cm = perimeter_hexagon(s)
                p = convert_length(p_cm, u)
                messagebox.showinfo("Περίμετρος", f"Περίμετρος: {p:.6g} {u}")
            except Exception as e:
                messagebox.showerror("Σφάλμα", str(e))
        ttk.Button(tab2, text="Υπολογισμός", command=calc_perim).pack(pady=10)

    def open_units_table(self):
        win = tk.Toplevel(self.root)
        win.title("Πίνακας Μονάδων")
        win.geometry("420x350")
        cols = ("Σύμβολο", "Ελληνικά", "Αγγλικά")
        tree = ttk.Treeview(win, columns=cols, show='headings', height=8)
        for c in cols:
            tree.heading(c, text=c)
            tree.column(c, width=120)
        units = [
            ("mm", "χιλιοστά (χιλ)", "millimeters (mm)"),
            ("cm", "εκατοστά (εκ)", "centimeters (cm)"),
            ("m", "μέτρα (μ)", "meters (m)"),
            ("km", "χιλιόμετρα (χλμ)", "kilometers (km)"),
            ("in", "ίντσες (ίντ)", "inches (in)"),
            ("ft", "πόδια (πτ)", "feet (ft)"),
            ("yd", "γιάρδες (γιαρ)", "yards (yd)"),
            ("mile", "μίλια (μίλ)", "miles (mile)")
        ]
        for u in units:
            tree.insert('', tk.END, values=u)
        tree.pack(padx=10, pady=10)
        ttk.Button(win, text="Κλείσιμο", command=win.destroy).pack(pady=5)


if __name__ == '__main__':
    root = tk.Tk()
    app = GeometryCalculator(root)
    root.mainloop()
