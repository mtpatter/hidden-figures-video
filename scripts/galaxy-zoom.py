# -----------------------------------------------------------------------------
# Modified by Maria Patterson
# From glumpy/examples/galaxy.py which is
# Copyright (c) 2009-2016 Nicolas P. Rougier. All rights reserved.
# Distributed under the (new) BSD License.
# -----------------------------------------------------------------------------
import numpy as np
import galaxy_specrend as galspec
from galaxy_simulation import Galaxy
from glumpy import app, gloo, gl, glm, data


vertex = """
#version 120
uniform mat4  u_model;
uniform mat4  u_view;
uniform mat4  u_projection;
uniform sampler1D u_colormap;
uniform float u_size;
uniform float time;


attribute float a_size;
attribute float a_dist;
attribute float a_type;
attribute vec2  a_position;
attribute float a_temperature;
attribute float a_brightness;


varying vec3 v_color;
varying float v_size;
varying float v_dist;

void main (void)
{
    gl_Position = (u_projection * u_view * u_model * vec4(a_position,0.0,0)) + vec4(0,0,0,1+500/time); //zoom
    if (a_size > 2.0)
    {
        gl_PointSize = a_size;
    } else {
        gl_PointSize = 0.0;
    }
    v_color = texture1D(u_colormap, a_temperature).rgb * a_brightness;
    if (a_type == 2)
        v_color *= vec3(2,1,1);
    else if (a_type == 3)
        v_color = vec3(.9);
    v_size  = a_size*u_size*.75;
    v_dist  = a_dist;
}
"""

fragment = """
#version 120
uniform sampler2D u_texture;
varying vec3 v_color;
varying float v_size;
varying float v_dist;

void main()
{
    gl_FragColor = vec4(texture2D(u_texture, gl_PointCoord).r*v_color, 1.0);
}
"""


window = app.Window(width=1600, height=1200)


@window.event
def on_init():
    gl.glBlendFunc(gl.GL_SRC_ALPHA, gl.GL_ONE)


@window.event
def on_draw(dt):
    window.clear()
    program['time'] += dt
    galaxy.update(50000)  # in years !
    program['a_size'] = galaxy['size'] * max(window.width/1200.0, window.height/1200.0)
    program['a_position'] = galaxy['position'] / 13000.0
    program.draw(gl.GL_POINTS)


@window.event
def on_resize(width, height):
    gl.glViewport(0, 0, width, height)
    projection = glm.perspective(450, width/float(height)/2, 20.0, 100.0)
    program['u_projection'] = projection


galaxy = Galaxy(35000)
galaxy.reset(13000, 4000, 0.0004, 0.90, 0.90, 0.5, 200, 300)
t0, t1 = 1000.0, 10000.0
n = 256
dt = (t1-t0)/n
colors = np.zeros((n, 3), dtype=np.float32)
for i in range(n):
    temperature = t0 + i*dt
    x, y, z = galspec.spectrum_to_xyz(galspec.bb_spectrum, temperature)
    r, g, b = galspec.xyz_to_rgb(galspec.SMPTEsystem, x, y, z)
    r = min((max(r, 0), 1))
    g = min((max(g, 0), 1))
    b = min((max(b, 0), 1))
    colors[i] = galspec.norm_rgb(r, g, b)


program = gloo.Program(vertex, fragment, count=len(galaxy))

view = np.eye(4, dtype=np.float32)
model = np.eye(4, dtype=np.float32)
projection = np.eye(4, dtype=np.float32)
glm.translate(view, 0, 0, -5)
program['time'] = 0
program['u_model'] = model
program['u_view'] = view
program['u_colormap'] = colors
program['u_texture'] = data.get("particle.png")
program['u_texture'].interpolation = gl.GL_LINEAR

program['a_temperature'] = (galaxy['temperature'] - t0) / (t1-t0)
program['a_brightness'] = galaxy['brightness'] / max(window.width/800.0, window.height/800.0)
program['a_size'] = galaxy['size']
program['a_type'] = galaxy['type']

gl.glClearColor(0.0, 0.0, 0.03, 1.0)
gl.glDisable(gl.GL_DEPTH_TEST)
gl.glEnable(gl.GL_BLEND)
gl.glBlendFunc(gl.GL_SRC_ALPHA, gl.GL_ONE)

app.run(framerate=60)
