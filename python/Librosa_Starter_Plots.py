# mel spectogram plot

import numpy as np
import librosa.display
import matplotlib.pyplot as plt

# heed file extension
path_to_mp3 = '/Users/nathanoasis/Downloads/Freaks_and_Geeks.mp3'
path_to_save = '/Users/nathanoasis/Downloads/Freaks_and_Geeks.eps'

# path_to_mp3 = '/Users/nathanoasis/Downloads/Moonlight_Sonata.mp3'
# path_to_save = '/Users/nathanoasis/Downloads/Moonlight_Sonata.eps'

y, sr = librosa.load(path_to_mp3)
spect = librosa.feature.melspectrogram(y=y, sr=sr,n_fft=2048, hop_length=512)
librosa.display.specshow(librosa.power_to_db(spect, ref=np.max), y_axis='mel', fmax=8000, x_axis='time')
plt.colorbar(format='%+2.0f dB')
plt.title('Mel Spectrogram')
plt.tight_layout()

plt.savefig(path_to_save, format='eps', dpi=1200)
# plt.show()