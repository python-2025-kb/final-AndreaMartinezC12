from flask import Flask, render_template, request, redirect, url_for
import hoteles
import vuelos
import atracciones

app=Flask(__name__)

resultadohoteles=[]
resultadovuelos=[]
cumplepresupuesto=[]

def calculopresupuesto(presupuesto, costovuelo, costohotel):
    costototal = int(costohotel) + int(costovuelo)
    print(costototal)
    print(presupuesto)
    if costototal > int(presupuesto):
        return "NO"
    elif costototal < int(presupuesto):
        return "SI"


@app.route('/')
def home():
    return render_template('inicio.html')

@app.route('/formulario', methods=['GET','POST'])
def formulario():
    global resultadohoteles
    global resultadovuelos
    global resultadoatracciones
    global cumplepresupuesto
    cumplepresupuesto=[]
    if request.method == 'POST':
        destino = request.form['destino']
        aeropuertoorigen = request.form['aeropuertoorigen']
        aeropuertodestino = request.form['aeropuertodestino']
        fechasalida = request.form['fechasalida']
        fecharegreso = request.form['fecharegreso']
        personas = request.form['personas']
        presupuesto = request.form['presupuesto']
        
        resultadohoteles = hoteles.searchhotels(destino, fechasalida, fecharegreso, personas)
        resultadovuelos = vuelos.searchflights(aeropuertoorigen, aeropuertodestino, fechasalida, fecharegreso, personas)
        resultadoatracciones = atracciones.search_attractions(destino)

        for i in range(0, 3):
            cumplepresupuesto.append(calculopresupuesto(presupuesto, resultadohoteles[i]['totalprice'], resultadovuelos[i]['price']))

        return redirect(url_for('resultados'))
    return render_template('formulario.html')

@app.route('/resultados')
def resultados():
    return render_template('resultados.html', opcioneshoteles = resultadohoteles, opcionesvuelos=resultadovuelos, cumplepresupuesto = cumplepresupuesto, opcionesatracciones = resultadoatracciones)

if __name__ == '__main__':
    app.run(debug=True)