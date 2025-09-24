"""
{
    'name': 'Vinod',
    'age': 52,
    'emails': [
        'vinod@vinod.co',
        'vinod@xmpl.com'
    ]
}

<person>
    <name>Vinod</name>
    <age>52</age>
    <emails>
        <email>vinod@vinod.co</email>
        <email>vinod@xmpl.com</email>
    </emails>
</person>

"""

import xml.etree.ElementTree as et

def main():
    p1 = { 'name': 'Vinod', 'age': 52,
        'emails': [ 'vinod@vinod.co', 'vinod@xmpl.com', 'vinod@cyblore.com' ],
        'phone': {
            'personal': '9731424784',
            'official': '9844393934',
            'landline': '8092872722'
        }
    }

    p2 = et.Element('person')
    et.SubElement(p2, 'name').text = p1['name']
    et.SubElement(p2, 'age').text = str(p1['age'])
    emails = et.SubElement(p2, 'emails')

    for email in p1['emails']:
        et.SubElement(emails, 'email').text = email

    phone = et.SubElement(p2, 'phone')
    for k,v in p1['phone'].items():
        et.SubElement(phone, k).text = v

    et.indent(p2)
    print(et.tostring(p2, encoding='unicode', xml_declaration=True))

if __name__ == '__main__':
    main()
