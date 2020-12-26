import requests
from bs4 import BeautifulSoup


def get_jobs(word):
    headers = {
        'Accept-Encoding': 'gzip, deflate, sdch',
        'Accept-Language': 'en-US,en;q=0.8',
        'Upgrade-Insecure-Requests': '1',
        'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/56.0.2924.87 Safari/537.36',
        'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8',
        'Cache-Control': 'max-age=0',
        'Connection': 'keep-alive',
    }

    url = f"https://remoteok.io/remote-{word}-jobs"

    res = requests.get(url, headers=headers)
    soup = BeautifulSoup(res.text, "html.parser")

    table = soup.find("table", {"id": "jobsboard"})
    trs = table.find_all("tr", {"class": "job"})

    jobs = []

    for tr in trs:
        td = tr.find("td", {"class": "company"})

        title = td.find("h2", {"itemprop": "title"}).string
        company = td.find("h3", {"itemprop": "name"}).string
        location = td.find("div", {"class": "location"})
        if location:
            location = location.string
        else:
            location = ""
        link = f"https://remoteok.io/{td.find('a').get('href')}"

        jobs.append({"title": title, "company": company,
                     "location": location, "link": link})

    return jobs
