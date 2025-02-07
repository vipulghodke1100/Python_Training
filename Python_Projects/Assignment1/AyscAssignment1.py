import json
import aiohttp
import asyncio
from bs4 import BeautifulSoup
import pandas as pd
import time

start = time.time()

async def Scrap(search_engine, comp, keyword, pages_to_extract):
    article = []
    count = 0
    match search_engine:
        case 'Google':
            base_url = 'https://news.google.com/search?q='
            url = f"{base_url}{comp} {keyword} "
            async with aiohttp.ClientSession() as session:
                async with session.get(url) as response:
                    soup = BeautifulSoup(await response.text(), 'html.parser')
                    results = soup.find_all('article', {'class': 'IFHyqb DeXSAc'})
                    
                    for result in results:
                        author = result.find('div', {'class': 'a7P8l'})
                        title = result.find('a', {'class': 'JtKRv'})
                        time = result.find('time', {'class': 'hvbAAd'})['datetime']
                        link = result.find('a', {'class': 'JtKRv'})['href']
                        if count < pages_to_extract * 10:
                            count += 1
                            article.append({'Search String': f'{comp} {keyword}', 'Search Engine': 'Google',
                                             'link': f"www.news.google.com{link}", "title": title.text, "timestamp": time, "Media": author.text})
                        else:
                            break
            print(len(article))
            return article

        case 'Yahoo':
            base_url = 'https://news.search.yahoo.com/search?q='
            url = f"{base_url}{comp} {keyword}&b{pages_to_extract * 10 + 1}"
            async with aiohttp.ClientSession() as session:
                async with session.get(url) as response:
                    soup = BeautifulSoup(await response.text(), 'html.parser')
                    results = soup.find_all('div', {'class': 'dd NewsArticle'})
                    for result in results:
                        author = result.find('span', {'class': 's-source fw-l'})
                        title = result.find('h4', {'class': 's-title fz-20 lh-m fw-500 ls-027 mt-8 mb-2'})
                        time = result.find('span', {'class': 's-time fz-14 lh-18 fc-dustygray fl-l mr-4'})
                        link_div = result.find('h4', {'class': 's-title fz-20 lh-m fw-500 ls-027 mt-8 mb-2'})
                        link = link_div.find('a')['href']
                        article.append({'Search String': f'{comp} {keyword}', 'Search Engine': 'Yahoo', 'link': f"{link}",
                                         "title": title.text, "timestamp": time.text, "Media": author.text})
            print(len(article))
            return article

        case 'Bing':
            base_url = 'https://www.bing.com/news/search?q='
            url = f"{base_url}{comp} {keyword}"
            async with aiohttp.ClientSession() as session:
                async with session.get(url) as response:
                    soup = BeautifulSoup(await response.text(), 'html.parser')
                    results = soup.find_all('div', {'class': 'news-card newsitem cardcommon'})
                    for result in results:
                        media = result['data-author']
                        title = result['data-title']
                        time_span = result.find('span', {'aria-label': True})
                        time = time_span['aria-label']
                        link = result['data-url']
                        if count < pages_to_extract * 10:
                            count += 1
                            article.append({'Search String': f'{comp} {keyword}', 'Search Engine': 'Bing', 'link': link,
                                             'title': title, 'timestamp': time, 'Media': media})
                        else:
                            break
            print(len(article))
            return article


async def load_json(path):
    with open(path, 'r') as file:
        config = json.load(file)
    
    companies = config.get('companies', [])
    keywords = config.get('keywords', [])
    pages_to_extract = config.get('pages_to_extract', 1)
    return companies, keywords, pages_to_extract

async def main():
    companies, keywords, pages_to_extract = await load_json('./config.json')
    search_engines = ['Google', 'Yahoo', 'Bing']

    tasks = []
    for comp in companies:
        for keyword in keywords:
            for ser_eng in search_engines:
                task = Scrap(ser_eng, comp, keyword, pages_to_extract)
                tasks.append(task)
    
    results = await asyncio.gather(*tasks)
    # print(len(results))
    all_articles = [item for sublist in results for item in sublist]
    convert_to_csv(all_articles)

def convert_to_csv(articles, filename='scraped_news.csv'):
    df = pd.DataFrame(articles)
    print(df.shape)
    df.to_csv(filename, index=False)
    print(f"CSV file saved as: {filename}")    

if __name__ == '__main__':
    asyncio.run(main())
    print(time.time() - start)
