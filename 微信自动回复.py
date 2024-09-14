import numpy as np
import pandas as pd
from uiautomation import WindowControl, ListControl
import time

wx = WindowControl(
    searchDepth=1, 
Name='微信')

wx.ListControl()
wx.SwitchToThisWindow()

hw = wx.ListControl(Name='会话')

df = pd.read_csv('回复数据.csv', encoding='GBK')

while True:
    we = hw.TextControl(searchDepth=5)

    while not we.Exists():
              pass   

#last_msg =wx.ListControl(Name='消息').GetChildren()[-1].Name    

    if we.Name:
         we.Click(simulateMove=False)
         last_msg =wx.ListControl(Name='消息').GetChildren()[-1].Name
         msg = df.apply(lambda x: x['回复内容'] if x['关键词'] in last_msg else None, axis=1)
         print(msg)

         msg.dropna(axis=0, inplace=True)
         ar=np.array(msg).tolist()
         if ar:
             wx.SendKeys(ar[0].replace('{br}', '{Shift}{Enter}'), waitTime=1)
        
             wx.SendKeys('{Enter}', waitTime=1)
             wx.TextControl(SubName=ar[0][:5]).RightClick()
         





     












