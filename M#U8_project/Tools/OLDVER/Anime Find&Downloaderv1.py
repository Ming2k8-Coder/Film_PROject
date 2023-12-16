#Preset
import M3U8
httpslink='https://s2.animeweb.xyz/media/video-clips/anime2/'
import time
import threading
import os
import requests
def downloadwk(target,name='output',count=0):
    start = time.perf_counter()
    threads = []
    for item in target:
        count += 1
        t = threading.Thread(target=M3U8.download,args=[item,f'D:\Film\{name}_{count}.mp4'])
        t.start()
        threads.append(t)
    for thread in threads:
        thread.join()
    finish = time.perf_counter()
    print(f'Thời gian hoàn thành {finish} seconds')
    print(f'Hoàn thành in {round(finish-start, 2)} seconds')
def main ():
    #Khai báo
    slg = []
    rdyfdown =[]
    #Dò hỏi 
    name=input('Tên bộ anime:')
    typeeps=input('Loại tập ova, tập thường bỏ trống,nếu là special gõ sp hoặc spe:')
    begineps=int(input('Tập bắt đầu:'))
    endeps=int(input('Tập kết thúc:'))
    slect=input('Muốn tải xuống gõ download, ghi vào file gõ write, chỉ kiểm tra gõ check:')
    #Xử lý info
    names=name.replace(' ','-')
    if begineps == endeps :
        if typeeps=='ova':
            begineps = ''
            slg.append(begineps)
        else:
            slg.append(begineps)
        print('CHÚ Ý: Tập bắt đầu, Tập kết thúc trùng nhau') 
    else :
        endeps +=1
        for i in range(begineps,endeps):
            slg.append(i) 
    prerqst=requests.head(f'{httpslink}{names}/{typeeps}{begineps}/{names}-{typeeps}{begineps}.m3u8')
    if prerqst.status_code == 404:
        print(f'Lỗi Link, lấy 1 link preset và so sánh \n Chú ý chỗ .../anime/sự khác biệt/{names}')
        print(f'{httpslink}{names}/{typeeps}{begineps}/{names}-{typeeps}{begineps}.m3u8')
        adder=input('Sự khác biệt:')
        ader=f'{adder}/'
    else:
        ader=''
    for item in slg:
        link=f'{httpslink}{ader}{names}/{typeeps}{item}/{names}-{typeeps}{item}.m3u8'
        print(f'Link :{link}')
        rqst=requests.head(f'{link}')
        if rqst.status_code == 200:
            print(f"This link online with status {rqst}")
            if slect== 'download':
                rdyfdown.append(link)
            elif slect== 'write':
                filew=open('CHECKED.txt','a')
                filew.write(link)
                filew.write('\n')
                filew.close()
        elif rqst.status_code == 404:
            print(f"This link offlne with status {rqst}")
        else:
            print(f"This link have problems with status {rqst}")
    if slect== 'download':
        confirm=input('Download Confirm?y/n:')
        if confirm=='y':
            for item in slg:
                print(f'{rdyfdown}{names}{begineps}')
                downloadwk(rdyfdown,names,begineps)
            
main()
