## Get started

### using docker
simply run this command

linux
```bash
./startserver.sh
```
windows
```bash
./startserver.bat
```
- run index.html using live server / simply open in the browser
- to stop run `docker stop finitive-notif`

### native run

- create a python environment
- `pip install -r requirements.txt`
- run server `python main.py`
- open other terminal and run broadcaster mock `python broadcaster.py`
- run index.html using live server / simply open in the browser