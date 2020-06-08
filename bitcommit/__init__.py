from bitcommit.handlers import setup_handlers
# Jupyter Extension points
def _jupyter_server_extension_paths():
    return [{
        'module': 'bitcommit',
    }]

def _jupyter_nbextension_paths():
    return [{
        "section": "notebook",
        "dest": "bitcommit",
        "src": "static",
        "require": "bitcommit/main"
    }]

def load_jupyter_server_extension(nbapp):
    setup_handlers(nbapp.web_app)
