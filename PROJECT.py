
import tkinter as tk
from tkinter import simpledialog  # Add this import statement

class Patient:
    def __init__(self, name, age, gender, health_issue=""):
        self.name = name
        self.age = age
        self.gender = gender
        self.health_issue= health_issue

class Doctor:
    def __init__(self, name, department):
        self.name = name
        self.department = department

class Appointment:
    def __init__(self, patient, doctor, date, time):
        self.patient = patient
        self.doctor = doctor
        self.date = date
        self.time = time

class Equipment:
    def __init__(self, name, quantity):
        self.name = name
        self.quantity = quantity

class Hospital:
    def __init__(self, name):
        self.name = name
        self.patients = []
        self.doctors = []
        self.appointments = []
        self.equipment = []

    def add_patient(self, name, age, gender, health_issue=""):
        patient = Patient(name, age, gender, health_issue)
        self.patients.append(patient)

    def add_doctor(self, name, department):
        doctor = Doctor(name, department)
        self.doctors.append(doctor)

    def schedule_appointment(self, patient_name, doctor_name, date, time):
        patient = next((p for p in self.patients if p.name == patient_name), None)
        doctor = next((d for d in self.doctors if d.name == doctor_name), None)
        if patient and doctor:
            appointment = Appointment(patient, doctor, date, time)
            self.appointments.append(appointment)
            return True
        else:
            return False

    def add_equipment(self, name, quantity):
        equipment = Equipment(name, quantity)
        self.equipment.append(equipment)

# Placeholder functions
def add_patient():
    pass

def schedule_appointment():
    pass

def view_doctors():
    pass

def view_patients():
    pass

def view_appointments():
    pass

# Function to add a new patient
def add_patient():
    # Open a new window for adding patient details
    add_patient_window = tk.Toplevel(window)
    add_patient_window.title("Add Patient")

    # Frame to hold patient details entry widgets
    patient_frame = tk.Frame(add_patient_window)
    patient_frame.pack(padx=10, pady=10)

    # Labels and Entry widgets for patient details
    patient_name_label = tk.Label(patient_frame, text="Name:")
    patient_name_label.grid(row=0, column=0, sticky="e")

    patient_name_entry = tk.Entry(patient_frame)
    patient_name_entry.grid(row=0, column=1)

    patient_age_label = tk.Label(patient_frame, text="Age:")
    patient_age_label.grid(row=1, column=0, sticky="e")

    patient_age_entry = tk.Entry(patient_frame)
    patient_age_entry.grid(row=1, column=1)

    patient_gender_label = tk.Label(patient_frame, text="Gender:")
    patient_gender_label.grid(row=2, column=0, sticky="e")

    patient_gender_entry = tk.Entry(patient_frame)
    patient_gender_entry.grid(row=2, column=1)

    patient_health_issue_label = tk.Label(patient_frame, text="Health Issue:")
    patient_health_issue_label.grid(row=3, column=0, sticky="e")

    patient_health_issue_entry = tk.Entry(patient_frame)
    patient_health_issue_entry.grid(row=3, column=1)

    # Function to add patient to hospital
    def add_patient_to_hospital():
        name = patient_name_entry.get()
        age = int(patient_age_entry.get())
        gender = patient_gender_entry.get()
        health_issue = patient_health_issue_entry.get()  # Get health issue
        hospital.add_patient(name, age, gender, health_issue)
        add_patient_window.destroy()

    # Button to confirm adding patient
    add_patient_button = tk.Button(patient_frame, text="Add", command=add_patient_to_hospital)
    add_patient_button.grid(row=4, columnspan=2, pady=10)

