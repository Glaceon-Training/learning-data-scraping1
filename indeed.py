import json
import requests
import bs4
import os
import pandas as pd
# import random


url = 'https://www.indeed.com/jobs?'
site = 'https://www.indeed.com'
params = {
    'q': 'python developer',
    'l': 'newyork',
    'from': 'searchOnDesktopSerp',
    'vjk': '6501e2f8f2ea1fde'
}
headers = {
    'authority': 'www.indeed.com',

    'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,'
    'application/signed-exchange;v=b3;q=0.7',

    'accept-encoding': 'gzip, deflate, br, zstd',

    'accept-language': 'en-US,en;q=0.9',

    'cookie': 'CTK=1hlkhu4f9jtdp800; indeed_rcc=CTK; FPID=FPID2.2.po5Z7yrhF3KuCRQDjyps0bulZKO%2Fxeg7qBEjED1PxII%3D.'
              '1706865697; CO=ID; _gcl_au=1.1.517032670.1717495456; LOCALE=en_ID; CO=ID; '
              'SESSION_START_TIME=1720604317229; '
              'SESSION_ID=1i2e04lhdgr7n800; OptanonAlertBoxClosed=2024-07-10T10:27:20.724Z; '
              'IRF=7YXfKDzcx1JT-QT4QnjgSCTX1d1rHCmgUBv0ioKVwdk7GWopHeLElQ==; SESSION_END_TIME=1720607681167; '
              '_ga_5KTMMETCF4=GS1.1.1720607228.1.1.1720608187.60.0.0; LC="co=ID&hl=en_ID"; '
              'RF="O4UqZrkZHCPbiP8RwX6gJN1PYGeTmrV171WUHFb0vXOweiLCmKVGzpjwouu0ikI8SyoDYSDsT6yc6w_67irgFg=="; '
              '_ga=GA1.1.381890904.1706865697; LOCALE=en_ID; CSRF=nhhpIwOKA8H2XKtA09SBGRz418fmLF07; '
              'INDEED_CSRF_TOKEN=Oq2QSHblRtZzDPECPp4yD2jkdR9vlsnt; _cfuvid=w1NuAA6R.N.Az_5jP8BVbmscerDitSVoptpglXbclIk-'
              '1724983809228-0.0.1.1-604800000; '
              'FPLC=SIWIicbfNreeWD5O4fczG1ThepUdFikqcMlixZnKJgGOS23M7LlLZNkum0iQuU6qM9j707'
              'uopr39midm2NPVscPJfH01fgSgZXQm%2F1qzrvuiFJLVOsxJEKhn4EiaAw%3D%3D; '
              'ENC_CSRF=79OX2Psvms3GQeZwo7t4xVaYA0WcDH9c; '
              'SHARED_INDEED_CSRF_TOKEN=RTqNXyptRjDjxjFLTFzjxcMprn2Gf1hl; '
              'MICRO_CONTENT_CSRF_TOKEN=B89UToUH0FSBi5Hb51nYUaghDZpTjJkw; SURF=mowx3XeeyONYCQI6mWQffvxAg3QUHx6z; '
              'PPID=""; __cf_bm=.0Nv5SPR7cBxpZPl.RuDgtBdDrYJLC.G2TrkVPV8b1g-1724986925-1.0.1.1-vAfwA9uWZIUvx7yuKjF_'
              'k8DWzdtqzSqTvMBD3d99RBaRYsW4S2X.Ezx0afDjUIvngH8OqQD1xm3Kimgb.i18Cg; gonetap=closed; '
              'PREF="TM=1724987727345:L=newyork"; LV="LA=1724987727:LV=1707118279:CV=1724987727:TS=1706865660"; '
              'indeed_rcc="LOCALE:PREF:LV:CTK:CO:RQ"; RQ="q=python+developer&l=newyork&ts=1724987760197:q=Suitability&'
              'l=&ts=1707120344509:q=Research&l=&ts=1707119920496:q=Suitability+Analyst&l=&ts=1707118514112&'
              'pts=1707113979189:q=environmental+analyst&l=&ts=1707118449126:q=environment+Analyst&l=&ts=1707118429355:'
              'q=hydrographer&l=&ts=1706865660434"; OptanonConsent=isGpcEnabled=0&'
              'datestamp=Fri+Aug+30+2024+10%3A15%3A54+GMT%2B0700+(Western+Indonesia+Time)&version=202210.1.0&'
              'isIABGlobal=false&hosts=&consentId=8dde0ab8-1649-4071-b7e2-cad0b59bf3e3&interactionCount=2&'
              'landingPath=NotLandingPage&groups=C0001%3A1%2CC0002%3A0%2CC0003%3A0%2CC0004%3A0%2CC0007%3A0&'
              'AwaitingReconsent=false&geolocation=%3B; JSESSIONID=3C1D0A9DB6A8B9B8A942CFD5051BA4EB; '
              '_ga_LYNT3BTHPG=GS1.1.1724986303.11.1.1724987763.0.0.1095128859; PTK=tk=1i6gkgnhp2bkr00g&'
              'type=jobsearch&subtype=topsearch',

    # 'cache-control': 'max-age=0',

    'priority': 'u=0, i',

    'referer': 'https://www.indeed.com/jobs?q=python+developer&l=newyork&from=searchOnHP&vjk=6501e2f8f2ea1fde',

    'sec-ch-ua': '"Chromium";v="128", "Not;A=Brand";v="24", "Google Chrome";v="128"',
    'sec-ch-ua-mobile': '?0',
    'sec-ch-ua-platform': '"Windows"',
    'sec-fetch-dest': 'document',
    'sec-fetch-mode': 'navigate',
    'sec-fetch-site': 'same-origin',
    'sec-fetch-user': '?1',
    'upgrade-insecure-requests': '1',

    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko)'
                  'Chrome/128.0.0.0 Safari/537.36'
}

