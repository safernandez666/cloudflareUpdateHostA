import requests
import json
from requests import get

# Funciones
def cambioRegistroA(dirActual):
    #url = 'https://api.cloudflare.com/client/v4/zones/bdeb407a4a822dfe7fe812fb128e4aaa/dns_records/10a08f03afbcd202d599e54b3dffc57f'
    url = 'https://api.cloudflare.com/client/v4/zones/ID_ZONE/dns_records/ID_RESOURSE'
    respuesta = requests.put(url, headers=headers, data='{"type":"A","name":"ftp.ironbox.com.ar","content":"%s","ttl":120,"proxied":false}' % dirActual )
    if respuesta.status_code == 200:
        print('Status:', respuesta.status_code,'. Se logro actualizar el registro, por %s.\n' % dirActual)
    else:
        print('Status:', respuesta.status_code,'. No s logro actualizar el registro.\n')


# Datos de Conexion
#url = 'https://api.cloudflare.com/client/v4/zones/bdeb407a4a822dfe7fe812fb128e4aaa/dns_records?page=1&per_page=20&order=type&direction=asc'
url = 'https://api.cloudflare.com/client/v4/zones/ID_ZONE/dns_records?page=1&per_page=20&order=type&direction=asc'
headers = {
    'Content-Type':'application/json',
    'X-Auth-Key':'XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX', 
    'X-Auth-Email':'XXXXXXXXXXXXXXXXXXXXXXXXXXX'
 }

# Obtengo mi Direccion Publica
dirActual = get('https://api.ipify.org').text
print ('\nDireccion Publica, actual, es:', dirActual)

# Obtengo los Registros de CloudFlare 
print("\nObteniendo Datos de CloudFlare\n")
datos = requests.get(url, headers=headers)

if datos.status_code == 200:
    print ('Status:', datos.status_code,'. Consulta Ok.\n')
    info=datos.json()
    FQDNCloudFlare = info['result'][0]['name']
    dirCloudFlare = info['result'][0]['content']
    # Comparo la direccion, acatual, con CloudFlare
    print (FQDNCloudFlare, dirCloudFlare,'\n')
    if dirActual == dirCloudFlare:  
        print('La direccion es la misma. No hace falta actualizar.\n')
    else:
        print('La direccion ha cambiado. Se requiere actualizar.\n')
        cambioRegistroA(dirActual)
else:
    print('Status:', datos.status_code,'. Problemas con la Consulta. Saliendo.\n')
