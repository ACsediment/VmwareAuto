# This script is for XShell.
# Add this to XShell, and enjoy on-click installation. :)
# Note: it must be an empty line at the end, otherwise you need to hit the Enter yourself.

mount /dev/cdrom /media/
cp /media/V* ~/vm.tar.gz
cd
tar -xzvf vm.tar.gz
./vmware-tools-distrib/vmware-install.pl -d
