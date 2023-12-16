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
    t = threading.Thread(target=download,args=[line,f'.\{name}_{count}.mp4'])
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
    name_file=[]
    fksource=input("Nhập nơi để file txt hoặc tên file (mặc định là playlist.txt),nhập local để chọn file txt\n YÊU CẦU SẮP XẾP THEO THỨ TỰ TẬP:")
    if fksource == 'local':
        for file in os.listdir("./"):
            if file.endswith(".txt"):
                  name_file.append(file)
        for i in range(len(name_file)):
            name=name_file[i]
            print(f'{i}:{name}')
        source=input('Mời chọn:')
    elif fksource=='':
        source='playlist.txt'
    chek=input("Press a key to download only,b to check one time and download, ckmode to checking only")          
    if chek == 'a':
            name=input("Name bộ anime này là :")
            download_task(name,source)
    elif chek == 'b':
        name=input("Name bộ anime này là :")
        checking(source)
        download_task(name,'playlist.chked.txt')
    elif chek == 'ckmode':
        checking(source)
        
        
    
        
        
    
    
