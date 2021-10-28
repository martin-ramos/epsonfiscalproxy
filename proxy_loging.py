import json
import logging
import sys 

logger = logging.getLogger(__name__)

logging.basicConfig(
    format="{asctime} {levelname:<8} {message}",
    style="{",
    level=logging.NOTSET,
    ##stream=stdout,
    filename='proxy.log',
    encoding='utf-8'
)

logger.addHandler(logging.StreamHandler(sys.stdout))
# {'cliente': 'Martin Ramos'
#                , "Importe": "100.00"
#                , "Items": 
#                  [{    "descripcion": "Coca Cola"
#                     , "importe": "120.00"}
#                  ]}
def log_error(error) :
    logger.error(error)

def log_debug(debug) :
    logger.debug(debug)

def log_info(info) :
    logger.info(info)

def log_error_input(req, metodo):
    log_error(
        "\n[METODO]:" + metodo +
        "\n[MENSAJE]:" +
        "Input incorrecto para el metodo utilizado \n" + 
        "[INPUT RECIBIDO]:"  
         + json.dumps(req)
    )

def log_error_output(metodo, res, comprobante) :
    if comprobante:
        log_error_output_ticket(metodo, res, comprobante)
    else :
        log_error_output_cierres(res, metodo)         


## Output recibido es la respuesta 
## por parte de la impresora
def log_error_output_ticket(metodo, res, comprobante) :
    log_error(
        "\n[METODO]:" + metodo +
        "\n[MENSAJE]:" +
        res['descripcion'] + 
        "\n[INPUT RECIBIDO]" + 
            json.dumps(comprobante)   
    )

def log_error_output_cierres(res, metodo) :
    log_error(
        "\n[METODO]:" + metodo +
        "\n[MENSAJE]:" +
        res['descripcion']
    )