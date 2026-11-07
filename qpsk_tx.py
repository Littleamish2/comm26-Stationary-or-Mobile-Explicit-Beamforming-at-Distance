import adi
import matplotlib.pyplot as plt
import numpy as np

# Initialize connection
PLUTO_IP = "192.168.2.1"
sdr = adi.Pluto(uri=f"ip:{PLUTO_IP}")

# TX frequencies
sdr.tx_lo = int(915e6) # 915 MHz
sdr.tx_hardwaregain_chan0 = -10 # dB, max = 0

# Simple sine wave
fs = sdr.sample_rate
f_signal = 100e3 # 100 kHz offset
t = np.arange(0, 10240) / fs
tx_signal = np.exp(1j * 2 * np.pi * f_signal * t) * 2**14 # Scale to fit Pluto's buffer requirements

# Send the buffer to the TX hardware
sdr.tx(tx_signal)