"""
ai_reasoner.py

AI reasoning engine for Mārga.
Analyzes a citizen's goal and recommends the required
government approvals, documents and estimated timelines.
"""

from typing import Dict


class AIReasoner:

    def __init__(self):

        self.business_rules = {
            "bakery": {
                "approvals": [
                    "Trade License",
                    "GST Registration",
                    "FSSAI License"
                ],
                "documents": [
                    "Aadhaar",
                    "PAN",
                    "Rental Agreement",
                    "Building Plan"
                ],
                "days": 14,
                "department": "Commerce"
            },

            "restaurant": {
                "approvals": [
                    "Trade License",
                    "GST Registration",
                    "FSSAI License",
                    "Fire NOC"
                ],
                "documents": [
                    "Aadhaar",
                    "PAN",
                    "Rental Agreement",
                    "Fire Safety Certificate"
                ],
                "days": 21,
                "department": "Commerce"
            },

            "shop": {
                "approvals": [
                    "Trade License",
                    "GST Registration"
                ],
                "documents": [
                    "Aadhaar",
                    "PAN",
                    "Rental Agreement"
                ],
                "days": 10,
                "department": "Revenue"
            },

            "building permit": {
                "approvals": [
                    "Municipality Approval",
                    "Engineering Review"
                ],
                "documents": [
                    "Building Plan",
                    "Ownership Proof",
                    "Tax Receipt"
                ],
                "days": 30,
                "department": "Engineering"
            }
        }

    def classify(self, goal: str):

        goal = goal.lower()

        for key in self.business_rules:

            if key in goal:
                return key

        return "general"

    def analyze(
        self,
        goal: str,
        state: str = "Kerala",
        business_type: str = ""
    ) -> Dict:

        category = business_type.lower().strip()

        if category == "":
            category = self.classify(goal)

        if category not in self.business_rules:

            return {
                "category": "General Service",
                "department": "Administration",
                "approvals": [],
                "documents": [],
                "estimated_days": 7,
                "confidence": 0.60,
                "next_step": "Submit request for manual review."
            }

        info = self.business_rules[category]

        return {

            "category": category.title(),

            "department": info["department"],

            "approvals": info["approvals"],

            "documents": info["documents"],

            "estimated_days": info["days"],

            "confidence": 0.95,

            "next_step":
                f"Begin with {info['approvals'][0]}."
        }

from flask import Flask, jsonify

app = Flask(__name__)

@app.route('/api/get-workflow', methods=['GET'])
def get_workflow():
    # This matches the structure your WorkflowGraph expects
    return jsonify({
        "nodes": [
            {"id": 1, "label": "Document Submission", "status": "Completed", "department": "Revenue"},
            {"id": 2, "label": "Verification", "status": "Pending", "department": "Admin"}
        ],
        "edges": [
            {"from": 1, "to": 2}
        ]
    })

if __name__ == '__main__':
    app.run(port=5000)
