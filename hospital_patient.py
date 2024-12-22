def search_patients(patients, disease):
    return [patient["Name"] for patient in patients if patient["Disease"] == disease]

patients = [
    {"Name": "Alice", "Age": 30, "Disease": "Flu"},
    {"Name": "Bob", "Age": 45, "Disease": "Diabetes"},
    {"Name": "Charlie", "Age": 35, "Disease": "Flu"}
]
print(f"Patients with Flu: {search_patients(patients, 'Flu')}")
