# _*_ coding : utf-8 _*_
# @Time : 2023/3/12 22:40
# @Author : Black
# @File : config
# @Project : Mel_recognition

columns_mean = [f'{i}_mean' for i in range(1, 21)]
columns_std = [f'{i}_std' for i in range(1, 21)]
columns = ['category', 'file_name', 'score'] + columns_mean + columns_std
used_feature_columns = columns_mean + columns_std
