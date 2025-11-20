Write-Host("Hello world")

# filesLab.ps1

# Name: Jose Alcala 
# Date: 11/20/2025
# Class: CIS 188

# Lab – Move PDFs and Images

# Set the working directory to the folder that contains all the subfolders/files
$basePath = "C:\powershell"

Set-Location $basePath

# Create destination folders if they do not exist
$pdfFolder = Join-Path $basePath "pdf"
$imgFolder = Join-Path $basePath "images"

if (-not (Test-Path $pdfFolder)) {
    New-Item -ItemType Directory -Path $pdfFolder | Out-Null
}

if (-not (Test-Path $imgFolder)) {
    New-Item -ItemType Directory -Path $imgFolder | Out-Null
}

Write-Output "PDF and images folders created (if not already present)."

# Get all files in all subdirectories
$allFiles = Get-ChildItem -Recurse -File

foreach ($file in $allFiles) {

    # Move PDFs
    if ($file.Extension -eq ".pdf") {
        Write-Output "Moving PDF: $($file.FullName)"
        Move-Item -Path $file.FullName -Destination $pdfFolder
    }

    # Move image files (jpg, jpeg, png, gif)
    elseif ($file.Extension -in (".jpg", ".jpeg", ".png", ".gif")) {
        Write-Output "Moving Image: $($file.FullName)"
        Move-Item -Path $file.FullName -Destination $imgFolder
    }
}

Write-Output "Done! All PDF and image files have been moved."
