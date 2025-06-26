/**
 * @license
 * SPDX-License-Identifier: Apache-2.0
*/

const numberDisplay = document.getElementById('number-display');
const generateBtn = document.getElementById('generate-btn');

if (generateBtn && numberDisplay) {
  generateBtn.addEventListener('click', () => {
    // Generate a random number between 1 and 99
    const randomNumber = Math.floor(Math.random() * 99) + 1;
    
    // Animate the number change
    numberDisplay.style.opacity = '0';
    setTimeout(() => {
        numberDisplay.textContent = randomNumber.toString();
        numberDisplay.style.opacity = '1';
    }, 150);
  });
}