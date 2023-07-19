# T5 Speech from Microsoft

![GNU GPL](https://badgen.net/badge/GNU%20GPL%20v3/license/orange) ![Huggingface](https://badgen.net/badge/icon/Huggingface?icon=huggingface&label=Transformers) ![Python](https://badgen.net/badge/icon/Python?icon=python&label=Python%203)

Based on their paper **[SpeechT5: Unified-Modal Encoder-Decoder Pre-Training for Spoken Language Processing](https://arxiv.org/abs/2110.07205)** and the original repository **[on Github](https://github.com/microsoft/SpeechT5/)** we bring you a simple script for using the SpeechT5 model from Microsoft using `Python` to generate speech from text.

Example code and the model card can be found on the [Huggingface model page](https://huggingface.co/microsoft/speecht5_tts).



## How it Works

The script uses the [Huggingface Transformers]() library to load the model and tokenizer. The model is then used to generate speech from text. The script is very simple and can be easily modified to suit your needs. It loads the file `prompt.txt` and processes it in batches that contain **two lines of input**. For every two lines, it outputs a `wav` file to disk as `speech_#.wave` where `#` is the number of the batch. The script will also print the the results to the console as it generates the audio files.

After editing `prompt.txt` to contain the text you want to generate speech from, you can run the script like this;

```bash
python3 app.py
```

You'll end up with files such as;

```
speech_0.wav
speech_1.wav
speech_2.wav
```

If you need a combined MP3 file of all the generated audio, you can use the `mp3.py` script to combine each of the files output by the model into a single MP3 file. You can run it like this;

```bash
python3 mp3.py
```

### NOTE: This script will overwrite any existing `speech_#.wav` files in the directory!

> We do not archive files, we overwrite them each run to keep the script simple. If you want to keep the files, move them to another directory before running the script again.

1. Write your script in `prompt.txt`
2. Run `python3 app.py`
3. Optionally preview `speech_#.wav` files
4. Run `python3 mp3.py` to combine all the `speech_#.wav` files into a single `output.mp3` file
5. Optionally preview `output.mp3` file
6. Archive `prompt.txt`, `speech_#.wav` and `output.mp3` files into their own directory.

> A future version may simply create a directory for each run and archive the files there by UUID.

## Requirements

You'll need to install the Python libraries;

```bash
pip install -r requirements.txt
```

This will load the following libraries - use a virtual environment if you want to keep your system clean;

```bash
transformers
numpy
torch
datasets
transformers
accelerate
soundfile
pathlib
pydub
sentencepiece
```

## License

This code is released fully under a GNU GPL v3 license. 

[See the Free Software Foundation's page for more information](https://www.gnu.org/licenses/gpl-3.0.html#license-text).

## Credits

- [Microsoft](http://www.microsoft.com)
- [Huggingface](https://huggingface.co)
- [The Henzi Foundation](https://henzi.org)