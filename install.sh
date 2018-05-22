
#install portaudio19-dev on ubuntu
apt-get update && apt-get install -y \
    python-pip \
    portaudio19-dev \
    python-pyaudio swig \
    libpulse-dev \
    espeak
&& rm -rf /var/lib/apt/lists/*
