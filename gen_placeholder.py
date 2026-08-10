import zlib, struct, os

def write_png(path, w, h, rgb):
    def chunk(typ, data):
        c = struct.pack('>I', len(data)) + typ + data
        c += struct.pack('>I', zlib.crc32(typ + data) & 0xffffffff)
        return c
    raw = b''.join(b'\x00' + bytes(rgb) * w for _ in range(h))
    png = b'\x89PNG\r\n\x1a\n'
    png += chunk(b'IHDR', struct.pack('>IIBBBBB', w, h, 8, 2, 0, 0, 0))
    png += chunk(b'IDAT', zlib.compress(raw, 9))
    png += chunk(b'IEND', b'')
    open(path, 'wb').write(png)
    print(path, w, 'x', h, os.path.getsize(path), 'bytes')

write_png('og-cover.png', 1200, 630, (26, 43, 74))
write_png('screenshot.png', 1080, 608, (238, 242, 248))
