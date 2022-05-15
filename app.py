import wikipedia
from flask import Flask

app = Flask(__name__)

@app.route("/", methods=['GET'])
def default():
    return "HELLO WORLD"

@app.route("/summary/<string:page_name>/", defaults={"num_sentences": None})
@app.route("/summary/<string:page_name>/<int:num_sentences>", methods=['GET'])
def get_wiki_data(page_name, num_sentences):
    summary = None
    if not num_sentences:
        try:
            summary = wikipedia.summary(page_name, auto_suggest=False)
        except Exception as e:
            print("Error has occured: ", e)
    else:
        # get specific number of sentences for the summary if num_sentences is provided
        try:
            summary = wikipedia.summary(page_name,sentences=num_sentences, auto_suggest=False)
        except Exception as e:
            print("Error has occured: ", e)

    # get the url for the company:
    url = None
    try:
        url = wikipedia.page(page_name, auto_suggest=False).url
    except Exception as e:
            print("Error has occured: ", e)
    print({"summary": summary, "link": url})
    return {"summary": summary, "link": url}


if __name__ == "__main__":
	get_wiki_data("St Louis Blues", 4)
