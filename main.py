import eel
import random

eel.init('web')  # 'web'是包含HTML/CSS/JS文件的目录

@eel.expose  # 将这个函数暴露给JavaScript
def random_number(start, end):
    return random.randint(start, end)

# 开始运行Eel，指定主页面和大小
eel.start('main.html', size=(400, 300))
