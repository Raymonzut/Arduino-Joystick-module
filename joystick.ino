const int x = A0;
const int y = A1;
//const int button = 2;
const int potMax = 700;
const float xOffset = -0.05;
const float yOffset = 0;

void setup() {
  Serial.begin(9600);
  pinMode(x, INPUT);
  pinMode(y, INPUT);
  //pinMode(button, INPUT);

}

void loop() {
  // Axis values are between 0 and potMax, convert to standard -1:1, do not forget to adjust the potMax to your Joystick
  float xAxis = (analogRead(x) - potMax / 2.0) / (potMax / 2.0) - xOffset;
  float yAxis = (analogRead(y) - potMax / 2.0) / (potMax / 2.0) - yOffset;
  //bool pressed = digitalRead(button);


  String output = String(xAxis) + "," + String(yAxis);
  //Will send the output over Serial
  Serial.println(output);

}
