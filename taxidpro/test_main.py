from .main import TaxIDPro
import os
from dotenv import load_dotenv

load_dotenv()

taxidpro = TaxIDPro(api_key=os.getenv('API_KEY'))


def test_validate():
    output = taxidpro.validate(country='au', tin='92873837267', type='entity')
    assert output['is_valid'] == True
    assert output['message'] == None
    assert output['country_name'] == 'Australia'
    assert output['tin_compact'] == '92873837267'
    assert output['tin_standard'] == '92 873 837 267'
    assert output['format_name'] == 'Business Number'


# {
#   "is_valid": True,
#   "message": None,
#   "country_name": "Australia",
#   "format_name": "Business Number"
#   "tin_compact": "92873837267",
#   "tin_standard": "92 873 837 267",
# }

def test_lookup():
    output = taxidpro.lookup(country='au', tin='49004028077')
    assert output['is_valid'] == True
    assert output['message'] == None
    assert output['country_name'] == 'Australia'
    assert output['format_name'] == 'Business Number'
    assert output['tin_compact'] == '49004028077'
    assert output['tin_standard'] == '49 004 028 077'
    assert output['lookup_data']['name'] == 'BHP GROUP LIMITED'
    assert output['lookup_data']['address'] == '3000 VIC'


# Output:
#
# {
#   is_valid: True,
#   message: None,
#   country_name: 'Australia',
#   format_name: 'Business Number',
#   tin_compact: '49004028077',
#   tin_standard: '49 004 028 077',
#   lookup_data: { name: 'BHP GROUP LIMITED', address: '3000 VIC' }
# }
