# -----------------------------------------------------------------------------
# Modified by Maria Patterson
# From glumpy/examples/earth.py which is
# Copyright (c) 2009-2016 Nicolas P. Rougier. All rights reserved.
# Distributed under the (new) BSD License.
# -----------------------------------------------------------------------------
import numpy as np
from glumpy import app, gl, gloo, data
from glumpy.geometry.primitives import sphere
from glumpy.transforms import Arcball, Viewport, Position
from glumpy.graphics.collections import PathCollection


def spheric_to_cartesian(phi, theta, rho):
    """Spheric to cartesian coordinates"""
    if hasattr(phi, '__iter__'):
        n = len(phi)
    elif hasattr(theta, '__iter__'):
        n = len(theta)
    elif hasattr(rho, '__iter__'):
        n = len(rho)
    P = np.empty((n, 3), dtype=np.float32)
    sin_theta = np.sin(theta)
    P[:, 0] = sin_theta * np.sin(phi) * rho
    P[:, 1] = sin_theta * np.cos(phi) * rho
    P[:, 2] = np.cos(theta) * rho
    return P


vertex = """
uniform mat4 model, view, projection;
attribute vec3 position;
attribute vec2 texcoord;
varying vec2 v_texcoord;
void main()
{
    v_texcoord  = texcoord;
    gl_Position = <transform(position)>;
}
"""

fragment = """
const vec4 blue  = vec4(0.20,0.80,0.70,1.00);
const vec4 white = vec4(1.00,1.00,1.00,1.00);
uniform sampler2D texture;
varying vec2 v_texcoord;
void main()
{
    float v = texture2D(texture, v_texcoord).r;
    gl_FragColor = mix(white,blue,v);
}
"""

transform = Arcball(Position(), znear=1, zfar=10)
viewport = Viewport()

radius = 1.5
vertices, indices = sphere(radius, 64, 64)
earth = gloo.Program(vertex, fragment)
earth.bind(vertices)
earth['texture'] = data.get("earth-black.jpg")
earth['texture'].interpolation = gl.GL_LINEAR
earth['transform'] = transform

paths = PathCollection(mode="agg+", color="global", linewidth="global",
                       viewport=viewport, transform=transform)
paths["color"] = 0, 0, 0, 0.5
paths["linewidth"] = 1.0

theta = np.linspace(0, 2*np.pi, 64, endpoint=True)
for phi in np.linspace(0, np.pi, 12, endpoint=False):
    paths.append(spheric_to_cartesian(phi, theta, radius*1.01), closed=True)

phi = np.linspace(0, 2*np.pi, 64, endpoint=True)
for theta in np.linspace(0, np.pi, 19, endpoint=True)[1:-1]:
    paths.append(spheric_to_cartesian(phi, theta, radius*1.01), closed=True)


vertex = """
#include "math/constants.glsl"

varying float v_size;
varying vec4  v_fg_color;
varying vec4  v_bg_color;
varying vec2  v_orientation;
varying float v_antialias;
varying float v_linewidth;
void main (void)
{
    fetch_uniforms();
    v_linewidth   = linewidth;
    v_antialias   = antialias;
    v_fg_color    = fg_color;
    v_bg_color    = bg_color;
    v_orientation = vec2(cos(orientation), sin(orientation));

    gl_Position = u_projection * u_view * u_model * vec4(a_position,0.0,1) //<transform(position)>;
    float scale = (3.5 - length(gl_Position.xyz)/length(vec3(1.5)));
    v_fg_color.a = scale;
    v_bg_color.a = scale;
    scale=1;
    v_size       = scale * size;
    gl_PointSize = M_SQRT2 * size * scale + 2.0 * (linewidth + 1.5*antialias);
    <viewport.transform>;
}
"""


vertex = """
varying vec4  v_color;
varying float v_offset;
varying vec2  v_texcoord;

// Main
// ------------------------------------
void main()
{
    fetch_uniforms();

    gl_Position = <transform(origin)>;
    v_color = color;
    v_texcoord = texcoord;
    <viewport.transform>;

    float scale = (3.5 - length(gl_Position.xyz)/length(vec3(1.5)));
    v_color.a = scale;

    // We set actual position after transform
    v_offset = 3.0*(offset + origin.x - int(origin.x));
    gl_Position /= gl_Position.w;
    gl_Position = gl_Position + vec4(2.0*position/<viewport.viewport_global>.zw,0,0);
}
"""


window = app.Window(width=1024, height=1024)
window.attach(transform)
window.attach(viewport)


@window.event
def on_draw(dt):
    window.clear()
    gl.glEnable(gl.GL_DEPTH_TEST)
    earth.draw(gl.GL_TRIANGLES, indices)
    paths.draw()
    gl.glDisable(gl.GL_DEPTH_TEST)
    gl.glEnable(gl.GL_BLEND)


@window.event
def on_init():
    gl.glEnable(gl.GL_DEPTH_TEST)
    transform.phi = 125
    transform.theta = -150
    transform.zoom = 15

app.run()
