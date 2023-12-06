import numpy as np
from scipy.io import wavfile
import matplotlib.pyplot as plt

sampling_rate = 44100

def generate_sine_wave(frequency, duration, amplitude):
    num_samples = int(sampling_rate * duration)
    time = np.linspace(0, duration, num_samples)
    audio_signal = amplitude * np.sin(2 * np.pi * frequency * time)
    return audio_signal

def generate_rectangular_wave(frequency, duration, amplitude):
    num_samples = int(sampling_rate * duration)
    time = np.linspace(0, duration, num_samples)
    audio_signal = amplitude * np.sign(np.sin(2 * np.pi * frequency * time))
    return audio_signal

def generate_asymetric_triangular_wave(frequency, duration, amplitude):
    num_samples = int(sampling_rate * duration)
    time = np.linspace(0, duration, num_samples)
    period = 1 / frequency
    audio_signal = amplitude * np.where(time % period < period / 2, 2 / period * time % period, -2 / period * time % period) - amplitude
    return audio_signal

def generate_symetric_triangular_wave(frequency, duration, amplitude):
    num_samples = int(sampling_rate * duration)
    time = np.linspace(0, duration, num_samples)
    period = 1 / frequency
    audio_signal = amplitude * (2 / period * np.abs(time % period - period / 2) - 1)
    return audio_signal

def visualize_signal(audio_signal, duration, title="Audio signal"):
    time = np.linspace(0, duration, len(audio_signal))
    plt.figure(figsize=(10, 6))
    plt.plot(time, audio_signal)
    plt.xlabel('Time (s)')
    plt.ylabel('Amplitude')
    plt.title(title)
    plt.grid(True)
    plt.show()

def plot_positive_spectrum(signal, title="Signal Spectrum (Positive Frequencies Only)"):
    signal_fft = np.fft.fft(signal)
    frequencies = np.fft.fftfreq(len(signal), 1 / sampling_rate)
    positive_frequencies = frequencies[:len(frequencies)//2]
    positive_signal_fft = 2.0 / len(signal) * np.abs(signal_fft[:len(signal)//2])
    plt.figure(figsize=(10, 6))
    plt.plot(positive_frequencies, positive_signal_fft)
    plt.xlabel('Frequency (Hz)')
    plt.ylabel('Amplitude')
    plt.title(title)
    plt.grid(True)
    plt.show()

def save_signal_to_wav(filename, signal):
    max_amplitude = np.max(np.abs(signal))
    normalized_signal = signal / max_amplitude
    wavfile.write(filename, sampling_rate, normalized_signal)

def main():
    frequency = 420  # Replace with the last digit of your faculty number!
    duration = 1
    amplitude = 1

    sine_wave = generate_sine_wave(frequency, duration, amplitude)
    visualize_signal(sine_wave, duration, title="Sine wave")
    plot_positive_spectrum(sine_wave, title="Sine wave spectrum (positive frequencies only)")
    save_signal_to_wav("sine_wave.wav", sine_wave)

    rectangular_wave = generate_rectangular_wave(frequency, duration, amplitude)
    visualize_signal(rectangular_wave, duration, title="Rectangular wave")
    plot_positive_spectrum(rectangular_wave, title="Rectangular wave spectrum (positive frequencies only)")
    save_signal_to_wav("rectangular_wave.wav", rectangular_wave)

    asymetric_triangular_wave = generate_asymetric_triangular_wave(frequency, duration, amplitude)
    visualize_signal(asymetric_triangular_wave, duration, title="Asymmetric triangular wave")
    plot_positive_spectrum(asymetric_triangular_wave, title="Asymmetric triangular wave spectrum (positive frequencies only)")
    save_signal_to_wav("asymmetric_triangle_wave.wav", asymetric_triangular_wave)

    symetric_triangular_wave = generate_symetric_triangular_wave(frequency, duration, amplitude)
    visualize_signal(symetric_triangular_wave, duration, title="Symmetric triangular wave")
    plot_positive_spectrum(symetric_triangular_wave, title="Symmetric triangular wave spectrum (positive frequencies only)")
    save_signal_to_wav("symmetric_triangle_wave.wav", symetric_triangular_wave)

if __name__ == "__main__":
    main()
