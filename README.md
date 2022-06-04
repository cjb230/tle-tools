# tle-tools
A project you probably should not use. It has two purposes:
1. to let me mess around with orbital dynamics (TLE = [two-line elements](https://en.wikipedia.org/wiki/Two-line_element_set)), and
2. to try some of the tools from the Hypermodern Python project.

The project is misnamed: I've already started on Keplerian elements and I think I'll probably do orbital state vectors as well.

I don't recommend anyone use this code for anything:
- commonly available TLE data is made for use with more precise models
- I haven't looked at precision, especially the way it deteriorates over time
- I haven't validated this code against any other code.

## Results

### Orbits
Things I've learned, or re-learned:
1. The formula for the area of an ellipse is easier than I would have guessed.
2. The eccentricity of an ellipse is _not_ the linear ratio between the axes.
3. There are a _lot_ of different reference frames.
4. By convention, inclination is measured from the prograde direction.


### Python Tools
A few issues encountered, and dealt with, along the way:
- I needed to get update xcode before anything else.
- My bash profile fired up a conda environment that I'd completely forgotten about.
-

As of right now, I'm a little stuck on the pre-commit stuff: I have black using the github repo instead of local settings, but if I make the pre-commit config file looks more like this: https://github.com/cjolowicz/hypermodern-python/blob/master/.pre-commit-config.yaml then I have binary incompatability issues. Apple's new silicon is nice, but has its own problems.
