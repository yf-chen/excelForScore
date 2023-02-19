import random

import openpyxl


def find_five_numbers_less70(total_sum):
    for a in range(60, 80):
        for b in range(60, 90):
            for c in range(60, 90):
                for d in range(60, 95):
                    # 计算四个数的和
                    sum_of_four = a + b + c + d
                    # 计算第五个数的值
                    e = total_sum - sum_of_four
                    # 判断是否符合条件
                    if e == 0 and sum_of_four == total_sum:
                        return [a, b, c, d, e]
    return None


def find_five_numbers_less80(total_sum):
    for a in range(65, 95):
        for b in range(65, 80):
            for c in range(70, 90):
                for d in range(80, 90):
                    for e in range(75, 95):
                        # 计算五个数的和
                        sum_of_five = a + b + c + d + e
                        # 判断是否符合条件
                        if sum_of_five == total_sum:
                            return [a, b, c, d, e]
    return None


def find_five_numbers_less90(total_sum):
    for a in range(75, 95):
        for b in range(70, 90):
            for c in range(60, 100):
                for d in range(60, 100):
                    for e in range(85, 95):
                        # 计算五个数的和
                        sum_of_five = a + b + c + d + e
                        # 判断是否符合条件
                        if sum_of_five == total_sum:
                            return [a, b, c, d, e]
    return None


def find_five_numbers_less100(total_sum):
    for a in range(80, 100):
        for b in range(90, 100):
            for c in range(90, 95):
                for d in range(90, 99):
                    for e in range(90, 101):
                        # 计算五个数的和
                        sum_of_five = a + b + c + d + e
                        # 判断是否符合条件
                        if sum_of_five == total_sum:
                            return [a, b, c, d, e]
    return None


workbook = openpyxl.load_workbook('wulian3.xlsx')

# 获取要操作的表格，假设为第一个表格
worksheet = workbook.worksheets[0]

# 遍历每行
for row in worksheet.iter_rows(min_row=3, max_row=38):  # 从第二行开始遍历，跳过标题行
    cell_result = row[14]
    final_score = cell_result.value
    score_sum = final_score * 5
    score_arr = []
    arr = [0, 1, 2, 3, 4]
    index_arr = random.sample(arr, len(arr))
    if final_score <= 70:
        score_arr = find_five_numbers_less70(score_sum)
    if 80 >= final_score > 70:
        score_arr = find_five_numbers_less80(score_sum)
    if 90 >= final_score > 80:
        score_arr = find_five_numbers_less90(score_sum)
    if 100 >= final_score > 90:
        score_arr = find_five_numbers_less100(score_sum)

    if score_arr != None:
        score_arr_final = []
        for ind in index_arr:
            score_arr_final.append(score_arr[ind])
        row[6].value = score_arr_final[0]
        row[7].value = score_arr_final[1]
        row[8].value = score_arr_final[2]
        row[9].value = score_arr_final[3]
        row[10].value = score_arr_final[4]
    else:
        print('final_score: ', final_score, 'score_sum: ', score_sum)

# 保存更改
workbook.save('wulian011.xlsx')
