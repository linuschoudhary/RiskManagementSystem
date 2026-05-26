from Model import model
from hashing import Hash



default_risks = [
    {
        "risk_description": "Unauthorized access to admin dashboard",
        "risk_priority": "High",
        "risk_status": "Open",
        "user_id": 1,
        "risk_type": "Security"
    },
    {
        "risk_description": "Database backup failure",
        "risk_priority": "Critical",
        "risk_status": "In Progress",
        "user_id": 2,
        "risk_type": "Infrastructure"
    },
    {
        "risk_description": "Delayed software deployment",
        "risk_priority": "Medium",
        "risk_status": "Open",
        "user_id": 3,
        "risk_type": "Operational"
    },
    {
        "risk_description": "Sensitive customer data leakage",
        "risk_priority": "Critical",
        "risk_status": "Mitigated",
        "user_id": 4,
        "risk_type": "Compliance"
    },
    {
        "risk_description": "Server downtime during peak traffic",
        "risk_priority": "High",
        "risk_status": "Monitoring",
        "user_id": 5,
        "risk_type": "Infrastructure"
    },
    {
        "risk_description": "Third-party API outage",
        "risk_priority": "Medium",
        "risk_status": "Open",
        "user_id": 2,
        "risk_type": "External"
    },
    {
        "risk_description": "Phishing attack targeting employees",
        "risk_priority": "High",
        "risk_status": "In Progress",
        "user_id": 1,
        "risk_type": "Security"
    },
    {
        "risk_description": "Failure in payment gateway integration",
        "risk_priority": "High",
        "risk_status": "Open",
        "user_id": 3,
        "risk_type": "Operational"
    }
]

default_users = [
    {
        "user_name": "Dipesh Soni",
        "user_role": "Employee",
        "user_email": "dipesh@gmail.com",
        "user_password": "dipesh123"
    },
    {
        "user_name": "Mohit Solanki",
        "user_role": "Manager",
        "user_email": "mohit@gmail.com",
        "user_password": "mohit123"
    },
    {
        "user_name": "Sanya Singh Deora",
        "user_role": "Employee",
        "user_email": "sanya@gmail.com",
        "user_password": "sanya"
    },
    {
        "user_name": "Priyanjali Bhati",
        "user_role": "Employee",
        "user_email": "priyanjali@gmail.com",
        "user_password": "priyanjali123"
    },
    {
        "user_name": "Prateeksha Khichi",
        "user_role": "Admin",
        "user_email": "prateeksha@gmail.com",
        "user_password": "prateeksha123"
    },
    {
        "user_name": "Sunil Choudhary",
        "user_role": "Admin",
        "user_email": "sunil@gmail.com",
        "user_password": "sunil123"
    }
]

def addALL(db):
    for user in default_users:
        new_user = model.User(
            user_name = user["user_name"],
            user_role = user["user_role"],
            user_email = user["user_email"],
            user_password = Hash.bcryptPassword(user["user_password"])
        )
        db.add(new_user)
        db.commit()
        db.refresh(new_user)

    for risk in default_risks:
        new_risk = model.Risk(
            risk_description = risk["risk_description"],
            risk_priority = risk["risk_priority"],
            risk_status = risk["risk_status"],
            user_id = risk["user_id"],
            risk_type = risk["risk_type"]
        )
        db.add(new_risk)
        db.commit()
        db.refresh(new_risk)