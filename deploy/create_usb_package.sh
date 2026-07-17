#!/bin/bash

VERSION="SYNERGIA_USB_INSTALLER_V3_17_07_2026"

echo "Creando paquete USB SYNERGIA..."

mkdir -p /tmp/$VERSION

cp -r deploy/usb_installer /tmp/$VERSION/

cp README.md /tmp/$VERSION/ 2>/dev/null

cd /tmp

tar -czf $VERSION.tar.gz $VERSION

echo ""
echo "PAQUETE CREADO:"
echo "/tmp/$VERSION.tar.gz"
