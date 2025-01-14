# from typing import List
#
#
# class Solution:
#     def generateParenthesis(self, n):
#
#         result = []
#
#         def backTrack(paren, leftCount, rightCount):
#
#             if leftCount > n: return
#
#             if rightCount > leftCount: return
#
#             if leftCount == rightCount == n:
#                 result.append(paren)
#                 return
#
#             backTrack(paren + "(", leftCount + 1, rightCount)
#             backTrack(paren + ")", leftCount, rightCount + 1)
#
#         backTrack("", 0, 0)
#         return result

import numpy as np
import matplotlib.pyplot as plt

# Tham số
bit_rate = 5  # bps
fc_ask = 20  # tần số sóng mang ASK
fc_fsk_1 = 20  # tần số cho bit 1
fc_fsk_0 = 10  # tần số cho bit 0
amp_ask_1 = 5  # Biên độ bit 1
amp_ask_0 = 2  # Biên độ bit 0
duration_per_bit = 1 / bit_rate  # Thời gian mỗi bit

# Tín hiệu số
data = '10001'

# Vẽ tín hiệu ASK
t_ask = np.arange(0, len(data) * duration_per_bit, 0.001)
signal_ask = np.zeros_like(t_ask)

for i, bit in enumerate(data):
    if bit == '1':
        signal_ask[i * 200:(i + 1) * 200] = amp_ask_1 * np.sin(2 * np.pi * fc_ask * t_ask[i * 200:(i + 1) * 200])
    else:
        signal_ask[i * 200:(i + 1) * 200] = amp_ask_0 * np.sin(2 * np.pi * fc_ask * t_ask[i * 200:(i + 1) * 200])

# Vẽ tín hiệu FSK
t_fsk = np.arange(0, len(data) * duration_per_bit, 0.001)
signal_fsk = np.zeros_like(t_fsk)

for i, bit in enumerate(data):
    if bit == '1':
        signal_fsk[i * 200:(i + 1) * 200] = 5 * np.sin(2 * np.pi * fc_fsk_1 * t_fsk[i * 200:(i + 1) * 200] + np.pi / 2)
    else:
        signal_fsk[i * 200:(i + 1) * 200] = 5 * np.sin(2 * np.pi * fc_fsk_0 * t_fsk[i * 200:(i + 1) * 200] + np.pi / 2)

# Vẽ
plt.figure(figsize=(12, 8))

# Vẽ tín hiệu ASK
plt.subplot(2, 1, 1)
plt.title('ASK Signal')
plt.plot(t_ask, signal_ask, color='blue')
plt.ylim(-6, 6)
plt.grid()
plt.xlabel('Time (s)')
plt.ylabel('Amplitude (V)')

# Vẽ tín hiệu FSK
plt.subplot(2, 1, 2)
plt.title('FSK Signal')
plt.plot(t_fsk, signal_fsk, color='red')
plt.ylim(-6, 6)
plt.grid()
plt.xlabel('Time (s)')
plt.ylabel('Amplitude (V)')

plt.tight_layout()
plt.show()
