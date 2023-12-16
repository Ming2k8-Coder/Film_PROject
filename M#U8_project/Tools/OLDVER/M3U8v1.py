#Doc string 
"""M3U8 Downloader /\/\ More info in download func"""
#import
import time
import threading
import os
import requests
def download(link,path):
      """Download Module /\/\ USING:(link,path)"""
      os.system(f'cmd /k hlsdl -b -o {path} {link}')
def download_task(name='output',source='playlist.txt',count=0):
 start = time.perf_counter()
 sourceed= open(source)
 txt= sourceed.readlines()
 threads = []
 for line in txt:
    count += 1
    line = line.replace("\n", "")
    t = threading.Thread(target=download,args=[line,f'D:\Film\{name}_{count}.mp4'])
    t.start()
    threads.append(t)
 for thread in threads:
    thread.join()
 finish = time.perf_counter()
 print(f'Thời gian hoàn thành {finish} seconds')
 print(f'Hoàn thành in {round(finish-start, 2)} seconds')
def checking(source):
    chkbf=open(source)
    chked=open('playlist.chked.txt','w')
    txt= chkbf.readlines()
    for line in txt:
        line = line.replace("\n", "")
        rqst=requests.head(line)
        if rqst.status_code == 200:
            print(f"{line} online with status {rqst}")
            line += '\n'
            chked.write(line)
        elif rqst.status_code == 404:
            print(f"{line} offlne with status {rqst}")
        else:
            print(f"{line} have problems with status {rqst}")
    chked.close()  
if __name__=='__main__':
#Lay info
    source=input("Nhập nơi để file txt hoặc tên file (mặc định là playlist.txt) \n YÊU CẦU SẮP XẾP THEO THỨ TỰ TẬP:")
    chek=input("Press a key to download only,b to check one time and download, ckmode to checking only")
    #Phan tich info
    if source == '':
          source='playlist.txt'
    if chek == 'a':
        download_task(name,source)
        name=input("Name bộ anime này là :")
    elif chek == 'b':
        checking(source)
        name=input("Name bộ anime này là :")
        download_task(name,'playlist.chked.txt')
    elif chek == 'ckmode':
        checking(source)
        
        
    
        
        
    
    
