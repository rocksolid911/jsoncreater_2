import json
import sys

from generate import generate

if __name__ == '__main__':
    in_path = sys.argv[1]
    out_path = sys.argv[2]
    # For windows path use double \\ after each directory
    # like C:\\user\\Documents\\any_folder\\file_name.json

    with open(in_path, 'r') as f:
        s = f.read()
        template = json.loads(s)
        print(json.dumps(generate(template), indent=4))
        with open(out_path, 'w') as o:
            o.write(json.dumps(generate(template), indent=4))
