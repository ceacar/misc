import io

def read_in_chunks(file_object: io.IOBase, chunk_size: int = 1024) -> 'Generator':
    """
	Lazy function read a file piece by piece.
    Default chunk size: 1k.
	"""
    while True:
        data = file_object.read(chunk_size)
        if not data:
            break
        yield data

