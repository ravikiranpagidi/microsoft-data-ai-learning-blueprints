param(
    [Parameter(Mandatory = $true)]
    [string]$ResourceGroupName,

    [Parameter(Mandatory = $true)]
    [string]$DataFactoryName,

    [Parameter(Mandatory = $true)]
    [string]$ArtifactPath,

    [Parameter(Mandatory = $true)]
    [ValidateSet("dev", "test", "prod")]
    [string]$Environment
)

$ErrorActionPreference = "Stop"

Write-Host "Deploying Azure Data Factory artifacts"
Write-Host "Resource group: $ResourceGroupName"
Write-Host "Data factory: $DataFactoryName"
Write-Host "Artifact path: $ArtifactPath"
Write-Host "Environment: $Environment"

$jsonFiles = Get-ChildItem -Path $ArtifactPath -Recurse -Filter *.json

foreach ($file in $jsonFiles) {
    Write-Host "Validated JSON artifact: $($file.FullName)"
    $null = Get-Content -Raw -Path $file.FullName | ConvertFrom-Json
}

Write-Host "This starter script validates ADF JSON templates."
Write-Host "For production, call az datafactory commands or ARM/Bicep deployments here."
