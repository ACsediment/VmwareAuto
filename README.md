# VmwareAuto
My collection of Wmware Automation tools. 一些用来实现Wmware自动化操作的小工具。

## TakeSnapshot.py
A simple tool that takes a snapshot for certain VMs. Under rare circumstance(ie my case lol) you can even create an EXE file and authorise one of your colleagues to use it, which might save your time (Actually, not really, since it would still be your job to clean up all these snapshots.). Note: Snapshot is not a panacea.

一个简单的小脚本，实现对指定虚拟机的一键快照，打包成exe之后方便授权给特定同事使用。虽说不推荐这么做（毕竟快照不是万灵药，而且你还得自己处理删快照的事），但有时候你懂得。

## InstallVmwareTool_XShell.sh
Add this to XShell, and enjoy on-click installation of Vmware Tool. :) 

Note: it must be an empty line at the end, otherwise you need to hit the Enter yourself.

WmwareTool一键安装脚本（Xshell）。注意结尾的空行必须保留，不然会需要你多按一下回车键~
