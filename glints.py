import requests
import bs4


params = {
    'keyword': 'python',
    'country': 'ID',
    'locationName': 'All Cities/Provinces'
}

headers = {
    'authority': 'td.doubleclick.net',

    'path': '/td/ga/rul?tid=G-FQ75P4PXDH&gacid=235625513.1724398817&gtm=45je48s0v886077570z877857200za200zb77857200\
            &dma=0&gcd=13l3l3l3l1l1&npa=0&pscdl=noapi&aip=1&fledge=1&frm=0&tag_exp=0&z=1917800471',

    'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,\
    application/signed-exchange;v=b3;q=0.7',

    'accept-encoding': 'gzip, deflate, br, zstd',
    'accept-language': 'en-US,en;q=0.9',

    'cookie': 'ar_debug=1; receive-cookie-deprecation=1; IDE=AHWqTUkpbwRlOj3GChX6-7_k-cls5VclqhhNzrMNEf4Ne6f\
    WMYJ2JAc_6rCAHkyQ3bE; DSID=AB_BQxkO1lrNHltJHl9UKgnKWNqUAjgow5Ij41PBb-Oz0kNUZoIF1gzg9cuD-Q7ljWNnmvP_Lm1BU2\
    FQGxYGoaNbJn-N8F42HuWrYb2tWyqDtoFnvcQC-cZWE9pS83HFqTN9Nk18xQrlaucKaVU4iPvCxa9XkHkG6Kla27k5TaYQo4QmBJm_AIJd\
    pOFytd9KlP3N6SQ8UCo-HOu1DwtF1JZqbIhRTwTbpLn1jHKailM-OcW9ZeThTPPCGO3ibsu4xghltM8h3z_YAXJkQ2d5OUfj9Sk22wJgy0\
    AVhJsAbx5FWFZXKExmWz4',

    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) \
    Chrome/128.0.0.0 Safari/537.36'
}

content = requests.get('https://glints.com/id/opportunities/jobs/explore?', params=params, headers=headers)
print(content.status_code)
# def get_all_items(query, location, start, page):
#     try:
#         content = requests.get('https://glints.com/')
#     except Exception:
#         return None
#
#     print(content.status_code)
