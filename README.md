# Audacity Image Glitcher

Python scripts for glitching images with Audacity.


# Prerequisites

- Install these dependencies:
	- [Python](https://www.python.org/)
	- [Audacity](https://www.audacityteam.org/)
- [Enable `mod-script-pipe` in Audacity](https://manual.audacityteam.org/man/modules_preferences.html)


# Usage

- Open a new Audacity project
- Open a new terminal window
- Run `python glitchit.py` to import a file as fullscreen and select all
- Select the section of the track you want to apply effects to, keeping in mind to deselect the file header data near the beginning of the file.
- Run `python effects.py` to apply effects to your selection
- Export your file from Audacity, check the results, and repeat!

![Example Waveform](https://raw.githubusercontent.com/juan0tron/audacity-glitcher/master/docs/example-waveform.png)
![Example Output](https://raw.githubusercontent.com/juan0tron/audacity-glitcher/master/docs/example-output.png)


# Audacity Scripting Reference

- [Audacity Scripting Wiki](https://manual.audacityteam.org/man/scripting.html)
- [Scripting Commands Reference](https://manual.audacityteam.org/man/scripting_reference.html)
- [Python test file for determining if `mod-script-pipe` is running](https://github.com/audacity/audacity/blob/master/scripts/piped-work/pipe_test.py)
- [Audacity Python Scripts](https://github.com/audacity/audacity/tree/master/scripts/piped-work)


# Image Sonification Reference

Links to Audacity glitching tutorials. Much credit goes to these people for figuring out that this works in the first place!

- [databending and glitch art primer, part 2: sonification](http://blog.animalswithinanimals.com/2008/09/databending-and-glitch-art-primer-part.html), by stAllio!
- [Databending using Audacity](https://www.hellocatfood.com/databending-using-audacity/), by hellocatfood
- [Tutorial on Databending and Glitch Art](https://critiquecollective.com/2014/03/13/tutorial-on-databending-and-glitch-art/), by Paul Weiner
- [Databending using Audacity Effects](https://questionsomething.wordpress.com/2012/07/26/databending-using-audacity-effects/), via questionsomething
- [Examples of glitch art created using Audacity](https://github.com/linkman15/glitch-art), by linkman15


# Artist Notes

You can see some of my glitch work at [jglover.space](https://jglover.space/).
