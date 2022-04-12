# 这是一个示例 Python 脚本。

# 按 Shift+F10 执行或将其替换为您的代码。
# 按 双击 Shift 在所有地方搜索类、文件、工具窗口、操作和设置。

#
# def print_hi(name):
#     # 在下面的代码行中使用断点来调试脚本。
#     print(f'Hi, {name}')  # 按 Ctrl+F8 切换断点。
#
#
# # 按间距中的绿色按钮以运行脚本。
# if __name__ == '__main__':
#     print_hi('PyCharm')

# 访问 https://www.jetbrains.com/help/pycharm/ 获取 PyCharm 帮助

import time

# stock_board_concept_name_em_df = ak.stock_board_concept_cons_em()
# print(stock_board_concept_name_em_df)
from selenium import webdriver

url='http://www.baidu.com'
driver = webdriver.Firefox()
driver.get(url)
driver.find_element('id','kw').send_keys('python')
driver.find_element('id','su').click()
time.sleep(2)
