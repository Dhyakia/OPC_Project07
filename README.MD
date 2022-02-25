# OPC_Project 07

The goal of this project is to make us of algorithm to fasten the execution of a program.


# Introduction

This program will take a .csv full of actions, with headers named: "name,cost,profit" and will return the best combination of actions for a capacity set in
```
MAX_COST = 500
```
This program is composed of two scripts:
1. bruteforce.py, who use a bruteforce algorithm
2. optimized.py, who use a greedy algorithm

---

## Requirements
* Python3 at https://www.python.org/downloads
* ... and that's it !
---

## Installation

### 1. Getting the code

Using the git tool or straight from the source.

#### Method git
```
mkdir mon_dossier
cd mon_dossier
git clone https://github.com/Dhyakia/OPC_Project04.git
```

#### Method Git desktop

1. Go [here](https://github.com/Dhyakia/OPC_Project04)
2. Click on "Code" (green button) and then "Open with GitHub Desktop"
3. Clone the file to desired location and you're done !

#### Method Manual
1. Go [here](https://github.com/Dhyakia/OPC_Project04)
2. Click on "Code" (green button) and then "Download Zip"
3. Un-zip the file and you're done !

### 2. Setting up a virtual environement
1. With the console command, navigate to the folder of instalation.
2. To create the virtual environement, enter this command :

   Windows : ```python3 -m venv c:\path\to\venv```

   MacOs/Linux : ```python3 -m venv venv```
3. Now that the virtual environoment is created, you need to activate it :

   Windows : ```cd venv/Scripts``` puis ```activate```
   
   MacOs/Linux : ```cd venv/bin``` puis ```activate```
   
4. You can now see the (venv) written at the very left of the line in the console command, signaling the success of the operation.
---

## Usage

Open a console and navigate to the location of the folder and enter:
For the brute force method:
```
python3 bruteforce.py
```
For the greedy method:
```
python3 optimized.py
```
---
# Futur viewing

This is the seventh out of thirteen python project.