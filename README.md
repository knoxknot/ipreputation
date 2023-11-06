#### Installation and Usage Guide
git clone https://github.com/knoxknot/ipreputation  # git clone the repository
cd ipreputation  # change into directory
pip install -r requirements.txt  # install dependencies
pyinstaller --onefile ipreputation.py --distpath $HOME/.local/bin/ --name ipreputation  # build and install ipreputation