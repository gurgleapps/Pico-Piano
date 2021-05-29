import board
import pwmio
import time
from analogio import AnalogIn

import note_utils

probe_pin = board.GP26_A0
speaker_pin = board.GP18
probe = AnalogIn(probe_pin)
speaker = pwmio.PWMOut(speaker_pin, frequency=440, duty_cycle=0, variable_frequency=True)


min_probe_val = 1500
e_minor = [[8000, "E4"], [13000, "G4"], [19000, "A4"], [30000, "B4"], [66000,"D5"]]
diatonic = [[2500,"C4"],[3000,"C#4"],[3600,"D4"]]

def update_tone(probe_limit_freq_list, debug = False):
    probe_value = probe.value
    if debug:
        time.sleep(1)
        print(probe_value)
    if probe_value < min_probe_val:
           speaker.duty_cycle = 0
           return
    for probe_limit_freq_pair in probe_limit_freq_list:
        if probe_value < probe_limit_freq_pair[0]:
            speaker.duty_cycle = int(65535/2)
            speaker.frequency = probe_limit_freq_pair[1]
            return 
        
def note_to_freq_list(probe_limit_note_list):
    probe_limit_freq_list = []
    for probe_limit_note_pair in probe_limit_note_list:
        temp_pair = []
        temp_pair.append(probe_limit_note_pair[0])
        temp_pair.append(note_utils.note_to_freq(probe_limit_note_pair[1],True))
        probe_limit_freq_list.append(temp_pair)
    return probe_limit_freq_list

loaded_list = note_to_freq_list(e_minor)
print(loaded_list)

while True:
    update_tone(loaded_list,True)