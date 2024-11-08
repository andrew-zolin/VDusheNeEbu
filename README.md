# Follow these steps to set up and configure your Windows PowerShell environment with Oh My Posh and additional configurations.

## Step 0: Make sure you have latest version of PowerShell
```plaintext
Okay Let`s goo
```
## Step 1: Create PowerShell Folder and Copy Files

1. **Create a folder** (if it doesn’t exist) at the following location:

   ```plaintext
   C:\Users\Current-User\Documents\WindowsPowerShell
    ```

2. **Copy all files from the __WindowsPowerShell__ folder** in this repository to your newly created folder.


## Step 2: Configure Windows Terminal

1. **Create a folder** (if it doesn’t exist) at the following location:
    ```plaintext
    C:\Users\Current-User\AppData\Local\Packages\Microsoft.WindowsTerminal_8wekyb3d8bbwe\LocalState
    ```

2. **Backup your existing terminal preferences** if you need to retain them.

3. **Copy all files from the __LocalState__ folder** in this repository to your newly created folder.


## Step 3: Install Oh My Posh

1. Download **Oh My Posh**. If you have winget installed, you can use the following command:
    ```bash
    winget install JanDeDobbeleer.OhMyPosh -s winget
    ```
2. **Verify** the installation by running:  
    ```bash
    oh-my-posh --version
    ```

## Step 4: Ensure Python Version 3.9 or Lower is Installed

1. Check your **Python** version with this command:
    ```bash
    python --version
    ```

2. If your version is 3.10 or higher, it’s recommended to install Python 3.9 or lower for compatibility with this project.


## Step 5: Donwload Cascadia Mono NF font 

```plaintext
https://github.com/microsoft/cascadia-code/releases/tag/v2404.23 
```


