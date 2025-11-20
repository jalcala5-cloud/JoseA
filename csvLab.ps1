# Import the employees.csv file
$employees = Import-Csv -Path "C:\powershell\employees.csv"

# Create a new array for the phone information
$phoneList = $employees | ForEach-Object {
    # Select only the properties we need
    [PSCustomObject]@{
        LastName  = $_.LastName
        FirstName = $_.FirstName
        Phone     = $_.PhoneNumber
    }
}

# Export the new array to phone.csv
$phoneList | Export-Csv -Path "C:\powershell\phone.csv" -NoTypeInformation
