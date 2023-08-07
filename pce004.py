# python code execution
import os
import time

os.system('clear')
print('\nWelcome User, There Is A Code Execution Vulnerability In This Bot, Can You Exploit It ?\n')

while True:
      user = input('Ask Me Anything >> ')
      if '<' in user:
         usr = user.split('<')
         print(os.system(usr[1]))
      if '_' in user:
         usr = user.split('_')
         print(os.system(usr[1]))
      else:
         print('\n'+user+'\n')
