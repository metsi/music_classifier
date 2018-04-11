#!/usr/bin/env python
"""
Podział pliku wav na okna
"""
import numpy as np
import scipy.io.wavfile

# Podajemy ścieżkę do pliku wav
filename = 'wav/song.wav'

# Wczytujemy plik wav
bitrate, stereo_sound = scipy.io.wavfile.read(filename)

# Spłaszczamy dźwięk do mono
mono_sound = np.mean(stereo_sound, axis = 1)

# Pobieramy sumaryczną długość strumienia audio
sound_length = len(mono_sound)

# Deklarujemy szerokość okna w sekundach
window_seconds = 4

# Obliczamy szerokość okna w bitach
window_length = window_seconds * bitrate

# Wyliczamy liczbę okien
n_windows = sound_length // window_length

# Przycinamy dźwięk do pełnych okien
mono_sound = mono_sound[:n_windows * window_length]

# Przekształcamy audio na reprezentację z oknami w wierszach i próbkami
# w kolumnach
windows = mono_sound.reshape((n_windows,-1))

# Iterujemy kolejne okna
for i in range(n_windows):
    # Pobieramy okno
    window = windows[i,:]

    # Dla przykładu wyliczamy i wyświetlamy średnią z okna
    mean_of_window = np.mean(window)
    print(mean_of_window)
