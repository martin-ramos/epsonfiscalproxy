from ctypes import c_int, create_string_buffer
import json
import platform

if platform.system() == "Linux" :
    from ctypes import cdll
else :
    from ctypes import windll

ID_TIPO_COMPROBANTE_TIQUET                = c_int( 1 ).value  # "83"  Tique
ID_TIPO_COMPROBANTE_TIQUE_FACTURA         = c_int( 2 ).value  # "81"  Tique Factura A, "82" Tique Factura B, "111" Tique Factura C, "118" Tique Factura M
ID_TIPO_COMPROBANTE_TIQUE_NOTA_DE_CREDITO = c_int( 3 ).value  # "110" Tique Nota de Credito, "112" Tique Nota de Credito A, "113" Tique Nota de Credito B, "114" Tique Nota de Credito C, "119" Tique Nota de Credito M
ID_TIPO_COMPROBANTE_TIQUE_NOTA_DE_DEBITO  = c_int( 4 ).value  # "115" Tique Nota de Debito A, "116" Tique Nota de Debito B, "117" Tique Nota de Debito C, "120" Tique Nota de Debito M
ID_TIPO_COMPROBANTE_NO_FISCAL = c_int( 21 ).value 

ID_TIPO_DOCUMENTO_NINGUNO           = c_int( 0 ).value
ID_TIPO_DOCUMENTO_DNI               = c_int( 1 ).value
ID_TIPO_DOCUMENTO_CUIL              = c_int( 2 ).value
ID_TIPO_DOCUMENTO_CUIT              = c_int( 3 ).value
ID_TIPO_DOCUMENTO_CEDULA_IDENTIDAD  = c_int( 4 ).value
ID_TIPO_DOCUMENTO_PASAPORTE         = c_int( 5 ).value
ID_TIPO_DOCUMENTO_LIB_CIVICA        = c_int( 6 ).value
ID_TIPO_DOCUMENTO_LIB_ENROLAMIENTO  = c_int( 7 ).value

ID_RESPONSABILIDAD_IVA_NINGUNO                              = c_int(  0 ).value
ID_RESPONSABILIDAD_IVA_RESPONSABLE_INSCRIPTO                = c_int(  1 ).value
ID_RESPONSABILIDAD_IVA_NO_RESPONSABLE                       = c_int(  3 ).value
ID_RESPONSABILIDAD_IVA_MONOTRIBUTISTA                       = c_int(  4 ).value
ID_RESPONSABILIDAD_IVA_CONSUMIDOR_FINAL                     = c_int(  5 ).value
ID_RESPONSABILIDAD_IVA_EXENTO                               = c_int(  6 ).value
ID_RESPONSABILIDAD_IVA_NO_CATEGORIZADO                      = c_int(  7 ).value
ID_RESPONSABILIDAD_IVA_MONOTRIBUTISTA_SOCIAL                = c_int(  8 ).value
ID_RESPONSABILIDAD_IVA_CONTRIBUYENTE_EVENTUAL               = c_int(  9 ).value
ID_RESPONSABILIDAD_IVA_CONTRIBUYENTE_EVENTUAL_SOCIAL        = c_int( 10 ).value
ID_RESPONSABILIDAD_IVA_MONOTRIBUTO_INDEPENDIENTE_PROMOVIDO  = c_int( 11 ).value

ID_MODIFICADOR_AGREGAR_ITEM                     = c_int( 200 ).value
ID_MODIFICADOR_ANULAR_ITEM                      = c_int( 201 ).value
ID_MODIFICADOR_AGREGAR_ITEM_RETORNO_ENVASES     = c_int( 202 ).value
ID_MODIFICADOR_ANULAR_ITEM_RETORNO_ENVASES      = c_int( 203 ).value
ID_MODIFICADOR_AGREGAR_ITEM_BONIFICACION        = c_int( 204 ).value
ID_MODIFICADOR_ANULAR_ITEM_BONIFICACION         = c_int( 205 ).value
ID_MODIFICADOR_AGREGAR_ITEM_DESCUENTO           = c_int( 206 ).value
ID_MODIFICADOR_ANULAR_ITEM_DESCUENTO            = c_int( 207 ).value
ID_MODIFICADOR_AGREGAR_ITEM_ANTICIPO            = c_int( 208 ).value
ID_MODIFICADOR_ANULAR_ITEM_ANTICIPO             = c_int( 209 ).value
ID_MODIFICADOR_AGREGAR_ITEM_DESCUENTO_ANTICIPO  = c_int( 210 ).value
ID_MODIFICADOR_ANULAR_ITEM_DESCUENTO_ANTICIPO   = c_int( 211 ).value
ID_MODIFICADOR_DESCUENTO                        = c_int( 400 ).value
ID_MODIFICADOR_AJUSTE                           = c_int( 401 ).value
ID_MODIFICADOR_AJUSTE_NEGATIVO                  = c_int( 402 ).value
ID_MODIFICADOR_AUDITORIA_DETALLADA              = c_int( 500 ).value
ID_MODIFICADOR_AUDITORIA_RESUMIDA               = c_int( 501 ).value

