

'''
Tools:
- AssetStudio from https://github.com/zhangjiequan/AssetStudio
- FFmpeg

1. copy resources/adv/movies to pc
2. extract usm videos using AssetStudio from https://github.com/zhangjiequan/AssetStudio
3. delete unneccessary stuff (main story vids, etc)
4. check/update script is still valid
5. run it
'''



from pathlib import Path
import re
import subprocess
from concurrent.futures import ThreadPoolExecutor

USM_VIDEOS = Path('TextAsset')
SAVE_PATH = Path('stuff')


NAME_PATTERN = re.compile(r'hs_(\w*)_mo_0([123])0([123])\.usm\.bytes')
SAVE_PATH.mkdir(exist_ok=True, parents=True)



def conv(f: Path):
    m = NAME_PATTERN.search(f.name)
    assert(m)
    g = SAVE_PATH / ('-'.join(m.groups()) + '.mp4')
    print(f'{f} >> {g}')
    subprocess.run(['ffmpeg', '-v', 'error', '-y', '-hide_banner', '-i', f, '-c', 'copy', g])

def main():
    with ThreadPoolExecutor() as pool:
        pool.map(conv, USM_VIDEOS.iterdir())


if __name__ == '__main__':
    main()
