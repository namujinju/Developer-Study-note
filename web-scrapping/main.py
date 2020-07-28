from indeed import extract_indeed_pages, extract_indeed_jobs

last_indeed_pages = extract_indeed_pages()
# last_indeed_pages = 20

indeed_jobs = extract_indeed_jobs(last_indeed_pages)
print(indeed_jobs)
