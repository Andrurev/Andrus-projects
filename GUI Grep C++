#include <iostream>
#include <string>
#include <stdio.h>  // for popen() and pclose()
#include <stdlib.h>  // for exit()
#include <FL/Fl.H>  // for the FLTK library
#include <FL/Fl_Window.H>  // for the FLTK window
#include <FL/Fl_Input.H>  // for the FLTK input field
#include <FL/Fl_Button.H>  // for the FLTK button
#include <FL/Fl_Output.H>  // for the FLTK output field

using namespace std;

// Function prototypes
void search_cb(Fl_Widget* w, void* p);

// Global variables
Fl_Input *patternInput;
Fl_Input *fileInput;
Fl_Output *outputField;

int main(int argc, char *argv[])
{
    // Create the main window
    Fl_Window *window = new Fl_Window(400, 200);

    // Create the input fields and button
    patternInput = new Fl_Input(100, 10, 280, 25, "Pattern:");
    fileInput = new Fl_Input(100, 45, 280, 25, "File:");
    Fl_Button *searchButton = new Fl_Button(140, 80, 100, 25, "Search");

    // Set the callback for the button
    searchButton->callback(search_cb);

    // Create the output field
    outputField = new Fl_Output(10, 115, 380, 75);

    // Show the main window and run the application
    window->end();
    window->show(argc, argv);
    return Fl::run();
}

// Callback function for the search button
void search_cb(Fl_Widget* w, void* p)
{
    // Get the pattern and file from the input fields
    string pattern = patternInput->value();
    string file = fileInput->value();

    // Use popen() to run the grep command and store the output in a string
    string command = "grep " + pattern + " " + file;
    FILE *pipe = popen(command.c_str(), "r");
    if (!pipe) exit(1);
    char buffer[128];
    string result = "";
    while (!feof(pipe)) {
        if (fgets(buffer, 128, pipe) != NULL)
            result += buffer;
    }
    pclose(pipe);

    // Set the output field to the result of the grep command
    outputField->value(result.c_str());
}
