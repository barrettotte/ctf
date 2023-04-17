# analogue-signal-processing

> Before the aliens had computers, they used analogue circuits to communicate. 
> One of their favourite tricks was to hide messages in the communication equipment itself, which often used inductors and high-tech, complex resistors. 
> Using a few samples from different locations in the circuit, can you figure out the parameters of the circuitry?

TODO: review writeup

HTB Discord:

```txt
the Python function simulates a ZL circuit (an impedance Z and an inductance L in series). The inductance is always 1 Henry (hardcoded), the impedance is 1j*ord(flag[i]).

Since the impedance is a purely imaginary number (no real part), it is actually a reactance and therefore the circuit is actually an LC circuit.
An ideal LC circuit has a resonance frequency equal to 1/(2*pi*sqrt(LC)).

The first circuit receives white noise as input, so if you take the output (the .wav file) and do a FFT on it, it only has one single peak at around 11.4583 Hz.

Each circuit from the second onwards receives as input the output of the previous one, so each time one new peak in the spectrum appears.

It is "just" a matter of finding the new frequency peak in each .wav file, obtaining all the frequencies, and then multiplying each of them by 2*pi to get the ascii value of each character of the flag 
```
