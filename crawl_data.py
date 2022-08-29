import requests
import sqlite3


def get_jobs(page):
    token = "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"
    url = 'https://api.github.com/repos/awesome-jobs/vietnam/issues?page=2&q=is%3Aissue+is%3Aopen'.format(page)
    resp = requests.get(url, headers={'Authorization': 'token {}'.format(token)})
    data = resp.json()
    return data


def main():
    page = 1
    my_id = 1
    while True:
        jobs = get_jobs(page)
        if jobs != []:
            for job in jobs:
                conn = sqlite3.connect("db.sqlite3")
                c = conn.cursor()
                title = job['title']
                detail = job['body']
                c.execute('INSERT INTO job_job VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)', (my_id, title, detail, job['created_at'], job['updated_at'], job['id'], "", "", "", "", "", "", "", "OPEN"))
                conn.commit()
                conn.close()
                my_id += 1
        else:
            break
        page += 1


if __name__ == "__main__":
    main()
