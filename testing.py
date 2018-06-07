import numpy as np
import robin.plotting.util

import echolocator
import render
import scene
import util

fs = 96000
device = util.DeviceShim(fs, 2, np.float64)
ex_echolocator = echolocator.ExampleEcholocator()
scene_to_render = [
    scene.Wall((-1, 2), (1, 2), 3),
    scene.Wall((1, 1), (1, -1), 3)
]

rendered = render.render_scene(fs, device, ex_echolocator, scene_to_render)
util.write_scene(fs, rendered, "output/test_charles_chirp.wav")
