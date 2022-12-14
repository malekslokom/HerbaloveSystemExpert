from flask import Flask, render_template, request
import KnowledgeEngine
app = Flask(__name__)
global inputUser
inputUser={}
@app.route("/", methods=["GET", "POST"])
def hello_world():
    predictionResult={"Crop":""}
    if request.method == "POST":
        if request.form.get('action1') == 'VALUE1':
            print(request.form)
            inputUser["Humidity"]=float(request.form["Humidity"])
            inputUser["Rainfall"]=float(request.form["Rainfall"])
            inputUser["Potassium"]=float(request.form["Potassium"])
            inputUser["Phosphorous"]=float(request.form["Phosphorous"])
            inputUser["Nitrogen"]=float(request.form["Nitrogen"])
            inputUser["Temperature"]=float(request.form["Temperature"])
            print(inputUser)
            predictionResult=KnowledgeEngine.main(inputUser)
            print(predictionResult)
            return render_template('result.html',result=predictionResult)
    return render_template('index.html')


if __name__=="__main__":
    app.run(debug=True)