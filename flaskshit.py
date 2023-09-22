from flask import Flask, request, jsonify

app = Flask (__name__)


if __name__ == "__main__ ":
    app.run(host='0.0.0.0', port=5000,debug=True)



@app.route('/llm', methods = ['POST'])
def processreq():
    try:
        data = request.get_json(force=True)
        query = data["query"]
        return llma(query)
    except:
        return jsonify("query failure")
    

def llma(query):
    # llm code goes here
    result = query;
    return result
    pass


