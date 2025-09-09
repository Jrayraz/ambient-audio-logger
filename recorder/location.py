import json
from datetime import datetime
import os

class LocationManager:
    def __init__(self, metadata_path):
        self.metadata_path = metadata_path
        self.location_data = {
            "city": "",
            "lat": None,
            "lon": None,
            "notes": "",
            "timestamp": None,
            "recording": None
        }

    def set_location(self, city, lat, lon, notes):
        self.location_data["city"] = city.strip()
        self.location_data["lat"] = float(lat) if lat else None
        self.location_data["lon"] = float(lon) if lon else None
        self.location_data["notes"] = notes.strip()
        self.location_data["timestamp"] = datetime.utcnow().isoformat()

    def tag_recording(self, filename):
        self.location_data["recording"] = os.path.basename(filename)

    def save_metadata(self):
        os.makedirs(os.path.dirname(self.metadata_path), exist_ok=True)
        with open(self.metadata_path, "w") as f:
            json.dump(self.location_data, f, indent=4)
        print(f"[INFO] Location metadata saved to {self.metadata_path}")

    def get_metadata(self):
        return self.location_data
