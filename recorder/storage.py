import os
import shutil
from tkinter import filedialog

class AudioStorage:
    def __init__(self, tmp_path):
        self.tmp_path = tmp_path

    def save_to_user_location(self):
        if not os.path.exists(self.tmp_path):
            print(f"[WARN] No audio file found at {self.tmp_path}")
            return None

        target_path = filedialog.asksaveasfilename(
            defaultextension=".wav",
            filetypes=[("WAV files", "*.wav")],
            title="Save Recording As"
        )

        if not target_path:
            print("[INFO] Save cancelled by user.")
            return None

        try:
            shutil.copy2(self.tmp_path, target_path)
            print(f"[INFO] Audio saved to {target_path}")
            return target_path
        except Exception as e:
            print(f"[ERROR] Failed to save audio: {e}")
            return None
