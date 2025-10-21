# ee250-lab6

## Team Members
- Rida Faraz (rfaraz)
- Leyaa George (chompers98)

## Reflection Questions
**1. Suppose you just cloned a repository that included one python file, my_first_file.py, and you now want to add a second file to your repository named
my_second_file.py which contains the following code and push it to Github.com. Code - print(“Hello World”). Complete the sequence of linux shell commands:**

`git clone git@github.com:my-name/my-imaginary-repo.git`

`cd my-imaginary-repo` 

`touch my_second_file.py`

`echo 'print("Hello World")' > my_second_file.py`

`git add .`

`git commit -m "second file added"`

`git push`

**2. Describe the workflow you adopted for this lab (i.e. did you develop on your VM and push/pull to get code to your RPi, did you edit files directly on your RPi, etc.). Are there ways you might be more efficient in the next lab (i.e. learning a text-based editor so you can edit natively on the RPi, understanding Git commands better, etc.)?**

The workflow that we used for this lab was directly editing code in the RPi terminal. We edited directly by using `nano`. It took us a while to adopt this workflow because both of us are used to editing in text editors, so in the future, familiarizing ourselves with the shell commands would help us later down the line. I think that this method was fine for this lab since there was only one GrovePi to test on, but in the future, it might be better to use Github for collaboration. This method was good for an individual, but it does not allow the other person to directly edit or get involved from a different device. 

**3. In the starter code, we added a 200 ms sleep. Suppose you needed to poll the ultrasonic ranger as fast as possible, so you removed the sleep function. Now, your code has just the function ultrasonicRead() inside a while loop. However, even though there are no other functions in the while loop, you notice there is a constant delay between each reading. Dig through the python library to find out why there is a constant delay. What is the delay amount? In addition, what communication protocol does the Raspberry Pi use to communicate with the Atmega328P on the GrovePi when it tries to read the ultrasonic ranger output using the `grovepi` python library?**

There is still a constant delay occurring because the ultrasonicRead() function itself contains a delay. Every time we call the function, there is already a delay() coded into it, and the delay amount is 60 ms. While examining the grovepi.cpp file further, we can see that the communication protocol that the Raspberry Pi uses to communicate with the Atmega328P on the GrovePi is I2C, or Inter-Integrated Circuit.

**4. When you rotate the Grove Rotary Angle Sensor, its analog output voltage changes between 0 V and 5 V and the GrovePi library reports integer values between 0 and 1023. Explain how this conversion works and why the Raspberry Pi cannot do it directly.**

This conversion is called an analog to digital conversion. The analog value, or the value observed in real time, is the voltage. The reason that this is analog, or continuous, is because this includes any value between 0V and 5V, including all intermediate decimal values. When we convert this to an integer, we have to take into account the memory limits. The GrovePi library supports 1,024 discrete values, or 2^10 values, so we have to mathematically convert the analog voltage reading to a digital decimal value. That is what is happening behind the scenes to actually make the conversion. It's a mathematical formula.

The reason that the RPi cannot do this conversion directly is because it doesn't have the ability to read analog values. It does not have the right sensors to recognize a continuous voltage value. This is why we need the GrovePi layer to extract that value and complete the analog to digital conversion. 

**5. Your LCD RGB Backlight screen is not displaying any text even though your code executes without errors. Describe how you would debug the issue. Include at least two terminal commands.**

I would briefly check the hardware to ensure that all the wires are connected properly and that all the right ports were defined. If the hardware checks do not work, I would try printing out values to see what is happening behind the scenes. It is possible that variables were set incorrectly and text was not even being initialized to print. If that doesn't work either, I would consider checking the connection. To see if these devices are even being connected to or recognized, I would use the command, `sudo i2cdetect -y 1`. This command will print out a schematic of I2C connections, and if I don't see the values associated with LCDs being printed, then I would try rebooting the I2C interface. In order to do the reboot, I would run `sudo raspi-config` and enable I2C. These two commands, combined, should help properly check the I2C interface, which is another plausible error that could arise when coding the LCD screens. 
