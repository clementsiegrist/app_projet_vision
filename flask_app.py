'''
https://stackoverflow.com/questions/59276105/how-can-i-add-images-to-flask
How can I add images to Flask?
https://www.analyticsvidhya.com/blog/2020/07/deploy-an-image-classification-model-using-flask/
<img src="{{ url_for('static', filename='image.jpg') }}" />
'''

from flask import Flask, render_template, redirect, url_for, render_template
app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def home():
    return render_template('/final.html') # template_folder=TEMPLATE_DIR, static_folder=STATIC_DIR)


if __name__ == '__main__':
    app.run(debug=True)