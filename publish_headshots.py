# Databall headshots: publish to GitHub so Google Sheets can load them with =IMAGE(url)
# Run in Jupyter:  exec(open('/Users/quintleale/databall/headshots_public/publish_headshots.py').read())
import os, subprocess, shutil

REPO_DIR = os.path.expanduser('~/databall/headshots_public')
OWNER, NAME = 'QuintLeale', 'databall-headshots'
REMOTE = f'https://github.com/{OWNER}/{NAME}.git'


def sh(cmd, check=True):
    print('$', cmd)
    r = subprocess.run(cmd, shell=True, cwd=REPO_DIR, capture_output=True, text=True)
    print((r.stdout + r.stderr).strip()[-1500:])
    if check and r.returncode != 0: raise SystemExit(f'failed: {cmd}')
    return r


os.chdir(REPO_DIR)
n = sum(len(f) for _, _, f in os.walk(os.path.join(REPO_DIR, 'circle')))
print(f'{n} circle badges ready in {REPO_DIR}')
if not os.path.isdir(os.path.join(REPO_DIR, '.git')):
    sh('git init -b main')
sh('git add -A')
sh('git -c user.name="Quint Leale" -c user.email="quintleale@gmail.com" commit -q -m "Databall headshot badges" || true', check=False)

if shutil.which('gh') and sh('gh auth status', check=False).returncode == 0:
    # creates the public repo the first time, then pushes
    if sh(f'gh repo view {OWNER}/{NAME}', check=False).returncode != 0:
        sh(f'gh repo create {OWNER}/{NAME} --public --source . --remote origin')
if sh('git remote get-url origin', check=False).returncode != 0:
    sh(f'git remote add origin {REMOTE}')
r = sh('git push -u origin main', check=False)
if r.returncode != 0:
    print(f'''
Push did not go through. Most likely the repo does not exist yet:
  1. open https://github.com/new  -> Repository name: {NAME}  -> Public  -> Create (leave README unticked)
  2. run this cell again.
''')
else:
    print(f'\nDone. Test link: https://raw.githubusercontent.com/{OWNER}/{NAME}/main/circle/bukayo-saka--soccer.png')
