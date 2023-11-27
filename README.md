# BurntChickenBotpy
Discord Bot

## Set up your bot

1. Install requirements

    * if you use NIXOS, add these in your `/etc/nixos/configuration.nix`

    ```nix
    environment.systemPackages = with pkgs; [
        tmux
        (python310.withPackages(ps: with ps; [
            discordpy
            requests
            dotenv
        ]))
    ]
    ```
    and run `sudo nixos-rebuild switch` to install

    * if you use other linux, run these in your terminal
    
    **You must use Python3.10**
    ```bash
    sudo apt update && sudo apt upgrade
    sudo apt install python310
    pip3 install discord.py dotenv requests
    ```

2. Set up your Token
    rename `example.env` to `.env` and replace with your token
3. Configure in `./data/strings.json`
    You can change `bot_name`, `prefix`, `GithubLink`
4. run `python3 main.py` in `tmux` (Recommended)