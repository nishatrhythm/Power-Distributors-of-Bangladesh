import json

def load_data():
    with open('data/distributors.json') as f:
        return json.load(f)

def get_distributors(data):
    return list(data.keys())

def get_company_details(data, company):
    return data.get(company.upper(), "Company not found")

if __name__ == "__main__":
    data = load_data()

    print("Available companies:")
    for company in get_distributors(data):
        print(company)

    company = input("Enter company name to get details: ").strip()
    details = get_company_details(data, company)
    print(json.dumps(details, indent=2))