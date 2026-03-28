String input = "";

const int LED_FORWARD = 2;
const int LED_LEFT    = 3;
const int LED_BACK    = 4;
const int LED_RIGHT   = 5;

void setup() {
  Serial.begin(115200);

  pinMode(LED_FORWARD, OUTPUT);
  pinMode(LED_LEFT, OUTPUT);
  pinMode(LED_BACK, OUTPUT);
  pinMode(LED_RIGHT,OUTPUT);

  Serial.println("[ARDUINO] Ready");
}
void resetLEDs() {
  digitalWrite(LED_FORWARD, LOW);
  digitalWrite(LED_LEFT, LOW);
  digitalWrite(LED_BACK, LOW);
  digitalWrite(LED_RIGHT, LOW);
}


void loop() {
  while (Serial.available() > 0) {
    char c = Serial.read();

    if (c == '\n') {
      input.trim();
      resetLEDs();

      if (input == "forward") {
        digitalWrite(LED_FORWARD, HIGH);
        Serial.println("[ACK] FORWARD");
      } 
      else if (input == "back") {
        digitalWrite(LED_BACK, HIGH);
        Serial.println("[ACK] STOP");
      } 
      else if (input == "left") {
        digitalWrite(LED_LEFT, HIGH)
        Serial.println("[ACK] LEFT");
      } 
      else if (input == "right") {
        digitalWrite(LED_RIGHT, HIGH);
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