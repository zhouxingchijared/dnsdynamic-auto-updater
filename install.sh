#!/bin/bash
service_location="/etc/systemd/system/"
service="update-host.service"
pwd=$(pwd)

cat > $service_location$service <<- _EOF
[Unit]
After=network.target

[Service]
ExecStart=$pwd/update-host.py

[Install]
WantedBy=default.target
_EOF

systemctl enable $service
systemctl start $service
echo "Installation complete"
