from os.path import join, abspath, basename
import re
from configsmash import ConfigSmasher

version_info = (0, 0, 1)
__version__ = '.'.join(map(str, version_info))
version = __version__

class SelectiveConfigSmasher(ConfigSmasher):
    def __init__(self, to_smash=None, pattern=None):
        ConfigSmasher.__init__(self, to_smash)
        self.pattern = re.compile(pattern)

    def _expand(self, path):
        """
        we are filtering the files found by the
        pattern
        """

        # get all the file's paths
        paths = ConfigSmasher._expand(self, path)

        # now filter by the pattern
        paths = filter(lambda p: self.pattern.match(basename(p)), paths)

        return paths


class CasConfig(dict):
    def __init__(self, configs_base='./configs'):
        # what's the base dir for the configs?
        self.configs_base = abspath(configs_base)

        # what process is this config for?
        self._proc = None

        # what type of configs ?
        self._type = None

        # respect
        dict.__init__(self)

    def setup(self, _type, proc=None):
        """
        reset the config and re-read config files
        _type -- the type of configs
        proc -- the process who's configs we are reading in
        """

        # create our list of dirs to read in from
        # starting w/ the root
        to_read = ['.']
        # and if we have a proc, it's dir
        if proc:
            to_read.append('./%s' % proc)
        # update w/ config base path
        to_read = [join(self.configs_base,p) for p in to_read]

        # setup our smasher
        type_pattern = '^%s.*' % _type
        smasher = SelectiveConfigSmasher(to_read, type_pattern)

        # read in our config files
        config = smasher.smash()

        # we can't reset ourself, so we'll clear and
        # update in place
        self.clear()
        self.update(config)

        return self
