from flask import Flask, render_template, request, redirect, url_for
import hoteles
import vuelos

app=Flask(__name__)

resultadohoteles=[]
resultadovuelos=[]

@app.route('/')
def home():
    return render_template('inicio.html')

@app.route('/formulario', methods=['GET','POST'])
def formulario():
    global resultadohoteles
    global resultadovuelos
    if request.method == 'POST':
        destino = request.form['destino']
        aeropuertoorigen = request.form['aeropuertoorigen']
        aeropuertodestino = request.form['aeropuertodestino']
        fechasalida = request.form['fechasalida']
        fecharegreso = request.form['fecharegreso']
        personas = request.form['personas']
        presupuesto = request.form['presupuesto']
        resultadohoteles = hoteles.searchhotels(destino, fechasalida, fecharegreso, personas)
        resultadovuelos = vuelos.searchflights(aeropuertoorigen, aeropuertodestino, fechasalida, fecharegreso)
        print(resultadovuelos)
        #contador_id += 1
        return redirect(url_for('resultados'))
    return render_template('formulario.html')

@app.route('/resultados')
def resultados():
    return render_template('resultados.html', opcioneshoteles = resultadohoteles, opcionesvuelos=resultadovuelos)

if __name__ == '__main__':
    app.run(debug=True)