ID_MODIFICADOR_AGREGAR                          = ID_MODIFICADOR_AGREGAR_ITEM
ID_MODIFICADOR_ANULAR                           = ID_MODIFICADOR_ANULAR_ITEM

ID_TASA_IVA_NINGUNO = c_int( 0 ).value
ID_TASA_IVA_EXENTO  = c_int( 1 ).value
ID_TASA_IVA_10_50   = c_int( 4 ).value
ID_TASA_IVA_21_00   = c_int( 5 ).value
ID_TASA_IVA_27_00   = c_int( 6 ).value

ID_IMPUESTO_NINGUNO            = c_int( 0 ).value
ID_IMPUESTO_INTERNO_FIJO       = c_int( 1 ).value
ID_IMPUESTO_INTERNO_PORCENTUAL = c_int( 2 ).value

ID_CODIGO_INTERNO = c_int( 1 ).value
ID_CODIGO_MATRIX  = c_int( 2 ).value

AFIP_CODIGO_UNIDAD_MEDIDA_SIN_DESCRIPCION            = c_int(  0 ).value
AFIP_CODIGO_UNIDAD_MEDIDA_KILOGRAMO                  = c_int(  1 ).value
AFIP_CODIGO_UNIDAD_MEDIDA_METROS                     = c_int(  2 ).value
AFIP_CODIGO_UNIDAD_MEDIDA_METRO_CUADRADO             = c_int(  3 ).value
AFIP_CODIGO_UNIDAD_MEDIDA_METRO_CUBICO               = c_int(  4 ).value
AFIP_CODIGO_UNIDAD_MEDIDA_LITROS                     = c_int(  5 ).value
AFIP_CODIGO_UNIDAD_MEDIDA_UNIDAD                     = c_int(  7 ).value
AFIP_CODIGO_UNIDAD_MEDIDA_PAR                        = c_int(  8 ).value
AFIP_CODIGO_UNIDAD_MEDIDA_DOCENA                     = c_int(  9 ).value
AFIP_CODIGO_UNIDAD_MEDIDA_QUILATE                    = c_int( 10 ).value
AFIP_CODIGO_UNIDAD_MEDIDA_MILLAR                     = c_int( 11 ).value
AFIP_CODIGO_UNIDAD_MEDIDA_MEGA_U_INTER_ACT_ANTIB     = c_int( 12 ).value
AFIP_CODIGO_UNIDAD_MEDIDA_UNIDAD_INT_ACT_INMUNG      = c_int( 13 ).value
AFIP_CODIGO_UNIDAD_MEDIDA_GRAMO                      = c_int( 14 ).value
AFIP_CODIGO_UNIDAD_MEDIDA_MILIMETRO                  = c_int( 15 ).value
AFIP_CODIGO_UNIDAD_MEDIDA_MILIMETRO_CUBICO           = c_int( 16 ).value
AFIP_CODIGO_UNIDAD_MEDIDA_KILOMETRO                  = c_int( 17 ).value
AFIP_CODIGO_UNIDAD_MEDIDA_HECTOLITRO                 = c_int( 18 ).value
AFIP_CODIGO_UNIDAD_MEDIDA_MEGA_UNIDAD_INT_ACT_INMUNG = c_int( 19 ).value
AFIP_CODIGO_UNIDAD_MEDIDA_CENTIMETRO                 = c_int( 20 ).value
AFIP_CODIGO_UNIDAD_MEDIDA_KILOGRAMO_ACTIVO           = c_int( 21 ).value
AFIP_CODIGO_UNIDAD_MEDIDA_GRAMO_ACTIVO               = c_int( 22 ).value
AFIP_CODIGO_UNIDAD_MEDIDA_GRAMO_BASE                 = c_int( 23 ).value
AFIP_CODIGO_UNIDAD_MEDIDA_UIACTHOR                   = c_int( 24 ).value
AFIP_CODIGO_UNIDAD_MEDIDA_JGO_PQT_MAZO_NAIPES        = c_int( 25 ).value
AFIP_CODIGO_UNIDAD_MEDIDA_MUIACTHOR                  = c_int( 26 ).value
AFIP_CODIGO_UNIDAD_MEDIDA_CENTIMETRO_CUBICO          = c_int( 27 ).value
AFIP_CODIGO_UNIDAD_MEDIDA_UIACTANT                   = c_int( 28 ).value
AFIP_CODIGO_UNIDAD_MEDIDA_TONELADA                   = c_int( 29 ).value
AFIP_CODIGO_UNIDAD_MEDIDA_DECAMETRO_CUBICO           = c_int( 30 ).value
AFIP_CODIGO_UNIDAD_MEDIDA_HECTOMETRO_CUBICO          = c_int( 31 ).value
AFIP_CODIGO_UNIDAD_MEDIDA_KILOMETRO_CUBICO           = c_int( 32 ).value
AFIP_CODIGO_UNIDAD_MEDIDA_MICROGRAMO                 = c_int( 33 ).value
AFIP_CODIGO_UNIDAD_MEDIDA_NANOGRAMO                  = c_int( 34 ).value
AFIP_CODIGO_UNIDAD_MEDIDA_PICOGRAMO                  = c_int( 35 ).value
AFIP_CODIGO_UNIDAD_MEDIDA_MUIACTANT                  = c_int( 36 ).value
AFIP_CODIGO_UNIDAD_MEDIDA_UIACTIG                    = c_int( 37 ).value
AFIP_CODIGO_UNIDAD_MEDIDA_MILIGRAMO                  = c_int( 41 ).value
AFIP_CODIGO_UNIDAD_MEDIDA_MILILITRO                  = c_int( 47 ).value
AFIP_CODIGO_UNIDAD_MEDIDA_CURIE                      = c_int( 48 ).value
AFIP_CODIGO_UNIDAD_MEDIDA_MILICURIE                  = c_int( 49 ).value
AFIP_CODIGO_UNIDAD_MEDIDA_MICROCURIE                 = c_int( 50 ).value
AFIP_CODIGO_UNIDAD_MEDIDA_U_INTER_ACT_HORMONAL       = c_int( 51 ).value
AFIP_CODIGO_UNIDAD_MEDIDA_MEGA_U_INTER_ACT_HORMONAL  = c_int( 52 ).value
AFIP_CODIGO_UNIDAD_MEDIDA_KILOGRAMO_BASE             = c_int( 53 ).value
AFIP_CODIGO_UNIDAD_MEDIDA_GRUESA                     = c_int( 54 ).value
AFIP_CODIGO_UNIDAD_MEDIDA_MUIACTIG                   = c_int( 55 ).value
AFIP_CODIGO_UNIDAD_MEDIDA_KILOGRAMO_BRUTO            = c_int( 61 ).value
AFIP_CODIGO_UNIDAD_MEDIDA_PACK                       = c_int( 62 ).value
AFIP_CODIGO_UNIDAD_MEDIDA_HORMA                      = c_int( 63 ).value

