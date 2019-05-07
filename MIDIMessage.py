import time

import pyaudio
import numpy as np
import threading

fs = 48000


def get_wave(note_key, duration, transpose=60):
    frequency = 440 * np.power(2, (note_key - transpose) / 12)
    return np.sin(2*np.pi*np.arange(fs*duration)*frequency/fs).astype(np.float32)


class MIDIMessage(threading.Thread):
    def __init__(self, value, p):
        threading.Thread.__init__(self)

        self.note = value.getNoteNumber()
        self.velocity = value.getVelocity()
        print(self.velocity)
        self.stream = p.open(format=pyaudio.paFloat32,
                             channels=1,
                             rate=fs,
                             output=True)

        self.is_stopped = False

    def run(self):
        wave = get_wave(self.note, 13)

        while True:
            if self.is_stopped:
                return

            self.stream.write(wave)

    def on_note_off(self):
        self.stream.stop_stream()
        self.is_stopped = True
