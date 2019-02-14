# -*- mode: python -*-

block_cipher = None


a = Analysis(['tinyfactorio.py'],
             pathex=['C:\\Users\\iivarimo\\Dropbox\\#games\\Factorio_0.16.51'],
             binaries=[],
             datas=[('empty.ogg','.'),('empty.png','.'),('empty.ttf','.'),('upx.exe','.'),('pngquant.exe','.')],
             hiddenimports=[],
             hookspath=[],
             runtime_hooks=[],
             excludes=[],
             win_no_prefer_redirects=False,
             win_private_assemblies=False,
             cipher=block_cipher,
             noarchive=False)
pyz = PYZ(a.pure, a.zipped_data,
             cipher=block_cipher)
exe = EXE(pyz,
          a.scripts,
          a.binaries,
          a.zipfiles,
          a.datas,
          [],
          name='tinyfactorio',
          debug=False,
          bootloader_ignore_signals=False,
          strip=False,
          upx=False,
          runtime_tmpdir=None,
          console=True )
