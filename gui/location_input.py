import tkinter as tk

class LocationInput:
    def __init__(self, root, location_manager):
        self.location_manager = location_manager

        frame = tk.LabelFrame(root, text="Location Info", padx=10, pady=10)
        frame.pack(padx=10, pady=10, fill="both", expand=True)

        # City
        tk.Label(frame, text="City:").grid(row=0, column=0, sticky="w")
        self.city_entry = tk.Entry(frame, width=25)
        self.city_entry.grid(row=0, column=1)

        # Latitude
        tk.Label(frame, text="Latitude:").grid(row=1, column=0, sticky="w")
        self.lat_entry = tk.Entry(frame, width=25)
        self.lat_entry.grid(row=1, column=1)

        # Longitude
        tk.Label(frame, text="Longitude:").grid(row=2, column=0, sticky="w")
        self.lon_entry = tk.Entry(frame, width=25)
        self.lon_entry.grid(row=2, column=1)

        # Notes
        tk.Label(frame, text="Notes:").grid(row=3, column=0, sticky="nw")
        self.notes_entry = tk.Text(frame, width=25, height=4)
        self.notes_entry.grid(row=3, column=1)

        # Submit button
        tk.Button(frame, text="Set Location", command=self._submit_location).grid(row=4, column=0, columnspan=2, pady=5)

    def _submit_location(self):
        city = self.city_entry.get()
        lat = self.lat_entry.get()
        lon = self.lon_entry.get()
        notes = self.notes_entry.get("1.0", tk.END).strip()

        self.location_manager.set_location(city, lat, lon, notes)
        print("[INFO] Location metadata updated.")
