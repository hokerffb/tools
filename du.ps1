# Set-ExecutionPolicy UnRestricted

function GetBarStr($max, $size)
{
    "=------------>"
    $max
    $size
    "<------------="
    $count = $size * 80 / $max
    $r = ""
    For ($i=0; $i -le $count; $i++) {
        $r = $r + "#"
    }
    return "##########"
}

function filesize ()
{
    
    [string]$filepath = Read-Host "Path"
    $sortedlength = @{ }
    $sorted = @{ }
    if ($filepath -eq $null)
    {
        throw "Error"
    }

    dir -Path $filepath |
    ForEach-Object -Process {
        if ($_.psiscontainer -eq $true)
        {
            $length = 0
            $name=$_.name
            dir -Path $_.fullname -Recurse | ForEach-Object{
                [long]$length += $_.Length
            }
            $sortedlength.Add($name,$length)
        }
    }
    
    $sorted=$sortedlength.GetEnumerator() | Sort-Object value -Descending
    $max = 0
    foreach ($a in $sorted.GetEnumerator())
    {
        if ($a.Value -gt $max) {
            $max = $a.Value
        }
        if ($a.Value -ge 1GB)
        {
            $l = $a.Value/1GB
            $a.Key + " {0:n1} GB" -f $l
        }
        elseif ($a.Value -ge 1MB)
        {
            $l = $a.Value/1MB
            #$a.Key + " {0:n1} MB" -f $l
            $bar = GetBarStr($max, $a.Value)
            $a.Key + " {0:n1} MB {1}" -f ($l, $bar)
        }
        else
        {
            $l = $a.Value/1KB
            $a.Key + " {0:n1} KB" -f $l
        }
    }

}
filesize

# Pause