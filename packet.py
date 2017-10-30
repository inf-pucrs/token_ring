class Packet(object):
    """Datagram: 2345;naocopiado:Bob:Alice:Oi Mundo!"""
    """Datagram: iden;statuscopy;origin;destination;msg"""
    """          0   ;1         ;2     ;3          ;4"""

    def __init__(self, packet_type: int, origin_nick: str, dest_nick: str, text: str):
        self.packet_type = packet_type
        self.origin_nick = origin_nick
        self.dest_nick = dest_nick
        self.text = text
        self.has_been_read = False

    def is_token(self):
        if self.packet_type == 1234:
            return True
        elif self.packet_type == 2345:
            return False

    def read(self):
        self.has_been_read = True

    @staticmethod
    def assemble_token():
        return Packet(1234, '', '', '')

    def to_bytes(self):
        return bytes(str(self), 'utf-8')

    def _pprint(self):
        return "\n{}\n{}\n{}\n{}\n{}".format(self.packet_type, self.has_been_read, self.origin_nick, self.dest_nick, self.text)

    def __str__(self) -> str:
        return "{};{};{};{};{}".format(
            self.packet_type, self.has_been_read, self.origin_nick, self.dest_nick, self.text)


if __name__ == "__main__":
    pkt1 = Packet.assemble_token()
    assert pkt1.packet_type == 1234
    pkt2 = Packet(2345, 'me', 'him', 'Sample Text.')
    print(pkt2, pkt2._pprint())
