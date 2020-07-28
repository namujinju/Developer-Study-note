from bs4 import BeautifulSoup
import requests

URL = "https://www.indeed.com/jobs?q=python&limit=50"
LIMIT = 50


def extract_indeed_pages():
    result = requests.get(URL)
    soup = BeautifulSoup(result.text, "html.parser")

    pagination = soup.find("div", {"class": "pagination"})
    links = pagination.find_all("a")

    spans = []
    for link in links[:-1]:
        spans.append(int(link.string))

    max_page = spans[-1]
    return max_page


def extract_job(html):

    title = html.find("h2").find("a")["title"]
    company = html.find("span", {"class": "company"})
    if company.find("a") != None:  # 링크가 있음
        company = company.find("a").string
    else:
        company = company.string
    company = company.strip()
    location = html.find("div", {"class": "recJobLoc"})["data-rc-loc"]
    job_id = html["data-jk"]
    link = f"https://www.indeed.com/viewjob?jk={job_id}"
    return {"title": title, "company": company, "location": location, "link": link}


def extract_indeed_jobs(last_page):
    jobs = []
    for page in range(last_page):
        print(f"Scrapping page {page}")
        result = requests.get(URL)
        soup = BeautifulSoup(result.text, "html.parser")

        clickcards = soup.find_all(
            "div", {"class": "jobsearch-SerpJobCard"})
        for clickcard in clickcards:
            job = extract_job(clickcard)
            jobs.append(job)

    return jobs
