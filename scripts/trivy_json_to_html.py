import json
import os
from jinja2 import Template

# -----------------------------
# Paths
# -----------------------------
workspace_dir = r"C:\ProgramData\Jenkins\.jenkins\workspace\Security Testing Skill 4"
reports_dir = os.path.join(workspace_dir, "reports")
json_file = os.path.join(reports_dir, "trivy-report.json")  # Correct file name
html_file = os.path.join(reports_dir, "trivy-report.html")

# -----------------------------
# Load JSON
# -----------------------------
with open(json_file, "r", encoding="utf-8") as f:
    data = json.load(f)

# -----------------------------
# HTML template
# -----------------------------
template_str = """
<html>
<head>
    <title>Trivy Security Report</title>
    <style>
        body { font-family: Arial, sans-serif; margin: 20px; }
        h1, h2, h3 { color: #2E4053; }
        table { border-collapse: collapse; width: 100%; margin-bottom: 20px; }
        th, td { border: 1px solid #ddd; padding: 8px; text-align: left; }
        th { background-color: #f2f2f2; }
        .low { background-color: #d4edda; }
        .medium { background-color: #fff3cd; }
        .high { background-color: #f8d7da; }
        .critical { background-color: #f5c6cb; }
        .na { background-color: #e2e3e5; }
    </style>
</head>
<body>
    <h1>Trivy Security Report</h1>
    <h2>Image: {{ image_name }}</h2>

    {% for result in results %}
        <h3>Target: {{ result.Target }}</h3>
        {% if result.Vulnerabilities %}
        <table>
            <tr>
                <th>Vulnerability ID</th>
                <th>Package Name</th>
                <th>Installed Version</th>
                <th>Severity</th>
                <th>Fixed Version</th>
                <th>Description</th>
            </tr>
            {% for vuln in result.Vulnerabilities %}
            <tr class="{{ vuln.Severity|lower if vuln.Severity else 'na' }}">
                <td>{{ vuln.VulnerabilityID }}</td>
                <td>{{ vuln.PkgName }}</td>
                <td>{{ vuln.InstalledVersion }}</td>
                <td>{{ vuln.Severity or 'N/A' }}</td>
                <td>{{ vuln.FixedVersion or 'N/A' }}</td>
                <td>{{ vuln.Description }}</td>
            </tr>
            {% endfor %}
        </table>
        {% else %}
            <p>No vulnerabilities found for this target ✅</p>
        {% endif %}
    {% endfor %}
</body>
</html>
"""

# -----------------------------
# Render HTML
# -----------------------------
template = Template(template_str)
html_content = template.render(
    image_name=data.get("ArtifactName", "Docker Image"),
    results=data.get("Results", [])
)

# -----------------------------
# Save HTML
# -----------------------------
with open(html_file, "w", encoding="utf-8") as f:
    f.write(html_content)

print(f"✅ Detailed HTML report generated at: {html_file}")