AFIP_CODIGO_OTROS_TRIBUTOS_IMPUESTOS_NACIONALES                 = c_int(  1 ).value
AFIP_CODIGO_OTROS_TRIBUTOS_IMPUESTOS_PROVINCIAL                 = c_int(  2 ).value
AFIP_CODIGO_OTROS_TRIBUTOS_IMPUESTO_MUNICIPAL                   = c_int(  3 ).value
AFIP_CODIGO_OTROS_TRIBUTOS_IMPUESTO_INTERNOS                    = c_int(  4 ).value
AFIP_CODIGO_OTROS_TRIBUTOS_INGRESOS_BRUTOS                      = c_int(  5 ).value
AFIP_CODIGO_OTROS_TRIBUTOS_PERCEPCION_DE_IVA                    = c_int(  6 ).value
AFIP_CODIGO_OTROS_TRIBUTOS_PERCEPCION_DE_INGRESOS_BRUTOS        = c_int(  7 ).value
AFIP_CODIGO_OTROS_TRIBUTOS_PERCEPCION_POR_IMPUESTOS_MUNICIPALES = c_int(  8 ).value
AFIP_CODIGO_OTROS_TRIBUTOS_OTRAS_PERCEPCIONES                   = c_int(  9 ).value
AFIP_CODIGO_OTROS_TRIBUTOS_OTROS                                = c_int( 99 ).value

