#include <iostream>
#include <map>
#include <cstdlib>
#include <ctime>

using namespace std; 

int main()
{
    map<int, int> hymnMap; //Create map of hymns

    int totaHymns = 20; //Total number of hymns
    int initiaHymn = 101;

    for ( size_t i = 1; i <= totaHymns; i++)
    {
        hymnMap[i] = initiaHymn;
        initiaHymn++;
    }

    char filename[] = "nouns.txt";
    FILE* fp = fopen(filename, "r");

    FILE* fp2 = fopen(filename, "a");

    //-------------------This is prop wrong
    int done = 0;
    while (done != 1)
    {
        //Randomly Select a key 
        srand(static_cast<unsigned>(time(0)));
        int randKey = 1 + (rand() % 20);

        //Check to see key has already been chosen
        if (fscanf (fp, "%d") != randKey)
        {
            cout << hymnMap[randKey] <<endl;

            char str[10];
            sprintf(str, "%d", randKey); // convert integer string
            fputs(str, fp2);

            done = 1;
        }
    }
    
    return 0;
}