### Alexandros Florides ###

import urllib.request, requests, json
from requests.auth import HTTPBasicAuth
from flask import Flask, render_template , request, make_response, jsonify, flash, redirect, url_for
import os

app = Flask(__name__)
# applying random secret key to app
app.secret_key = os.urandom(24)

# unique list id
listID = "99e10beca5f9e4eed14875b8d50d4302"
# unique api id
apiID = "GqtlOln5vbv3T45V80JJkVK3zAAekhhDivEP6RZjQIMnopCMaFZJ32lt0k1BL84ND2Sb31kw8gQvXLumvQtf0AeOyp04e/wbl4uBLiDHK8h1sW7xNfrAww9Pso32HVTkqdp1Q1+o6eJCGroR6LoTHA=="

# get request with basic authentication header to access the campaign monitor api
r = requests.get('https://api.createsend.com/api/v3.2/lists/'+listID+'/active.json', auth=(apiID, ''))

cont = r.json()
# dumps the json object into an element
json_str = json.dumps(cont)

# load the json to a string
resp = json.loads(json_str)

subscriber = {}

# extract an element in the response
for idx, r in enumerate(resp['Results']):
  name = resp['Results'][idx]['Name']
  email = resp['Results'][idx]['EmailAddress']
  subscriber[email] = name


@app.route("/", methods=['GET', 'POST'])
def home(subscriber=subscriber):
    if request.method =='POST': 
        # data received from the submitted form
        full_name = request.form.get('Full_Name')
        email_address = request.form.get('Email_Address')
        x = {'EmailAddress': email_address, 'Name': full_name, "ConsentToTrack":"Unchanged", "State":"Active"}
        # post request with basic authentication and passing appropriate data to add new subscriber
        res = requests.post('https://api.createsend.com/api/v3.2/subscribers/'+listID+'.json', 
            auth=(apiID, ''), 
            json=x)
        cont = res.json()
        json_str = json.dumps(cont)
        resp = json.loads(json_str)
        # sendind messages to python using flash method
        if res.ok:
            flash("Subscriber added successfuly!")
        else:
            flash(resp["Message"])
        # redirect to the home function (itself)
        return redirect(url_for("home"))
    
    # get request with basic authentication header to access the campaign monitor api
    r = requests.get('https://api.createsend.com/api/v3.2/lists/'+listID+'/active.json', auth=(apiID, ''))

    cont = r.json()
    json_str = json.dumps(cont)
    resp = json.loads(json_str)

    subscriber = {}

    # extract an element in the response
    for idx, r in enumerate(resp['Results']):
        name = resp['Results'][idx]['Name']
        email = resp['Results'][idx]['EmailAddress']
        subscriber[email] = name

    # open template.html file with subscriber parameter using render_template method
    return render_template("template.html", subscriber=subscriber)
    
if __name__ == "__main__":
    # run app with debug enabled to see any potential problems that may occur
    app.run(debug=True)
    

### Alexandros Florides ###