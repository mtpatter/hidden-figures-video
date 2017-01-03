# -----------------------------------------------------------------------------
# Modified by Maria Patterson
# From glumpy/examples/collection-point.py which is
# Copyright (c) 2009-2016 Nicolas P. Rougier. All rights reserved.
# Distributed under the (new) BSD License.
# -----------------------------------------------------------------------------
import numpy as np
from glumpy import app
from glumpy.graphics.collections import PointCollection

window = app.Window(1024, 1024, color=(0, 0, 0, 1))
points = PointCollection("agg", color="local", size="local")


@window.event
def on_draw(dt):
    window.clear()
    points.draw()
    if len(points) < 10000:
        points.append(np.random.normal(0.0, 0.5, (1, 3)),
                      color=np.random.uniform(0, 1, 4),
                      size=np.random.uniform(1, 24, 1))

window.attach(points["transform"])
window.attach(points["viewport"])
app.run()
