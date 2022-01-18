#!/usr/bin/env python
import get_hostName_ip
uim_installation_type = input("Provide uim_installation_type (fresh/upgrade) :  ").strip().lower()
print(uim_installation_type)

fresh_common_variables = ['USER_INSTALL_DIR', 'DB_NORMALIZED_PROVIDER_NAME', 'DB_CREATE_MODE', 'DB_VERSION',
                          'DB_SERVER', 'DB_PORT', 'DB_NAME', 'DB_ADMIN_USERNAME', 'DB_ADMIN_PASSWD', 'NM_ADMIN_PASSWD',
                          'NMS_FIRST_PROBE_PORT', 'WASP_PORT_HTTP', 'TELEMETRY_UPLOAD_OPT_IN_FLAG']

upgrade_common_variables = ['NM_ADMIN_PASSWD', 'WASP_PORT_HTTP', 'TELEMETRY_UPLOAD_OPT_IN_FLAG']

sqlserver_db_variables = ['DB_AUTH_MODE', 'DB_ENABLE_TLS', 'DB_TRUST_STORE_PATH', 'DB_TRUST_STORE_PASSWD']

oracle_db_variables = ['DB_SERVICENAME', 'DB_TABLESPACENAME', 'DB_SYS_PASSWD', 'DB_ORACLE_INSTANTCLIENT_DIR',
                       'DB_WALLET_TYPE', 'DB_WALLET_STORE_PATH', 'DB_WALLET_STORE_PASSWD', 'DB_CLIENT_AUTH_NEEDED']

secure_bus_enabled_variables = ['TUNNEL_PORT', 'CA_CERT_PASSWD', 'CLIENT_CERT_PASSWD']

installer_properties = {'NMS_PRIMARY_ROBOT_NAME' : get_hostName_ip.get_hostname(), 'NMS_PRIMARY_HUB_NAME' : '{}_hub'.format(get_hostName_ip.get_hostname()), 'NMS_PRIMARY_HUB_IP': get_hostName_ip.get_ip(), 'NMS_DOMAIN' : '{}_domain'.format(get_hostName_ip.get_hostname()), 'ENABLE_SECURE_BUS': 'false'}


def get_installer_properties():

    # Checking UIM installation type (fresh/upgrade)
    if uim_installation_type == 'upgrade':
        print(' Selected uim_installation_type is : ', uim_installation_type)
        secure_bus_enable_input = str(input("Do you want to enable secure bus (true|false) :  ").strip().lower())
        ''' Writing installer_properties variables for upgrade installation'''
        for upgrade_variable in upgrade_common_variables:
            user_input = input("Provide {} value :  ".format(upgrade_variable)).strip().lower()
            print(user_input)
            # writing variables into installer_properties dictionary for upgrade scenario
            installer_properties[upgrade_variable] = user_input

        ''' Checking secure bus enabled or not true/false) '''
        if secure_bus_enable_input == 'true':
            installer_properties['ENABLE_SECURE_BUS'] = 'true'
            for secure_bus_variable in secure_bus_enabled_variables:
                secure_bus_input = input("Provide {} value :  ".format(secure_bus_variable)).strip().lower()
                print(secure_bus_input)
                installer_properties[secure_bus_variable] = secure_bus_input
            print(installer_properties)
        elif secure_bus_enable_input not in ['true', 'false']:
            print('Provided ENABLE_SECURE_BUS (true/false) is not correct, Given input is :', secure_bus_enable_input)
            exit()

    elif uim_installation_type == 'fresh':
        for variable in fresh_common_variables:
            user_input = input("Provide {} value :  ".format(variable)).strip().lower()
            print(user_input)
            # writing variables into installer_properties dictionary for fresh scenario
            installer_properties[variable] = user_input

            '''  adding DB specific variables to installer_properties dictionary  '''

        if installer_properties['DB_NORMALIZED_PROVIDER_NAME'] == 'sqlserver':
            print(installer_properties['DB_NORMALIZED_PROVIDER_NAME'])
            for sql_variable in sqlserver_db_variables:
                sql_user_input = input("Provide {} value :  ".format(sql_variable)).strip().lower()
                print(sql_user_input)
                installer_properties[sql_variable] = sql_user_input
        elif installer_properties['DB_NORMALIZED_PROVIDER_NAME'] == 'oracle':
            print(installer_properties['DB_NORMALIZED_PROVIDER_NAME'])
            for oracle_variable in oracle_db_variables:
                oracle_user_input = input("Provide {} value :  ".format(oracle_variable)).strip().lower()
                print(oracle_user_input)
                installer_properties[oracle_variable] = oracle_user_input

    elif uim_installation_type not in ['fresh', 'upgrade']:
        print('Provided ENABLE_SECURE_BUS (fresh/upgrade) is not correct, Given input is :', uim_installation_type)
        exit()
    print(installer_properties)
    # print(installer_properties['USER_INSTALL_DIR'])
    # creating installer.properties file and writing the variables
    with open(r"C:\sw\robot_install\installer.properties", "a+") as pfile:
        for key, value in installer_properties.items():
            # print(key, value)
            # writing all variables into installer.properties file
            pfile.write('{}={}\n'.format(key, value))
    pfile.close()  # closing the file


get_installer_properties()
