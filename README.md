## This is the code for our Pico-Piano
##### Go check out our video giving you instructions on how to use this code or follow the instructions below:


#### For CircuitPython on line 8 and 9 where the code says:
    probe_pin = board.GP26_A0
    speaker_pin = board.GP18
##### You can replace the .GP<mark>26</mark>_A0 with GP<mark>*your analog pin*</mark>_A0  .
##### You can also replace the .GP<mark>18</mark> with .GP<mark>*your speaker PWM pin*</mark> .


#### For MicroPython on line 5 and 6 where the code says:
    probe_pin = 26
    speaker_pin = 2
##### You replace the <mark>26</mark> with <mark>*Your analog pin*</mark> and the <mark>2</mark> with <mark>*your speaker PWM pin*</mark>.


#### On line 14 in CircuitPython or 10 in MicroPython where the code says:
    min_probe_val = 1500
##### You can replace <mark>*1500*</mark> with your minimum probe value eg: the highest number it prints when your probe isn't touching any key/resistor!


#### On line 15 and 16 for CircuitPython or 11 and 12 in MicroPython where the code says:
    e_minor = [[8000, "E4"], [13000, "G4"], [19000, "A4"], [30000, "B4"], [66000,"D5"]]
    diatonic = [[2500,"C4"],[3000,"C#4"],[3600,"D4"]]
##### We have given you some notes that sound good together that you can edit or you could even make a new list below for your custom notes! Example:
    custom = [[your probe value,"C"], [your other probe value, "E"] ext...]
##### You then have to go to line 41 in CircuitPython or 37 in MicroPython where it says:
    loaded_list = note_to_freq_list(e_minor)
##### and then replace <mark>*(e_minor)*</mark> with your custom list - in my example I would replace it with custom.

#### At the bottom on line 45 in CircuitPython or 41 in MicroPython where it says:
    update_tone(loaded_list,True)
###### You have the option of printing the probe value(for debuging) which will have a 1 second delay or having it off - with no delay! You can do this by putting a <mark>*True*</mark> like we already have or getting rid of it for no delay if you don't want to debug!
