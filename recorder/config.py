import os

def get_config():
    return {
        "sample_rate": 44100,               # CD-quality capture
        "channels": 2,                      # Stereo recording
        "tmp_path": os.path.join("/tmp", "ambient_capture.wav"),
        "bit_depth": 16,                    # 16-bit PCM
        "max_duration_sec": 3600,           # Optional: max record time (1 hour)
        "log_path": os.path.join("logs", "session.log"),
        "metadata_path": os.path.join("metadata", "tags.json"),
        "default_location": {
            "city": "",
            "lat": None,
            "lon": None,
            "notes": ""
        }
    }
