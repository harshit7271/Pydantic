# when in pydantic we start using a model in another model as a Field that's called nested model
from pydantic import BaseModel

class Address(BaseModel):

    city: str
    state: str
    pin: str

class Patient(BaseModel):

    name: str
    gender: str
    age: int
    address: Address

address_dict = {
    'city': 'Varanasi', 
    'state': 'Uttar Pradesh', 
    'pin': '221008'
    }

address1 = Address(**address_dict)

patient_dict = {
    'name': 'Harshit Singh',
    'gender': 'male', 
    'age': 23, 
    'address': address1
    }
patient1 = Patient(**patient_dict)

 # exporting the model 
 
temp = patient1.model_dump()  # we can add dump(inclucde/exclude =['whatever we wanna call']) and also we can use patient1.model_dump_json() to convert in json file

print(temp)


# Better organization of related data (e.g., vitals, address, insurance)

# Reusability: Use Vitals in multiple models (e.g., Patient, MedicalRecord)

# Readability: Easier for developers and API consumers to understand

# Validation: Nested models are validated automatically—no extra work needed