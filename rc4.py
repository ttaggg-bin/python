

class Rc4:
    def __init__(self, key=b''):
        self.key = key
        self.state = bytearray([0] * 256)
        for i in range(0, 256):
            self.state[i] = i

        j = 0
        for i in range(0, 256):
            j = (j + self.state[i] + key[i % len(key)]) % 256
            self.state[i], self.state[j] = self.state[j] , self.state[i]

    def update(self, data):
        length = len(data)
        result = bytearray([0] * length)
        a = j = 0
        for i in range (0, length):
            a = (a + 1) % 256
            j = (j + self.state[a]) % 256
            self.state[a], self.state[j] = self.state[j], self.state[a]
            c = data[i] ^ self.state[(self.state[a] + self.state[j]) % 256]
            result[i] = c

        return result

