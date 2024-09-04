import requests
import bs4
import os

description = 'To get commodities data from tradingeconomics.com'

headers = {
    'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) \
    Chrome/128.0.0.0 Safari/537.36'
}

# content = requests.get('https://tradingeconomics.com/', headers=headers)
# print(content.status_code)


def data_extract():
    try:
        content = requests.get('https://tradingeconomics.com/', headers=headers)
    except Exception:
        return None
    print(content.status_code)
    # content = requests.get('https://tradingeconomics.com/', headers=headers)

    # try:
    #     os.mkdir('temp_trade')
    # except FileExistsError:
    #     pass
    #
    # with open('temp_trade/res.html', 'w+') as outfile:
    #     outfile.write(content.text)
    #     outfile.close()
    # if content.status_code == 200:
    #     soup = bs4.BeautifulSoup(content.text, 'html.parser')
    #     scrap = soup.find('table', {'class': 'table-1043302008 table table-hover table-striped table-heatmap'})
    #     # scrap = scrap.findChildren('th')
    #     # title = scrap.text
    #     print(scrap)

        # extract = dict()
        # extract['title'] = title


# def show_data(result):
#     if result is None:
#         print('No Data Available')
#         return
#     print(f'Title = {result['title']}')
#
#
# if __name__ == '__main__':
#     result = data_extract()
