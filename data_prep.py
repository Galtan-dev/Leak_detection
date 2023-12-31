from scipy.io import wavfile
import numpy as np
import math

# open file with sound data
sampling_frequency, sound_data_orig = wavfile.read("record_2.wav")



filter_length = 10   # vždy se udělá o jeden méně ve výsledku, počítat s tím u nastavování filtru při detekci, nebude 50 vstupů ale jen 49
start = 220000
end = 280000
sound_data = []

for i in range(0, len(sound_data_orig)):
    if sound_data_orig[i]==0:
        sound_data.append(sound_data_orig[i])
    else:
        sound_data.append(math.log(abs(sound_data_orig[i])))

in_matrix = []
target_matrix = []

# separation of inputs
for i in range(1, filter_length):
    name = "in_" + str(i)
    name = []
    for j in range((start + (i - 1)), end + i):
        name.append(sound_data[j])
    for k in range(0, len(name)):
        in_matrix.append(name[k])

target = []
for i in range(start + (filter_length - 1), end + filter_length):
    target.append(sound_data[i])
for i in range(0, len(target)):
    target_matrix.append(target[i])

m = len(name)
in_matrix = np.asarray(in_matrix)
in_matrix = np.reshape(in_matrix, [m, filter_length - 1], order="F")
target_vector = np.reshape(target_matrix, (m,))

np.savetxt("in_sound_data.csv", in_matrix, delimiter=",")
np.savetxt("target_sound_data.csv", target_vector, delimiter=",")










# # inputs one by one - continuously drifted by one
# in_1 = []
# in_2 = []
# in_3 = []
# in_4 = []
# in_5 = []
# target = []
# for i in range(start, end + 1):
#     in_1.append(sound_data[i])
# for i in range(start + 1, end + 2):
#     in_2.append(sound_data[i])
# for i in range(start + 2, end + 3):
#     in_3.append(sound_data[i])
# for i in range(start + 3, end + 4):
#     in_4.append(sound_data[i])
# for i in range(start + 4, end + 5):
#     in_5.append(sound_data[i])
# for i in range(start + 5, end + 6):
#     target.append(sound_data[i])

# # creation of matrix of inputs and target vector
# k = len(in_1)
# in_matrix = []
# target_matrix = []
# for i in range(0, k):
#     in_matrix.append(in_1[i])
# for i in range(0, k):
#     in_matrix.append(in_2[i])
# for i in range(0, k):
#     in_matrix.append(in_3[i])
# for i in range(0, k):
#     in_matrix.append(in_4[i])
# for i in range(0, k):
#     in_matrix.append(in_5[i])
# for i in range(0, k):
#     target_matrix.append(target[i])