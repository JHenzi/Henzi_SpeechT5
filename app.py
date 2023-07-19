import torch
from datasets import load_dataset
from transformers import SpeechT5Processor, SpeechT5ForTextToSpeech, SpeechT5HifiGan
import soundfile as sf
import numpy as np

processor = SpeechT5Processor.from_pretrained("microsoft/speecht5_tts")
model = SpeechT5ForTextToSpeech.from_pretrained("microsoft/speecht5_tts")
vocoder = SpeechT5HifiGan.from_pretrained("microsoft/speecht5_hifigan")

prompt_file = '/docker/nix-tts/prompt.txt'
output_dir = '/docker/nix-tts/'
batch_size = 2  # Number of lines to process at a time

with open(prompt_file, 'r') as file:
    lines = file.readlines()

num_lines = len(lines)
# Calculate the number of batches
num_batches = (num_lines + batch_size - 1) // batch_size

for i in range(num_batches):
    start_idx = i * batch_size
    end_idx = (i + 1) * batch_size
    batch_lines = lines[start_idx:end_idx]

    # Join the batch_lines into a single string
    prompt_text = "".join(batch_lines)

    inputs = processor(text=prompt_text, return_tensors="pt")

    # load xvector containing speaker's voice characteristics from a dataset
    embeddings_dataset = load_dataset(
        "Matthijs/cmu-arctic-xvectors", split="validation")
    speaker_embeddings = torch.tensor(
        embeddings_dataset[7306]["xvector"]).unsqueeze(0)

    speech = model.generate_speech(
        inputs["input_ids"], speaker_embeddings, vocoder=vocoder)

    output_filename = f"speech_{i}.wav"
    output_path = output_dir + output_filename
    sf.write(output_path, speech.numpy(), samplerate=16000)

    print(
        f"Batch {i+1}/{num_batches} processed. Output saved as {output_filename}")
