import requests
import json

url = "http://localhost:3002/legalData/legalCase"

payload = json.dumps({
  "resolution_type": "resolution_type",
  "resolution_number": "resolution_number",
  "resolution_year": "resolution_year",
  "resolution_BIS": "resolution_BIS",
  "registration_date": "registration_date",
  "numeric_type": "numeric_type",
  "register_type": "register_type",
  "language": "language",
  "descriptive_synthesis": "descriptive_synthesi",
  "analytic_synthesis": "analytic_synthesis",
  "boe_number": "boe_number",
  "boe_date": "boe_date",
  "green_tome_number": "green_tome_number",
  "signature_date": "signature_date",
  "boe_reference": "boe_reference",
  "case_id": "case_id",
  "xml_boe_corrections": "xml_boe_corrections",
  "last_update": "last_update",
  "content_irrelevant_for_internet": "content_irrelevant_for_internet",
  "cache_date": "cache_date"
})
headers = {
  'Content-Type': 'application/json'
}

response = requests.post(url, headers=headers, data=payload)

print(response.text)