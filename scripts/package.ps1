$ErrorActionPreference = "Stop"

$Root = Split-Path -Parent $PSScriptRoot
$SkillDir = Join-Path $Root "skills\html-go"
$DistDir = Join-Path $Root "dist"
$Packager = "D:\code\daily\.agents\skills\skill-creator\scripts\package_skill.py"

if (!(Test-Path -LiteralPath $Packager)) {
  $Packager = "$env:USERPROFILE\.codex\skills\.system\skill-creator\scripts\package_skill.py"
}

python $Packager $SkillDir $DistDir
