# Setup Program

1. Clone repo ini
2. Jalankan `python -m venv venv` lalu install libraries dengan `pip install -r requirements.txt`
3. Ubah hal berikut di package dronekit `venv/Lib/site-packages/dronekit/__init__.py`,

- tambahkan kode berikut di line 38

```
import sys
if sys.version_info.major == 3 and sys.version_info.minor >=  10:
    from collections.abc import MutableMapping
else:
    from collections import MutableMapping
```

- lalu ubah di file yang sama sekitar line 2694, dari

```
class Parameters(collections.MutableMapping, HasObservers)
```

menjadi

```
class Parameters(MutableMapping, HasObservers)
```

# Setup Mission Planner

Buka mission planner dan connect ke plane seperti biasanya

Lalu ctrl+f dan pilih mavlink, terdapat di kolom paling kiri urutan ke 6 dari atas

<img src="./img/setting.png" />

Setelah itu set sebagai berikut

<img src="./img/tcphost.png" />
Setelah semuanya telah disetup, bisa langsung jalankan `contoh_penggunaan.py`

# Output

<img src="./img/output.png" />
