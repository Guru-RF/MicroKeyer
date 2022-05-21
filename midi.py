import time
import random
import usb_midi
import adafruit_midi

from adafruit_midi.note_on import NoteOn
from adafruit_midi.note_off import NoteOff
from adafruit_midi.pitch_bend import PitchBend
from adafruit_midi.control_change import ControlChange

midi = adafruit_midi.MIDI(midi_out=usb_midi.ports[1], out_channel=0)

print("Midi test")

print("Default output MIDI channel:", midi.out_channel + 1)

while True:
    midi.send(NoteOn(44, 120))  # G sharp 2nd octave
    time.sleep(2)
    midi.send(NoteOff(44, 120))  # G sharp 2nd octave
    time.sleep(2)