AFIP_CODIGO_FORMA_DE_PAGO_CARTA_DE_CREDITO_DOCUMENTARIO       = c_int(  1 ).value
AFIP_CODIGO_FORMA_DE_PAGO_CARTAS_DE_CREDITO_SIMPLE            = c_int(  2 ).value
AFIP_CODIGO_FORMA_DE_PAGO_CHEQUE                              = c_int(  3 ).value
AFIP_CODIGO_FORMA_DE_PAGO_CHEQUES_CANCELATORIOS               = c_int(  4 ).value
AFIP_CODIGO_FORMA_DE_PAGO_CREDITO_DOCUMENTARIO                = c_int(  5 ).value
AFIP_CODIGO_FORMA_DE_PAGO_CUENTA_CORRIENTE                    = c_int(  6 ).value
AFIP_CODIGO_FORMA_DE_PAGO_DEPOSITO                            = c_int(  7 ).value
AFIP_CODIGO_FORMA_DE_PAGO_EFECTIVO                            = c_int(  8 ).value
AFIP_CODIGO_FORMA_DE_PAGO_ENDOSO_DE_CHEQUE                    = c_int(  9 ).value
AFIP_CODIGO_FORMA_DE_PAGO_FACTURA_DE_CREDITO                  = c_int( 10 ).value
AFIP_CODIGO_FORMA_DE_PAGO_GARANTIAS_BANCARIAS                 = c_int( 11 ).value
AFIP_CODIGO_FORMA_DE_PAGO_GIROS                               = c_int( 12 ).value
AFIP_CODIGO_FORMA_DE_PAGO_LETRAS_DE_CAMBIO                    = c_int( 13 ).value
AFIP_CODIGO_FORMA_DE_PAGO_MEDIOS_DE_PAGO_DE_COMERCIO_EXTERIOR = c_int( 14 ).value
AFIP_CODIGO_FORMA_DE_PAGO_ORDEN_DE_PAGO_DOCUMENTARIA          = c_int( 15 ).value
AFIP_CODIGO_FORMA_DE_PAGO_ORDEN_DE_PAGO_SIMPLE                = c_int( 16 ).value
AFIP_CODIGO_FORMA_DE_PAGO_PAGO_CONTRA_REEMBOLSO               = c_int( 17 ).value
AFIP_CODIGO_FORMA_DE_PAGO_REMESA_DOCUMENTARIA                 = c_int( 18 ).value
AFIP_CODIGO_FORMA_DE_PAGO_REMESA_SIMPLE                       = c_int( 19 ).value
AFIP_CODIGO_FORMA_DE_PAGO_TARJETA_DE_CREDITO                  = c_int( 20 ).value
AFIP_CODIGO_FORMA_DE_PAGO_TARJETA_DE_DEBITO                   = c_int( 21 ).value
AFIP_CODIGO_FORMA_DE_PAGO_TICKET                              = c_int( 22 ).value
AFIP_CODIGO_FORMA_DE_PAGO_TRANSFERENCIA_BANCARIA              = c_int( 23 ).value
AFIP_CODIGO_FORMA_DE_PAGO_TRANSFERENCIA_NO_BANCARIA           = c_int( 24 ).value
AFIP_CODIGO_FORMA_DE_PAGO_OTROS_MEDIOS_DE_PAGO                = c_int( 99 ).value

def cargarLibreria() :
    sistema = platform.system()
    if sistema == "Linux" :
        return cdll.LoadLibrary("./EpsonFiscalInterface.so")
    else :
        if sistema == "Windows" :
            return windll.LoadLibrary("./EpsonFiscalInterface.dll")
