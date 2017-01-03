Video clips
===========

Typing in a terminal
--------------------

![terminal](/images/terminal.png)

The console in [`terminal.py`](terminal.py) is modified from Glumpy's gloo-terminal.py example. It will read whatever is in the local file `commands.txt`, which must be created first. To record as mp4, add the flag --record and your desired output file name.

```
python terminal.py --record my-terminal-video.mp4
```

To make the visualization for typing slowly in the terminal, write the text into another file and use the [`slowtyper.py`](slowtyper.py) script to pipe into the `commands.txt` file. The following command, for example, will type "look i'm typing" into the terminal.

```
python slowtyper.py typing.txt
```

For a fast response, like an error message, just add an echo command.

```
python slowtyper.py typing.txt && echo "no i'm typing" >> commands.txt
```

Creating entropy visualization
------------------------------

![entropy](/images/create-entropy.png)

The viz in [`create-entropy.py`](create-entropy.py) is modified from Glumpy's collection-point.py example for a black background.

```
python create-entropy.py --record my-entropy-video.mp4
```

Creating order visualization
----------------------------

![entropy](/images/create-order.png)

The viz in [`create-order.py`](create-order.py) is essentially the same as the entropy example, except I round the locations of the points so that they appear on a grid.

```
python create-order.py --record my-order-video.mp4
```

Audio clips
===========
