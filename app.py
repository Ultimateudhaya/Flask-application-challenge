import requests
from bs4 import BeautifulSoup
from flask import Flask,render_template, request

def get_url(url):
    req = requests.get(url)
    soup = BeautifulSoup(req.text, 'html.parser')

    urls = []
    for link in soup.find_all():
        a = link.get('href')
        if a != None and "https://" in a:
            urls.append(a)
    return urls

app = Flask(__name__,template_folder = 'client/templates')

@app.route('/', methods=["GET", "POST"])
def page():
    if request.method == "GET":
        return render_template('index.html')
    else:
        url = request.form["url"]
        links = get_url(url)
        return render_template('index.html',
                               li = links)



if __name__ == '__main__':
    app.run(debug=True)