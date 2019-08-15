import time
import os

path = '/home/jyfelt/workspace/DataVizProject'
os.chdir(path)
commit_message = 'backpack updated: %s' % time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())
log_name = 'backpack_%s.log' % time.strftime("%Y%m%d", time.localtime())

# os.system('git pull')
os.system('rm log/*.log')
os.system('touch log/%s' % log_name)
