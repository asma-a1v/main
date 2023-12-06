@echo off

setlocal enabledelayedexpansion

set "cwd=%cd%"

echo =============================================

for /r "%cwd%" %%a in (*) do (
    echo %%a
)

echo =============================================

setlocal

for /f "tokens=* usebackq" %%f in (`dir /b /a "%cwd%"`) do (
    echo %%f
)