from flask import Flask, request, send_from_directory, render_template, redirect, jsonify

import editor
import effects

app = Flask(__name__, static_url_path='')

# ====== Home Page ======

@app.route('/')
def index():
	return render_template('index.html')


# ====== Static Files ======

@app.route('/img/<path:path>')
def send_img(path):
	return send_from_directory('img', path)

@app.route('/js/<path:path>')
def send_js(path):
	return send_from_directory('js', path)

@app.route('/css/<path:path>')
def send_css(path):
	return send_from_directory('css', path)


# ====== Actions ======

# ====== Editor Buttons ======

@app.route('/export/', methods = ['POST'])
def export():
	editor.exportFile()
	return "EXPORT"

@app.route('/import/', methods = ['POST'])
def open():
	editor.startProject()
	return "IMPORT"

@app.route('/select-all/', methods = ['POST'])
def select_all():
	editor.selectAll()
	return "SELECT_ALL"
	
@app.route('/undo/', methods = ['POST'])
def undo_action():
	editor.undo()
	return "UNDO"

# ====== Effect Buttons ======


@app.route('/glitchit/', methods = ['POST'])
def glitchit():
	effects.glitchit()
	return "glitchit"

@app.route('/echo/', methods = ['POST'])
def echo():
	effects.echo()
	return "echo"

@app.route('/fade-in/', methods = ['POST'])
def fadeIn():
	effects.fadeIn()
	return "fadein"

@app.route('/fade-out/', methods = ['POST'])
def fadeOut():
	effects.fadeOut()
	return "fadeout"

@app.route('/filter-curve/', methods = ['POST'])
def filterCurve():
	effects.filterCurve()
	return "filtercurve"

@app.route('/graphic-eq/', methods = ['POST'])
def graphicEQ():
	effects.graphicEQ()
	return "GRAPHIC EQ"

@app.route('/invert/', methods = ['POST'])
def invert():
	effects.invert()
	return "INVERT"

@app.route('/reverb/', methods = ['POST'])
def reverb():
	effects.reverb()
	return "REVERB"

@app.route('/reverse/', methods = ['POST'])
def reverse():
	effects.reverse()
	return "REVERSE"

@app.route('/paulstretch/', methods = ['POST'])
def paulstretch():
	effects.paulstretch()
	return "PAULSTRETCH"

@app.route('/phaser/', methods = ['POST'])
def phaser():
	effects.phaser()
	return "PHASER"

@app.route('/wahwah/', methods = ['POST'])
def wahwah():
	effects.wahwah()
	return "WAHWAH"
	
if __name__ == '__main__':
	app.run(debug=True)
