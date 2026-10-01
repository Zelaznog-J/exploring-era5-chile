from pathlib import Path
from PIL import Image

root = Path(__file__).resolve().parent
folders = [root / 'agregados_tp' / 'figuras', root / 'agregados_t2m' / 'figuras']

for src_dir in folders:
    dst_dir = src_dir.parent / 'figuras_web'
    dst_dir.mkdir(exist_ok=True)

    for src in sorted(src_dir.glob('*.png')):
        img = Image.open(src)
        rgb = img.convert('RGBA') if img.mode in {'RGBA', 'LA'} else img.convert('RGB')
        dst = dst_dir / f'{src.stem}.webp'
        rgb.save(dst, 'WEBP', quality=75, optimize=True)
        print(f'{src} -> {dst}')

print('Listo: se generaron copias optimizadas en figuras_web/.')
