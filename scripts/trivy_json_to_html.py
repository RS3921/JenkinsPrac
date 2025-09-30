import json
import sys
import os

def convert_trivy_json_to_html(json_file, html_file):
    # Check if input file exists
    if not os.path.exists(json_file):
        print(f"[ERROR] Trivy JSON file not found: {json_file}")
        sys.exit(1)

    # Load JSON
    with open(json_file, "r", encoding="utf-8") as f:
        try:
            data = json.load(f)
        except json.JSONDecodeError as e:
            print(f"[ERROR] Failed to parse JSON: {e}")
            sys.exit(1)

    # Start HTML
    html_content = """
    <html>
    <head>
        <title>Trivy Scan Report</title>
        <style>
            body { font-family: Arial, sans-serif; padding: 20px; }
            h1 { color: #333; }
            table { width: 100%; border-collapse: collapse; margin-top: 20px; }
            th, td { border: 1px solid #ccc; padding: 8px; text-align: left; }
            th { background: #eee; }
            tr:nth-child(even) { background: #f9f9f9; }
            .HIGH { background-color: #ffcccc; }
            .MEDIUM { background-color: #fff2cc; }
            .LOW { background-color: #ccffcc; }
        </style>
    </head>
    <body>
        <h1>Trivy Security Scan Report</h1>
        <table>
            <tr>
                <th>Target</th>
                <th>Vulnerability ID</th>
                <th>Pkg Name</th>
                <th>Installed Version</th>
                <th>Fixed Version</th>
                <th>Severity</th>
                <th>Description</th>
            </tr>
    """

    # Extract results
    for result in data.get("Results", []):
        target = result.get("Target", "Unknown")
        for vuln in result.get("Vulnerabilities", []):
            vuln_id = vuln.get("VulnerabilityID", "N/A")
            pkg_name = vuln.get("PkgName", "N/A")
            installed = vuln.get("InstalledVersion", "N/A")
            fixed = vuln.get("FixedVersion", "N/A")
            severity = vuln.get("Severity", "UNKNOWN")
            description = vuln.get("Description", "No description available")

            html_content += f"""
            <tr class="{severity}">
                <td>{target}</td>
                <td>{vuln_id}</td>
                <td>{pkg_name}</td>
                <td>{installed}</td>
                <td>{fixed}</td>
                <td>{severity}</td>
                <td>{description[:200]}...</td>
            </tr>
            """

    # Close HTML
    html_content += """
        </table>
    </body>
    </html>
    """

    # Save output
    os.makedirs(os.path.dirname(html_file), exist_ok=True)
    with open(html_file, "w", encoding="utf-8") as f:
        f.write(html_content)

    print(f"[SUCCESS] HTML report generated at: {html_file}")


if __name__ == "__main__":
    if len(sys.argv) != 3:
        print("Usage: python trivy_json_to_html.py <input_json> <output_html>")
        sys.exit(1)

    json_file = sys.argv[1]
    html_file = sys.argv[2]

    convert_trivy_json_to_html(json_file, html_file)
