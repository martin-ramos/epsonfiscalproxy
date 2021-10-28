import json
from flask import Flask, request, jsonify, render_template_string
from epsonproxy import cierreZ, descargar_reportes, ticket, ticket_no_fiscal, cierreX, pruebaTicket

app = Flask(__name__)

@app.route('/')
def home():
    return render_template_string('<h1>Conexión exitosa!</h1>')

@app.route('/ticket', methods=['POST'])
def imprimirTicket():
    comprobante_json = request.json
    if(not comprobante_json):
        return chequearJsonInput(comprobante_json)
    res = json.loads(ticket(comprobante_json))
    return chequearJsonOutput(res)

@app.route('/ticketNoFiscal', methods=['POST'])
def imprimirTicketNoFiscal():
    comprobante_json = request.json
    if(not comprobante_json):
        return chequearJsonInput(comprobante_json)
    res = json.loads(ticket_no_fiscal(comprobante_json))
    return chequearJsonOutput(res)

@app.route('/testTicket', methods=['POST'])
def imprimirTicketTest():
    comprobante_json = request.json
    if(not comprobante_json):
        return chequearJsonInput(comprobante_json)
    res = json.loads(pruebaTicket(comprobante_json))
    return chequearJsonOutput(res)

@app.route('/cierreX', methods=['POST'])
def imprimirCierreX():
    res = json.loads(cierreX())
    return chequearJsonOutput(res)

@app.route('/cierreZ', methods=['POST'])
def imprimirCierreZ():
    res = json.loads(cierreZ())
    return chequearJsonOutput(res)

@app.route('/descargarReportes', methods=['POST'])
def descargarReportes():
    descargar_reportes()
    return "OK"

def chequearJsonInput(req):
    response = app.response_class(
            response=json.dumps({"error": "Comprobante Incorrecto"}),
            status=500,
            mimetype='application/json')
    return response

def chequearJsonOutput(res):
    if(res['con_errores'] == 1):
        response = app.response_class(
                response=json.dumps({"error": res['descripcion']}),
                status=500,
                mimetype='application/json')
        return response
    else:
        return jsonify(res)

if __name__ == "__main__":
    app.run(debug=True)
