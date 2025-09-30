import json
import sys
import os

def convert_trivy_json_to_html(input_file, output_file):
    # Ensure input file exists
    if not os.path.exists(input_file):
        print(f"❌ Input file not found: {input_file}")
        sys.exit(1)

    # Load Trivy JSON report
    with open(input_file, "r") as f:
        data = json.load(f)

    # Start building HTML
    html = """
    <html>
    <head>
        <title>Trivy Scan Report</title>
        <style>
            body { font-family: Arial, sans-serif; margin: 20px; }
            h1 { color: #2c3e50; }
            table { border-collapse: collapse; width: 100%; }
            th, td { border: 1px solid #ccc; padding: 8px; text-align: left; }
            th { background-color: #f4f4f4; }
            tr:nth-child(even) { background-color: #f9f9f9; }
        </style>
    </head>
    <body>
        <h1>Trivy Scan Report</h1>
        <table>
            <tr>
                <th>Vulnerability ID</th>
                <th>Pkg Name</th>
                <th>Installed Version</th>
                <th>Fixed Version</th>
                <th>Severity</th>
                <th>Title</th>
            </tr>
    """

    # Parse vulnerabilities
    for result in data.get("Results", []):
        for vuln in result.get("Vulnerabilities", []):
            html += f"""
            <tr>
                <td>{vuln.get('VulnerabilityID', '')}</td>
                <td>{vuln.get('PkgName', '')}</td>
                <td>{vuln.get('InstalledVersion', '')}</td>
                <td>{vuln.get('FixedVersion', '')}</td>
                <td>{vuln.get('Severity', '')}</td>
                <td>{vuln.get('Title', '')}</td>
            </tr>
            """

    html += """
        </table>
    </body>
    </html>
    """

    # Write output HTML
    os.makedirs(os.path.dirname(output_file), exist_ok=True)
    with open(output_file, "w", encoding="utf-8") as f:
        f.write(html)

    print(f"✅ HTML report generated at {output_file}")


if __name__ == "__main__":
    if len(sys.argv) != 3:
        print("Usage: python trivy_json_to_html.py <input_json> <output_html>")
        sys.exit(1)

    input_file = sys.argv[1]
    output_file = sys.argv[2]
    convert_trivy_json_to_html(input_file, output_file)
