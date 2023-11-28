@echo off
:: 檢查是否已有管理員權限
net session >nul 2>&1
if %errorLevel% == 0 (
    echo 已有管理員權限!
) else (
    echo 沒有管理員權限，正嘗試以管理員權限重新執行。
    pause
    :: 試著以管理員權限重新執行此腳本
    powershell -Command "Start-Process -Verb RunAs -FilePath '%0'"
    exit
)
echo 請選擇以下操作：
echo 1. 一般自動回覆
echo 2. 休假自動回覆
set /p mainChoice="請輸入選項（1/2）："

if "%mainChoice%"=="1" (
    echo 切換為一般自動回覆...
    schtasks /change /tn "Rocket.Chat-AutoReplyEnable" /enable
    schtasks /change /tn "Rocket.Chat-AutoReplyEnableDayoff" /disable
    echo 切換完畢
    pause
) else if "%mainChoice%"=="2" (
    echo 切換為休假自動回覆...
    schtasks /change /tn "Rocket.Chat-AutoReplyEnable" /disable
    schtasks /change /tn "Rocket.Chat-AutoReplyEnableDayoff" /enable
    echo 切換完畢
    pause
) else (
    echo 無效選項，請重新執行。
    exit /b 1
)