Portfolio 1: Project 1
======================

This package is built as a part of the CSC1034: Portfolia-1.

This is an animation of a panda bear with a camera revolving around it.
It has sights and sounds of a forest and also bear roars.
<br>It is poorly and inefficiently coded due to my inability to code and deal with python yet but it is still fun to 
mess with. 

####Details of functionality:

Type `python hello_world.py` to test and see some useful information about python version.

Type `python python2.0.py` to see a panda animation with a 
camera spinning around it.You can also hear forest sounds and 
the panda roaring.

You can play around with this program by executing the 
file with commands through the command line. <br> It uses argparse 
library to handle arguments and commands

You can execute commands by passing in arguments with appropriate keys. 
<br>The keys `--spinCamera` or `--sc` manage the spinning camera
<br>The keys `--animatePanda` or `--ap` manage panda animations

 *Note: All the keys above are optional and the default value for them is true if left unchanged through a command*
 
 Use the example below to format the commands you want to execute in the terminal or command line
>python python2.0.py --sc <True/False or Integer value> --ap <True/False or Integer value>

Integer value that is `>0` is considered positive
######Example commands
Type `python python2.0.py --sc 0 --ap true` in the command line and you will get an animated scene of a panda

If `python python2.0.py --sc false --ap false` is issued there will be no camera or panda animation. 

*Note: Panda sound wont play if it is not animated*

For more information use command:
>python python2.0.py -h



