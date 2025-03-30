import json

import urllib


class Downloader(object):
    """
    A class used to access the KoNLPy data server, which can be used to download packages.
    """
    PACKAGE_URL = 'http://konlpy.github.io/konlpy-data/packages/%s.%s'
    SCRIPT_URL = 'http://konlpy.github.io/konlpy-data/packages/%s.sh'
    INDEX_URL = 'http://konlpy.github.io/konlpy-data/index.json'

    INSTALLED = 'installed'
    NOT_INSTALLED = 'not installed'
    STALE = 'corrupt or out of date'

    def __init__(self, download_dir=None):
        self._download_dir = download_dir

    def download(self, id=None, download_dir=None):
        """The KoNLPy data downloader.
        With this module you can download corpora, models and other data packages
        that can be used with KoNLPy.

        Downloading packages
        ====================

        Individual packages can be downloaded by passing a single argument, the package identifier for the package that should be downloaded:

        >>> download('corpus/kobill')
        [konlpy_data] Downloading package 'kobill'...
        [konlpy_data]   Unzipping corpora/kobill.zip.

        To download all packages, simply call ``download`` with the argument 'all' (not yet implemented):

        >>> download('all')
        [konlpy_data] Downloading package 'kobill'...
        [konlpy_data]   Unzipping corpora/kobill.zip.
        ...
        """

        if download_dir is None:
            download_dir = self._download_dir

        if id is None:
            raise ValueError("Please specify a package to download. To download all available packages, pass 'all' to the argument: ``konlpy.download('all')``.")
        if id == 'all':
            raise NotImplementedError("This function is not implemented yet. Please download each package individually until further notice.")
        info = self._get_info(id)
        for msg in self._download_package(info, download_dir):
            print(msg)

    
    def _get_info(self, id):
        self.index = json.loads(urllib.urlopen(self.INDEX_URL).read().decode())
        if self.index.get(id):
            return self.index.get(id)
        raise ValueError("Could not find a matching item to download")