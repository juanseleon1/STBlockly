# -*- coding: utf-8 -*-
"""Collection of actions sent to robot through the ardublocklyserver for relieved HTTP requests.

Copyright (c) 2017 IQBots 
"""
from __future__ import unicode_literals, absolute_import, print_function


def send_code_to_robot(robot_action, socket_mgmt):
    """
    Handles Robot Connection and maessage lifecycle.
    - robot_action: robot information and action description.
    - socket_mgmt: Socket manager interface.
    """
    success = True
    ide_mode = 'unknown'
    std_out, err_out = '', ''
    exit_code = 0
    try:
        ip = robot_action['ip']
        if "emomsg" in robot_action:
            print(robot_action['emomsg'], "emotionText")
            socket_mgmt.send_msg(ip,robot_action['emomsg'])
        if "msg" in robot_action:
            success = socket_mgmt.send_msg(ip,robot_action['msg'],robot_action['ack'])
        if not success:
                err_out = 'ACK recibido es erroneo'
                exit_code = 101
    except Exception:
        success = False
        exit_code = 102
        err_out = 'Conexion con el robot fallida. Revisa la ip configurada o la red.'

    return success, ide_mode, std_out, err_out, exit_code


