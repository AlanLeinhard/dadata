import xml.etree.ElementTree as ET
tree = ET.parse('adrobj.xml')
root = tree.getroot()

for child in root.findall('OBJECT'):
    name = child.get('NAME')
    id = child.get('ID')
    aoguid = child.get('OBJECTGUID')
    formalname = child.get('NAME')
    streetcode = child.get('NAME')
    offname = child.get('NAME')
    shortname = child.get('SHORTNAME')
    aoid = child.get('NAME')
    plaincode = child.get('NAME')
    divtype = child.get('NAME')
    print(child.tag, child.attrib)



# import xml.etree.ElementTree as etree








# tree = etree.parse("./adrobj.xml")
# root = tree.getroot()

# for child in root:
#     print(child.tag)
#     print(child.keys())
#     print(child.items())







# import subprocess

# from app.models import Post, Project, db, User, Role, roles_users, Item

# import psycopg2
# from psycopg2 import sql
# from psycopg2.extensions import ISOLATION_LEVEL_AUTOCOMMIT # <-- ADD THIS LINE
# import psycopg2
# import sys
# from lxml import etree

# con = psycopg2.connect(dbname='postgres',
#       user='postgres', host='localhost',
#       password='postgres')

# con.set_isolation_level(ISOLATION_LEVEL_AUTOCOMMIT) # <-- ADD THIS LINE

# cursor = con.cursor()


# parser = etree.parse("AS.XML")


# root = etree.parse("AS.XML")
# for i in root.findall("item"):
#     p = [i.find(n).text for n in ("TYPENAME", "NAME", "LEVEL", "LEVEL", "LEVEL")]
#     # now you get list with values of parameters

#     postgres = ('INSERT INTO epg_live (program, start, duration) VALUES (%s, %s, %s)', p)
#     cursor.execute(parser,postgres)
#     cursor.commit()
