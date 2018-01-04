from mongoengine import *
connect('Labdataexchange')

class Organization(Document):
    org_name = StringField(max_length=40, required=True)
    org_type = StringField(max_length=40)
    department = StringField(max_length=40)
    tax_id = StringField(max_length=13)
    size = StringField(max_length=5)
    house_number = StringField(max_length=5)
    street = StringField(max_length=30)
    subdistrict = StringField(max_length=30)
    district = StringField(max_length=30)
    province = StringField(max_length=30)
    postal_code = StringField(max_length=5, required=True)

class Person(Document):
    first_name = StringField(max_length=20, required=True)
    last_name = StringField(max_length=20, required=True)
    email = StringField(required=True)
    licence_id = StringField(max_length=10)
    affiliation = ReferenceField(Organization)

mt = Organization(org_name= 'Faculty of Medical Technology', postal_code= '73170')
mt.org_type = 'Academic'
mt.department = 'Community Medical Technology'
mt.house_number = '9'
mt.street = 'Phutthamonthon Sai 4'
mt.subdistrict = 'Salaya'
mt.district = 'Phutthamonthon'
mt.province = 'Nakhonpathom'
mt.save()

sittha = Person(first_name= 'Sittha', last_name= 'Maneemas', email= 'sittha_maneemas@yahoo.com')
sittha.licence_id = '10532'
sittha.affiliation = mt
sittha.save()



