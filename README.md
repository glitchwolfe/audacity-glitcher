# Audacity Image Glitcher

Python scripts for glitching images with Audacity.

![Example Editing UI](https://raw.githubusercontent.com/juan0tron/audacity-glitcher/master/docs/editor-example.jpg)


# Prerequisites

- Install these dependencies on your computer:
	- [Python](https://www.python.org/)
	- [Audacity](https://www.audacityteam.org/)
- [Enable `mod-script-pipe` in Audacity](https://manual.audacityteam.org/man/modules_preferences.html)
- Install [Flask](https://palletsprojects.com/p/flask/) (`pip install flask` or `pip install -r requirements.txt`)


# Usage

- Open a new Audacity project
- Open a new terminal window and navigate to the root of this repository
- Run `python server.py` to start the Flask server
- Navigate to [localhost:5000](http://localhost:5000) in your browser
- Import your image file
- Apply as many effects as you want!
- Export your file
- Check your results, and repeat!


# Example Output

![Example Output](https://raw.githubusercontent.com/juan0tron/audacity-glitcher/master/docs/glitchit.png)


-----


# Image Sonification Tutorials

If you're new to glitching in Audacity, these tutorials will help you understand what's going on under the hood.

- [databending and glitch art primer, part 2: sonification](http://blog.animalswithinanimals.com/2008/09/databending-and-glitch-art-primer-part.html), by stAllio!
- [Databending using Audacity](https://www.hellocatfood.com/databending-using-audacity/), by hellocatfood
- [Tutorial on Databending and Glitch Art](https://critiquecollective.com/2014/03/13/tutorial-on-databending-and-glitch-art/), by Paul Weiner
- [Databending using Audacity Effects](https://questionsomething.wordpress.com/2012/07/26/databending-using-audacity-effects/), via questionsomething


# Audacity Scripting Reference

Useful links for anyone looking to write their own scripts.

- [Audacity Scripting Wiki](https://manual.audacityteam.org/man/scripting.html)
- [List of available scripting commands](https://manual.audacityteam.org/man/scripting_reference.html)
- [Python test file for determining if `mod-script-pipe` is running](https://github.com/audacity/audacity/blob/master/scripts/piped-work/pipe_test.py)
- [Example Python Scripts](https://github.com/audacity/audacity/tree/master/scripts/piped-work)


-----


# Artist Notes

You can see some of my glitch work at [jglover.space](https://jglover.space/).
