import multiprocessing
import requests
import time
import os
import warnings
warnings.filterwarnings('ignore')

 
def downloadImage(url,idx,dir):
    try:
        reponse=requests.get(url,verify=False)
        with open(os.path.join(dir,f"image_{idx}.jpg"),'wb') as file:
            file.write(reponse.content)
        print(f"Downloaded image_{idx}.jpg")
    except Exception as e:
        print(f"e")

def download_serially(url,start,end,dir):
    for  i in range(start,end+1):
        downloadImage(url,i,dir)
        
                
if __name__=='__main__':

    url="https://picsum.photos/2000/3000"
    dir="./images"
    
    if not os.path.exists(dir):
        os.makedirs(dir)
        
    print("downloading 5 images serially")
    start=time.time()
    download_serially(url,1,5,dir)
    end=time.time()
    print(f"Time required to download image serially: {end-start}\n")
    print(f"Downloading another 5 images using multiProcessing")
    

    processes=[]
    start=time.time()
    for i in range(6,11):
        p=multiprocessing.Process(target=downloadImage,args=(url,i,dir))
        processes.append(p)
        p.start()
        
    for p in processes:
        p.join()
        
    end=time.time()
    print(f"Time required to download image using multiprocessing: {end-start}")
    
    
    