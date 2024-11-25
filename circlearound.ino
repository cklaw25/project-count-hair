volatile int YTIME;
volatile int XTIME;
volatile int ZTIME;
volatile boolean STAT;
volatile boolean TRY;
volatile boolean GOFORIT;
volatile int xaxis;
volatile int yaxis;
volatile int downaxis;
volatile boolean readyrecieved = false;
volatile int number1, number2;
volatile int xtravel, ytravel;
volatile boolean READYAGAIN;
//volatile int value1;
//volatile int value2;

void X1() {
  digitalWrite(3,HIGH);
  digitalWrite(2,HIGH);
  delayMicroseconds(XTIME);
  digitalWrite(2,LOW);
  delayMicroseconds(XTIME);
}

void X2() {
  digitalWrite(3,LOW);
  digitalWrite(2,HIGH);
  delayMicroseconds(XTIME);
  digitalWrite(2,LOW);
  delayMicroseconds(XTIME);
}

void X3() {
  digitalWrite(2,HIGH);
}

void Y1() {
  digitalWrite(9,LOW);
  digitalWrite(7,HIGH);
  digitalWrite(6,HIGH);
  digitalWrite(8,HIGH);
  delayMicroseconds(YTIME);
  digitalWrite(6,LOW);
  digitalWrite(8,LOW);
  delayMicroseconds(YTIME);
}

void Y2() {
  digitalWrite(9,HIGH);
  digitalWrite(7,LOW);
  digitalWrite(6,HIGH);
  digitalWrite(8,HIGH);
  delayMicroseconds(YTIME);
  digitalWrite(6,LOW);
  digitalWrite(8,LOW);
  delayMicroseconds(YTIME);
}

void Y3() {
  digitalWrite(6,HIGH);
  digitalWrite(8,HIGH);
}

void Z1() {
  digitalWrite(5,LOW);
  digitalWrite(4,HIGH);
  delayMicroseconds(ZTIME);
  digitalWrite(4,LOW);
  delayMicroseconds(ZTIME);
}

void Z2() {
  digitalWrite(5,HIGH);
  digitalWrite(4,HIGH);
  delayMicroseconds(ZTIME);
  digitalWrite(4,LOW);
  delayMicroseconds(ZTIME);
  //Z2 goes up and highest is 0
}

void Z3() {
  digitalWrite(4,HIGH);
}

void MOVING() {
  READYAGAIN = false;
  for (int i = 1; i <= downaxis; i = i+(1)) {
    Z1();
    //downaxis = downaxis - (1);
  }
  downaxis = 0;
  delay(2000);
  if (xtravel >= 0) {
    for (int i = 1; i <= xtravel; i = i + (1)) {
      X2(); //left max
      xaxis = xaxis + (1);
    }
  }
  if (xtravel < 0) {
    for (int i = 1; i <= (xtravel * (-1)); i = i + (1)) {
      X1(); //left max
      xaxis = xaxis - (1);
    }
  }
  if (ytravel >= 0) {
    for (int i = 1; i <= ytravel; i = i + (1)) {
      Y1(); //front max
      yaxis = yaxis + (1);
    }
  }
  if (ytravel < 0) {
    for (int i = 1; i <= (ytravel * (-1)); i = i + (1)) {
      Y2(); //back max
      yaxis = yaxis - (1);
    }
  }
  while (true) {
    Z2();
    downaxis = downaxis + (1);
    if (digitalRead(12) == false) {
      Z3();
      for (int i = 1; i <= 60; i = i + (1)) {
        Z1();
        downaxis = downaxis - (1);
      }
      Z3();
      break;
    }
  }
  Serial.print(xaxis);
  Serial.print(" ");
  Serial.print(yaxis);
  Serial.print(" ");
  Serial.println(downaxis);
  READYAGAIN = true;
}

void setup() {
  // put your setup code here, to run once:
  YTIME = 800;
  XTIME = 800;
  ZTIME = 800;
  STAT = true;
  TRY = false;
  GOFORIT = false;
  READYAGAIN = false;
  xaxis = 0;
  yaxis = 0;
  downaxis = 0;
  Serial.begin(9600);
  //Serial.setTimeout(1);
  pinMode(10, INPUT);
  pinMode(11, INPUT);
  pinMode(12, INPUT);
  pinMode(9, OUTPUT);
  pinMode(7, OUTPUT);
  pinMode(6, OUTPUT);
  pinMode(8, OUTPUT);
  pinMode(3, OUTPUT);
  pinMode(2, OUTPUT);
  pinMode(A2, INPUT);
  pinMode(A3, INPUT);
  pinMode(5, OUTPUT);
  pinMode(4, OUTPUT);
}

void loop() {
  while (STAT) {
    while (true) {
      Y2();
      if (digitalRead(10) == false) {
        Y3();
        for (int i = 1; i <= 1; i = i + (1)) {
          Y1();
        }
        Y3();
        break;
      }
    }
    while (true) {
      X2();
      if (digitalRead(11) == false) {
        X3();
        for (int i = 1; i <= 1; i = i + (1)) {
          X1();
        }
        X3();
        break;
      }
    }
    while (true) {
      Z2();
      if (digitalRead(12) == false) {
        Z3();
        for (int i = 1; i <= 450; i = i + (1)) {
          Z1();
        }
        Z3();
        break;
      }
    }
    for (int i = 1; i <= 1150; i = i + (1)) {
      X1(); //left max
      //xaxis = xaxis - (1);
    }
    STAT = false;
    Serial.print(xaxis);
    Serial.print(" ");
    Serial.print(yaxis);
    Serial.print(" ");
    Serial.println(downaxis);
    //TRY = true;
    break;
  }


  if (Serial.available() > 0){
    String input = Serial.readStringUntil('\n');
    int spaceIndex = input.indexOf(' ');
    if (spaceIndex != -1) {
      number1 = input.substring(0, spaceIndex).toInt();
      number2 = input.substring(spaceIndex+1).toInt();
      readyrecieved = true;
    }
    if (readyrecieved) {
      xtravel = number1;
      ytravel = number2;
      MOVING();
      readyrecieved = false;
    }
  }
}
