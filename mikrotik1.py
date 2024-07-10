from netmiko import ConnectHandler

router_mikrotik = {
    'device_type': 'mikrotik_routeros',
    'host':   '10.0.0.66',
    'username': 'admin',
    'password': '1234',
    'port' : 22,            # optional, defaults to 22
    'secret': '',           # optional, defaults to ''
}

conexion = ConnectHandler(**router_mikrotik)

# Definir comandos a ejecutar
configurar = [
    '/ip address add address=172.26.14.1/25 interface=ether3',
    '/ip address add address=192.168.14.1/25 interface=ether2',
    '/ip dhcp-client add interface=ether3',
    '/ip pool add name=pool_lan_2 ranges=172.26.14.1-172.26.14.126',
    '/ip dhcp-server add address-pool=pool_lan_2 interface=ether3 name=dhcp_lan_2',
    '/ip dhcp-server network add address=172.26.14.0/25 gateway=172.26.14.1',
    '/ip service enable ssh',
    '/ip service set ssh port=22',
    '/ip firewall nat add chain=srcnat out-interface=ether3 action=masquerade',
]

# Ejecutar comandos (send_config_set - para enviar comandos de configuración)
accion1 = conexion.send_config_set(configurar)
print(accion1)

# Visualizar comandos (send_command - para enviar comandos de visualización)
accion2 = conexion.send_command('/ip address print')
print(accion2)

# Cerrar la conexión
conexion.disconnect()