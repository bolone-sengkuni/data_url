import aiohttp, asyncio, re
from bs4 import BeautifulSoup
import logging, aiofiles, time
import schedule

logging.basicConfig(
    format='%(asctime)s %(levelname)s - %(message)s',
    level=logging.INFO
)

FILE_URL = 'config.txt'
WORKING_PROXY = []

async def scrape_proxy(client, url):
    logging.info(f"Start {url.replace('https://raw.githubusercontent.com/', '').strip()}")
    async with client.get(url) as resp:
        res = await resp.text()
        return res.splitlines()


async def get_proxy():
    async with aiohttp.ClientSession() as client:
        result = await asyncio.gather(
            *[
                asyncio.ensure_future(
                    scrape_proxy(
                        client=client,
                        url=url
                    )
                ) for url in open(FILE_URL, 'r').readlines()
            ]
        )
        hasil_proxy = sum(result, [])
        return hasil_proxy


async def cek_proxy_lazada(client, proxies):
    headers = {
        "accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8",
        "accept-language": "id-ID,en-US;q=0.9",
        "cookie": f"utdid=zzzzz; hng=ID|id|IDR|360; la_darkmode_type=light",
        "host": "pages.lazada.co.id",
        "upgrade-insecure-requests": "1",
        "user-agent": "Mozilla/5.0 (Linux; U; Android 11; zh-CN; Redmi Note 7 Build/RQ3A.211001.001) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/69.0.3497.100 UWS/3.22.1.227 Mobile Safari/537.36 AliApp(LA/7.26.1) UCBS/2.11.1.1 TTID/600000@lazada_android_7.26.1 WindVane/8.5.0 1080X2134",
        "x-app-ver": "7.26.1",
        "x-appkey": "23867946",
        "x-requested-with": "com.lazada.android",
        "x-utdid": "zzzzz"
    }
    logging.info(f'Cek proxy {proxies}')
    try:
        async with client.get(
            'https://pages.lazada.co.id/wow/gcp/id/ug-newuser/nulp?source=homepage_free_buy&source=homepage_free_buy&item=7447890484,7400654849,7099562384&itemId=7447890484,7400654849,7099562384&price_max=120000.0&price_min=0.0&spm=a211g0.home.combinedNUC.voucher1&laz_event_id=422_1685126965416_75405',
            proxy=f'http://{proxies}',
            headers=headers
            # timeout=60
        ) as resp:
            assert resp.status == 200
            text_resp = await resp.text()
            soup  = BeautifulSoup(text_resp, "html.parser")
            text  = soup.body.get_text(separator=u' ')
            cek   = text.strip().split('Ambil')[0]
            WORKING_PROXY.append(proxies)
            logging.info(f'{proxies} || Live')
    except:
        logging.error(f'{proxies} || Die')
        pass


async def main():
    list_proxy = await get_proxy()
    async with aiohttp.ClientSession() as client:
        await asyncio.gather(
            *[ 
            asyncio.ensure_future(
                    cek_proxy_lazada(
                        client=client,
                        proxies=p
                    )
                ) for p in list_proxy
            ]
        )
        print(WORKING_PROXY)
    async with aiofiles.open('data.txt', 'w') as w:
        for p in WORKING_PROXY:
            await w.write(p + '\n')




start = time.time()
asyncio.run(
    main()
)
end = time.time()
hasil = end - start
print(f'{hasil} detik')