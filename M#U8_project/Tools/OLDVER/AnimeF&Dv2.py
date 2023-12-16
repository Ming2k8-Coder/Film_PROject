#import
import time
import threading
import os
import requests
#preset
#Oder of parameter:serverlink list(svlst), different list(diflst)
parameter='AF&D_parameterv2.txt'
parameter_file=os.path.exists(parameter)
if parameter_file == False:
    httpslink=''
    print('Manual mode!')
else:
    httpslink='automode'
    print('Automatic mode!')
def replace(file, pattern, subst):
    # Read contents from file as a single string
    file_handle = open(file, 'r')
    file_string = file_handle.read()
    file_handle.close()

    # Use RE package to allow for replacement (also allowing for (multiline) REGEX)
    file_string = (re.sub(pattern, subst, file_string))

    # Write contents to file.
    # Using mode 'w' truncates the file.
    file_handle = open(file, 'w')
    file_handle.write(file_string)
    file_handle.close()
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
    serlin=[]
    diff=[]
    breakcon1=0
    global httpslink
    #Dò hỏi
    name=input("Tên bộ anime:")
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
        for i in range(begineps,endeps):
            slg.append(i)
    #Dò link
    if httpslink == 'automode':
        fparam=open(parameter)
        paramstr=fparam.readlines()
        for line in paramstr :
            line = line.replace("\n", "")
            if line.find('#') == -1:
                if line.find('svlst') != -1:
                    line = line.replace(" svlst", "")
                    
                    serlin.append(line)
                if line.find('diflst')!= -1:
                    line = line.replace(" diflst", "")
                    diff.append(line)
        print(serlin)
        print(diff)
        for item in serlin:
            print(breakcon1)
            if breakcon1 == 0 :                
                prerqst=requests.head(f'{item}{names}/{typeeps}{begineps}/{names}-{typeeps}{begineps}.m3u8')
                if prerqst.status_code == 200:
                    print(f'Link:{item}{names}/{typeeps}{begineps}/{names}-{typeeps}{begineps}.m3u8')
                    httpslink=item
                    ader=''
                    print(httpslink)
                else:
                    print(f'Link không đơn giản{item} ,đang thử lại')         
                    for item in serlin:
                        for i in range(len(diff)):
                            adder = diff[i]
                            testdiff=f'{adder}/'
                            prerqst=requests.head(f'{item}{testdiff}/{names}/{typeeps}{begineps}/{names}-{typeeps}{begineps}.m3u8')
                            if prerqst.status_code == 200:
                                httpslink=item
                                print(f'Link:{item}{testdiff}{names}/{typeeps}{begineps}/{names}-{typeeps}{begineps}.m3u8')
                                ader=testdiff
                                breakcon1 += 1
                            else:
                                print(f'{item}{testdiff}/{names}/{typeeps}{begineps}/{names}-{typeeps}{begineps}.m3u8, vui lòng thêm vào file!')
            else:
                break
    else:
        prerqst=requests.head(f'{httpslink}{names}/{typeeps}{begineps}/{names}-{typeeps}{begineps}.m3u8')
        if prerqst.status_code == 404:
            print(f'Lỗi Link, lấy 1 link preset và so sánh \n Chú ý chỗ .../anime/sự khác biệt/{names}')
            print(f'{httpslink}{names}/{typeeps}{begineps}/{names}-{typeeps}{begineps}.m3u8')
            adder=input('Sự khác biệt:')
            ader=f'{adder}/' 
        else:
            ader=''
    #Kiểm tra            
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
