# Установка кодировки UTF-8
$OutputEncoding = [System.Text.Encoding]::UTF8
[Console]::InputEncoding = [System.Text.Encoding]::UTF8
[Console]::OutputEncoding = [System.Text.Encoding]::UTF8

python C:\\Users\\Curent-User\\Documents\\WindowsPowerShell\\encode_ascii_art\\utils\\getArt.py
$ohMyPoshPath = "C:\Users\Curent-User\AppData\Local\Programs\oh-my-posh\bin\oh-my-posh.exe"
$themePath = "C:\Users\Curent-User\AppData\Local\Packages\Microsoft.WindowsTerminal_8wekyb3d8bbwe\LocalState\purple-man.json"  # Вы можете выбрать другую тему
oh-my-posh init pwsh --config $themePath | Invoke-Expression

