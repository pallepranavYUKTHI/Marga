import json
import os

BASE_DIR = os.path.dirname(__file__)
KNOWLEDGE_DIR = os.path.join(BASE_DIR, "..", "knowledge")
WORKFLOW_DIR = os.path.join(BASE_DIR, "..", "workflows")


def load_json(filename, folder=KNOWLEDGE_DIR):
    with open(os.path.join(folder, filename), "r", encoding="utf-8") as f:
        return json.load(f)


# Load datasets
SERVICES = load_json("government_services.json")
LICENSES = load_json("license_database.json")
DEPARTMENTS = load_json("department_mapping.json")
DOCUMENTS = load_json("document_requirements.json")
TIMES = load_json("processing_times.json")
FEES = load_json("fee_database.json")
CATEGORIES = load_json("business_categories.json")

WORKFLOWS = load_json("startup_workflows.json", WORKFLOW_DIR)
DEPENDENCIES = load_json("dependency_rules.json", WORKFLOW_DIR)


def get_business_advice(business_name):
    """
    Returns complete workflow knowledge for a business.
    """

    if business_name not in LICENSES:
        return {
            "success": False,
            "message": f"No knowledge available for '{business_name}'."
        }

    license_info = LICENSES[business_name]
    workflow = WORKFLOWS.get(business_name, {})

    result = {
        "success": True,
        "business": business_name,
        "category": license_info.get("category"),
        "description": license_info.get("description"),
        "estimated_setup_days": license_info.get("estimated_setup_days"),
        "estimated_setup_cost": license_info.get("estimated_setup_cost"),
        "risk_level": license_info.get("risk_level"),
        "licenses": []
    }

    total_fee = 0

    for license_name in license_info["required_licenses"]:

        department = DEPARTMENTS.get(license_name, {})
        docs = DOCUMENTS.get(license_name, [])
        timing = TIMES.get(license_name, {})
        fee = FEES.get(license_name, {})
        dependency = DEPENDENCIES.get(license_name, {})

        govt_fee = fee.get("government_fee", 0)
        service_fee = fee.get("service_charge", 0)

        total_fee += govt_fee + service_fee

        result["licenses"].append({

            "license": license_name,

            "department": department.get("department_name"),

            "government_level": department.get("government_level"),

            "portal": department.get("portal"),

            "processing_days": timing.get("average_days"),

            "delay_risk": timing.get("delay_risk"),

            "documents": docs,

            "government_fee": govt_fee,

            "service_charge": service_fee,

            "depends_on": dependency.get("required_before", []),

            "parallel_with": dependency.get("can_run_parallel_with", []),

            "recommendation": dependency.get("recommendation", "")
        })

    result["estimated_government_cost"] = total_fee

    result["workflow"] = workflow

    return result