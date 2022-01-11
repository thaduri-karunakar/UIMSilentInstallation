#!/usr/bin/env python
#-*- coding: utf-8 -*-
comman_variables = ['USER_INSTALL_DIR','DB_NORMALIZED_PROVIDER_NAME']

"""               ,'DB_CREATE_MODE','DB_VERSION','DB_SERVER',
                    'DB_PORT','DB_NAME','DB_ADMIN_USERNAME','DB_ADMIN_PASSWD','NM_ADMIN_PASSWD','NMS_DOMAIN',
                    'NMS_PRIMARY_HUB_NAME','NMS_PRIMARY_ROBOT_NAME','NMS_FIRST_PROBE_PORT','NMS_PRIMARY_HUB_IP',
                    'WASP_PORT_HTTP','TELEMETRY_UPLOAD_OPT_IN_FLAG']
"""

sqlserver_db_variables = ['DB_AUTH_MODE','DB_ENABLE_TLS','DB_TRUST_STORE_PATH','DB_TRUST_STORE_PASSWD']
oracle_db_variables = ['DB_SERVICENAME','DB_TABLESPACENAME','DB_SYS_PASSWD','DB_ORACLE_INSTANTCLIENT_DIR',
                       'DB_WALLET_TYPE','DB_WALLET_STORE_PATH','DB_WALLET_STORE_PASSWD','DB_CLIENT_AUTH_NEEDED']
secure_bus_enabled_variables = ['ENABLE_SECURE_BUS','TUNNEL_PORT','CA_CERT_PASSWD','CLIENT_CERT_PASSWD']
installer_properties = {}

def get_installer_Pproperties():
    for variable in comman_variables:
        user_input = input("Provide {} value :  ".format(variable)).strip().lower()
        print(user_input)
        installer_properties[variable] = user_input  ## writing variables into dictionary

    print(installer_properties)
    # print(installer_properties['USER_INSTALL_DIR'])

    with open(r"C:\sw\robot_install\installer.properties",
              "a+") as pfile:  ## creating installer.properties file and writing the variables
        for key, value in installer_properties.items():
            # print(key, value)
            pfile.write('{}={}\n'.format(key, value))  ## writing all variables into installer.properties file
    pfile.close()  ## closing the file

get_installer_Pproperties()

