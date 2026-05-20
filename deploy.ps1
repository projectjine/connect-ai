Param(
    [switch]$RunSurgery = $false,
    [string]$JsPath = "C:\\wp-sites\\sociallogiclab\\wp-content\\themes\\child-theme\\assets\\index-5EKcGoY5.js",
    [string]$ThemePath = "C:\\wp-sites\\sociallogiclab\\wp-content\\themes\\child-theme"
)

# 1️⃣ 복사 전역 파일들
Write-Host "🔄 복사 중: 전역 CSS/JS 및 functions.php"
Copy-Item -Path ".\stitch-global.css" -Destination "$ThemePath\stitch-global.css" -Force
Copy-Item -Path ".\stitch-global.js"  -Destination "$ThemePath\stitch-global.js"  -Force
Copy-Item -Path ".\functions.php"  -Destination "$ThemePath\functions.php" -Force

# 2️⃣ 옵션: 웹마스터 수술 스크립트 실행
if ($RunSurgery) {
    Write-Host "🛠️ 웹마스터 수술 스크립트 실행 (새 포스트 삽입)"
    $sampleJson = '{"title":"Ops 자동 삽입","excerpt":"PowerShell 배포 테스트","categories":["Ops"],"image":"https://example.com/ops.jpg","content":"<p>Ops 배포 성공</p>"}'
    python .\scripts\web_master_surgery.py "$JsPath" $sampleJson
}

# 3️⃣ 압축 → SFTP 전송 (WinSCP 사용)
$zipFile = "theme.zip"
if (Test-Path $zipFile) { Remove-Item $zipFile }
Compress-Archive -Path "$ThemePath\*" -DestinationPath $zipFile -Force

Write-Host "🚚 WinSCP 로 전송 중..."
$scpScript = @"
open sftp://$env:WP_USER:$env:WP_PASS@$env:WP_HOST -hostkey="ssh-rsa 2048 xx:xx:xx:..."
put $zipFile /var/www/html/wp-content/themes/
exit
"@
$scpScript | Out-File -Encoding ascii winSCPscript.txt
winscp.com /script=winSCPscript.txt

# 4️⃣ 원격 SSH 명령 실행 (WP‑CLI 캐시 플러시)
Write-Host "🔧 원격 서버에서 압축 해제 및 캐시 플러시 중"
ssh $env:WP_USER@$env:WP_HOST "cd /var/www/html/wp-content/themes/; unzip -o theme.zip -d child-theme; rm theme.zip; wp cache flush"

Write-Host "Deployment complete"
