from os.path import join, abspath
import re
from configsmash import ConfigSmasher

class SelectiveConfigSmasher(ConfigSmasher):
    def __init__(self, to_smash=None, pattern=None):
        super(SelectiveConfigSmasher,self).__init__(to_smash)
        self.pattern = re.compile(pattern)

    def _expand(self, path):
        """
        we are filtering the files found by the
        pattern
        """

        print 'expanding: %s' % path

        # get all the file's paths
        paths = super(SelectiveConfigSmasher,self)._expand(path)

        print 'original: %s' % paths

        # now filter by the pattern
        paths = filter(paths, lambda p: self.pattern.match(basename(p)))

        print 'filtered: %s' % paths

        return paths



class CasConfig(dict):
    def __init__(self, *args, **kwargs):
        # what's the base dir for the configs?
        self.configs_base = abspath(kwargs.get('configs_base','./configs'))
        if kwargs.get('configs_base'):
            del kwargs['configs_base']

        # what process is this config for?
        self._proc = None

        # what type of configs ?
        self._type = None

        print 'args: %s' % str(args)
        print 'kwargs: %s' % str(kwargs)

        super(CasConfig, self).__init__(*args, **kwargs)

    def update(self, _type, proc=None):
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
