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


        if resultadovuelos[0]['layoverqty_dep'] == 0:
            resultadovuelos[0]['layovers_dep'] = "None"

        if resultadovuelos[1]['layoverqty_ret'] == 0:
            resultadovuelos[1]['layovers_ret'] = "None"

        if resultadovuelos[2]['layoverqty_dep'] == 0:
            resultadovuelos[2]['layovers_dep'] = "None"

        if resultadovuelos[3]['layoverqty_ret'] == 0:
            resultadovuelos[3]['layovers_ret'] = "None"

        if resultadovuelos[4]['layoverqty_dep'] == 0:
            resultadovuelos[4]['layovers_dep'] = "None"

        if resultadovuelos[5]['layoverqty_ret'] == 0:
            resultadovuelos[5]['layovers_ret'] = "None"
       

        for i in range(0, 3):
            cumplepresupuesto.append(calculopresupuesto(presupuesto, resultadohoteles[i]['totalprice'], resultadovuelos[i]['price']))

        return redirect(url_for('resultados'))
    return render_template('formulario.html')

@app.route('/resultados')
def resultados():
    return render_template('resultados.html', opcioneshoteles = resultadohoteles, opcionesvuelos=resultadovuelos, cumplepresupuesto = cumplepresupuesto, opcionesatracciones = resultadoatracciones)

if __name__ == '__main__':
    app.run(debug=True)