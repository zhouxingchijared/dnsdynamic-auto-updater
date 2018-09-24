#!/bin/bash
service_location="/etc/systemd/system/"
service="test.service"
systemctl stop $service
systemctl disable $service
rm /etc/systemd/system/$service
rm /etc/systemd/system/$service
systemctl daemon-reload
systemctl reset-failed
