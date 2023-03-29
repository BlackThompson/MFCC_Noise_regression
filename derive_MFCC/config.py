# _*_ coding : utf-8 _*_
# @Time : 2023/3/12 22:40
# @Author : Black
# @File : config
# @Project : Mel_recognition

columns_mean = [f'{i}_mean' for i in range(1, 21)]
columns_std = [f'{i}_std' for i in range(1, 21)]
columns_25_percentile = [f'{i}_25_per' for i in range(1, 21)]
columns_75_percentile = [f'{i}_75_per' for i in range(1, 21)]
# 峰度
columns_kurtosis = [f'{i}_kurtosis' for i in range(1, 21)]
# 偏度
columns_skew = [f'{i}_skew' for i in range(1, 21)]

columns = ['category', 'file_name', 'score'] + columns_mean + columns_std

columns_new_1 = ['category', 'file_name', 'score'] + columns_mean + columns_25_percentile + \
                columns_75_percentile + columns_kurtosis + columns_skew
