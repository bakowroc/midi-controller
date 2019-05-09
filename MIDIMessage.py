import pyaudio
import numpy as np
import threading

from sounds.sounds import clean

fs = 44100


def get_wave(note_key, attack, duration=1.0, transpose=72):
    frequency = 440 * np.power(2, (note_key - transpose) / 12)
    return attack * clean(frequency, duration)


class MIDIMessage(threading.Thread):
    def __init__(self, value, p):
        threading.Thread.__init__(self)

        self.note = value.getNoteNumber()
        self.velocity = value.getVelocity()
        self.stream = p.open(format=pyaudio.paFloat32,
                             channels=1,
                             rate=fs,
                             input=False,
                             output=True)

        self.is_stopped = False

    def run(self):
        print(self.velocity)
        attack = (self.velocity / 127) / 4
        wave = get_wave(self.note, attack)

        while True:
            if self.is_stopped:
                self.stream.stop_stream()
                return

            self.stream.write(wave)

    def on_note_off(self):
        self.is_stopped = True
