# Whisper - speech recognition
Using [Whisper](https://github.com/openai/whisper) to transcribe audio oral history interviews. Whisper is a free and open-source model from [OpenAI](https://openai.com/blog/whisper/).

Thanks to Shawn Graham for the tip from his [blog](https://electricarchaeology.ca/2022/09/22/whisper-from-openai-for-transcribing-audio/).


## Install
See setup information [here](https://github.com/openai/whisper#setup)

Can also install using [Miniconda](https://conda.io/projects/conda/en/stable/user-guide/install/index.html) package managament system:

```conda create -n whisperai python=3.9```
* **whisperai** is the name I gave my conda environment

```conda activate whisperai```

```conda install pytorch torchvision torchaudio -c pytorch-nightly```

```pip install ffmpeg```

```pip install rust```

```pip install git+https://github.com/openai/whisper.git```


Then in the future to use, activate the conda environment:

```conda activate whisperai```

* once activated, enter the *whisper* commands you'd like to run

## Run
```whisper 'home/myFiles/audio/audioFile.mp3' --model medium --language en --fp16 False --output_dir 'home/myFiles/transcripts'```

Example output

![Terminal window showing whisper output](/screenshots/screenshot_terminal-whisper.png)

Output will be saved with the same name as the audio file and includes three files: **.srt**, **.txt**, and **.vtt**

See more information about usage options on the [Whisper GitHub page](https://github.com/openai/whisper#available-models-and-languages), including how to translate speech into English. Or you can run the following command to view all options in the terminal window:

```whisper --help```

**Keep in mind of [VRAM requirements](https://github.com/openai/whisper#available-models-and-languages)** - small model only requires 2 GB whereas medium model requires 5 GB.
* small model requires less computing power and will be slightly faster but not as accurate (though still really good!)
* medium model takes more computing resources, is slower, but VERY accurate
