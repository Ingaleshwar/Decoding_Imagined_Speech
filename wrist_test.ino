#include <Servo.h>

Servo shoulder;
Servo elbow;
Servo elbow_pivot;
Servo wrist;

void setup()
{
    Serial.begin(9600);
    shoulder.attach(9);
    elbow.attach(10);
    elbow_pivot.attach(11);
    wrist.attach(6);
}

void loop()
{
    shoulder.write(0);
    elbow.write(90);
    elbow_pivot.write(0);
    wrist.write(90);

    Serial.println("Input");

    while (Serial.available() == 0){
    }

    int Choice = Serial.parseInt();

    switch (Choice)
    {
    case 1:
        shoulder.write(30);
        elbow.write(135);
        elbow_pivot.write(0);
        wrist.write(45);
        delay(6000);

        break;
    case 2:
        shoulder.write(45);
        elbow.write(70);
        elbow_pivot.write(90);
        wrist.write(90);
        delay(2000);
        for (int shake = 0; shake <= 2; shake += 1)
        {
            for (int angle = 0; angle <= 85; angle += 1)
            {
                elbow.write(angle);
                delay(10);
            }

            for (int angle = 85; angle >= 70; angle -= 1)
            {
                elbow.write(angle);
                delay(10);
            }
        }
        delay(1500);
        break;
    case 3:
        shoulder.write(90);
        elbow.write(0);
        elbow_pivot.write(0);
        wrist.write(0);
        delay(4000);

    default:
        shoulder.write(0);
        elbow.write(0);
        elbow_pivot.write(0);

        break;
    }
}

