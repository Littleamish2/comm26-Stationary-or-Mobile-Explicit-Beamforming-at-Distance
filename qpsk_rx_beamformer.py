import adi
import matplotlib.pyplot as plt
import numpy as np

# Initialize connection
PLUTO_IP = "192.168.2.1"
sdr = adi.Pluto(uri=f"ip:{PLUTO_IP}")

try:
    # Configure RF Parameters
    sdr.sample_rate = int(2.4e6)
    sdr.rx_lo = int(100.1e6)  # Center frequency
    sdr.rx_rf_bandwidth = int(2e6)
    sdr.rx_buffer_size = 1024 * 10  # Number of samples to read per buffer

    # Configure gain mode
    sdr.gain_control_mode_chan0 = 'manual'
    sdr.rx_hardwaregain_chan0 = 30  # in dB

    print(f"Streaming from PlutoSDR at {sdr.rx_lo / 1e6} MHz...")

    # Enable dual channels
    sdr.rx_enabled_channels = [0, 1]
    iq_samples = sdr.rx() # 1x2 array of received samples from each channel

    # Time Domain & Spectrum Visual
    fig, (ax1, ax2) = plt.subplots(2, 1, figsize=(10, 6))

    # Plot Power Spectral Density (Frequency Domain)
    ax2.psd(iq_samples, NFFT=1024, Fs=sdr.sample_rate / 1e6, Fc=sdr.rx_lo / 1e6)
    ax2.set_title("Frequency Domain (PSD)")

    plt.tight_layout()
    plt.show()

finally:
    del sdr
