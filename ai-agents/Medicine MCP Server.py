# ==========================================
# Medicine MCP Server
# AI Medicine Reminder & Health Assistant
# ==========================================

from mcp.server.fastmcp import FastMCP


# Create MCP Server
mcp = FastMCP("Medicine Server")


# Medicine Database
medicine_db = {

    "metformin": {
        "name": "Metformin",
        "dosage": "500mg tablet twice daily with meals",
        "purpose": "Used for Type 2 Diabetes management",
        "warning": "Do not skip meals. Monitor blood sugar levels."
    },


    "lisinopril": {
        "name": "Lisinopril",
        "dosage": "10mg tablet once daily in the morning",
        "purpose": "Used for blood pressure management",
        "warning": "Monitor blood pressure regularly."
    },


    "aspirin": {
        "name": "Aspirin",
        "dosage": "81mg tablet once daily",
        "purpose": "Used for heart health protection",
        "warning": "May increase bleeding risk."
    },


    "paracetamol": {
        "name": "Paracetamol",
        "dosage": "500mg tablet as directed",
        "purpose": "Used for fever and mild pain relief",
        "warning": "Do not exceed recommended dosage."
    }
}



# MCP Tool
@mcp.tool()
def get_medication_info(medicine_name: str) -> str:
    """
    Get medicine dosage, purpose and warnings.
    
    Args:
        medicine_name:
            Name of the medicine
    """

    medicine_name = medicine_name.lower().strip()


    if medicine_name in medicine_db:

        medicine = medicine_db[medicine_name]


        return f"""
Medicine Name: {medicine['name']}

Dosage:
{medicine['dosage']}

Purpose:
{medicine['purpose']}

Warning:
{medicine['warning']}
"""


    return (
        f"Medicine '{medicine_name}' not found "
        "in the database. Please consult a doctor."
    )



# Tool for medicine list
@mcp.tool()
def get_available_medicines() -> list:
    """
    Returns available medicines in database.
    """

    return list(medicine_db.keys())



# Run MCP Server
if __name__ == "__main__":

    mcp.run(
        transport="stdio"
    )