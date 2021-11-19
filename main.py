from flask import render_template,request
import requests, json
from forms import Search
from bs4 import BeautifulSoup
from config import scrapper

@scrapper.route('/',methods=['GET','POST'])
def index():
    form = Search()
    if request.method == "POST":
        query = request.form.get("search")
        # count = form.count.data
        query = query.replace(' ', '+')
        final_arr = []
        while True:
            results = query_search(query, count=0)
            final_arr += results
            if (len(final_arr) > 0):
                break
        print("final count: ", len(final_arr))
        return render_template('index.html',form=form, arr=final_arr)
    return render_template('index.html', form=form)

@scrapper.route('/api/search',methods=['GET','POST'])
def api():
    query = request.args.get('k')
    # count = request.args.get('count')
    # count = int(count)
    query = query.replace(' ', '+')
    final_arr = []
    while True:
        results = query_search(query, count=0)
        final_arr += results
        if (len(final_arr) > 0):
            break
    result_json = json.dumps(final_arr)
    print("final count: ",len(final_arr))
    return result_json

def query_search(query, count):
    results = []
    URL = f"https://shopping.google.com/search?q={query}&start={count}"
    USER_AGENT = "Mozilla/5.0 (Macintosh; Intel Mac OS X 10.14; rv:65.0) Gecko/20100101 Firefox/65.0"
    headers = {"user-agent": USER_AGENT}
    resp = requests.get(URL, headers=headers)
    if resp.status_code == 200:
        soup = BeautifulSoup(resp.content, "html.parser")
        for g in soup.find_all('article'):
            anchors = g.find_all('a')
            arr = g.find_all('div')
            try:
                link = anchors[0]['href']
                title = arr[4].find('div').text
                prices = anchors[0].find('div').find('div').find('div').text
                img = arr[2].find('img')['src']
                item = {
                    "title": title,
                    "prices": prices,
                    "link": link,
                    "image": img
                }
                results.append(item)
            except Exception as e:
                print(e)
    return results


if __name__ == '__main__':
    scrapper.run(debug=True)

