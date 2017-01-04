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

Galaxy zoom visualization
-------------------------

![galaxy](/images/galaxy-zoom.png)

The galaxy visualization in [`galaxy-zoom.py`](galaxy-zoom.py) is modified from Glumpy's galaxy.py example to zoom in to a wee white dot and then create a galaxy spinning at an angle and requires local access to the `galaxy` directory distributed with that example.

```
python galaxy-zoom.py --record my-galaxy-video.mp4
```

Earth zoom out visualization
----------------------------

![galaxy](/images/earth-viz.png)

The earth zoom out visualization in [`earth-viz.py`](earth-viz.py) is modified from Glumpy's earth.py example to use colors I like better and get rid of the capital labels and markers. While recording, you can use your mouse to zoom in and move around the globe.

```
python earth-viz.py --record my-earth-video.mp4
```

Brain visualization
-------------------

![galaxy](/images/brain-viz.png)

The brain visualization in [`brain-viz.py`](brain-viz.py) is just Glumpy's brain.py example modified to show a white background instead of the default black.

```
python brain-viz.py --record my-brain-video.mp4
```

Audio clips
===========

Creating entropy music
----------------------

The [`create-entropy-music.py`](create-entropy-music.py) script is the [generate melodies example from Pyo](https://github.com/belangeo/pyo#examples) modified to record a .wav file. Some example generated output can be found in the [`entropy.wav`](entropy.wav) file.

Other data
==========

Galaxy NGC 4258
---------------

![ngc 4258](/images/ngc-4258.png)

This is a 3-color image I made of the galaxy NGC 4258 with U, B, and R band imaging data from my thesis work using the Kitt Peak 4-meter Mosaic instrument. If you use it, please credit me (Maria Patterson) and consider citing [my dissertation](https://scholar.google.com/citations?view_op=view_citation&hl=en&user=x1kZj8MAAAAJ&citation_for_view=x1kZj8MAAAAJ:YsMSGLbcyi4C).

Dwarf planet Ceres
------------------

| Ceres first image             | Ceres later image             |
|-------------------------------|-------------------------------|
| ![ceres1](/images/ceres1.png) | ![ceres2](/images/ceres2.png) |

These images are made from .fits files from the following query for data on Ceres from the [Near Earth Object (NEO) Survey Search Tool](http://sbntools.psi.edu/neosearch/TargetQuery/form.action): http://sbntools.psi.edu/neosearch/TargetQuery/results.action?startDate=19960417&endDate=20030311&targetName=ceres
