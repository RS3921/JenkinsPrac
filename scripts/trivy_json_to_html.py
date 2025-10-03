import json, html

with open("reports/trivy-report.json") as f:
    data = json.load(f)

html_content = "<html><head><title>Trivy Report</title></head><body>"
html_content += "<h1>Trivy Vulnerability Report</h1>"

for result in data.get("Results", []):
    target = result.get("Target", "Unknown")
    html_content += f"<h2>Target: {html.escape(target)}</h2>"
    vulnerabilities = result.get("Vulnerabilities", [])
    if vulnerabilities:
        html_content += "<table border='1'><tr><th>ID</th><th>PkgName</th><th>Installed Version</th><th>Severity</th><th>Description</th></tr>"
        for vuln in vulnerabilities:
            html_content += "<tr>"
            html_content += f"<td>{html.escape(vuln.get('VulnerabilityID',''))}</td>"
            html_content += f"<td>{html.escape(vuln.get('PkgName',''))}</td>"
            html_content += f"<td>{html.escape(vuln.get('InstalledVersion',''))}</td>"
            html_content += f"<td>{html.escape(vuln.get('Severity',''))}</td>"
            html_content += f"<td>{html.escape(vuln.get('Description',''))}</td>"
            html_content += "</tr>"
        html_content += "</table>"
    else:
        html_content += "<p>No vulnerabilities found.</p>"

html_content += "</body></html>"

with open("reports/trivy_report.html", "w") as f:
    f.write(html_content)
