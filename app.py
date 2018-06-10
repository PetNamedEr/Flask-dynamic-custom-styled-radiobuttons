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

customRadioFieldChoicesVertical = ["Paul","John","Ringo","George"]
customRadioFieldChoicesHorizontal = ["Ben Linus","Claire Littleton","Jack Shepard","Hugo Reyes","Kate Austen","Karen DeGroot",\
                            "Desmond Hume","Juliet Burke","The Man in Black","Claudia"]

@app.route('/', methods=['GET', 'POST'])
def index():
    horizontalForm = RadioFieldForm(request.form)
    verticalForm = RadioFieldForm(request.form)
    if request.method == 'GET':
        horizontalForm.setChoices(customRadioFieldChoicesHorizontal)
        verticalForm.setChoices(customRadioFieldChoicesVertical)
        return render_template('CustomRadioButtons.html',horizontalForm=horizontalForm,verticalForm=verticalForm)
    if request.method == 'POST':
        return render_template('Results.html',horizontalResult=request.form['chosenValueHorizontal'],
                                verticalResult=request.form['chosenValueVertical'])

@app.route('/addNewRadioFieldChoiceHorizontal', methods=['GET', 'POST'])
def addNewRadioFieldChoiceHorizontal():
    customRadioFieldChoicesHorizontal.append(request.form['newChoiceHorizontal'])
    return redirect('/')

@app.route('/addNewRadioFieldChoiceVertical', methods=['GET', 'POST'])
def addNewRadioFieldChoiceVertical():
    customRadioFieldChoicesVertical.append(request.form['newChoiceVertical'])
    return redirect('/')
