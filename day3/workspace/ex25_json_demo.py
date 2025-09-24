from pprint import pprint
import json


def main():
    p1_json = """{
   "name": "Shyam Sundar",
   "age": 45,
   "married": true,
   "email": {
      "personal": "shyam@xmpl.com",
      "official": "shyamsundarkc@gmail.com"
   },
   "phones": [
      "9731424000",
      "9844083111"
   ]
}"""
    p1 = json.loads(p1_json)
    pprint(p1)
    print(f'{p1['name'] = }')
    print(f'{p1['age'] = }')
    print(f'{p1['married'] = }')
    print(f'{p1['email']['personal'] = }')
    print(f'{p1['email']['official'] = }')
    print(f'{p1['phones'][0] = }')
    print(f'{p1['phones'][1] = }')


def main_1():
    p1 = dict(name='Vinod', age=52, married=True)
    p1['email'] = dict(personal='vinod@xmpl.com', official='vinod@vinod.co')
    p1['phones'] = ['9731424784', '9844083934']

    pprint(p1)

    p1_json = json.dumps(p1, indent=3)
    print(p1_json)

if __name__ == '__main__':
    main()
