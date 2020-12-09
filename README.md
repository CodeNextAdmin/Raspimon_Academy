
# Welcome

Welcome to your Raspimon on your Raspberry Pi. This quick guide will help you get started. 
 
## How to download code from GitHub
- Locate the green "Code" button on the right side of the page near the "About" section
   - **Note*: Use your touchscreen to navigate*
- Select that option and download zip
- Extract zip files to /home/pi/Desktop

## Add the Libraries
If you are not using this  [Raspimon Kit](https://www.pishop.us/product/raspimon-academy-kit/), then you will need to install a few Python libraries. After you download this repo, follow these steps in your Terminal (the Terminal Application is found on the main Menu bar):

Go to the Raspimon_Academy directory, which should be on your Desktop by entering this command after the $:
```bash
$ cd /home/pi/Desktop/Raspimon_Academy

```
Install the libraries with this script:
```bash
$ bash setup.sh

```

## What is in this repo?

The Raspimon folder on the Desktop of your Pi contains everything you need. There are four stage folders, each with different activities or training labs for your Raspimon. Begin at Stage1, however feel free to explore the other files, if you are curious. 

You will also find
- a raspimon_builder tool that can help you draw images with the joystick and save them in the LED_designs.txt file. 

- a LED_designs.txt file where any Raspimons you save with the builder will be exported.

- a colors.txt file that has several colors you can use. Not all colors look good on an RGB LED, so these have been selected for you. Feel free to add others, however all the Raspimons in this activites will use this color palette. This file is purely for reference. 

- a My_Raspimons folder where you will find a sample_raspimon.py file to show a very basic build and another emptier file called my_raspimon.py which you will use to build your first Raspimon.

- a Bestiary where you can get samples of Raspimon models to use or modify. The bestiary is in the form of a Python script that loops through all the examples, but you can also use the PDF version to copy and paste. 

## How to progress
Start with Stage 1, where you will begin by running welcome.py, your first script using Thonny, a Python editing tool that will also run all of your scripts.

Simply open the Stage1 Raspimon folder (/home/pi/Desktop/Raspimon_Academy-main/Stage1) and right-click 
on welcome.py. Choose Thonny Python IDE to open the file with.

Follow the labs at https://codenext.withgoogle.com/curriculum

Each lab has a Goals section to help you understand what Python concepts and Raspimon skills you are learning.

The Learn section is meant to guide your understanding of new concepts. Follow along and add the code to the appropriate file for the lab. Make sure to save the file often. 

The Try section is meant for you to apply some of the concepts you learned to that lab's Raspimon. 

Note, your own Raspimon in the My_Raspimon folder will also need to be updated as you go along, as you take in new features you decide to add. You do NOT have to add every interaction or skill to your my_raspimon.py file. You can also create other Raspimons that react in different ways. It's up to you. 


## Success
There are 3 main stages filled with skills for your Raspimon, and a fourth final stage to set you off on more adventures, but simply finishing the first stage will give you enough skills to breathe life into your Raspimon. They will be able to dance, move, walk, eat, and other gestures that can be stitched together. Your Raspimon will also be able to scroll text to the LED, giving you the power to tell stories with your Raspimon.

Stage 2 is mainly about adding interactivity to your Raspimon. The Sense Hat has sensors you can use to trigger events that your Raspimon can react to, like accelerometer, gyroscope and temperature sensors.

In Stage 3 you will be using Artificial Intelligence (AI) to detect facial gestures, objects and text with a camera, adding a whole new level of interactivity. These activities are built using Google Cloud Vision.

Stage 4 is a final stage where you can begin to explore other ideas and extensions to this set of activities.

You do not have to complete every lab, however some of the labs will have skills that you might need later on, so it is a good idea to check them all out, even if you don't intend to complete them.

## Stuck?
You can always check the examples branch of this repo for solutions to all of the labs. Simply switch to the examples branch with this button above, or  visit https://github.com/CodeNextAdmin/Raspimon_Academy/tree/examples


