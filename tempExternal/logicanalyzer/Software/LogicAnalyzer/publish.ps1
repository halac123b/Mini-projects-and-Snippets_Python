# Require arg string packageVersion
param (
    [Parameter(Mandatory=$true)]
    [string]$packageVersion
)

# Names of files to be published (an array)
$projectNames = @("LogicAnalyzer", "TerminalCapture")
$mergedName = "all-in-one_$packageVersion"

# Create the packages folder if it doesn't exist
$packagesDir = "..\Packages"
if (-not (Test-Path $packagesDir)) {    # Check if the directory exists
    New-Item -ItemType Directory -Path $packagesDir
}

# Clean the subfolders of the packages folder
Get-ChildItem -Path $packagesDir -Directory | Remove-Item -Recurse -Force

# Create the merge folder if it doesn't exist
$mergedDir = "..\Merged"
if (-not (Test-Path $mergedDir)) {
    New-Item -ItemType Directory -Path $mergedDir
}