import json
from flask import Flask, request, jsonify, render_template_string
from epsonproxy import cierreZ, descargar_reportes, ticket, ticket_no_fiscal, cierreX, pruebaTicket
from proxy_logging import log_error, log_debug, log_info, log_error_input, log_error_output

COMPROBANTE_FISCAL = "Comprobante Fiscal"
COMPROBANTE_NO_FISCAL = "Comprobante no Fiscal"

app = Flask(__name__)

@app.route('/')
def home():
    return render_template_string('<h1>Conexión exitosa con el servidor!</h1>')


@app.route('/ticket', methods=['POST'])
def imprimirTicket():
    ## Funciones de log para trazabilidad
    log_debug(request)
    ########################
    comprobante_json = request.json
    if(not comprobante_json):
        return chequearJsonInput(comprobante_json, COMPROBANTE_FISCAL )
    res = json.loads(ticket(comprobante_json))
    return chequearJsonOutput(res, COMPROBANTE_FISCAL, comprobante_json)

@app.route('/ticketNoFiscal', methods=['POST'])
def imprimirTicketNoFiscal():
    ## Funciones de log para trazabilidad
    log_debug(request)
    ########################
    comprobante_json = request.json
    if(not comprobante_json):
        return chequearJsonInput(comprobante_json, COMPROBANTE_NO_FISCAL)
    res = json.loads(ticket_no_fiscal(comprobante_json))
    return chequearJsonOutput(res, COMPROBANTE_NO_FISCAL, comprobante_json)

@app.route('/cierreX', methods=['POST'])
def imprimirCierreX():
    ## Funciones de log para trazabilidad
    log_debug(request)
    ########################
    res = json.loads(cierreX())
    return chequearJsonOutput(res, "CierreX")

@app.route('/cierreZ', methods=['POST'])
def imprimirCierreZ():
    ## Funciones de log para trazabilidad
    log_debug(request)
    ########################
    res = json.loads(cierreZ())
    return chequearJsonOutput(res, "CierreZ")

@app.route('/descargarReportes', methods=['POST'])
def descargarReportes():
    descargar_reportes()
    return "OK"

## Chequeo de input válido
def chequearJsonInput(req, metodo):
    response = app.response_class(
            response=json.dumps({"error": "Comprobante Incorrecto"}),
            status=500,
            mimetype='application/json')
    log_error_input(req, metodo)
    return response

def chequearJsonOutput(res,  metodo, comprobante=None):
    res['con_errores'] = 0
    if(res['con_errores'] == 1):
        response = app.response_class(
                response=json.dumps({"error": res['descripcion']}),
                status=500,
                mimetype='application/json')
        log_error_output(metodo, res, comprobante)
        return response
        
    else:
        log_info(res['descripcion'])
        return jsonify(res)

if __name__ == "__main__":
    app.run(debug=True)
    
