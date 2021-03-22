import socket
import pickle
HEADER_LENGTH = 20
PACKET_LENGTH = 10
ENCODING = 'utf-8'

def sendMsg( _msg, connection ):
    try:
        msg_in_bytes = pickle.dumps(_msg)
        msg_len = len(msg_in_bytes)
        header_to_send = '{header:<20}'.format(header=msg_len)
        connection.send( header_to_send.encode(ENCODING) )
        connection.send( msg_in_bytes )
    except:
        print("Problem with msg pickling...")

def readMsg( connection: socket ):
    data = b''
    decoded_data = ''
    msg_len = connection.recv( HEADER_LENGTH )
    if( msg_len ):
        msg_len = int( msg_len.decode(ENCODING) )
        while True:
            if(msg_len > PACKET_LENGTH):
                data += connection.recv( PACKET_LENGTH )
                msg_len -= PACKET_LENGTH
            else:
                data += connection.recv( msg_len )
                break
        return pickle.loads(data)
