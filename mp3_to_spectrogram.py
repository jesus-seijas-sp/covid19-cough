import os
import glob
from pydub import AudioSegment
import librosa
import librosa.display
import matplotlib as mpl
import matplotlib.pyplot as plt
from matplotlib import cm
import numpy as np

mpl.rcParams['savefig.pad_inches'] = 0
def save_spectrogram_mel(file_path, target_file_path):
    # Get the sample rate of the audio
    audio = AudioSegment.from_mp3(file_path)
    sample_rate = audio.frame_rate
    # Load the current audio with librosa
    y, sr = librosa.load(file_path, sr=sample_rate)
    stft = librosa.stft(y)
    plt.figure(figsize=[4,4], dpi = 100)
    #librosa.display.specshow(librosa.amplitude_to_db(stft, ref=np.max), y_axis='linear', x_axis='time', cmap=cm.viridis)
    librosa.display.specshow(librosa.amplitude_to_db(stft, ref=np.max), y_axis='linear', x_axis='time')
    plt.autoscale(tight=True)
    plt.axis('off')
    plt.ylim(0, 4000)
    plt.savefig(target_file_path, bbox_inches='tight', pad_inches=0)
    plt.close()

for filename in glob.iglob('./audios/**/*.mp3', recursive=True):
  path = os.path.normpath(filename)
  tokens = path.split(os.sep)
  targetpath = os.path.join('./spectrograms/', tokens[1])
  target = os.path.join(targetpath, os.path.splitext(tokens[2])[0]+'.png')
  print(target)
  if not os.path.isfile(target):
    os.makedirs(targetpath, exist_ok = True)
    try:
      save_spectrogram_mel(filename, target)
    except:
      print('Error processing ' + filename)
