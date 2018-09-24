# dnsdynamic-auto-updater

## Intro
If you want to have your own home server out on the internet, here is a tool for you.
This tool is for dnsdynaic, a free dns service provider only.

## Install
### Before you run installation script
* Change your credentials in the `update-host.py`
### Then you can install
* Use `sudo ./install.sh` to install as a systemd service.
* It will immediately and start on boot by default.

## Uninstall
* Use `sudo ./uninstall.sh` to remove service from systemd.
* Delete this directory.

## Notes
* You can use `systemctl` commands to manage the service.
* the name of service is `update-host.service`.
