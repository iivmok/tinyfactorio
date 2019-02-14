import fnmatch
from os import path, walk
import os
import shutil
import subprocess
import sys

if not path.isfile('./bin/x64/factorio.exe'):
    print('please put me in the factorio directory')
    input('Press ENTER')
    sys.exit(1)


local_dir = path.dirname(path.realpath(__file__))

if getattr(sys, 'frozen', False):
        # we are running in a bundle
        frozen = 'ever so'
        local_dir = sys._MEIPASS
print('local_dir is ' + local_dir)
print('. is ' + path.realpath('.'))

try:
    empty_png = path.join(local_dir, 'empty.png')
except:
    print('empty.png not found')
    sys.exit(1)
try:
    empty_ogg = path.join(local_dir, 'empty.ogg')
except:
    print('empty.ogg not found')
    sys.exit(1)
try:
    empty_ttf = path.join(local_dir, 'empty.ttf')
except:
    print('empty.ttf not found')
    sys.exit(1)
try:
    upx_path = path.join(local_dir, 'upx.exe')
except:
    print('upx.exe not found')
    sys.exit(1)
try:
    pngquant_path = path.join(local_dir, 'pngquant.exe')
except:
    print('pngquant.exe not found')
    sys.exit(1)


print('Removing high resolution pngs')

for root, dirnames, filenames in walk('.'):
    for filename in fnmatch.filter(filenames, 'hr-*.png'):
        full = path.realpath(path.join(root, filename))
        if path.getsize(full) > 10240:
            shutil.copyfile(empty_png, full)
            print(full)

print('Removing music ogg')

for root, dirnames, filenames in walk('./data/base/sound/ambient'):
    for filename in fnmatch.filter(filenames, '*.ogg'):
        full = path.realpath(path.join(root, filename))
        if path.getsize(full) > 10240:
            shutil.copyfile(empty_ogg, full)
            print(full)

print('Removing locale fonts')

for root, dirnames, filenames in walk('./data/core/locale'):
    for filename in fnmatch.filter(filenames, '*.ttf'):
        full = path.realpath(path.join(root, filename))
        if path.getsize(full) > 10240:
            shutil.copyfile(empty_ttf, full)
            print(full)

def try_nuke_f(f):
    try:
        os.remove(f)
    except: pass

def try_nuke_d(d):
    try:
        shutil.rmtree(d)
    except: pass

def try_call(x):
    try:
        subprocess.call(x.split())
    except Exception as e:
        print(e)

print('Removing debug info, changelog, docs, tests, campaign')

try_nuke_f('./bin/x64/factorio.pdb')
try_nuke_f('./data/changelog.txt')
try_nuke_d('./doc-html')
try_nuke_d('./tests')
try_nuke_d('./data/base/campaigns')
#try_nuke_d('./data/base/scenarios')


print('Running UPX on factorio.exe')

try_call(upx_path + ' -9 ./bin/x64/factorio.exe')

def lossy_png(f):
    if os.path.getsize(f) > 100*1024:
        try_call( pngquant_path + ' --force --verbose --quality=45-85 ' + f)
        newf = f[:-4] + '-fs8.png'
        shutil.copyfile(newf, f)
        os.remove(newf)
    else:
        print(f)

print('Lossy PNG compression')

for root, dirnames, filenames in walk('./data'):
    for filename in fnmatch.filter(filenames, '*.png'):
        full = path.realpath(path.join(root, filename))
        lossy_png(full)


input('Done. Press ENTER')