import hashlib

def generate_sha384(input):
    sha384 = hashlib.sha384()
    sha384.update(input.encode())
    return sha384.hexdigest()

input = "dawodu"
sha384_show = generate_sha384(input)
print(f"sha384 Hash: {sha384_show}")