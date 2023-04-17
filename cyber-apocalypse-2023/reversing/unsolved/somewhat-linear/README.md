# somewhat-linear

> Deep in the alien cave system, you find a strange device. 
> It seems to be some sort of communication cipherer, but only a couple of recordings are still intact. 
> Can you figure out what the aliens were trying to say? The flag is all lower case

TODO: review writeup

HTB discord:

```py
import numpy as np
import soundfile as sf

shuffled_flag, rate = sf.read('shuffled_flag.wav')
impulse_response, _ = sf.read('impulse_response.wav')

# Take the FFT of the impulse response
fft_ir = np.fft.rfft(impulse_response)

# Divide the FFT of the shuffled audio file by the FFT of the impulse response
fft_shuffled = np.fft.rfft(shuffled_flag)
fft_orig = fft_shuffled / fft_ir

# Inverse FFT the result to get the original audio file
orig = np.fft.irfft(fft_orig)

# Save the recovered audio file
sf.write('new.wav', orig, rate)
```

## Attempt

- https://github.com/x41x41x41/hackingpotato/blob/master/techniques/stenography.md
- https://ctftime.org/writeup/12665

```sh
file impulse_response.wav
file shuffled_flag.wav

strings shuffled_flag.wav | less

# binwalk install
git clone git@github.com:ReFirmLabs/binwalk.git
sudo python3 setup.py install

binwalk impulse_response.wav
# 2159736       0x20F478        MySQL MISAM compressed data file Version
# actually apparently useless

binwalk shuffled_flag.wav
```