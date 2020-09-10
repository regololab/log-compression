import os, time, sys, yaml
from datetime import datetime

class LogCompression():
    
    def __init__(self):
        self.now = time.time()
        self.delete_old_file = 7 # day
        self.lista = './log_list.yaml'
        self.one_mega = 1048576 # 1MB
        self.max_size_file = self.one_mega / 10 # 100KB
        
    def read_list_and_compress_log(self):
        with open(self.lista) as file:
            logs = yaml.load(file, Loader=yaml.FullLoader)
            date_time = datetime.today().strftime('%Y-%m-%d_%H_%M_%S')
            name_file = ''
            path = ''
            for K,R in logs.items():
                statinfo = os.stat(R)
                name_file = R.split('/')[-1].split('.')[0]
                path = '/'.join(R.split('/')[0:-1])+'/'
                if statinfo.st_size > self.max_size_file:
                    os.system(f'gzip -c {R} > {path}{name_file}-{date_time}.gz')
                    os.system(f'rm -f {R}')
                    os.system(f'touch {R}')
                # delete old file
                self.__delete_file(path)
    
    def __delete_file(self, path):
        for R in os.listdir(path):
            if R.endswith('.gz'):
                if os.stat(path+R).st_mtime < self.now - self.delete_old_file * 86400:
                    os.system(f'rm -f {path}{R}')

logmin = LogCompression()
logmin.read_list_and_compress_log()
