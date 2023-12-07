
from flask import Flask, render_template, request
#from text_summary import summarizer, get_text_from_link
from text_summary import textrank_summarizer, get_text_from_link

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/analyze', methods=['POST'])


def analyse():
    rawtext = request.form['rawtext']
    
  
    link = request.form.get('link', None)    # to check link if present
    
    if '://' in rawtext:
        rawtext = get_text_from_link(rawtext)
    
    percentage = int(request.form.get('percentage', 30) or 30) #using default value 30 when percent not provided
    
    summary, original_txt, len_orig_txt, len_summary = textrank_summarizer(rawtext, percentage)
    
    return render_template("summary.html", summary=summary, original_txt=original_txt,
                           len_orig_txt=len_orig_txt, len_summary=len_summary)

if __name__ == "__main__":
    app.run(debug=True)
