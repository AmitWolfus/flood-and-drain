import RPi.GPIO as GPIO

relay_pin = -1
is_running = True


def init(pin_number):
  GPIO.setmode(GPIO.BOARD)
  relay_pin = pin_number
  GPIO.setup(relay_pin, GPIO.OUT)
  GPIO.output(relay_pin, GPIO.HIGH)
  is_running = False


def start():
  GPIO.output(relay_pin, GPIO.LOW)
  is_running = True


def stop():
  GPIO.output(relay_pin, GPIO.HIGH)
  is_running = False


def cleanup():
  GPIO.cleanup()