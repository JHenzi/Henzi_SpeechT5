from pydub import AudioSegment
import os
import pathlib

# Set the directory where the WAV files are located
wav_directory = str(pathlib.Path(__file__).parent.resolve())

# Set the output path and filename for the final MP3 file
output_path = str(pathlib.Path(__file__).parent.resolve())
output_filename = 'output.mp3'

# Get a sorted list of WAV files in the directory
wav_files = sorted(
    [f for f in os.listdir(wav_directory) if f.endswith(".wav")],
    key=lambda f: int(os.path.splitext(f)[0].split("_")[1])
)

# Initialize an empty AudioSegment object to store the combined audio
combined_audio = AudioSegment.silent(duration=0)

# Iterate over the sorted WAV files
for filename in wav_files:
    wav_file = os.path.join(wav_directory, filename)

    # Load the WAV file using pydub
    audio = AudioSegment.from_wav(wav_file)

    # Append the current audio to the combined audio
    combined_audio += audio

# Export the combined audio as an MP3 file
combined_audio.export(os.path.join(output_path, output_filename), format="mp3")

print("Conversion to MP3 complete!")
