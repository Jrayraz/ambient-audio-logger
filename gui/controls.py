import tkinter as tk
from recorder import AudioCapture, AudioPlayback, AudioStorage, LocationManager, get_config

class GUIControls:
    def __init__(self, root):
        self.config = get_config()
        self.capture = AudioCapture(self.config)
        self.playback = AudioPlayback(self.config["tmp_path"])
        self.storage = AudioStorage(self.config["tmp_path"])
        self.location = LocationManager(self.config["metadata_path"])

        self._build_buttons(root)

    def _build_buttons(self, root):
        tk.Button(root, text="Record", command=self.capture.start).pack(pady=5)
        tk.Button(root, text="Stop", command=self.capture.stop).pack(pady=5)
        tk.Button(root, text="Play", command=self.playback.play).pack(pady=5)
        tk.Button(root, text="Pause", command=self.playback.pause).pack(pady=5)
        tk.Button(root, text="Save", command=self._save_with_metadata).pack(pady=5)

    def _save_with_metadata(self):
        saved_path = self.storage.save_to_user_location()
        if saved_path:
            self.location.tag_recording(saved_path)
            self.location.save_metadata()
