function setInitValueOnPageLoad()
{
  var radioButtonChoices = document.getElementsByName('usersChoice');
  radioButtonChoices[radioButtonChoices.length - 1].checked = 1;

  setAnswerValue(radioButtonChoices.length - 1)
}

function setAnswerValue(userSelectedRadioButtonIndex)
{
  var radioButtonChoices = document.getElementsByName('usersChoice');
  document.getElementById('chosenValue').value = radioButtonChoices[userSelectedRadioButtonIndex].value;
}
