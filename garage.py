import time
import smtplib
import pifacedigitalio as p
import datetime

# Set PiFace outputs
pfd = p.PiFaceDigital()
# Door 1
pfd.output_pins[0].value = 1
# Door 2
pfd.output_pins[1].value = 1
# Back Door
pfd.output_pins[2].value = 1

# How long between messages. 900 = 15 minutes.
countTime = 900

# Start loop
while 1:
  time.sleep(1)

  # Set email information
  server = smtplib.SMTP( "smtp.gmail.com", 587 )
  server.starttls()
  server.login('emailaddress@gmail.com', 'password')
  # Garage email address
  FROM = "emailaddress@gmail.com"
  # Phone Numer
  TO = ["8125555555@txt.att.net"]

  # Set timestamp
  now = time.ctime()
  parsed = time.strptime(now)
  currentTime = time.strftime("%I:%M %p", parsed)

  # Garage Door 1
  if (pfd.input_pins[0].value == 0) :
    counter = 0
    door1 = 0
    door2 = 0
    door3 = 0

    # Time to count.
    while (pfd.input_pins[0].value == 0) and (counter < countTime):
      # While this door is open, check to see if other doors have opened.

      # Check Door 1
      if pfd.input_pins[0].value == 0:
        while door1 == 0:
          message = "\nGarage Door 1 is open at "
          msg = message + currentTime
          server.sendmail( FROM, TO, msg )
          door1 += 1
          time.sleep(1)

      # Check Door 2
      if pfd.input_pins[1].value == 0:
        while door2 == 0:
          message = "\nGarage Door 2 is open at "
          msg = message + currentTime
          server.sendmail( FROM, TO, msg )
          door2 += 1
          time.sleep(1)

      # Check Door 3
      if pfd.input_pins[2].value == 0:
        while door3 == 0:
          message = "\nGarage Back Door is open at "
          msg = message + currentTime
          server.sendmail( FROM, TO, msg )
          door3 += 1
          time.sleep(1)

      counter += 1
      time.sleep(1)

  # Garage Door 2
  if (pfd.input_pins[1].value == 0) :
    counter = 0
    door1 = 0
    door2 = 0
    door3 = 0

    # Time to count.
    while (pfd.input_pins[1].value == 0) and (counter < countTime):
      # While this door is open, check to see if other doors have opened.

      # Check Door 1
      if pfd.input_pins[0].value == 0:
        while door1 == 0:
          message = "\nGarage Door 1 is open at "
          msg = message + currentTime
          server.sendmail( FROM, TO, msg )
          door1 += 1
          time.sleep(1)

      # Check Door 2
      if pfd.input_pins[1].value == 0:
        while door2 == 0:
          message = "\nGarage Door 2 is open at "
          msg = message + currentTime
          server.sendmail( FROM, TO, msg )
          door2 += 1
          time.sleep(1)

      # Check Door 3
      if pfd.input_pins[2].value == 0:
        while door3 == 0:
          message = "\nGarage Back Door is open at "
          msg = message + currentTime
          server.sendmail( FROM, TO, msg )
          door3 += 1
          time.sleep(1)

      counter += 1
      time.sleep(1)

  # Garage Door 3
  if (pfd.input_pins[2].value == 0) :
    counter = 0
    door1 = 0
    door2 = 0
    door3 = 0

    # Time to count.
    while (pfd.input_pins[2].value == 0) and (counter < countTime):
      # While this door is open, check to see if other doors have opened.

      # Check Door 1
      if pfd.input_pins[0].value == 0:
        while door1 == 0:
          message = "\nGarage Door 1 is open at "
          msg = message + currentTime
          server.sendmail( FROM, TO, msg )
          door1 += 1
          time.sleep(1)

      # Check Door 2
      if pfd.input_pins[1].value == 0:
        while door2 == 0:
          message = "\nGarage Door 2 is open at "
          msg = message + currentTime
          server.sendmail( FROM, TO, msg )
          door2 += 1
          time.sleep(1)

      # Check Door 3
      if pfd.input_pins[2].value == 0:
        while door3 == 0:
          message = "\nGarage Back Door is open at "
          msg = message + currentTime
          server.sendmail( FROM, TO, msg )
          door3 += 1
          time.sleep(1)

      counter += 1
      time.sleep(1)
