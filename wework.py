import requests
from bs4 import BeautifulSoup


def get_jobs(word):
    url = f"https://weworkremotely.com/remote-jobs/search?utf8=%E2%9C%93&term={word}"

    res = requests.get(url)
    soup = BeautifulSoup(res.text, "html.parser")

    section = soup.find("section", {"class": "jobs"})
    article = section.find("article")
    ul = article.find("ul")

    lists = ul.find_all("li")
    jobs = []

    for job in lists[:-1]:
        title = job.find("span", {"class": "title"}).string
        company = job.find("span", {"class": "company"}).string
        location = job.find("span", {"class": "region"}).string
        link = f"https://weworkremotely.com/{job.get('href')}"

        jobs.append({"title": title, "company": company,
                     "location": location, "link": link})

    return jobs
