import sounddevice as sd
import wave
import numpy as np
import threading
import os

class AudioPlayback:
    def __init__(self, tmp_path):
        self.tmp_path = tmp_path
        self.playing = False
        self.paused = False
        self.thread = None
        self.stream = None
        self.lock = threading.Lock()

    def play(self):
        if not os.path.exists(self.tmp_path):
            print(f"[WARN] File not found: {self.tmp_path}")
            return
        if self.playing:
            print("[INFO] Already playing.")
            return

        self.playing = True
        self.paused = False
        self.thread = threading.Thread(target=self._play_thread)
        self.thread.start()

    def _play_thread(self):
        with wave.open(self.tmp_path, 'rb') as wf:
            samplerate = wf.getframerate()
            channels = wf.getnchannels()
            dtype = 'int16'

            print(f"[INFO] Playback started — {samplerate} Hz, {channels} channel(s)")

            def callback(outdata, frames, time, status):
                if status:
                    print(f"[WARN] Playback status: {status}")
                with self.lock:
                    if self.paused:
                        outdata[:] = np.zeros((frames, 2 if channels == 1 else channels), dtype=dtype)
                        return

                    data = wf.readframes(frames)
                    if len(data) == 0:
                        raise sd.CallbackStop()

                    buffer = np.frombuffer(data, dtype=dtype)

                    if channels == 1:
                        mono = buffer.reshape(-1, 1)
                        stereo = np.repeat(mono, 2, axis=1)
                        padded = np.zeros((frames, 2), dtype=dtype)
                        padded[:len(stereo)] = stereo
                        outdata[:] = padded
                    else:
                        expected_samples = frames * channels
                        actual_samples = len(buffer)

                        if actual_samples < expected_samples:
                            padded = np.zeros(expected_samples, dtype=dtype)
                            padded[:actual_samples] = buffer
                            reshaped = padded.reshape(-1, channels)
                        else:
                            reshaped = buffer.reshape(-1, channels)

                        padded_out = np.zeros((frames, channels), dtype=dtype)
                        padded_out[:len(reshaped)] = reshaped
                        outdata[:] = padded_out

            with sd.OutputStream(samplerate=samplerate, channels=2 if channels == 1 else channels, dtype=dtype, callback=callback):
                while self.playing and wf.tell() < wf.getnframes():
                    sd.sleep(100)

        self.playing = False
        print("[INFO] Playback finished.")

    def pause(self):
        with self.lock:
            self.paused = not self.paused
        print(f"[INFO] Playback {'paused' if self.paused else 'resumed'}.")

    def stop(self):
        self.playing = False
        self.paused = False
        print("[INFO] Playback stopped.")
