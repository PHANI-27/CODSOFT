const display = document.getElementById('display');
const buttons = document.querySelectorAll('.btn');
let currentInput = '';
let resetNext = false;

buttons.forEach(button => {
  button.addEventListener('click', () => {
    const value = button.getAttribute('data-value');

    if (button.id === 'clear') {
      currentInput = '';
      display.textContent = '0';
    } else if (button.id === 'equal') {
      try {
        currentInput = eval(currentInput).toString();
        display.textContent = currentInput;
        resetNext = true;
      } catch (e) {
        display.textContent = 'Error';
        currentInput = '';
      }
    } else {
      if (resetNext) {
        currentInput = '';
        resetNext = false;
      }
      currentInput += value;
      display.textContent = currentInput;
    }
  });
});
