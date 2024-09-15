



import psutil,time,os
import pyperclip
import pyautogui as gui

people = '小贱贱'	# 好友全称
message = '试试'	# 发送的消息




   





def send_msg(people, msg):
    if 1:
       
        gui.moveTo(1610, 1394, duration=0.1)#定位到你的qq图标，qq要开最大化，不然会识别不到

        gui.click()
       
        
        time.sleep(0.5)
    else:
        pass
        
      

   
    gui.moveTo(247, 58, duration=0.2)#定位到搜索框
    gui.click()
    time.sleep(0.5)
    pyperclip.copy(people)
    gui.hotkey('ctrl', 'v')
    time.sleep(1)
    gui.hotkey('Enter')
   
    time.sleep(1)

    
    gui.moveTo(611, 1200, duration=0.5)#定位到消息框

    gui.click()

    pyperclip.copy(msg)
    i=0
    while 1:
          gui.hotkey('ctrl', 'v')
          gui.hotkey('Enter')
          
          i+=1
          if i>100:# 最多发送n条,写几条发几条
              break

    
  

   



if __name__ == "__main__":
    send_msg(people, message)

    

