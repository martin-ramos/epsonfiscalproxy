import json
import logging
import sys 

def setup_logger(logger_name, log_file, level=logging.INFO):
    logger = logging.getLogger(logger_name)
    formatter = logging.Formatter("%(asctime)s %(levelname)s : %(message)s")
    fileHandler = logging.FileHandler(log_file)
    fileHandler.setFormatter(formatter)
    streamHandler = logging.StreamHandler()
    streamHandler.setFormatter(formatter)
    logger.setLevel(level)
    logger.addHandler(fileHandler)
    logger.addHandler(streamHandler)


setup_logger("log_errores", "log_errores.log", logging.INFO)
setup_logger("proxy_log", "proxy.log", logging.DEBUG)

log_errores = logging.getLogger('log_errores')
logger_info = logging.getLogger('proxy_log')

log_errores.addHandler(logging.StreamHandler(sys.stdout))
logger_info.addHandler(logging.StreamHandler(sys.stdout))




##logger.addHandler(logging.StreamHandler(sys.stdout))
# {'cliente': 'Martin Ramos'
#                , "Importe": "100.00"
#                , "Items": 
#                  [{    "descripcion": "Coca Cola"
#                     , "importe": "120.00"}
#                  ]}
def log_error(error) :
    logger_info.error(error)
    log_errores.error(error)

def log_debug(debug) :
    logger_info.debug(
                "\n[REQUEST]:" + str(debug) +
                "\n[BODY]:" + json.dumps(debug.json)
                
    )

def log_info(info) :
    logger_info.info(info)

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
        "\n[METODO]: {} \n[MENSAJE]: {} \n[INPUT RECIBIDO] {}".format(metodo, res['descripcion'], json.dumps(comprobante)) 
            
    )

def log_error_output_cierres(res, metodo) :
    log_error(
        "\n[METODO]:{} \n[MENSAJE]: {}".format(metodo, res['descripcion'])
    )