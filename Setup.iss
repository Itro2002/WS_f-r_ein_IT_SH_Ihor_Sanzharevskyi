[Setup]
AppName=WS_für_ein_IT_SH_Ihor_Sanzharevskyi
AppVersion=1.0
DefaultDirName={pf}\WS_für_ein_IT_SH_Ihor_Sanzharevskyi
DefaultGroupName=WS_für_ein_IT_SH_Ihor_Sanzharevskyi
OutputBaseFilename=Installer
Compression=lzma
SolidCompression=yes

[Files]
Source: "dist\run_app.exe"; DestDir: "{app}"; Flags: ignoreversion
Source: "Base\*"; DestDir: "{app}\Base"; Flags: recursesubdirs ignoreversion

[Icons]
Name: "{group}\Server- und Konsolenstart"; Filename: "{app}\run_app.exe"
Name: "{commondesktop}\WS_für_ein_IT_SH_Ihor_Sanzharevskyi"; Filename: "{app}\run_app.exe"; Tasks: desktopicon

[Tasks]
Name: "desktopicon"; Description: "Erstellen Sie eine Verknüpfung auf dem Desktop"; GroupDescription: "Zusätzlich:"

[Run]
Filename: "{app}\run_app.exe"; Description: "Nach der Installation ausführen"; Flags: nowait postinstall skipifsilent