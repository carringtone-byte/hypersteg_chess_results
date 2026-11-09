& "$PSScriptRoot\..\.venv\Scripts\python.exe" -m hypersteg.cli smoke
if ($LASTEXITCODE -ne 0) { exit $LASTEXITCODE }
& "$PSScriptRoot\..\.venv\Scripts\python.exe" -m hypersteg.cli run-mock --condition C1
exit $LASTEXITCODE
