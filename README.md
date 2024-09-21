# Tax ID Validation Library

Tax ID Pro allows you to quickly integrate tax ID validation into your existing applications and workflows. You can validate over 200 different tax ID formats for over 100 countries. Tax ID Pro ensures your system can handle the diverse tax identification needs of your international customer base.

Lookup is available for VAT Numbers from the European Union (EU), plus the United Kingdom and Australia. Tax ID Pro provides a simple way to check the validity of VAT numbers and ensure compliance with EU regulations.

### Install

```bash
pip install taxidpro
```

### Usage

Provide your API key to the `TaxIDPro` class. You can obtain an API key by signing up at [Tax ID Pro](https://taxid.pro/).

```py
from taxidpro import TaxIDPro

taxidpro = TaxIDPro('YOUR_API_KEY')

taxidpro.validate(
  country='au',
  tin='92873837267',
  type='entity'
)

# Output:
#
# {
#   "is_valid": true,
#   "message": null,
#   "tin_compact": "92873837267",
#   "tin_standard": "92 873 837 267",
#   "country_name": "Australia",
#   "format_name": "Business Number"
# }

taxidpro.lookup(
  country='au',
  tin='49004028077'
)

# Output:
#
# {
#   country_name: 'Australia',
#   tin_compact: '49004028077',
#   tin_standard: '49 004 028 077',
#   format_name: 'Business Number',
#   is_valid: true,
#   message: null,
#   lookup_data: { name: 'BHP GROUP LIMITED', address: '3000 VIC' }
# }
```
