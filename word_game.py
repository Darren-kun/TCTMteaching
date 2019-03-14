# -*- coding: utf-8 -*-
"""
Created on Wed Mar 13 17:08:34 2019

@author: Darren


简单打字游戏


知识点：

库：time random
知识：变量  print input if list while for range 占位符


游戏思路：

统计正确率
分析跟踪打字速度变化（可视化图）

                运行开始提示 < ----------------------|
                    |                               |
     开始 <---------|---> 取消 ---> 是否退出游戏 ------->退出
       |
 游戏开始。。。 倒数 3 2 1（跳动效果）
       |
    循环随机出现 一个 字母（A B C ...)(可以设置 循环的次数)
       |
    计算每一次回复是否正确，输入的时间，记录下来
       |
     游戏结束 ---> 输出本次的打字结果数据（正确率多少，平均反应速度）


"""
#----  简单版本 -----
#import time
#import random
#
#word_l = list('ZXCVBNMLKJHGFDSAQWERTYUIOP')
#translation_speed = []
#
#def word_game(max_nummber):
#    print('游戏即将开始 ...')
#    for i in range(3,0,-1):
#        print(i)
#        time.sleep(1)
#    number = 0
#    while number <= max_nummber:
#        random_word = random.choice(word_l)
#        start_time = time.time()
#        word = input(f'{random_word}  ---> ')
#        end_tiem = time.time()
#        
#        use_time = end_tiem - start_time
#        if word == random_word:
#            print(f'TRUE \n use time : {str(use_time)}')
#            translation_speed.append([])
#        else:
#            print(f'FALSE  -_- \n use time : {str(use_time)}')
#        number += 1
#    print('游戏结束')
##    print()
#            
#max_nummber = 10    
#word_game(max_nummber)













        