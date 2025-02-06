
## With synchronous
import time

def fetch_data():
    print("Fetching data")
    time.sleep(3)
    print("Data fetched")

def process_data():
    print("Processing data")
    time.sleep(3)
    print("Data processed")

start_time = time.time()
fetch_data()
process_data()
end_time = time.time()
print(f"It took {end_time - start_time} seconds")

# With asynchronous
import asyncio

async def fetch_data():
    print("Fetching data")
    await asyncio.sleep(3)
    print("Data fetched")

async def process_data():
    print("Processing data")
    await asyncio.sleep(3)
    print("Data processed")

async def main():
    await asyncio.gather(fetch_data(), process_data())

start_time = time.time()
asyncio.run(main())
end_time = time.time()
print(f"It took {end_time - start_time} seconds")


# With synchronous 
import requests, time
def fetch_url(url):
    response = requests.get(url)
    print(f"Fetched {url} and it has {len(response.text)} characters")

start_time = time.time()
urls = ['https://example.org', 'https://httpbin.org', 'https://python.org']
[fetch_url(url) for url in urls]
end_time = time.time()
print(f"It took {end_time - start_time} seconds")


# With asynchronous
# I mentioned in the session we cant use requests library, but there is a way to use it:
    # Refer https://youtu.be/GpqAQxH1Afc?si=AfhHktqPEdMoo8Wa 

import asyncio, aiohttp

async def fetch_url(url):
    async with aiohttp.ClientSession() as session:
        async with session.get(url) as response:
            print(f"Fetched {url} and it has {len(await response.text())} characters")

async def main():
    urls = ['https://example.org', 'https://httpbin.org', 'https://python.org']
    tasks = [fetch_url(url) for url in urls]
    await asyncio.gather(*tasks)  # asyncio.gather(fetch_url(1), fetch_url(2),....)

start_time = time.time()
asyncio.run(main())
end_time = time.time()
print(f"It took {end_time - start_time} seconds")
