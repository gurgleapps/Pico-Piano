def note_to_midi(note):
    name = note.rstrip("0123456789-")
    octave = int(note[len(name):])
    note_to_num = {
        "C": 0,
        "C#": 1,
        "D": 2,
        "D#": 3,
        "E": 4,
        "F": 5,
        "F#": 6,
        "G": 7,
        "G#": 8,
        "A": 9,
        "A#": 10,
        "B": 11
    }
    midi = octave*12+note_to_num[name]+12
    return midi
################################################################################    

def midi_to_freq(midi_num, should_round = False):
    distance = midi_num-69
    freq = 440*2**(distance/12)
    if should_round:
        return round(freq)
    return freq
################################################################################

def note_to_freq(note, should_round = False):
    midi = note_to_midi(note)
    return midi_to_freq(midi, should_round)