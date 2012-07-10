from casconfig import CasConfig
import os


def test_end_to_end():

    ## THIS TEST WAS written to work w/o paster being available
    # to make the value's native types (bool,int)

    # setup our config
    config = CasConfig(configs_base='./tests/configs')

    # read in for the tester process the development files
    config.setup('development', 'tester')

    # assert what we know should be present
    assert config.get('root') == 'True'
    assert config.get('wsgi',{}).get('wsgi_found') == 'True'
    assert config.get('in_proc') == 'True'
    assert config.get('extras',{}).get('we_have_more') == 'fun'

