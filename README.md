I will share here the various software I wrote while learning Python.

# 使用 PyInstaller 打包为可执行文件

## 1.安装 PyInstaller
pip install pyinstaller

## 2.准备图标文件
准备一个 icon.ico 图标文件，放在与 mynotepad.py 相同的目录下。您可以使用任意自定义图标，确保格式为 .ico。

## 3.打包程序
在命令提示符中，导航到脚本所在的目录，然后运行：
pyinstaller --noconsole --onefile --icon=icon.ico mynotepad.py

--noconsole：不显示命令行窗口。
--onefile：将所有文件打包成一个可执行文件。
--icon=icon.ico：指定程序的图标。

## 4.检查生成的可执行文件

打包完成后，在 dist 文件夹中会生成 mynotepad.exe，这是打包后的可执行文件。

# 创建安装程序

## 下载并安装 Inno Setup

从官方网站下载 Inno Setup：https://jrsoftware.org/isdl.php

## 编写安装脚本

创建一个新的脚本文件 setup.iss，内容如下：

```
[Setup]
AppName=MyNotepad
AppVersion=1.0
DefaultDirName={pf}\MyNotepad
DefaultGroupName=MyNotepad
DisableProgramGroupPage=yes
OutputBaseFilename=MyNotepadSetup
Compression=lzma
SolidCompression=yes
WizardStyle=modern

[Languages]
Name: "chinesesimplified"; MessagesFile: "compiler:Languages\ChineseSimplified.isl"

[Files]
Source: "dist\mynotepad.exe"; DestDir: "{app}"; Flags: ignoreversion

[Icons]
Name: "{desktop}\MyNotepad"; Filename: "{app}\mynotepad.exe"
Name: "{startmenu}\MyNotepad"; Filename: "{app}\mynotepad.exe"

[Run]
Filename: "{app}\mynotepad.exe"; Description: "运行 MyNotepad"; Flags: nowait postinstall skipifsilent

```

## 注意事项
将 Source 的路径修改为实际的可执行文件路径，如果不在 dist 文件夹中，请调整路径。

DisableProgramGroupPage=yes：安装时不创建程序组页面。

WizardStyle=modern：使用现代安装向导样式。

## 编译安装程序
打开 Inno Setup Compiler。

通过“文件” -> “打开”菜单，打开刚刚创建的 setup.iss 脚本。

点击工具栏上的“编译”按钮，开始编译安装程序。

编译完成后，会在脚本所在目录生成 MyNotepadSetup.exe，即安装程序。

