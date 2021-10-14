import json

from generate import generate

if __name__ == '__main__':
    with open('./templates/sample.json', 'r') as f:
        s = f.read()
        template = json.loads(s)
        print(json.dumps(generate(template), indent=4))
        with open('./output/output.txt','w') as o:
            o.write(json.dumps(generate(template), indent=4))

