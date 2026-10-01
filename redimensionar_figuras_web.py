from pathlib import Path
from PIL import Image

root = Path(r'D:\Documents\Proyectos\era5')
for folder in [root / 'agregados_tp' / 'figuras_web', root / 'agregados_t2m' / 'figuras_web']:
    for p in sorted(folder.glob('*.webp')):
        img = Image.open(p)
        width = img.width
        height = img.height
        max_width = 900
        if width > max_width:
            new_height = max(1, int(height * max_width / width))
            img = img.resize((max_width, new_height), Image.Resampling.LANCZOS)
            img.save(p, 'WEBP', quality=75, optimize=True)
            print(f'{p.name}: {width}x{height} -> {img.width}x{img.height}')
print('Listo: se redimensionaron las figuras web.')
