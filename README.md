- [This is the code for our Pico-Piano](#this-is-the-code-for-our-pico-piano)
        - [Go check out our video giving you instructions on how to use this code or follow the instructions below:](#go-check-out-our-video-giving-you-instructions-on-how-to-use-this-code-or-follow-the-instructions-below)
  - [For MicroPython on line 5 and 6 where the code says:](#for-micropython-on-line-5-and-6-where-the-code-says)
  - [On line 14 in CircuitPython or 10 in MicroPython where the code says:](#on-line-14-in-circuitpython-or-10-in-micropython-where-the-code-says)
  - [On line 15 and 16 for CircuitPython or 11 and 12 in MicroPython where the code says:](#on-line-15-and-16-for-circuitpython-or-11-and-12-in-micropython-where-the-code-says)


# This is the code for our Pico-Piano
##### Go check out our video giving you instructions on how to use this code or follow the instructions below:



## For CircuitPython on line 8 and 9 where the code says:
```python
    probe_pin = board.GP26_A0
    speaker_pin = board.GP18
```
 You can replace the .GP**26**_A0 with GP**your analog pin**_A0  .
 You can also replace the .GP**18** with .GP **your speaker PWM pin** .



## For MicroPython on line 5 and 6 where the code says:
```python
    probe_pin = 26
    speaker_pin = 2
```
You replace the **26** with **Your analog pin** and the **2** with **your speaker PWM pin**.



## On line 14 in CircuitPython or 10 in MicroPython where the code says:
```python
    min_probe_val = 1500
```
 You can replace **1500** with your minimum probe value eg: the highest number it prints when your probe isn't touching any key/resistor!



## On line 15 and 16 for CircuitPython or 11 and 12 in MicroPython where the code says:
```python
    e_minor = [[8000, "E4"], [13000, "G4"], [19000, "A4"], [30000, "B4"], [66000,"D5"]]
    diatonic = [[2500,"C4"],[3000,"C#4"],[3600,"D4"]]
```
We have given you some notes that sound good together that you can edit or you could even make a new list below for your custom notes! Example:
```python
    custom = [[your probe value,"C"], [your other probe value, "E"] ext...]
```

You then have to go to line 41 in CircuitPython or 37 in MicroPython where it says:
    loaded_list = note_to_freq_list(e_minor)
and then replace **(e_minor)** with your custom list - in my example I would replace it with custom.

At the bottom on line 45 in CircuitPython or 41 in MicroPython where it says:
    update_tone(loaded_list,True)

You have the option of printing the probe value(for debuging) which will have a 1 second delay or having it off - with no delay! You can do this by putting a **True** like we already have or getting rid of it for no delay if you don't want to debug!
