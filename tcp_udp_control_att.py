def tcp_or_udp_check(port_number=int):
    try:
        Port_Result_TCP = socket.getservbyport(port_number,"tcp")
        Result_Port = Port_Result_TCP
        return Result_Port + " " +"TCP"
    except:
        pass
    try:
        Port_Result_UDP = socket.getservbyport(port_number,"udp")
        Result_Port = Port_Result_UDP
        return Result_Port + " " +"UDP"
    except:
        Result_Port = "NOT FOUND"
        return Result_Port
        pass
