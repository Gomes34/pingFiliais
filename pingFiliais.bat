@echo off
color 2
cls
cd /d "./pingSwitch"


if "%tipoFilial%"=="Pompeia" (
    color 60
	start cmd /c pingSwitchPomps252.bat %filial%
    start cmd /c pingSwitchPomps253.bat %filial%
    start cmd /c pingSwitchPomps254.bat %filial%
    ping 192.168.%filial%.1 -t

)else if "%tipoFilial%" =="pompeia" (
    color 60
	start cmd /c pingSwitchPomps252.bat %filial% //fazer
    start cmd /c pingSwitchPomps253.bat %filial%
    start cmd /c pingSwitchPomps254.bat %filial%
    ping 192.168.%filial%.1 -t

)else if "%tipoFilial%"=="Gang" (
    color 90
    start cmd /c pingSwitchGang.bat %filial%
	start cmd /c pingSwitchGang253.bat %filial%
    ping 172.16.%filial%.1 -t

)else if "%tipoFilial%"=="gang" (
    color 90
    start cmd /c pingSwitchGang.bat %filial%
	start cmd /c pingSwitchGang253.bat %filial%
    ping 172.16.%filial%.1 -t

)else (
	echo Error 500
	timeout /t 30
)

