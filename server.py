from flask import Flask, request, send_from_directory, render_template, redirect

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
# TODO: Make these async POST requests instead of redirecting to home

# ====== Editor Buttons ======

@app.route('/export/')
def export():
	editor.exportFile()
	return redirect("/", code=302)

@app.route('/import-raw/')
def open():
	editor.startProject()
	return redirect("/", code=302)

@app.route('/select-all/')
def select_all():
	editor.selectAll()
	return redirect("/", code=302)

@app.route('/undo/')
def undo_action():
	editor.undo()
	return redirect("/", code=302)


# ====== Effect Buttons ======


@app.route('/glitchit/')
def glitchit():
	effects.glitchit()
	return redirect("/", code=302)

@app.route('/echo/')
def echo():
	effects.echo()
	return redirect("/", code=302)

@app.route('/fade-in/')
def fadeIn():
	effects.fadeIn()
	return redirect("/", code=302)

@app.route('/fade-out/')
def fadeOut():
	effects.fadeOut()
	return redirect("/", code=302)

@app.route('/filter-curve/')
def filterCurve():
	effects.filterCurve()
	return redirect("/", code=302)

@app.route('/graphic-eq/')
def graphicEQ():
	effects.graphicEQ()
	return redirect("/", code=302)

@app.route('/invert/')
def invert():
	effects.invert()
	return redirect("/", code=302)

@app.route('/reverb/')
def reverb():
	effects.reverb()
	return redirect("/", code=302)

@app.route('/reverse/')
def reverse():
	effects.reverse()
	return redirect("/", code=302)

@app.route('/paulstretch/')
def paulstretch():
	effects.paulstretch()
	return redirect("/", code=302)

@app.route('/phaser/')
def phaser():
	effects.phaser()
	return redirect("/", code=302)

@app.route('/wahwah/')
def wahwah():
	effects.wahwah()
	return redirect("/", code=302)


if __name__ == '__main__':
	app.run(debug=True)