# -----------------------------------------------------------------------------
# Function: ticket
# -----------------------------------------------------------------------------
def ticket(datos_ticket):
    try :

        # get handle from DLL
        Handle_HL = cargarLibreria()

        # # connect
        ###Handle_HL.ConfigurarVelocidad( c_int(9600).value )
        Handle_HL.ConfigurarPuerto( "0" )
        ejecutarComando(Handle_HL, Handle_HL.Conectar())
        
        # # try cancel all
        ejecutarComando(Handle_HL, Handle_HL.Cancelar())

        # # open
        ejecutarComando(Handle_HL, Handle_HL.AbrirComprobante( ID_TIPO_COMPROBANTE_TIQUET ))
        ## Aca en esta funcion tenemos que poder evaluar los errores que puede arrojar
        
        # # get document number
        str_doc_number_max_len = 20
        str_doc_number = create_string_buffer( b'\000' * str_doc_number_max_len )
        error = Handle_HL.ConsultarNumeroComprobanteActual( str_doc_number, c_int(str_doc_number_max_len).value )
        print("Get Doc. Number Error : "),
        print(error)
        print("Doc Number            : "),
        print(str_doc_number.value)

        # # get document type
        str_doc_type_max_len = 20
        str_doc_type = create_string_buffer( b'\000' * str_doc_type_max_len )
        print(str_doc_type)
        error = Handle_HL.ConsultarTipoComprobanteActual( str_doc_type, c_int(str_doc_type_max_len).value )
        print("Get Type Doc. Error   : "),
        print(error)
        print("Doc Type              : "),
        print(str_doc_type.value)

        # item
        #   imprimirItems(datos_ticket['items'], Handle_HL) 
        for item in datos_ticket['itemsComprobante'] :
        # error = Handle_HL.ImprimirItem( ID_MODIFICADOR_AGREGAR, "Sardinas", "1", "100.1234", ID_TASA_IVA_EXENTO, ID_IMPUESTO_NINGUNO, "0", ID_CODIGO_INTERNO, "CodigoInterno4567890123456789012345678901234567890", "", AFIP_CODIGO_UNIDAD_MEDIDA_KILOGRAMO )
            error = ejecutarComando(Handle_HL, Handle_HL.ImprimirItem( ID_MODIFICADOR_AGREGAR, enviar_texto(item["descripcion"]), enviar_texto(item['cantidad']), enviar_texto(item["importeOriginal"]), ID_TASA_IVA_EXENTO, ID_IMPUESTO_NINGUNO, "0", ID_CODIGO_INTERNO, enviar_texto(item["codigo"]), "", AFIP_CODIGO_UNIDAD_MEDIDA_UNIDAD))
            print(str(item['cantidad'] + ' ' + item['descripcion'].ljust(40) + item['importeOriginal']))
        
        # subtotal
        ejecutarComando(Handle_HL, Handle_HL.ImprimirSubtotal())
        # print(datos_ticket["total"])
        print(str("IMPORTE" + " ").ljust(42) + str(datos_ticket["total"]))

        # get subtotal gross amount
        str_subtotal_max_len = 20
        str_subtotal = create_string_buffer( b'\000' * str_subtotal_max_len )
        error = Handle_HL.ConsultarSubTotalBrutoComprobanteActual( str_subtotal, c_int(str_subtotal_max_len).value )
        print("Get Subtotal Gross    : "),
        print(error)
        print("Subtotal Gross Amount : "),
        print(str_subtotal.value)

        # get subtotal gross amount
        str_subtotal_max_len = 20
        str_subtotal = create_string_buffer( b'\000' * str_subtotal_max_len )
        print("como imprime:" + str(str_subtotal))
        error = Handle_HL.ConsultarSubTotalNetoComprobanteActual( str_subtotal, c_int(str_subtotal_max_len).value )
        print("Get Subtotal Net      : "),
        print(error)
        print("Subtotal Net Amount   : "),
        print(str_subtotal.value)

        # close
        ejecutarComando(Handle_HL, Handle_HL.CerrarComprobante())
        res = {"con_errores": 0, "descripcion": "OK", "numero": str(str_doc_number.value)[2:-1]}

    except Exception as err : 
        res = {"con_errores": 1, "descripcion": str(err)}
    
    finally:
        ejecutarComando(Handle_HL, Handle_HL.Desconectar())
        return json.dumps(res)
        

