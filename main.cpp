#include <iostream>
#include <connect2server.cpp>

using namespace std;

/*
    Hymns done:
    2025-04-27 - 31, 101, NULL, 90
    2025-05-04 - 23, 105, NULL, 1004
*/

int main(int argc, char const *argv[])
{ 
    try 
    {
        cout << "How many hymns do you want to select?" << endl;
        short hymnsNeeded; 
        cin >> hymnsNeeded;
        
        if (hymnsNeeded < 1 || hymnsNeeded > 4) 
        {
            throw invalid_argument("Please select between 1 and 4 hymns.");
        }
    }

    // Catch section 

    
    




    
    return 0;
}

