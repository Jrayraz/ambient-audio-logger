# Ambient Audio Logger

Modular, forensic-grade ambient audio capture suite with manual location tagging, rollback-safe metadata, and CLI-native playback. Designed for bug bounty sweeps, field ops, and timestamped audit trails.

---

## 🔧 Setup

### 1. System Dependencies

Install ALSA and PortAudio development headers:

```bash
sudo apt-get update
sudo apt-get install -y \
  portaudio19-dev \
  libasound2-dev \
  alsa-utils \
  python3-dev \
  python3-pip

#python virt env
python3 -m venv venv
source venv/bin/activate

pip install -r requirements.txt


##RUN###
python3 main.py
