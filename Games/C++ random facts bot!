#include <iostream>
#include <cstdlib>  // for rand() and srand()
#include <ctime>    // for time()

using namespace std;

int main()
{
    // Initialize the random seed
    srand(time(NULL));

    // Create an array of facts
    const int NUM_FACTS = 10;
    string facts[NUM_FACTS] = {
        "The earth is roughly 4.5 billion years old.",
        "The sun is a star.",
        "The human heart has four chambers.",
        "The capital of France is Paris.",
        "Water boils at 100 degrees Celsius.",
        "The chemical symbol for oxygen is O.",
        "The tallest mountain in the world is Mount Everest.",
        "The speed of light is 299,792,458 meters per second.",
        "The element with atomic number 1 is hydrogen.",
        "The currency of Japan is the Japanese yen."
    };

    // Pick a random fact and print it to the user
    int factIndex = rand() % NUM_FACTS;
    cout << "Fact of the day: " << facts[factIndex] << endl;

    return 0;
}
To use this program, save it to a file (e.g. fact-of-the-day.cpp), compile it with a C++ compiler (e.g. g++ fact-of-the-day.cpp -o fact-of-the-day), and then run the compiled binary (e.g. ./fact-of-the-day). The program will output a random fact from the array every time it is run. Note that you can add or remove facts from the array as needed to customize the program.
