#include <iostream>  // Include the input/output stream library

int main() {
    // Declare variables for weight and height
    float weight, height, bmi;

    // Ask the user for their weight
    std::cout << "Enter your weight in kilograms: ";
    std::cin >> weight;

    // Ask the user for their height
    std::cout << "Enter your height in meters: ";
    std::cin >> height;

    // Calculate BMI
    bmi = weight / (height * height);

    // Display the result
    std::cout << "Your BMI is: " << bmi << std::endl;

    // Provide a simple interpretation of the BMI
    if (bmi < 18.5) {
        std::cout << "You are underweight." << std::endl;
    } else if (bmi < 24.9) {
        std::cout << "You have a normal weight." << std::endl;
    } else if (bmi < 29.9) {
        std::cout << "You are overweight." << std::endl;
    } else {
        std::cout << "You are obese." << std::endl;
    }

    return 0;  // Indicate that the program ended successfully
}

