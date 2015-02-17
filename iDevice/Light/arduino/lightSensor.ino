void setup() {
    Serial.begin(9600);
}

void loop() {
    int value = analogRead(A0);
    
    if(Serial.available()) {
        char ch = Serial.read();
        Serial.println(ch);
        if (ch == '0') {
            Serial.println("LED ON!");
        } else if (ch == '1') {
                  Serial.println("LED OFF!");
        } else {
            Serial.println("Nothing!");
        }
    }

    Serial.println(value);
    Serial.println("value read!");
    delay(5000);
}