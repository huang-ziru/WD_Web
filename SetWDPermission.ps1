$pythonroot = "C:\Python39"
$py = Join-Path -Path $pythonroot -ChildPath "python.exe"
$Project = "C:\p4\WD_Web\WD"
$testcase = Join-Path -Path $Project -ChildPath "permission.py"
$ResultFile = "C:\p4\WD_Web\log.xml"
Set-Location -Path $Project
Start-Process -FilePath $py -ArgumentList $testcase
$process = Get-Process -Name "python"