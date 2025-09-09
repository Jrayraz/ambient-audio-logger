import subprocess
import threading
import os
from datetime import datetime

class AudioCapture:
    def __init__(self, config):
        self.tmp_path = config.get("tmp_path", "/tmp/ambient_capture.wav")
        self.recording = False
        self.process = None
        self.thread = None

    def start(self):
        if self.recording:
            print("[INFO] Already recording.")
            return

        # Remove old file if it exists
        if os.path.exists(self.tmp_path):
            os.remove(self.tmp_path)

        print(f"[INFO] Starting ALSA capture to {self.tmp_path}...")
        self.recording = True

        def record():
            try:
                self.process = subprocess.Popen([
                    "arecord",
                    "-f", "cd",           # 16-bit stereo 44.1kHz
                    "-t", "wav",          # WAV format
                    self.tmp_path
                ])
                self.process.wait()
            except Exception as e:
                print(f"[ERROR] arecord failed: {e}")
            finally:
                self.recording = False

        self.thread = threading.Thread(target=record)
        self.thread.start()
        print(f"[INFO] Recording started at {datetime.utcnow().isoformat()}")

    def stop(self):
        if not self.recording or not self.process:
            print("[INFO] No active recording to stop.")
            return

        print("[INFO] Stopping ALSA capture...")
        self.process.terminate()
        self.thread.join()
        self.recording = False
        print(f"[INFO] Audio written to {self.tmp_path} at {datetime.utcnow().isoformat()}")

    def get_tmp_path(self):
        return self.tmp_path
