<html>
<head><title>Trivy Vulnerability Report</title></head>
<body>
<h1>Trivy Vulnerability Report</h1>
{{ range .Artifacts }}
  <h2>Target: {{ .Target }}</h2>
  {{ if .Vulnerabilities }}
  <table border="1">
    <tr>
      <th>ID</th>
      <th>PkgName</th>
      <th>Installed Version</th>
      <th>Severity</th>
      <th>Description</th>
    </tr>
    {{ range .Vulnerabilities }}
    <tr>
      <td>{{ .VulnerabilityID }}</td>
      <td>{{ .PkgName }}</td>
      <td>{{ .InstalledVersion }}</td>
      <td>{{ .Severity }}</td>
      <td>{{ .Description }}</td>
    </tr>
    {{ end }}
  </table>
  {{ else }}
  <p>No vulnerabilities found.</p>
  {{ end }}
{{ end }}
</body>
</html>
