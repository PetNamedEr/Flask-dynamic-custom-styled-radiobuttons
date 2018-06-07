from flask import Flask, request, render_template, redirect
from wtforms import Form, RadioField
app = Flask(__name__)

class RadioFieldForm(Form):
    value = RadioField('', choices=[])

    def setChoices(self,listOfChoices):
        self.value.choices.clear()
        i = 0
        for choice in listOfChoices:
            self.value.choices.append((i,choice))
            i += 1

    def getChoices(self):
        return self.value.choices

customRadioFieldChoices = ["Paul","John","Ringo","George"]

@app.route('/', methods=['GET', 'POST'])
def index():
    form = RadioFieldForm(request.form)
    if request.method == 'GET':
        form.setChoices(customRadioFieldChoices)
        return render_template('CustomRadioButtons.html',form=form)
    if request.method == 'POST':
        #return str(request.form)
        return "You chose: " + request.form['chosenValue']

@app.route('/addNewRadioFieldChoice', methods=['GET', 'POST'])
def addCustomRadioFieldChoice():
    customRadioFieldChoices.append(request.form['newChoice'])
    return redirect('/')