# Function to display a detailed window for successful appointment schedule
def show_success_window():
    success_window = tk.Toplevel(window)
    success_window.title("Appointment Scheduled Successfully")

    success_label = tk.Label(success_window, text="Appointment Scheduled Successfully!", font=("Arial", 16, "bold"))
    success_label.pack(padx=20, pady=20)

    # Display appointment details
    appointment = hospital.appointments[-1]  # Get the latest appointment
    details_frame = tk.Frame(success_window)
    details_frame.pack(padx=20, pady=10)

    patient_label = tk.Label(details_frame, text=f"Patient: {appointment.patient.name}")
    patient_label.grid(row=0, column=0, sticky="w")

    doctor_label = tk.Label(details_frame, text=f"Doctor: {appointment.doctor.name}")
    doctor_label.grid(row=1, column=0, sticky="w")

    date_label = tk.Label(details_frame, text=f"Date: {appointment.date}")
    date_label.grid(row=2, column=0, sticky="w")

    time_label = tk.Label(details_frame, text=f"Time: {appointment.time}")
    time_label.grid(row=3, column=0, sticky="w")

    ok_button = tk.Button(success_window, text="OK", command=success_window.destroy)
    ok_button.pack(pady=10)

    # Center the window
    success_window.update_idletasks()
    width = success_window.winfo_width()
    height = success_window.winfo_height()
    x = (success_window.winfo_screenwidth() // 2) - (width // 2)
    y = (success_window.winfo_screenheight() // 2) - (height // 2)
    success_window.geometry(f"{width}x{height}+{x}+{y}")

# Function to schedule an appointment
def schedule_appointment_gui():
    schedule_appointment_window = tk.Toplevel(window)
    schedule_appointment_window.title("Schedule Appointment")

    # Appointment scheduling frame
    appointment_frame = tk.Frame(schedule_appointment_window)
    appointment_frame.pack(padx=10, pady=10)

    patient_name_label = tk.Label(appointment_frame, text="Patient Name:")
    patient_name_label.grid(row=0, column=0, sticky="e")

    patient_name_entry = tk.Entry(appointment_frame)
    patient_name_entry.grid(row=0, column=1)

    doctor_name_label = tk.Label(appointment_frame, text="Doctor Name:")
    doctor_name_label.grid(row=1, column=0, sticky="e")

    doctor_name_entry = tk.Entry(appointment_frame)
    doctor_name_entry.grid(row=1, column=1)

    date_label = tk.Label(appointment_frame, text="Date:")
    date_label.grid(row=2, column=0, sticky="e")

    date_entry = tk.Entry(appointment_frame)
    date_entry.grid(row=2, column=1)

    time_label = tk.Label(appointment_frame, text="Time:")
    time_label.grid(row=3, column=0, sticky="e")

    time_entry = tk.Entry(appointment_frame)
    time_entry.grid(row=3, column=1)

    def schedule_appointment():
        patient_name = patient_name_entry.get()
        doctor_name = doctor_name_entry.get()
        date = date_entry.get()
        time = time_entry.get()
        if hospital.schedule_appointment(patient_name, doctor_name, date, time):
            show_success_window()  # Call the success window
        else:
            error_label = tk.Label(schedule_appointment_window, text="Error: Patient or doctor not found!")
            error_label.pack(pady=10)

    schedule_button = tk.Button(schedule_appointment_window, text="Schedule", command=schedule_appointment)
    schedule_button.pack(pady=10)

# Function to display list of patients
def view_patients_gui():
    view_patients_window = tk.Toplevel(window)
    view_patients_window.title("Patients")

    patients_label = tk.Label(view_patients_window, text="List of Patients", font=("Arial", 14, "bold"))
    patients_label.pack(pady=10)

    for patient in hospital.patients:
        patient_label = tk.Label(view_patients_window, text=f"{patient.name} - {patient.age} - {patient.gender}")
        patient_label.pack()

# Function to display list of scheduled appointments
def view_appointments_gui():
    view_appointments_window = tk.Toplevel(window)
    view_appointments_window.title("Appointments")

    appointments_label = tk.Label(view_appointments_window, text="Scheduled Appointments", font=("Arial", 14, "bold"))
    appointments_label.pack(pady=10)

    if hospital.appointments:
        for appointment in hospital.appointments:
            appointment_label = tk.Label(view_appointments_window, text=f"Patient: {appointment.patient.name}, Doctor: {appointment.doctor.name}, Date: {appointment.date}, Time: {appointment.time}")
            appointment_label.pack()
    else:
        no_appointments_label = tk.Label(view_appointments_window, text="No appointments scheduled.")
        no_appointments_label.pack(pady=10)

# Function to display details of a specific patient
def view_patient_details_gui():
    view_patient_details_window = tk.Toplevel(window)
    view_patient_details_window.title("Patient Details")

    # Entry for patient name
    patient_name_frame = tk.Frame(view_patient_details_window)
    patient_name_frame.pack(padx=10, pady=10)

    patient_name_label = tk.Label(patient_name_frame, text="Patient Name:")
    patient_name_label.grid(row=0, column=0)

    patient_name_entry = tk.Entry(patient_name_frame)
    patient_name_entry.grid(row=0, column=1)

    def show_patient_details():
        name = patient_name_entry.get()
        for patient in hospital.patients:
            if patient.name == name:
                details_window = tk.Toplevel(view_patient_details_window)
                details_window.title("Patient Details")
                details_label = tk.Label(details_window, text=f"Name: {patient.name}\nAge: {patient.age}\nGender: {patient.gender}")
                details_label.pack(padx=10, pady=10)
                return
        not_found_label = tk.Label(view_patient_details_window, text="Patient not found!")
        not_found_label.pack(pady=10)

    search_button = tk.Button(view_patient_details_window, text="Search", command=show_patient_details)
    search_button.pack(pady=10)
    
# Function to display list of equipment
def view_equipment_gui():
    view_equipment_window = tk.Toplevel(window)
    view_equipment_window.title("Equipment")

    equipment_label = tk.Label(view_equipment_window, text="List of Equipment", font=("Arial", 14, "bold"))
    equipment_label.pack(pady=10)

    for item in hospital.equipment:
        equipment_label = tk.Label(view_equipment_window, text=f"{item.name} - Quantity: {item.quantity}")
        equipment_label.pack()

# Function to display list of doctors
def view_doctors_gui():
    view_doctors_window = tk.Toplevel(window)
    view_doctors_window.title("Doctors")

    doctors_label = tk.Label(view_doctors_window, text="List of Doctors", font=("Arial", 14, "bold"))
    doctors_label.pack(pady=10)

    for doctor in hospital.doctors:
        doctor_label = tk.Label(view_doctors_window, text=f"{doctor.name} - {doctor.department}")
        doctor_label.pack()

# Function to add new equipment
def add_equipment_gui():
    add_equipment_window = tk.Toplevel(window)
    add_equipment_window.title("Add Equipment")

    equipment_frame = tk.Frame(add_equipment_window)
    equipment_frame.pack(padx=10, pady=10)

    equipment_name_label = tk.Label(equipment_frame, text="Equipment Name:")
    equipment_name_label.grid(row=0, column=0, sticky="e")

    equipment_name_entry = tk.Entry(equipment_frame)
    equipment_name_entry.grid(row=0, column=1)

    equipment_quantity_label = tk.Label(equipment_frame, text="Quantity:")
    equipment_quantity_label.grid(row=1, column=0, sticky="e")

    equipment_quantity_entry = tk.Entry(equipment_frame)
    equipment_quantity_entry.grid(row=1, column=1)

    def add_equipment():
        name = equipment_name_entry.get()
        quantity = int(equipment_quantity_entry.get())
        hospital.add_equipment(name, quantity)
        add_equipment_window.destroy()

    add_button = tk.Button(add_equipment_window, text="Add", command=add_equipment)
    add_button.pack(pady=10)

# Function to display patient history
def view_patient_history():
    view_patient_history_window = tk.Toplevel(window)
    view_patient_history_window.title("Patient History")

    # Create labels to display patient history
    for appointment in hospital.appointments:
        if appointment.patient.health_issue:
            history_label = tk.Label(view_patient_history_window, text=f"Patient: {appointment.patient.name}, Health Issue: {appointment.patient.health_issue}, Doctor Consulted: {appointment.doctor.name}")
            history_label.pack()

# Function to display doctor's patient history
def view_doctor_patient_history():
    view_doctor_patient_history_window = tk.Toplevel(window)
    view_doctor_patient_history_window.title("Doctor's Patient History")

    doctor_name = simpledialog.askstring("Input", "Enter Doctor's Name", parent=view_doctor_patient_history_window)

    if doctor_name:
        # Create labels to display doctor's patient history
        for appointment in hospital.appointments:
            if appointment.doctor.name == doctor_name:
                history_label = tk.Label(view_doctor_patient_history_window, text=f"Patient: {appointment.patient.name}, Health Issue: {appointment.patient.health_issue}")
                history_label.pack()

# Main window
window = tk.Tk()
window.title("Hospital Management System")

# Menu bar
menu_bar = tk.Menu(window)
window.config(menu=menu_bar)

# Menu options
file_menu = tk.Menu(menu_bar, tearoff=0)
menu_bar.add_cascade(label="File", menu=file_menu)
file_menu.add_command(label="Add Patient", command=add_patient)
file_menu.add_command(label="Schedule Appointment", command=schedule_appointment_gui)
file_menu.add_separator()
file_menu.add_command(label="Exit", command=window.quit)

equipment_menu = tk.Menu(menu_bar, tearoff=0)
menu_bar.add_cascade(label="Equipment", menu=equipment_menu)
equipment_menu.add_command(label="View Equipment", command=view_equipment_gui)
equipment_menu.add_command(label="Add Equipment", command=add_equipment_gui)

management_menu = tk.Menu(menu_bar, tearoff=0)
menu_bar.add_cascade(label="Management", menu=management_menu)
management_menu.add_command(label="View Doctors", command=view_doctors_gui)
management_menu.add_command(label="View Patients", command=view_patients_gui)
management_menu.add_command(label="View Appointments", command=view_appointments_gui)

history_menu = tk.Menu(menu_bar, tearoff=0)
menu_bar.add_cascade(label="History", menu=history_menu)
history_menu.add_command(label="View Patient History", command=view_patient_history)
history_menu.add_command(label="View Doctor's Patient History", command=view_doctor_patient_history)

# Hospital instance
hospital = Hospital("My Hospital")
hospital.add_doctor("Dr. Smith", "Cardiology")
hospital.add_doctor("Dr. Johnson", "Neurology")
hospital.add_patient("Stalin", 69, "Nil","Blood cancer")
hospital.add_patient("Jane Smith", 25, "Female","TB")
hospital.add_equipment("Oxygen Cylinders",20)
hospital.add_equipment("MRI Machines",4)
hospital.add_equipment("Syringes",90)

# Run the GUI
window.mainloop()
