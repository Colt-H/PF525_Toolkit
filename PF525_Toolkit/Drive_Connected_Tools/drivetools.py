from pycomm3 import CIPDriver, Services, INT
#from pycomm3.logger import logging, LOG_VERBOSE

def connection_setup():
    print("Are you connecting through a PLC or directly to drive? (P)LC or (D)rive")
    connection_type = input('>>> ')
    if connection_type.lower() == 'p':
        print("Enter PLC IP Address:")
        plc_ip = input('>>> ')
        print("Enter communication card backplane slot:")
        bp_slot = input('>>> ')
        print("Enter Drive IP Address:")
        drive_ip = input('>>> ')

        drive_path = plc_ip + '/bp/' + bp_slot + '/enet/' + drive_ip

        print("Drive set up as: " + drive_path)

        return drive_path, connection_type

    elif connection_type.lower() == 'd':
        print("Enter Drive IP Address:")
        drive_ip = input('>>> ')

        drive_path = drive_ip

        print("Drive set up as: " + drive_path)

        return drive_path, connection_type

def read_params():
    connection = connection_setup()
    drive_path = connection[0]
    conn_type = connection[1]
    if conn_type == 'p':
        connected_send = False
        unconnected_send = True
        route_path = False
    elif conn_type == 'd':
        connected_send = True
        unconnected_send = False
        route_path = True

    print("Enter a parameter to read:")
    param_to_read = input('>>> ')

    with CIPDriver(drive_path) as drive:
        param = drive.generic_message(
            service=Services.get_attribute_single,
            class_code=b'\x93',
            instance=int(param_to_read),
            attribute=b'\x09',
            data_type=INT,
            connected=connected_send,
            unconnected_send=unconnected_send,
            route_path=route_path,
            name='PF525_Param'
        )
        print(param)

def write_params():
    drive_path = connection_setup()
    print(drive_path[0])

def drive_tools_main():
    print("Choose an Option:\n(1) Read Drive Parameters\n(2) Write Drive Parameters")
    selection = input('>>> ')
    if selection == '1':
        read_params()
    elif selection == '2':
        write_params()
    elif selection.lower() == 'q':
        return
