# Assignment: Async API Logger 

# Task: Build an Asynchronous API Request Logger using Decorators & Asyncio 

# Scenario: 
# You are developing a Python application that fetches data from multiple APIs 
# concurrently using asyncio. You need to log each API request using a decorator to 
# track:  Start time, End time, API URL and Execution time
 
# Requirements: 
# 1) Create a decorator named log_execution_time that: 
# • Logs the start time before making an API request. 
# • Logs the end time and total execution time after the request completes. 

# 2) Use asyncio and aiohttp to: 
# • Install aiohttp library 
# • Check aiohttp documentation: https://docs.aiohttp.org/en/stable/ 
# • Fetch data from multiple APIs concurrently. 
# • Use async def and await to handle API requests asynchronously. 


# 3)  Fetch data from at least 3 sample APIs 
# • Check dummy API from https://jsonplaceholder.typicode.com 
# • Use following API links to fetch data: 
# o https://jsonplaceholder.typicode.com/users/6 
# o https://jsonplaceholder.typicode.com/users/4 
# o https://jsonplaceholder.typicode.com/todos/19


import time
import asyncio , aiohttp

def dcrt_log_execution(fn):
    def wrapper(*args):
        api_url=args[0]
        start=time.time()
        print(f"API URL: {api_url}")
        print(f"Start Time:{start}")
        data=fn(api_url)
        end=time.time()
        print(f"End time: {end}")
        print(f"Total execution time: {end-start}")
        print(data)
        return data
    return wrapper


@dcrt_log_execution
async def get_Data_from_url(api_url):
    async with aiohttp.ClientSession() as session:
        async with session.get(api_url) as response:
            print(f'Fetched_{api_url} and data: {await response.text()}')
            await response.text()
       
async def main():
    urls=["https://jsonplaceholder.typicode.com/users/6","https://jsonplaceholder.typicode.com/users/4", "https://jsonplaceholder.typicode.com/todos/19"]
    data=[get_Data_from_url(api_url) for api_url in urls]
    await asyncio.gather(*data)
    
def fetch_data():
    asyncio.run(main())
    
fetch_data()