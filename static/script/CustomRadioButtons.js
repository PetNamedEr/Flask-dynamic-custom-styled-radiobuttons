function setInitValueOnPageLoad()
{
  var radioButtonChoicesHorizontal = document.getElementsByName('usersChoiceHorizontal');
  radioButtonChoicesHorizontal[radioButtonChoicesHorizontal.length - 1].checked = 1;

  setAnswerValueHorizontal(radioButtonChoicesHorizontal.length - 1)

  var radioButtonChoicesVertical = document.getElementsByName('usersChoiceVertical');
  radioButtonChoicesVertical[radioButtonChoicesVertical.length - 1].checked = 1;

  setAnswerValueVertical(radioButtonChoicesVertical.length - 1)
}

function setAnswerValueHorizontal(userSelectedRadioButtonIndex)
{
  var radioButtonChoices = document.getElementsByName('usersChoiceHorizontal');
  document.getElementById('chosenValueHorizontal').value = radioButtonChoices[userSelectedRadioButtonIndex].value;
}

function setAnswerValueVertical(userSelectedRadioButtonIndex)
{
  var radioButtonChoices = document.getElementsByName('usersChoiceVertical');
  document.getElementById('chosenValueVertical').value = radioButtonChoices[userSelectedRadioButtonIndex].value;
}
