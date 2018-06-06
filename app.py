from flask import Flask, request, render_template
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

@app.route('/')
def hello_world():
    radioFieldChoices = ["Paul","John","Ringo","George"]
    form = RadioFieldForm(request.form)
    form.setChoices(radioFieldChoices)
    return render_template('CustomRadioButtons.html',form=form)
