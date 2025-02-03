'''
import time
import asyncio

def fetch_data():
    print("Fetching data")
    time.sleep(3)
    print("Data fetched")
    
    
def process_data():
    print("processing the data")
    time.sleep(3)
    print("Data processed")
    
    
def main():
    print("without async io")
    start=time.time()
    fetch_data()
    process_data()
    end=time.time()
    print(f"serially completed in: {end-start}")
    print('with asyncio')
    start=time.time()
    asyncio.run(async_main())
    end=time.time()
    print(f"asynchronously completed in: {end-start}")
    
    
async def fetch_data1():
    print('fetching data')
    await asyncio.sleep()
    print('data fetched')
    
async def processData():
    print("Processing data")
    await asyncio.sleep()
    print('data Processed')

def async_main():
    return asyncio.gather(fetch_data(),process_data())    
    
      
# start=time.time()
# asyncio.run(main())
# end=time.time()
# print(f"asynchronously completed in: {end-start}")
if __name__=='__main__':
    main()
    
    
'''

''' asynchronus data fetching '''
import asyncio
import aiohttp



async def fetch_data(url):
    async with aiohttp.ClientSession() as session:
        async with session.get(url) as reponse:
            print(await reponse.text())
            
asyncio.run(fetch_data('https://google.co.in'))
        