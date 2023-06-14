
#include <iostream>
#include <time.h>
#include <Arduino.ino>

void setup() {
    Serial.begin(9600);

}

void loop(){
    if(Serial.available()){


           // assigning value to string s
    std::string command = Serial.readString();
  
    const int length = command.length();
  
    // declaring character array (+1 for null terminator)
    char* comm_array = new char[length + 1];
    
    // copying the contents of the
    // string to char array
    strcpy(comm_array, command.c_str());
  
    for (int i = 0; i < length; i++)
    {
        std::cout << comm_array[i];
    }

    switch (comm_array[0])
    {
    case 'l': // move linke seite
        if(comm_array[1] == '+'){
            // öffnen 
        }else if (comm_array[1] == '-'){
            // schließen 
        }
        else{
            // stop
        }
        break;
    case 'r': // move rechte seite
        if(comm_array[1] == '+'){
            // öffnen 
        }else if (comm_array[1] == '-'){
            // schließen 
        }
        else{
            // stop
        }
        break;
    case 'm': // move mitte
        if(comm_array[1] == '+'){
            // rechts 
        }else if (comm_array[1] == '-'){
            // links 
        }
        else{
            // stop
        }
        break;

    case 's':// set/run
        run((int)comm_array[1]);
        break;
    
    default:
        break;
    }

    }
}
void run(int blende){

}
void moveBlende(){
    
}
void rotate(){
    
    Serial.println(analogRead(A0));
}
