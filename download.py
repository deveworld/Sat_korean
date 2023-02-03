import wget
import zipfile
from sat_db import files, zip_files, unzip_files

def download(url, name, use_indexed_unzip=True):
  if name in zip_files:
    wget.download(url, out=f"{name}.zip")
    with zipfile.ZipFile(f"{name}.zip") as z:
      if use_indexed_unzip:
        before_name = list(unzip_files[name].keys())[0]
        after_name = unzip_files[name][before_name]
      else:
        before_name = z.namelist()[0]
        after_name = name
      with open(f"{after_name}.pdf", 'wb') as f:
        f.write(z.read(before_name))
    os.remove(f"{name}.zip")
    return f"{after_name}.pdf"
  else:
    wget.download(url, out=f"{name}.pdf")
    return f"{name}.pdf"
