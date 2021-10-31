from flask import render_template,request
import requests, json
from bs4 import BeautifulSoup
from config import scrapper

@scrapper.route('/',methods=['GET','POST'])
def index():
    if request.method == "POST":
        query = request.form["search"]
        query = query.replace(' ', '+')
        results = query_search(query)
        # final_arr = []
        # while True:
            # final_arr += results
            # if (len(list) > 100):
            #     break
        return render_template('index.html', arr=results)
    return render_template('index.html')

@scrapper.route('/api',methods=['GET','POST'])
def api():
    query = request.args.get('search')
    count = request.args.get('count')
    query = query.replace(' ', '+')
    # final_arr = []
    # while True:
    results = query_search(query)
    # final_arr += results
    # if (len(list) > 100):
    #     break
    result_json = json.dumps(results)
    return result_json

def query_search(query):
    results = []
    URL = f"https://shopping.google.com/search?q={query}"
    USER_AGENT = "Mozilla/5.0 (Macintosh; Intel Mac OS X 10.14; rv:65.0) Gecko/20100101 Firefox/65.0"
    headers = {"user-agent": USER_AGENT}
    resp = requests.get(URL, headers=headers)
    print(resp)
    if resp.status_code == 200:
        soup = BeautifulSoup(resp.content, "html.parser")
        for g in soup.find_all('article'):
            anchors = g.find_all('a')
            arr = g.find_all('div')
            link = anchors[0]['href']
            prices = anchors[0].find('div').find('span').text
            title = arr[4].find('div').text
            img = arr[2].find('img')['src']
            item = {
                "prices": prices,
                "link": link,
                "title": title,
                "image": img
            }
            results.append(item)
    return results


if __name__ == '__main__':
    scrapper.run(debug=True)

