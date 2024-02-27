// Get the display element
let display = document.getElementById('display');

// Function to append value to the display
function appendToDisplay(value) {
    display.value += value;
}

// Function to clear the display
function clearDisplay() {
    display.value = '';
}

// Function to calculate the expression
function calculate() {
    try {
        // Evaluate the expression and display the result
        display.value = eval(display.value);
    } catch (error) {
        // Handle any errors and display "Error" on the display
        display.value = 'Error';
    }
}