# user_agent_list = [
#     'Mozilla/5.0 (iPad; CPU OS 12_2 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Mobile/15E148',
#     'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko)'
#     'Chrome/99.0.4844.83 Safari/537.36',
#     'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko)'
#     'Chrome/99.0.4844.51 Safari/537.36'
# ]
# response = requests.get(url, params=params, headers={'User-Agent': random.choice(user_agent_list)})
# print(response.status_code)


response = requests.get(url, params=params, headers=headers)


def get_total_pages(query, location):
    params = {
        'q': query,
        'l': location,
        'from': 'searchOnDesktopSerp',
        'vjk': '6501e2f8f2ea1fde'
    }
    response = requests.get(url, params=params, headers=headers)

    try:
        os.mkdir('temp')
    except FileExistsError:
        pass

    with open('temp/res.html', 'w+') as outfile:
        outfile.write(response.text)
        outfile.close()

    total_pages = []

    # Scraping Steps
    soup = bs4.BeautifulSoup(response.text, 'html.parser')
    pagination = soup.find('ul', 'css-1g90gv6 eu4oa1w0')
    pages = pagination.find_all('li')
    for page in pages:
        total_pages.append(page.text)

    total = int(max(total_pages))
    return total


def get_all_items(query, location, start, page):
    params = {
        'q': query,
        'l': location,
        'start': start,
        'from': 'searchOnDesktopSerp',
        'vjk': '6501e2f8f2ea1fde'
    }
    response = requests.get(url, params=params, headers=headers)

    with open('temp/res.html', 'w+') as outfile:
        outfile.write(response.text)
        outfile.close()

    soup = bs4.BeautifulSoup(response.text, 'html.parser')

    # Scraping Process
    contents = soup.find_all('div', 'mosaic-zone')

    # pick items
    # * title
    # * company name
    # * company address

    jobs_list = []
    for item in contents:
        title = item.find('h2', 'jobTitle css-198pbd eu4oa1w0').text
        company = item.find('div', 'css-1qv0295 e37uo190')
        company_name = company.text
        company_address = item.find('div', 'css-1p0sjhy eu4oa1w0')

    # Sorting data
    data_dict = {
        'title': title,
        'company name': company_name,
        'company address': company_address
    }
    jobs_list.append(data_dict)

    # Writing JSON
    try:
        os.mkdir('json_result')
    except FileExistsError:
        pass

    with open(f'json_result/{query}_in_{location}_page_{page}.json', 'w+') as json_data:
        json.dump(jobs_list, json_data)

    return jobs_list


def create_document(dataframe, filename):  # Create CSV
    try:
        os.mkdir('data_result')
    except FileExistsError:
        pass

    df = pd.DataFrame(dataframe)
    df.to_csv(f'data_result/{filename}.csv', index=False)
    df.to_excel(f'data_result/{filename}.xlsx', index=False)

    # Data Created Notice
    print(f'File {filename}.csv and {filename}.xlsx successfully created')


def run():
    query = input('Enter Your Query: ')
    location = input('Enter Your Location: ')

    total = get_total_pages(query, location)
    counter = 0

    final_result = []
    for page in range(total):
        page += 1
        counter += 10
        final_result =+ get_all_items(query, location, counter, page)

    # Formatting Data
    try:
        os.mkdir('reports')
    except FileExistsError:
        pass

    with open('reports/{}.json'. format(query), 'w+') as final_report:
        json.dump(final_result, final_report)

    print('JSON data successfully created')

    # Create Document
    create_document(final_report, query)


if __name__ == '__main__':
    run()
