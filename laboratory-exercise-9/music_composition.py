import numpy as np
from scipy.io import wavfile
 
class MusicGenerator:
 
    def __init__(self, sampling_rate):
        self.sampling_rate = sampling_rate
 
    def generate_sine_wave(self, frequency, duration, amplitude):
        """
        Generates a simple audio signal with a sine wave form.
 
        Arguments:
            frequency: The frequency of the signal in Hz.
            duration: The duration of the signal in seconds.
            amplitude: The amplitude of the signal.
 
        Returns:
            A simple audio signal with a sine wave form.
        """
 
        num_samples = int(self.sampling_rate * duration)
        time = np.linspace(0, duration, num_samples)
        audio_signal = amplitude * np.sin(2 * np.pi * frequency * time)
 
        return audio_signal
 
    def generate_music(self, notes):
        """
        Generates a simple musical composition.
 
        Arguments:
            notes: A list of notes to play.
 
        Returns:
            composed music.
        """
 
        # Generate the audio signals for each note.
        composed_music = np.array([])
        for note in notes:
            note_length = note[2]
            audio_signal = self.generate_sine_wave(note[1], note_length, 0.2)
            composed_music = np.append(composed_music, audio_signal)
 
        return composed_music
 
    def save_signal_to_wav(self, filename, signal):
        """
        Save a signal to a WAV file.
 
        Arguments:
            filename (str): The name of the output WAV file.
            signal (numpy.ndarray): The signal data as a NumPy array.
 
        Returns:
            None
        """
 
        max_amplitude = np.max(np.abs(signal))
        normalized_signal = signal / max_amplitude
        wavfile.write(filename, self.sampling_rate, normalized_signal.astype(np.float32))
 
    def get_frequency_from_note_name(self, note):
        notes_dict = {
            'C': 261.63, 'C#': 277.18, 'D': 293.66, 'D#': 311.13,
            'E': 329.63, 'F': 349.23, 'F#': 369.99, 'G': 392.00,
            'G#': 415.30, 'A': 440.00, 'A#': 466.16, 'B': 493.88
        }
        octave = int(note[-1])
        note_name = note[:-1]
        frequency = notes_dict[note_name] * (2 ** octave)
        return frequency
 
 
def main():
 
    sampling_rate = 44100
 
    # Create a music generator with the given sampling rate
    music_generator = MusicGenerator(sampling_rate)
 
    # Define musical notes with frequency and duration for "Für Elise" in a higher octave
    notes = [
        ('E5', 659.26, 0.5),   # E in the 5th octave
        ('D#5', 622.25, 0.5),  # D# in the 5th octave
        ('E5', 659.26, 0.5),   # E in the 5th octave
        ('D#5', 622.25, 0.5),  # D# in the 5th octave
        ('E5', 659.26, 0.5),   # E in the 5th octave
        ('B4', 493.88, 0.5),   # B in the 4th octave
        ('D5', 587.33, 0.5),   # D in the 5th octave
        ('C5', 523.25, 0.5),   # C in the 5th octave
        ('A4', 440.00, 1),   # A in the 4th octave
    ]
 
    # Generate the music.
    composed_music = music_generator.generate_music(notes)
 
    # Save the music.
    music_generator.save_signal_to_wav("composed_music.wav", composed_music)
 
if __name__ == "__main__":
    main()