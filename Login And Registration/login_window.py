import customtkinter as ctk

class LoginPage(ctk.CTkFrame):
    def __init__(self, master):
        super().__init__(master)

        self.master.title("Login Page")
        self.master.geometry("400x300")

        # Create a frame for the login form
        login_frame = ctk.CTkFrame(self, corner_radius=10)
        login_frame.pack(padx=20, pady=20)

        # Create labels and entry fields
        username_label = ctk.CTkLabel(login_frame, text="Username:", font=("Arial", 14))
        username_label.grid(row=0, column=0, padx=5, pady=5, sticky="w")
        self.username_entry = ctk.CTkEntry(login_frame, placeholder_text="Enter username")
        self.username_entry.grid(row=0, column=1, padx=5, pady=5)

        password_label = ctk.CTkLabel(login_frame, text="Password:", font=("Arial", 14))
        password_label.grid(row=1, column=0, padx=5, pady=5, sticky="w")
        self.password_entry = ctk.CTkEntry(login_frame, placeholder_text="Enter password", show="*")
        self.password_entry.grid(row=1, column=1, padx=5, pady=5)

        # Create login button
        login_button = ctk.CTkButton(login_frame, text="Login", command=self.login)
        login_button.grid(row=2, column=0, columnspan=2, pady=10)

        # Create register button
        register_button = ctk.CTkButton(login_frame, text="Register", command=self.open_registration)
        register_button.grid(row=3, column=0, columnspan=2, pady=10)

        self.pack(expand=True, fill="both")

    def open_registration(self):
        # Create a registration window instance
        from registration_window import RegistrationPage
        registration_window = RegistrationPage(self.master)
        self.master.switch_frame(registration_window)

    def login(self):
        # Replace this with your actual login logic
        username = self.username_entry.get()
        password = self.password_entry.get()

        if username == "your_username" and password == "your_password":
            # Successful login, navigate to main window or perform other actions
            print("Login successful!")
        else:
            # Incorrect credentials, display error message
            print("Incorrect username or password")
