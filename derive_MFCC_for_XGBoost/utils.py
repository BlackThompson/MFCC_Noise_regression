import numpy as np
import librosa


def Afilter(wav, sr):
    f1 = 20.60
    f2 = 107.7
    f3 = 737.9
    f4 = 12194
    dft = np.fft.fft(wav)
    freq = np.fft.fftfreq(len(wav)) * sr
    freq_x = freq[freq != 0]
    freq_u = ((f4 ** 2) * (freq_x ** 4))
    freq_d = (freq_x ** 2 + f1 ** 2) * ((freq_x ** 2 + f2 ** 2) ** 0.5) * ((freq_x ** 2 + f3 ** 2) ** 0.5) * \
             (freq_x ** 2 + f4 ** 2)
    a_weighting = 20 * np.log10(freq_u / freq_d) + 1.9998
    dft[freq == 0] = dft[freq == 0] * (10 ** (a_weighting[0] / 20))
    dft[freq != 0] = dft[freq != 0] * (10 ** (a_weighting / 20))
    a_wav = np.fft.ifft(dft)
    a_wav = np.real(a_wav)
    return a_wav


def cal_laeq(data, sr):
    # data = data[:, 0]
    # 上面这一行是为了保证输入的数据是单声道的
    data = Afilter(data, sr)
    pp = 0
    for i in range(0, len(data)):
        pp += data[i] ** 2

    pa = np.sqrt(pp / len(data))
    p0 = 7.071 * 1e-6
    laeq = 20 * np.log10(pa / p0)
    return laeq


def amplitude(data, sr, target_laeq=60):
    current_laeq = cal_laeq(data, sr)
    data = data * (10 ** ((target_laeq - current_laeq) / 20))
    return data


def extract_mfcc(path, sr=44100, n_mfcc=13):
    data, sr = librosa.load(path, sr=sr)
    data = amplitude(data, sr)
    mfcc = librosa.feature.mfcc(y=data, sr=sr, n_mfcc=n_mfcc)
    mfcc = mfcc.T
    return mfcc


def first_order_diff_mean_var(x):
    diff = np.diff(x, n=1)
    mean = np.mean(diff)
    var = np.var(diff)
    return mean, var


def second_order_diff_mean(x):
    diff = np.diff(x, n=2)
    mean = np.mean(diff)
    return mean

# if __name__ == '__main__':
#     path = r'test_sound/'
#     sound_list = os.listdir(path)
#     ret = pd.DataFrame(columns=['file_name', 'A_dB'])
#     for i_2 in range(0, len(sound_list)):
#         sound, fs = sf.read(path + sound_list[i_2])
#         sound = sound[:, 0]
#         sound = Afilter(sound, fs)
#
#         pp = 0
#         for i_1 in range(0, len(sound)):
#             pp += sound[i_1] ** 2
#
#         pa = np.sqrt(pp / len(sound))
#         p0 = 7.071 * 1e-6
#         spl_value = 20 * np.log10(pa / p0)
#         ret.loc[i_2, 'file_name'] = sound_list[i_2]
#         ret.loc[i_2, 'A_dB'] = spl_value
#         print(sound_list[i_2])
#         print(spl_value)
# ret.to_csv('self_a_ret2.csv')
