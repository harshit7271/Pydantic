from pydantic import BaseModel, EmailStr, AnyUrl, Field, field_validator
from typing import List, Dict, Optional, Annotated

class Patient(BaseModel):

    name : str
    email : EmailStr
    age : int
    weight : float
    married : float
    allergies : List[str]
    contact_details : Dict[str,str]

    @field_validator('email')
    @classmethod
    def email_vgalidator(cls,value):

        valid_domains = ['hdfc.com', 'icici.com']
        # abc@gmail.com
        domain_name = value.split('@')[-1]

        if domain_name not in valid_domains:
            raise ValueError('Not a valid domain')
        
        return value

def update_patient_data(patient : Patient) :