## Formato de datos de ticket
# ticket_str = "{'cliente': 'Martin Ramos'}"
#             #   , "Importe": "100.00"
#             #   , "Items": 
#             #     [{    "descripcion": "Coca Cola"
#             #         , "importe": "120.00"}
#             #     ]}
def ticket_no_fiscal(datos_ticket):
    try :

        # get handle from DLL
        Handle_HL = cargarLibreria()

        # connect
        ###Handle_HL.ConfigurarVelocidad( c_int(9600).value )
        Handle_HL.ConfigurarPuerto( "0" )
        ejecutarComando(Handle_HL, Handle_HL.Conectar())

        # try cancel all
        ejecutarComando(Handle_HL, Handle_HL.Cancelar())
        
        # open
        ejecutarComando(Handle_HL, Handle_HL.AbrirComprobante( ID_TIPO_COMPROBANTE_NO_FISCAL ))

        ejecutarComando(Handle_HL, Handle_HL.ImprimirTextoLibre(enviar_texto("Numero: " + str(datos_ticket['numero']))))
        ejecutarComando(Handle_HL, Handle_HL.ImprimirTextoLibre(enviar_texto(datos_ticket['cliente'])))
        imprimirItems(datos_ticket['itemsComprobante'], Handle_HL)

        # subtotal
        ejecutarComando(Handle_HL, Handle_HL.ImprimirTextoLibre(enviar_texto(str("IMPORTE" + " ").ljust(40) + str(datos_ticket['total']))))

        # close
        ejecutarComando(Handle_HL, Handle_HL.CerrarComprobante())

        res = {"con_errores": 0, "descripcion": 'OK'}

    except Exception as err : 
        res = {"con_errores": 1, "descripcion": str(err)}
    
    finally:
        ejecutarComando(Handle_HL, Handle_HL.Desconectar())
        return json.dumps(res)

def enviar_texto(string) :
    return string.encode('ascii')


def imprimirItems(datos_items, Handle_HL) :
    for item in datos_items :
        ejecutarComando(Handle_HL, Handle_HL.ImprimirTextoLibre(enviar_texto(str(item['cantidad'] + ' ' + item['descripcion'].ljust(40) + item['importeOriginal']))))    
  
def encabezado()  :
    #title 
    print("*** Seteando Encabezado ***")

    # get handle from DLL
    Handle_HL = cargarLibreria()

    # connect
    ###Handle_HL.ConfigurarVelocidad( c_int(9600).value )
    Handle_HL.ConfigurarPuerto( "0")
    error = Handle_HL.Conectar()
    print("Connect               : "),
    print(hex(error))

    # try cancel all
    error = Handle_HL.Cancelar()
    print("Cancel                : "),
    print(hex(error))

    error = Handle_HL.EstablecerEncabezado(1, "Universidad Nacional de Quilmes")
    print("Cancel                : "),
    print(hex(error))

      # disconect
    error = Handle_HL.Desconectar()
    print("Disconect             : "),
    print(error)


def descargar_reportes() :
    #title 
    print("*** Seteando Encabezado ***")

    # get handle from DLL
    Handle_HL = cargarLibreria()

    # connect
    ###Handle_HL.ConfigurarVelocidad( c_int(9600).value )
    Handle_HL.ConfigurarPuerto( "0" )
    error = Handle_HL.Conectar()
    print("Connect               : "),
    print(hex(error))

    # try cancel all
    error = Handle_HL.Cancelar()
    print("Cancel                : "),
    print(hex(error))

    error = Handle_HL.Descargar(enviar_texto("201021"), enviar_texto("211021"), "downloads")
    print("Descargando Auditoria                : "),
    print(hex(error))

    # disconect
    error = Handle_HL.Desconectar()
    print("Disconect             : "),
    print(error)


