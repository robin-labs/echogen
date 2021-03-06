
from . import robin.pulse
from . import robin.plotting
import scipy.stats

import distribution
from . import util

fs = 96000


def Q(x): return scipy.stats.norm.pdf(
    x if x <= 180 else x - 360,
    loc=0,
    scale=1
)


chirp = robin.pulse.Chirp(2e4, 3e4, 50e3)

res = distribution.render_pulse_with_distribution(fs, chirp, Q)
util.plot_scene(fs, res)
util.write_scene(fs, res, "dist4.wav")
