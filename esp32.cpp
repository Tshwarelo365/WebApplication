#include <WiFi.h>
#include <HTTPClient.h>

const char* ssid = "LAPTOP-A99PS0B9 8004";
const char* password = "buhle365";
int User_Id = 221967575;

const char* serverName = "http://192.168.0.112:5000/add_data";

unsigned long previousMillis = 0;
const long interval = 10000; // 10 minutes (in milliseconds)

void setup() {
  Serial.begin(9600);  // You can change to 115200 if needed

  WiFi.begin(ssid, password);

  while (WiFi.status() != WL_CONNECTED) {
    delay(1000);
    Serial.println("Connecting to WiFi...");
  }

  Serial.println("Connected to WiFi");
}

void loop() {
  unsigned long currentMillis = millis();

  if (currentMillis - previousMillis >= interval) {
    previousMillis = currentMillis;

    float light_intensity = analogRead(34); // Assuming you're using pin 34 for the light sensor
    sendLightIntensity(light_intensity);
  }
}

void sendLightIntensity(float light_intensity) {
  if (WiFi.status() == WL_CONNECTED) {
    HTTPClient http;
    http.begin(serverName);
    http.addHeader("Content-Type", "application/json");

    String jsonPayload = "{\"User_Id\": " + String(User_Id) + ", \"light_intensity\": " + String(light_intensity, 2) + "}";

    int httpResponseCode = http.POST(jsonPayload);

    if (httpResponseCode > 0) {
      String response = http.getString();
      Serial.println(httpResponseCode);
      Serial.print("http responded");
      Serial.println(response);
    } else {
      Serial.print("Error on sending POST: ");
      Serial.println(httpResponseCode);
    }

    http.end();
  } else {
    Serial.println("Error in WiFi connection");
  }
}

