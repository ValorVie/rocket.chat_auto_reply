@echo off
:: �ˬd�O�_�w���޲z���v��
net session >nul 2>&1
if %errorLevel% == 0 (
    echo �w���޲z���v��!
) else (
    echo �S���޲z���v���A�����եH�޲z���v�����s����C
    pause
    :: �յۥH�޲z���v�����s���榹�}��
    powershell -Command "Start-Process -Verb RunAs -FilePath '%0'"
    exit
)
echo �п�ܥH�U�ާ@�G
echo 1. �@��۰ʦ^��
echo 2. �𰲦۰ʦ^��
set /p mainChoice="�п�J�ﶵ�]1/2�^�G"

if "%mainChoice%"=="1" (
    echo �������@��۰ʦ^��...
    schtasks /change /tn "Rocket.Chat-AutoReplyEnable" /enable
    schtasks /change /tn "Rocket.Chat-AutoReplyEnableDayoff" /disable
    echo ��������
    pause
) else if "%mainChoice%"=="2" (
    echo �������𰲦۰ʦ^��...
    schtasks /change /tn "Rocket.Chat-AutoReplyEnable" /disable
    schtasks /change /tn "Rocket.Chat-AutoReplyEnableDayoff" /enable
    echo ��������
    pause
) else (
    echo �L�Ŀﶵ�A�Э��s����C
    exit /b 1
)