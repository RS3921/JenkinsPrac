<html>
<head><title>Trivy Vulnerability Report</title></head>
<body>
<h1>Trivy Vulnerability Report</h1>
<table border="1">
<tr><th>Target</th><th>VulnerabilityID</th><th>PkgName</th><th>Severity</th><th>Description</th></tr>
{{ range .Results }}
  {{ range .Vulnerabilities }}
  <tr>
    <td>{{ $.Target }}</td>
    <td>{{ .VulnerabilityID }}</td>
    <td>{{ .PkgName }}</td>
    <td>{{ .Severity }}</td>
    <td>{{ .Description }}</td>
  </tr>
  {{ end }}
{{ end }}
</table>
</body>
</html>
