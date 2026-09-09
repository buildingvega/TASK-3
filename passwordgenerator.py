import tkinter as tk
from tkinter import messagebox
import string
import secrets
import pyperclip


class PasswordGenerator:
    def __init__(self, root):
        self.root = root
        self.root.title("Random Password Generator")
        self.root.geometry("600x720")
        self.root.resizable(False, False)

        self.history = []

        self.length_var = tk.IntVar(value=12)
        self.upper_var = tk.BooleanVar(value=True)
        self.lower_var = tk.BooleanVar(value=True)
        self.number_var = tk.BooleanVar(value=True)
        self.symbol_var = tk.BooleanVar(value=True)
        self.ambiguous_var = tk.BooleanVar(value=True)

        self.password_var = tk.StringVar()
        self.strength_var = tk.StringVar(value="Strength: -")

        self.create_gui()

    def create_gui(self):
        tk.Label(
            self.root,
            text="🔐 Random Password Generator",
            font=("Arial", 22, "bold")
        ).pack(pady=20)

        main_frame = tk.Frame(self.root)
        main_frame.pack(padx=30, fill="both")

        length_frame = tk.LabelFrame(
            main_frame,
            text="Password Length",
            font=("Arial", 11, "bold"),
            padx=15,
            pady=15
        )
        length_frame.pack(fill="x", pady=10)

        self.length_label = tk.Label(
            length_frame,
            text="Length: 12",
            font=("Arial", 12)
        )
        self.length_label.pack()

        tk.Scale(
            length_frame,
            from_=8,
            to=64,
            orient="horizontal",
            variable=self.length_var,
            length=450,
            command=self.update_length
        ).pack()

        type_frame = tk.LabelFrame(
            main_frame,
            text="Character Types",
            font=("Arial", 11, "bold"),
            padx=15,
            pady=10
        )
        type_frame.pack(fill="x", pady=10)

        tk.Checkbutton(
            type_frame,
            text="Uppercase Letters (A-Z)",
            variable=self.upper_var,
            font=("Arial", 11)
        ).pack(anchor="w")

        tk.Checkbutton(
            type_frame,
            text="Lowercase Letters (a-z)",
            variable=self.lower_var,
            font=("Arial", 11)
        ).pack(anchor="w")

        tk.Checkbutton(
            type_frame,
            text="Numbers (0-9)",
            variable=self.number_var,
            font=("Arial", 11)
        ).pack(anchor="w")

        tk.Checkbutton(
            type_frame,
            text="Symbols (!@#$...)",
            variable=self.symbol_var,
            font=("Arial", 11)
        ).pack(anchor="w")

        options_frame = tk.LabelFrame(
            main_frame,
            text="Security Options",
            font=("Arial", 11, "bold"),
            padx=15,
            pady=10
        )
        options_frame.pack(fill="x", pady=10)

        tk.Checkbutton(
            options_frame,
            text="Exclude ambiguous characters (0, O, o, 1, I, l)",
            variable=self.ambiguous_var,
            font=("Arial", 11)
        ).pack(anchor="w")

        password_frame = tk.LabelFrame(
            main_frame,
            text="Generated Password",
            font=("Arial", 11, "bold"),
            padx=15,
            pady=15
        )
        password_frame.pack(fill="x", pady=10)

        tk.Entry(
            password_frame,
            textvariable=self.password_var,
            font=("Consolas", 15),
            justify="center",
            width=40
        ).pack(pady=5)

        tk.Label(
            password_frame,
            textvariable=self.strength_var,
            font=("Arial", 12, "bold")
        ).pack(pady=5)

        button_frame = tk.Frame(main_frame)
        button_frame.pack(pady=15)

        tk.Button(
            button_frame,
            text="Generate Password",
            font=("Arial", 11, "bold"),
            width=20,
            height=2,
            command=self.generate_password
        ).grid(row=0, column=0, padx=8)

        tk.Button(
            button_frame,
            text="Copy Password",
            font=("Arial", 11, "bold"),
            width=20,
            height=2,
            command=self.copy_password
        ).grid(row=0, column=1, padx=8)

        history_frame = tk.LabelFrame(
            main_frame,
            text="Generation History (Last 5)",
            font=("Arial", 11, "bold"),
            padx=10,
            pady=10
        )
        history_frame.pack(fill="x", pady=10)

        self.history_listbox = tk.Listbox(
            history_frame,
            height=5,
            font=("Consolas", 11)
        )
        self.history_listbox.pack(fill="x")

    def update_length(self, value):
        self.length_label.config(
            text=f"Length: {int(float(value))}"
        )

    def get_character_sets(self):
        sets = []

        if self.upper_var.get():
            sets.append(string.ascii_uppercase)

        if self.lower_var.get():
            sets.append(string.ascii_lowercase)

        if self.number_var.get():
            sets.append(string.digits)

        if self.symbol_var.get():
            sets.append(string.punctuation)

        if self.ambiguous_var.get():
            ambiguous = "0Oo1Il"
            sets = [
                "".join(c for c in s if c not in ambiguous)
                for s in sets
            ]

        return [s for s in sets if s]

    def generate_password(self):
        length = self.length_var.get()
        character_sets = self.get_character_sets()

        if len(character_sets) < 2:
            messagebox.showerror(
                "Invalid Selection",
                "Select at least 2 character types."
            )
            return

        if length < len(character_sets):
            messagebox.showerror(
                "Invalid Length",
                "Password length is too short."
            )
            return

        all_characters = "".join(character_sets)

        password = [
            secrets.choice(char_set)
            for char_set in character_sets
        ]

        for _ in range(length - len(password)):
            password.append(
                secrets.choice(all_characters)
            )

        secrets.SystemRandom().shuffle(password)

        password = "".join(password)

        self.password_var.set(password)

        self.calculate_strength(
            password,
            len(character_sets)
        )

        self.add_to_history(password)

    def calculate_strength(self, password, diversity):
        length = len(password)
        score = diversity

        if length >= 8:
            score += 1

        if length >= 12:
            score += 1

        if length >= 16:
            score += 1

        if score <= 3:
            strength = "Weak"
        elif score <= 5:
            strength = "Medium"
        else:
            strength = "Strong"

        self.strength_var.set(
            f"Strength: {strength}"
        )

    def copy_password(self):
        password = self.password_var.get()

        if not password:
            messagebox.showwarning(
                "No Password",
                "Generate a password first."
            )
            return

        pyperclip.copy(password)

        messagebox.showinfo(
            "Copied",
            "Password copied to clipboard!"
        )

    def add_to_history(self, password):
        self.history.insert(0, password)
        self.history = self.history[:5]

        self.history_listbox.delete(0, tk.END)

        for password in self.history:
            self.history_listbox.insert(
                tk.END,
                password
            )


if __name__ == "__main__":
    root = tk.Tk()
    PasswordGenerator(root)
    root.mainloop()