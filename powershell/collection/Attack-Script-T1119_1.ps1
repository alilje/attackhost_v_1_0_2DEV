'***********T1119_1---Automated Collection---Automated Collection Command Prompt**********'| Out-File -FilePath $args[0]
cmd.exe /c 'mkdir T1119_command_prompt_collection >nul 2>&1' |  Out-File -FilePath $args[0] -Append
cmd.exe /c 'dir c: /b /s .docx | findstr /e .docx' |  Out-File -FilePath $args[0] -Append
cmd.exe /c 'for /R c: %f in (*.docx) do copy %f T1119_command_prompt_collection' |  Out-File -FilePath $args[0] -Append
