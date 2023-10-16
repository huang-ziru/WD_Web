$pythonroot = "C:\Python39"
$py = Join-Path -Path $pythonroot -ChildPath "python.exe"
$Project = "C:\p4\UIautomation\DesktopApem\testcase"
$testcase = Join-Path -Path $Project -ChildPath "AllTest.py"
$ResultFile = "C:\p4\UIautomation\DesktopApem\report\test.xml"
Set-Location -Path $Project
 Start-Process -FilePath $py -ArgumentList $testcase
 $process = Get-Process -Name "python"
while($process.Responding)
{
Start-Sleep -Seconds 10
  if(Test-Path -Path $ResultFile)
  {
  Stop-Process -Name "python"
    break
  }
 }