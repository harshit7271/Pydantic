# FIELD VALIDATOR WORKS ON ONE SINGLE FIELD ONLY AT A TIME

from pydantic import BaseModel, EmailStr, AnyUrl, Field, field_validator
from typing import List, Dict, Optional, Annotated

class Patient(BaseModel):

    name : str
    email : EmailStr
    age : int
    weight : float
    married: bool = Field(default=False)
    allergies : List[str]
    contact_details : Dict[str,str]

    @field_validator('email')
    @classmethod
    def email_validator(cls,value):

        valid_domains = ['hdfc.com', 'icici.com']
        # abc@gmail.com
        domain_name = value.split('@')[-1]

        if domain_name not in valid_domains:
            raise ValueError('Not a valid domain')
        
        return value
    
    # If we want the names to be in capital only 

    @field_validator('name')
    @classmethod
    def transfor_name(cls,value) : 
        return value.upper()
    
    @field_validator('age', mode='after')
    @classmethod
    def validate_age(cls,value):
        if 0 < value < 100 :
            return value
        else :
            raise ValueError('Age should be in between 0 and 100')

        
def update_patient_data(patient : Patient):
    print(patient.name)
    print(patient.age)
    print(patient.allergies)
    print(patient.married)
    print('updated')


patient_info = {
    'name' : 'HARSHIT SINGH',
    'email' : 'abc@icici.com',
    'age' : '23',
    'weight' : 75.8,
    'allergies' : ['eggs', 'cigrettes'],
    'contact_details' : {
        'phone' : '1234567'
    }
}

patient1 = Patient(**patient_info)

update_patient_data(patient1)


