# mel spectogram plot

import numpy as np
import librosa.display
import matplotlib.pyplot as plt

# heed file extension

path_to_mp3 = '/Users/nathanoasis/Downloads/'
path_to_save = '/Users/nathanoasis/Desktop/spectogram_plots/'
song_file_names = [('Freaks_and_Geeks', 'Rap'), ('Moonlight_Sonata', 'Classical'), ('Go_Thru_Your_Phone', 'RnB'),('In_A_Sentimental_Mood', 'Jazz')]
# song_file_names = [('Freaks_and_Geeks', 'Rap')]

# plt.figure(figsize=(4, 2.5))
plt.rcParams.update({'font.size': 18.25})
plt.rcParams['xtick.major.size'] = 7.5
plt.rcParams['xtick.major.width'] = 4
plt.rcParams['ytick.minor.size'] = 7.5
plt.rcParams['ytick.minor.width'] = 4


def save_spectogram(genre, mp3_path, save_img_path):
    # print('load path', mp3_path+'.mp3')
    # print('save path', save_img_path+'.eps')
    plt.figure(figsize=(10.5, 6))
    y, sr = librosa.load(mp3_path+'.mp3', offset=0, duration=120.0)
    # y, sr = librosa.load(mp3_path+'.mp3')
    spect = librosa.feature.melspectrogram(y=y, sr=sr,n_fft=2048, hop_length=512)
    librosa.display.specshow(librosa.power_to_db(spect, ref=np.max), y_axis='mel', fmax=8000, x_axis='time')
    plt.colorbar(format='%+2.0f dB')
    plt.title(genre, fontsize=37.5, fontweight='semibold', fontname='Arial')
    plt.xlabel('Time', fontsize=29.5, fontweight='roman', fontname='Arial')
    plt.ylabel('Hz', fontsize=29.5, fontweight='roman', fontname='Arial')

    plt.tight_layout()
    # plt.savefig(save_img_path+'.eps', format='eps', dpi=300)
    plt.savefig(save_img_path+'.png', format='png', dpi=350, bbox_inches='tight')
    # plt.show()
    plt.clf()
    plt.cla()
    plt.close()

for song in song_file_names:
    save_spectogram(song[1], path_to_mp3+song[0], path_to_save+song[0])
    print('finished song', song[0])