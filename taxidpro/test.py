from main import TaxIDPro
import os
from dotenv import load_dotenv

load_dotenv()

taxidpro = TaxIDPro(api_key=os.getenv('API_KEY'))

print(taxidpro.validate(country='au', tin='92873837267', type='entity'))

print(taxidpro.lookup(country='au', tin='49004028077'))
