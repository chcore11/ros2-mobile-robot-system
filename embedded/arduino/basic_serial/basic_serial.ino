String input = "";

void setup() {
  Serial.begin(115200);
  Serial.println("[ARDUINO] Ready");
}

void loop() {
  while (Serial.available() > 0) {
    char c = Serial.read();

    if (c == '\n') {
      input.trim();

      if (input == "forward") {
        Serial.println("[ACK] FORWARD");
      } 
      else if (input == "stop") {
        Serial.println("[ACK] STOP");
      } 
      else if (input == "left") {
        Serial.println("[ACK] LEFT");
      } 
      else if (input == "right") {
        Serial.println("[ACK] RIGHT");
      } 
      else {
        Serial.print("[ACK] UNKNOWN: ");
        Serial.println(input);
      }

      input = "";
    } else {
      input += c;
    }
  }
}