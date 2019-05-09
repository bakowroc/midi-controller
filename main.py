import rtmidi
import pyaudio

from MIDIMessage import MIDIMessage
from sounds.sounds import plot, clean

EXAMINE = False
p = pyaudio.PyAudio()
active_sounds = {}


def print_message(value):
    note = value.getNoteNumber()

    if value.isNoteOn():
        if note not in active_sounds:
            midi_msg = MIDIMessage(value, p)
            active_sounds[note] = midi_msg
            midi_msg.start()

    elif value.isNoteOff():
        try:
            active_sounds[note].on_note_off()
            del active_sounds[value.getNoteNumber()]
        except KeyError:
            pass


if __name__ == "__main__":
    if EXAMINE:
        print('Examine')
        plot(clean(440))
    else:
        MIDIDevice = rtmidi.RtMidiIn()

        MIDIDevice.openPort(1)
        while True:
            message = MIDIDevice.getMessage(100)
            if message:
                print_message(message)

