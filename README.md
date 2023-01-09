# kambanizeX

Offline client for Kambanize

## Goals

Kambanize is a kamban feature. Despites  its seemingly cool interface, the quality of the exposed html is, to say the minimum, highly questionable.

The fact that the exposed HTML is not semantically reasonable, keyboard navigation is poor and that several other issues exist has profound inpacts on a vast number of potential users, specially those who rely on assistive technology. 

As Kambanize's clients are corporations unlikely to change their kamban suppliers and as jobs of people who should (but don't) receive a workable, semantic, WCAG compatible html might very well be impacted to say the minimum, be at risk more realistically, we are trying to use their api to provide a wx based client which, hopefully, can give these people a chance to be productive in their kamban usage with Kambanuize.

## installation

We are using wx python.
At the moment, only Windows is oficially supported, though the application should run on *nix without problems.

You will need python 3.10.
We strongly recomend the 64 bits version, although you can perfectly try to use python versions as low as 3.7 and vary between 32 and 64 bits.
The only noticeable consequence of using other python versions is that perhaps wxwidgets will need to be built at installation time if there are no pre compiled binaries targetting your python version and architecture, and building wx widgets is not an easy task.  Generally, try to stick with python 3.10, 64 bits if you can. This will be easier.

1. Go to the project folder.
2. Execute venv. This will create and activate the virtual environment.
3. Make sure you have the most up to date pip. You should need to perform the command below only once per virtual environment, which means that you should do it as soon as you execute the venv script for the first time.  
python -m pip install --upgrade pip  
Remember that you don't need to execute this command everytime you activate the virtual environment, only the first time.
4. make a pip install -r requirements.txt

## Run

You will need a Kambanize Api key. This will be stored in a config file, which is not versioned in git.

You can run the application from sources executing KambanizeX in the project root directory. Do not forget to make the venv command to activate the virtual environment before running.