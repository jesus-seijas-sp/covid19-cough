import os
import glob
from pydub import AudioSegment
import librosa
import librosa.display
import matplotlib as mpl
import matplotlib.pyplot as plt
import numpy as np

mpl.rcParams['savefig.pad_inches'] = 0
def save_spectrogram_mel(file_path, target_file_path, mels = 40):
    # Get the sample rate of the audio
    audio = AudioSegment.from_mp3(file_path)
    sample_rate = audio.frame_rate
    # Load the current audio with librosa
    y, sr = librosa.load(file_path, sr=sample_rate)
    input_nfft = int(round(sample_rate * 0.025))
    input_stride = int(round(sample_rate * 0.010))
    mel = librosa.feature.melspectrogram(y = y, n_mels = mels, n_fft = input_nfft, hop_length = input_stride)
    plt.figure(figsize=[4,4], dpi = 100)
    librosa.display.specshow(librosa.power_to_db(mel, ref=np.max), y_axis='mel', sr=sr, hop_length=input_stride, x_axis='time')
    plt.autoscale(tight=True)
    plt.axis('off')
    plt.savefig(target_file_path, bbox_inches='tight', pad_inches=0)
    plt.close()

for filename in glob.iglob('./audios/**/*.mp3', recursive=True):
  path = os.path.normpath(filename)
  tokens = path.split(os.sep)
  targetpath = os.path.join('./mel/', tokens[1])
  target = os.path.join(targetpath, os.path.splitext(tokens[2])[0]+'.png')
  os.makedirs(targetpath, exist_ok = True)
  print(target)
  save_spectrogram_mel(filename, target)
