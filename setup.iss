#define MyAppName "Dungeon Blitz Reboot"
#define MyAppVersion "1.0"
#define MyAppPublisher "Dungeon Blitz Community"
#define MyAppExeName "DungeonBlitz.exe"

[Setup]
AppId=533C1E80-49B2-4A17-B15B-BC721A1113BC
AppName={#MyAppName}
AppVersion={#MyAppVersion}
AppPublisher={#MyAppPublisher}
DefaultDirName={userappdata}\{#MyAppName}
DisableProgramGroupPage=yes
SetupIconFile=C:\installer-dungeon-blitz-reboot\dist\image\icon.ico
UninstallDisplayIcon={app}\{#MyAppExeName}
Compression=lzma
SolidCompression=yes
WizardStyle=modern
PrivilegesRequired=lowest

[Languages]
Name: "english"; MessagesFile: "compiler:Default.isl"
Name: "brazilianportuguese"; MessagesFile: "compiler:Languages\BrazilianPortuguese.isl"

[CustomMessages]
brazilianportuguese.MyMessage=Bem-vindo ao Dungeon Blitz!
english.MyMessage=Welcome to Dungeon Blitz!

[Tasks]
Name: "desktopicon"; Description: "{cm:CreateDesktopIcon}"; GroupDescription: "{cm:AdditionalIcons}"; Flags: unchecked

[Files]
Source: "C:\installer-dungeon-blitz-reboot\dist\DungeonBlitz\*"; DestDir: "{app}"; Flags: ignoreversion recursesubdirs createallsubdirs
Source: "C:\installer-dungeon-blitz-reboot\dist\python\*"; DestDir: "{app}\python"; Flags: ignoreversion recursesubdirs createallsubdirs
Source: "C:\installer-dungeon-blitz-reboot\dist\flashplayer.exe"; DestDir: "{app}"; Flags: ignoreversion
Source: "C:\installer-dungeon-blitz-reboot\dist\image\*"; DestDir: "{app}\image"; Flags: ignoreversion recursesubdirs createallsubdirs
Source: "C:\installer-dungeon-blitz-reboot\dist\font\*"; DestDir: "{app}\font"; Flags: ignoreversion recursesubdirs createallsubdirs

[Icons]
Name: "{autoprograms}\{#MyAppName}"; Filename: "{app}\{#MyAppExeName}"
Name: "{autodesktop}\{#MyAppName}"; Filename: "{app}\{#MyAppExeName}"; Tasks: desktopicon

[Run]
Description: "{cm:LaunchProgram,{#StringChange(MyAppName, '&', '&&')}}"; Filename: "{app}\{#MyAppExeName}"; Flags: nowait postinstall skipifsilent

[UninstallDelete]
Type: filesandordirs; Name: "{app}"
