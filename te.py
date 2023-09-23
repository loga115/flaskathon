from flask import Flask, render_template, request, flash  # jsonif
from markupsafe import escape
app = Flask(__name__)


@app.route('/')
def homepage():
    return render_template('site.html')

@app.route('/submit', methods=['POST'])
def submit_form():
    if request.method == 'POST':
        # Get data from the form
        name = request.form['sending-party']
        reciev = request.form['recieving-party']
        rel = request.form['relation']
        doctype = request.form['document-type']
        details = request.form['details']

        # Create a dictionary with the form data
        data = {
            'sending-party': name,
            'recieving-party':reciev,
            'relation':rel,
            'document-type':doctype,
            'details':details
        }

        # Convert the dictionary to JSON
        # response_json = jsonify(data)
        return "Your name is: "+escape(name)+" and your recieving party is: "+escape(reciev)+" and your details is: "+escape(details)



if __name__ == '__main__':
    app.run(debug=True)

    
