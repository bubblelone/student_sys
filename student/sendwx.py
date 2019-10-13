"""
@Version: 1.0
@Project: PythonCookBook
@Author: bubblelone
@Date: 2019/3/12 9:16
@File: sendwx.py
@License: MIT
"""

import itchat

itchat.auto_login(hotReload=True)

itchat.send('Hello, filehelper23', toUserName='filehelper')

author = itchat.search_friends(name='阿发')
#author.send('greeting, 黄国龙!')
print(author)

