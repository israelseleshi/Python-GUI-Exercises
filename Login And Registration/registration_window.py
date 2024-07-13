import customtkinter as ctk

class RegistrationPage(ctk.CTkFrame):
    def __init__(self, master):
        super().__init__(master)

        self.master.title("Registration Page")
        self.master.geometry("400x400")

        # Create a frame for the registration form
        registration_frame = ctk.CTkFrame(self, corner_radius=10)
        registration_frame.pack(padx=20, pady=20)

        # Create labels and entry fields
        name_label = ctk.CTkLabel(registration_frame, text="Name:", font=("Arial", 14))
        name_label.grid(row=0, column=0, padx=5, pady=5, sticky="w")
        self.name_entry = ctk.CTkEntry(registration_frame, placeholder_text="Enter your name")
        self.name_entry.grid(row=0, column=1, padx=5, pady=5)

        username_label = ctk.CTkLabel(registration_frame, text="Username:", font=("Arial", 14))
        username_label.grid(row=1, column=0, padx=5, pady=5, sticky="w")
        self.username_entry = ctk.CTkEntry(registration_frame, placeholder_text="Enter username")
        self.username_entry.grid(row=1, column=1, padx=5, pady=5)

        email_label = ctk.CTkLabel(registration_frame, text="Email:", font=("Arial", 14))
        email_label.grid(row=2, column=0, padx=5, pady=5, sticky="w")
        self.email_entry = ctk.CTkEntry(registration_frame, placeholder_text="Enter email")
        self.email_entry.grid(row=2, column=1, padx=5, pady=5)

        password_label = ctk.CTkLabel(registration_frame, text="Password:", font=("Arial", 14))
        password_label.grid(row=3, column=0, padx=5, pady=5, sticky="w")
        self.password_entry = ctk.CTkEntry(registration_frame, placeholder_text="Enter password", show="*")
        self.password_entry.grid(row=3, column=1, padx=5, pady=5)

        confirm_password_label = ctk.CTkLabel(registration_frame, text="Confirm Password:", font=("Arial", 14))
        confirm_password_label.grid(row=4, column=0, padx=5, pady=5, sticky="w")
        self.confirm_password_entry = ctk.CTkEntry(registration_frame, placeholder_text="Confirm password", show="*")
        self.confirm_password_entry.grid(row=4, column=1, padx=5, pady=5)

        # Create register button
        register_button = ctk.CTkButton(registration_frame, text="Register", command=self.register)
        register_button.grid(row=5, column=0, columnspan=2, pady=10)

        # Create back button
        back_button = ctk.CTkButton(registration_frame, text="Back to Login", command=self.open_login)
        back_button.grid(row=6, column=0, columnspan=2, pady=10)

        self.pack(expand=True, fill="both")

    def open_login(self):
        # Create a login window instance
        from login_window import LoginPage
        login_window = LoginPage(self.master)
        self.master.switch_frame(login_window)

    def register(self):
        # Replace this with your actual registration logic
        name = self.name_entry.get()
        username = self.username_entry.get()
        email = self.email_entry.get()
        password = self.password_entry.get()
        confirm_password = self.confirm_password_entry.get()

        if password != confirm_password:
            print("Passwords do not match")
            return

        # Add user data to database or perform other actions
        print("Registration successful!")