def cierreZ():
        #title 
    print("*** Haciendo Cierre Z ***")
    try :
        # get handle from.so
        Handle_HL = cargarLibreria()

        # connect
        ###Handle_HL.ConfigurarVelocidad( c_int(9600).value )
        error = Handle_HL.ConfigurarPuerto( "0" )
        ejecutarComando(Handle_HL, Handle_HL.Conectar())
        
        # try cancel all
        ejecutarComando(Handle_HL, Handle_HL.Cancelar())

        ejecutarComando(Handle_HL, Handle_HL.ImprimirCierreZ())
        res = {"con_errores": 0, "descripcion": 'OK'}

    except Exception as err : 
        res = {"con_errores": 1, "descripcion": str(err)}
    
    finally:
        ejecutarComando(Handle_HL, Handle_HL.Desconectar())
        return json.dumps(res)

def cierreX():
    print("*** Haciendo Cierre X ***")
    try :
        # get handle from.so
        Handle_HL = cargarLibreria()

        # connect
        error = Handle_HL.ConfigurarPuerto( "0" )
        ejecutarComando(Handle_HL, Handle_HL.Conectar())
        
        # try cancel all
        ejecutarComando(Handle_HL, Handle_HL.Cancelar())

        ejecutarComando(Handle_HL, Handle_HL.ImprimirCierreX())
        
        res = {"con_errores": 0, "descripcion": 'OK'}

    except Exception as err : 
        res = {"con_errores": 1, "descripcion": str(err)}

    finally:
        ejecutarComando(Handle_HL, Handle_HL.Desconectar())
        return json.dumps(res)

def ejecutarComando(Handle_HL, comando) :
    ### En caso que el hexa sea 0x0 o bien 0x05000024
    if not (comando == 0 or comando == 83886116 or comando == 83886127) :
      raise ValueError(verificarError(Handle_HL, comando))


def verificarError(Handle_HL, error) :
    descripcion_error =  create_string_buffer(b'\000' * 500)
    error = Handle_HL.ConsultarDescripcionDeError(error, descripcion_error, c_int(500).value)
    
    return str(descripcion_error.value)[1:]

def reportes() :
    print("*** Reportes ***")

    # get handle from DLL
    Handle_HL = cargarLibreria()

    # connect
    ###Handle_HL.ConfigurarVelocidad( c_int(9600).value )
    Handle_HL.ConfigurarPuerto( "0" )
    error = Handle_HL.Conectar()
    print("Connect               : "),
    print(hex(error))

    # try cancel all
    ##error = Handle_HL.Cancelar()
    print("Cancel                : "),
    print(hex(error))

    error = Handle_HL.EnviarComando( "0970|0000|1|3")

    print("Reporte                : "),
    print(hex(error))

def pruebaTicket(datos_ticket):
    try :
        Handle_HL = cargarLibreria()

        for item in datos_ticket['itemsComprobante'] :
            print(str(item['cantidad'] + ' ' + item['descripcion'].ljust(40) + item['importeOriginal']))

        print(str("IMPORTE" + " ").ljust(42) + str(datos_ticket["total"]))
        raise ValueError("Esto es un error de prueba")
        res = {"con_errores": 0, "descripcion": "OK"}

    except Exception as err : 
        res = {"con_errores": 1, "descripcion": str(err)}
    
    finally:
        return json.dumps(res)

# # -----------------------------------------------------------------------------
# # main
# # -----------------------------------------------------------------------------
# print(" ")
# print(" ")
# print("----Basic Test")
# # dll_version()
# # dll_ll_test_comm()
# # equipment_machine_version()
# # print_X_and_Z()
# # set_and_get_header_trailer()
# # set_and_get_datetime()
# # cancel_all()
# print(" ")
# print(" ")
# print("----Testing Sales")


# ##encabezado()
# # ticket_str = '{"cliente": "Martin Ramos", "items": [{"cantidad":"2", "codigo":"123456789", "descripcion": "coca cola", "importe": "120.00"}], "total": "240"}'
# # ticket(ticket_str)
# # ticket_no_fiscal(ticket_str)
# # cierreZ()
# # cierreX()
# # descargar_reportes()
# #prueba_json(ticket_str)

# cierreX()


# # ticket_from_ticket_invoice()
# # ticket_invoice()
# # ticket_invoice_B()
# # ticket_debit_note()
# # ticket_debit_note_B()
# # ticket_credit_note()
# # ticket_credit_note_B()
# print(" ")
# print(" ")
# print("----Test Close Day")
# # audit()
# # download()
