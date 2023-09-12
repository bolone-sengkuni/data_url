SOURCES = [
    {
        "id": "free-proxy-list.net",
        "url": "https://free-proxy-list.net",
        "method": "GET",
        "parser": {
            "pandas": {
                "table_index": 0,
                "ip": "IP Address",
                "port": "Port",
                "combined": None,
            },
        }
    },
    {
        "id": "us-proxy.org",
        "url": "https://www.us-proxy.org",
        "method": "GET",
        "parser": {
            "pandas": {
                "table_index": 0,
                "ip": "IP Address",
                "port": "Port",
                "combined": None,
            },
        }
    }
    ,
    {
        "id": "proxydb.net",
        "url": "http://proxydb.net",
        "method": "GET",
        "parser": {
            "pandas": {
                "table_index": 0,
                "ip": None,
                "port": None,
                "combined": "Proxy",
            },
        }
    },
    {
        "id": "free-proxy-list.com",
        "url": "https://free-proxy-list.com/?page=&port=&type%5B%5D=http&type%5B%5D=https&up_time=0&search=Search",
        "method": "GET",
        "parser": {
            "pandas": {
                "table_index": 1,
                "ip": "IP Address",
                "port": "Port",
                "combined": None,
            },
        }
    },
    {
        "id": "proxy-list.download",
        "url": "https://www.proxy-list.download/HTTP",
        "method": "GET",
        "parser": {
            "pandas": {
                "table_index": 0,
                "ip": "IP Address",
                "port": "Port",
                "combined": None,
            },
        }
    },
    {
        "id": "vpnoverview.com",
        "url": "https://vpnoverview.com/privacy/anonymous-browsing/free-proxy-servers",
        "method": "GET",
        "parser": {
            "pandas": {
                "table_index": 0,
                "ip": "IP address",
                "port": "Port",
                "combined": None,
            },
        }
    },
    {
        "id": "proxylist.geonode.com",
        "url": "https://proxylist.geonode.com/api/proxy-list?limit=300&page=1&sort_by=lastChecked&sort_type=desc&protocols=http,https",
        "method": "GET",
        "parser": {
            "json": {
                "data": "data",
                "ip": "ip",
                "port": "port",
            },
        }
    },
    {
        "id": "proxyscrape.com",
        "url": "https://api.proxyscrape.com/v2/?request=displayproxies&protocol=http&timeout=10000&country=all&ssl=all&anonymity=all",
        "method": "GET",
        "parser": {
            "txt": {},
        }
    },
    {
        "id": "github.com/clarketm/proxy-list",
        "url": "https://raw.githubusercontent.com/clarketm/proxy-list/master/proxy-list-raw.txt",
        "method": "GET",
        "parser": {
            "txt": {},
        }
    },
    {
        "id": "github.com/monosans/proxy-list",
        "url": "https://raw.githubusercontent.com/monosans/proxy-list/main/proxies/http.txt",
        "method": "GET",
        "parser": {
            "txt": {},
        }
    },
    {
        "id": "github.com/TheSpeedX/PROXY-List",
        "url": "https://raw.githubusercontent.com/TheSpeedX/PROXY-List/master/http.txt",
        "method": "GET",
        "parser": {
            "txt": {},
        }
    },
    {
        "id": "Bardiafa/Proxy-Checker/main/good.txt",
        "url": "https://raw.githubusercontent.com/Bardiafa/Proxy-Checker/main/good.txt",
        "method": "GET",
        "parser": {
            "txt": {},
        }
    },
    {
        "id": "ALIILAPRO/Proxy/main/http.txt",
        "url": "https://raw.githubusercontent.com/ALIILAPRO/Proxy/main/http.txt",
        "method": "GET",
        "parser": {
            "txt": {}
        }
    },
    {
        "id": "parserpp/ip_ports/main/proxyinfo.txt",
        "url": "https://raw.githubusercontent.com/parserpp/ip_ports/main/proxyinfo.txt",
        "method": "GET",
        "parser": {
            "txt": {}
        }
    },
    {
        "id": "mm-dream-team/http-proxy-scraper/main/docs/data.txt",
        "url": "https://raw.githubusercontent.com/mm-dream-team/http-proxy-scraper/main/docs/data.txt",
        "method": "GET",
        "parser": {
            "txt": {}
        }
    },
    {
        "id": "mertguvencli/http-proxy-list/main/proxy-list/data.txt",
        "url": "https://raw.githubusercontent.com/mertguvencli/http-proxy-list/main/proxy-list/data.txt",
        "method": "GET",
        "parser": {
            "txt": {}
        }
    },
    {
        "id": "Bardiafa/Proxy-Leecher/main/proxies-IR.txt",
        "url": "https://raw.githubusercontent.com/Bardiafa/Proxy-Leecher/main/proxies-IR.txt",
        "method": "GET",
        "parser": {
            "txt": {}
        }
    },
    {
        "id": "zuoxiaolei/proxys/main/proxys/proxys.txt",
        "url": "https://raw.githubusercontent.com/zuoxiaolei/proxys/main/proxys/proxys.txt",
        "method": "GET",
        "parser": {
            "txt": {}
        }
    },
    {
        "id": "UptimerBot/proxy-list/master/proxies/http.txt",
        "url": "https://raw.githubusercontent.com/UptimerBot/proxy-list/master/proxies/http.txt",
        "method": "GET",
        "parser": {
            "txt": {}
        }
    },
    {
        "id": "saschazesiger/Free-Proxies/master/proxies/new.txt",
        "url": "https://raw.githubusercontent.com/saschazesiger/Free-Proxies/master/proxies/new.txt",
        "method": "GET",
        "parser": {
            "txt": {}
        }
    },
    {
        "id": "Anonym0usWork1221/Free-Proxies/main/proxy_files/http_proxies.txt",
        "url": "https://raw.githubusercontent.com/Anonym0usWork1221/Free-Proxies/main/proxy_files/http_proxies.txt",
        "method": "GET",
        "parser": {
            "txt": {}
        }
    }
]


