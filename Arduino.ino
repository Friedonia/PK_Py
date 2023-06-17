#include <time.h>
int countRealais = 4;
int relais[] = {1,2,3,4};
void setup() {
    for(int i=0; i<countRealais; i++){
        pinMode(relais[i],OUTPUT); // set relay pins as output
        digitalWrite(relais[i],HIGH); // turn relay off
    }
    Serial.begin(9600);

}

void loop(){
    if(Serial.available()){


    // assigning value to string s
    String command = Serial.readString();
  
    int str_len = command.length();
  
    // declaring character array (+1 for null terminator)
    char comm_array[str_len + 1];
    
    command.toCharArray(comm_array, str_len);
    
    switch (comm_array[0])
    {
    case 'l': // move linke seite
        if(comm_array[1] == '+'){
             digitalWrite(relais[0],HIGH);
             digitalWrite(relais[1],LOW);
             delay(1000);
        }else if (comm_array[1] == '-'){
             digitalWrite(relais[0],LOW);
             digitalWrite(relais[1],HIGH);
             delay(1000);        
        }else{
             digitalWrite(relais[0],LOW);
             digitalWrite(relais[1],LOW);
             delay(1000);        
        }
        break;
    case 'r': // move rechte seite
        if(comm_array[1] == '+'){
             digitalWrite(relais[2],HIGH);
             digitalWrite(relais[3],LOW);
             delay(1000);
        }else if (comm_array[1] == '-'){
             digitalWrite(relais[2],LOW);
             digitalWrite(relais[3],HIGH);
             delay(1000);        
        }else{
             digitalWrite(relais[2],LOW);
             digitalWrite(relais[3],LOW);
             delay(1000);        
        }
        
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
    // A0 ist Ultraschall und A1 ist Rotations Sensor
    Serial.println(analogRead(A0)+ "/" + analogRead(A1));

}
void run(int blende){
  
  for(int i =0 ; i < blende; i++){
      moveBlenden();
   }
}
void moveBlenden(){
    
}
void rotate(){
    
}
void rest(){
    
}
