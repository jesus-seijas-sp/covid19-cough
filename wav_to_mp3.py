import os
import glob
from pydub import AudioSegment

for filename in glob.iglob('./source/**/*.wav', recursive=True):
  path = os.path.normpath(filename)
  tokens = path.split(os.sep)
  targetpath = os.path.join('./audios/', tokens[2])
  target = os.path.join(targetpath, os.path.splitext(tokens[3])[0]+'.mp3')
  os.makedirs(targetpath, exist_ok = True)
  sound = AudioSegment.from_wav(filename)
  sound.export(target, format = 'mp3')
  print(target)
