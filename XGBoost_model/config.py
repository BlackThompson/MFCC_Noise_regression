# _*_ coding : utf-8 _*_
# @Time : 2023/4/24 14:29
# @Author : Black
# @File : config
# @Project : Mel_recognition


# columns_std = [f'{i}_std' for i in range(1, 14)]
# columns_25_percentile = [f'{i}_25_per' for i in range(1, 14)]
# columns_75_percentile = [f'{i}_75_per' for i in range(1, 14)]

# 均值
columns_mean = [f'{i}_mean' for i in range(1, 14)]
# 峰度
columns_kurtosis = [f'{i}_kurtosis' for i in range(1, 14)]
# 偏度
columns_skew = [f'{i}_skew' for i in range(1, 14)]
# 一阶差分均值
columns_diff_1_mean = [f'{i}_diff_1_mean' for i in range(1, 14)]
# 一阶差分方差
columns_diff_1_std = [f'{i}_diff_1_std' for i in range(1, 14)]
# 二阶差分均值
columns_diff_2_mean = [f'{i}_diff_2_mean' for i in range(1, 14)]

columns = ['category', 'file_name', 'score'] + columns_mean + columns_kurtosis + columns_skew + \
          columns_diff_1_mean + columns_diff_1_std + columns_diff_2_mean

used_feature_columns = columns_mean + columns_kurtosis + columns_skew + \
               columns_diff_1_mean + columns_diff_1_std + columns_diff_2_mean
