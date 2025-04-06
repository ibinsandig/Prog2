from machine import Pin

# Configure D1 (GPIO5) as an output pin
transistor = Pin(5, Pin.OUT)

# Configure D2 (GPIO2) as an output pin for an LED
led = Pin(2, Pin.OUT)  # Example: D2 (GPIO2) for an LED

# Set the initial state of the transistor (off)
transistor.off()

# Set the initial state of the LED (off)
led.off()